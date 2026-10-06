# Worldnet authentication, hashes and signatures (derived)

> Sources: `merchant-api/openapi_worldnet.yaml` (info.description: "Authentication"), `pages/selfcare/api_specification/special_fields_and_parameters.md`,
> `pages/hosted_pages/*.md`, `pages/gochip/support/authentication.md`. **Placeholders only** - never put real keys, JWTs or secrets in a Solution Design.
> Paths relative to `references/`.

## 1. Credential types at a glance

| Credential | Used by | Created where | Header / field |
|---|---|---|---|
| **API key** (Merchant-level) | REST API, gochip SDK/Websockets 1.6+ | Selfcare -> Settings -> API Keys -> NEW API KEY; set alias, per-sub-API permission modes, allowed terminals; "View Authentication Key" | `Authorization: Basic <API_KEY>` (once, to get a JWT) |
| **API key** (Integration-level / ISV) | REST API | Created by Worldnet support/integration team on request; delivered by email as an encrypted file | same |
| **Integration ID** | REST (merchant-level keys used by an ISV), gochip | From Worldnet support / existing account | `X-Integration-ID: <INTEGRATION_ID>` |
| **JWT access token** | REST API (everything but `authenticate`) | `GET /api/v1/account/authenticate` | `Authorization: Bearer <JWT_TOKEN>` |
| **Terminal shared secret** | HPP, MPI, bulk, XML, plugins, account-updater | Selfcare -> Settings -> Terminal (Secret + Confirm; blank = unchanged) | not sent; mixed into `HASH` |
| **Terminal ID** | HPP, XML, SDK init, plugins | Assigned by Worldnet | `TERMINALID` / `terminal` |

## 2. REST: API key -> JWT (spec "Authentication")

1. Obtain an API key (above). Merchant-level keys are limited to one merchant; **ISV integration-level keys** can span multiple merchants
   ("only one API Key for a whole integration"). ISVs may still use merchant-level keys for isolation - then the gateway requires `X-Integration-ID`
   on **every** request. Spec recommends merchant-level keys during integration/test because ISV developers cannot self-create integration keys.
2. Exchange: `GET {base}/api/v1/account/authenticate` with `Authorization: Basic <API_KEY>`.
3. Response (`AccessToken`): `audience`, `boundTo` (key alias), `tokenType: Bearer`, `token` (<JWT_TOKEN>), `expiresIn` (**hours**; do not hard-code, "subject to change without prior notice"),
   `enableHypermedia`, `roles[]`, `allowedTerminals[]`.
4. Call everything else with `Authorization: Bearer <JWT_TOKEN>` and `Content-Type: application/json`.
5. Expired JWT -> `401 Unauthorized` with `WWW-Authenticate`. Missing permission/terminal -> `403` (re-authenticating will not help).
6. Implement token refresh by tracking `expiresIn` (sandbox test list: "Access tokens are re-generated before they expire" - `pages/selfcare/integration_docs/introduction.md`).

Skeleton (placeholders):
```
curl {BASE}/api/v1/account/authenticate -H "Authorization: Basic <API_KEY>"
curl {BASE}/api/v1/account/terminals?pageSize=10 -H "Content-Type: application/json" -H "Authorization: Bearer <JWT_TOKEN>"
```
Sandbox `{BASE}` = `https://testpayments.worldnettps.com/merchant` (spec). Compare Payroc: `payroc-vs-worldnet.md`.

## 3. HPP / MPI / bulk hash (SHA-512)

Defined in `pages/selfcare/api_specification/special_fields_and_parameters.md` ("Hash Parameter"):
- Every request and response carries `HASH` = SHA-512 (hex, UTF-8) of **colon-joined element values** ending with `<TERMINAL_SECRET>`.
- The colon is added **only between elements that have values**; if an optional element is absent, omit it and its separator.
- Worked example in the wiki: `TERMINALID:ORDERID:AMOUNT:DATETIME:<SECRET>` (do not copy the wiki's sample secret/digest).
- Multi-currency ("MC") terminal IDs: add `CURRENCY` to the request and response hash (position per feature).
- **Legacy MD5**: older integrations are still accepted; fields are the same but **no `:` separator**. Selfcare setting
  *Integration -> Force SHA-512 Hashing Algorithm* forces SHA-512 for a terminal. (A 3DS sample in `3d_secure.md` still shows MD5 JavaScript.)
- Validate the **response hash** before trusting a receipt; compare against your recomputation.

Formula table: see `hosted-pages.md` ("Hash formulas") - single source of truth for per-feature formulas. Additional:

| Message | Formula |
|---|---|
| Account-updater row (request from gateway) | `TERMINALNUMBER:MASKEDCARDDETAILS:MERCHANTREF:CARDTYPE:STATUS:CURRENTEXPIRYDATE:CARDMODIFICATIONDATE:UUID:MSGEXPIRESIN:SCCF1:SCCF2:SCCF3:TERMINALSECRET`, algorithm named in the CSV `ALGORITHM` column (MD5, SHA-256, SHA-384, SHA-512; default SHA-512) |
| Account-updater reply row | `TERMINALNUMBER:UUID:SUCCESS:ERRORMSG:TERMINALSECRET` |
Source: `pages/selfcare/api_specification/account_updater.md`.

## 4. XML API hash

The XML gateway uses the same hash concept (shared terminal secret, MD5 in older code, SHA-512 current). PHP samples compute an
MD5 response hash like `terminalId . UniqueRef . (currency if multi-currency) . amount . DateTime . ResponseCode . ResponseText . secret`
(`pages/selfcare/sample_codes/php_xml_payments.md`). The per-request XML hash tables are in XML feature pages that are
**not in the snapshot** -> "not documented in snapshot".

## 5. Secure-token "authentication"

Tokens (REST `credentialsNumber` 12-19 chars, HPP `CARDREFERENCE`) are **references, not credentials**: using one still requires normal
auth (JWT or hash). Rules: unique `MERCHANTREF` per terminal/portfolio (setting-dependent), optional sharing across a merchant's
terminals or a portfolio (Selfcare settings in `pages/selfcare/important_integration_settings.md`), stored-credential agreement
(`UNSCHEDULED|RECURRING|INSTALLMENT`) required at registration. REST single-use `paymentToken` (128 chars) lives 30 minutes. Worldnet tokens are not
interchangeable with Payroc tokens (see `payroc-vs-worldnet.md`).

## 6. SDK / Websockets authentication

- gochip 1.6+: API key (+ Integration ID) set in `payconfig.xml`, code (`setApiKey`, `setIntegrationId`) or Websockets `REQ_SET_API_KEY` / `REQ_SET_INTEGRATION_ID`
  with `data.key`; then `REQ_INIT_WITH_CONFIGURATION` (terminalId) authenticates to the gateway and downloads settings
  (`pages/gochip/pos/coding_101.md`, `pages/gochip/support/authentication.md`).
- Credential errors surface as `INCORRECT_SETTINGS_TERMINAL` / `INCORRECT_SETTINGS_TOKEN`. Decryption (KSN) errors need the device KSN registered by Worldnet.
- gochip <= 1.5.x used Terminal ID + secret (`pages/gochip/pos/1_5_x/getting_started.md`).

## 7. Webhook / callback authenticity

| Callback | Verification | Source |
|---|---|---|
| HPP receipt redirect | response `HASH` | `hpp_payment_features.md` |
| Validation URL (background validation) | request `HASH`; reply plain `OK` | `hpp_background_validation.md` |
| MPI receipt | `RESULT:MPIREF:ORDERID:DATETIME:<SECRET>` | `3d_secure.md` |
| Account updater | per-row hash | `account_updater.md` |
| Bead payment-status webhook (inbound to Worldnet) | HMAC in `x-webhook-signature`, IP allow-list | `openapi_worldnet.yaml` (`/api/v1/webhook/bead`) |
| Merchant REST "event subscriptions" | **not documented in snapshot** | - |

## 8. Signature (not auth) field
`SIGNATURE` strings encode points on a 300x100 canvas (4 chars per point, base-28 digits `0-9a-r`, 4..1600 chars) -
`pages/selfcare/api_specification/special_fields_and_parameters.md`. REST signatures are retrieved via `GET /api/v1/transaction/signatures/{uniqueReference}`.

## Open questions (not documented in snapshot)
- Key rotation/expiry policy for API keys and terminal secrets; secret length rules (Payroc docs state 16-48 characters; Worldnet snapshot does not).
- IP allow-listing / mTLS requirements for merchant endpoints.
- How Payroc-issued (UAT/prod Payroc identity) keys relate to Worldnet API keys - confirm with Product.
