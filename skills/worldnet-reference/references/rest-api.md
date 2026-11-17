# Worldnet Merchant REST API - overview (derived)

> Derived from `merchant-api/openapi_worldnet.yaml` (OpenAPI 3.0.1, "Merchant API", version `v1`) and
> `merchant-api/endpoints.md` (66 operations). Snapshot date: see `snapshot.json`. Boarding API is **excluded**.
> Spec section names cited below are the `info.description` headings and `tags` in the YAML.

## Base URLs

| Environment | Base URL | Source |
|---|---|---|
| Sandbox | `https://testpayments.worldnettps.com/merchant` (spec `servers[0]`, "Sandbox Server") | `merchant-api/openapi_worldnet.yaml` |
| Production | `https://payments.worldnettps.com/merchant` (appears only in gochip `payconfig.xml` samples) | `pages/gochip/support/troubleshooting.md` |
| Dev | `https://devpayments.worldnettps.com/merchant` (gochip `payconfig.xml` only) | `pages/gochip/support/troubleshooting.md` |

The OpenAPI spec itself documents **only the sandbox server**. A production base for the REST API is not
stated in the spec; the production host above is inferred from SDK config samples (and those samples contain
a doubled `https://https://` typo in some versions). Confirm the production URL with Worldnet support before
committing it to a Solution Design. Paths are `/api/v1/...` under the base, for example
`https://testpayments.worldnettps.com/merchant/api/v1/account/authenticate`.

## Authentication in one paragraph

API key (Basic) -> `GET /api/v1/account/authenticate` -> JWT (`Bearer`) with `expiresIn` in hours; use the
Bearer JWT on every other call. Merchant-level vs integration-level (ISV) keys; merchant-level keys used
by an ISV also need the `X-Integration-ID` header. Details: `auth-and-signatures.md`.

## Resource groups (from `x-tagGroups`)

Spec groups: ACCOUNT API, CUSTOMER API, CARD TRANSACTION API, BANK TRANSFER API, REPORTING API, WEBHOOK API.

### Payments (tag `payments`) - card transactions
| Capability | Operation | Notes (spec text) |
|---|---|---|
| Authorize / pre-auth / sale | `POST /api/v1/transaction/payments` (`payment`) | "online or offline authorizations and pre-authorizations over POS, eCommerce and MoTo channels". `channel` discriminator: `POS` (default), `WEB`, `MOTO`. `WEB` accepts `threeDSecure`. |
| Retrieve | `GET /api/v1/transaction/payments/{uniqueReference}` | |
| Update | `PATCH /api/v1/transaction/payments/{uniqueReference}` | operator, customer contact, status only. Status moves: READY->PENDING, PENDING->READY, REFERRAL->READY or PENDING. |
| Capture | `PATCH .../payments/{uniqueReference}/capture` | optional `captureAmount` (differs from auth within the processor's safe margin); `terminal` allowed only for pre-auths. |
| Reverse (void) | `PATCH .../payments/{uniqueReference}/reverse` | optional `reversalAmount`, `reversalReason`. |
| Refund (referenced) | `POST .../payments/{uniqueReference}/refunds` | Up to 100% cumulative; "can also lead to a full or partial reversal" for unsettled payments. Limit configurable per terminal by support. |
| Search | `GET /api/v1/transaction/transactions` (tag `transactions`) | `batchType` filter selects open batch vs closed batches. |
| Signature | `GET /api/v1/transaction/signatures/{uniqueReference}` | tag `signatures` |

Key `PaymentRequest` fields: `terminal` (required), `order{orderId<=24, currency, totalAmount}` (required),
`customer`, `customerAccount` (payload), `credentialOnFile{tokenize, merchantReference, usageAgreement, externalVault}`,
`autoCapture` (default true; false -> pre-auth if "Allow Pre-Auth" enabled, else PENDING), `processAsSale`
(requires `autoCapture=true`), `offlineProcessing`, `additionalDataFields` (custom fields), `operator`
(defaults to API-key alias).
Payload types by channel (spec "Customer Account Payloads"): WEB = `KEYED`, `SECURE_CREDENTIALS`, `DIGITAL_WALLET`;
POS = `KEYED`, `EMV`, `RAW`, `MAG_STRIPE`; MOTO = `KEYED`, `SECURE_CREDENTIALS`. The `CardPayload` schema also
lists `PAYMENT_TOKEN` (single-use token) and `APPLE_TAP_TO_PAY`.

### Refunds (tags `refunds`)
`POST /api/v1/transaction/refunds` (unreferenced - "only available on certain accounts upon request to our support
team" and must be approved by the acquirer), `GET|PATCH .../refunds/{uniqueReference}`, `PATCH .../refunds/{uniqueReference}/reverse`.

### Bank transfer (tags `bankTransferPayments`, `bankTransferRefunds`) - ACH / PAD
| Operation | Path |
|---|---|
| Make payment | `POST /api/v1/bankTransfer/payments` (payload types `ACH`, `PAD`, secure-credentials account payload) |
| Get / reverse | `GET /api/v1/bankTransfer/payments/{uniqueReference}`, `PATCH .../reverse` |
| Refund referenced | `POST .../payments/{uniqueReference}/refunds` |
| Re-present / close returned | `PATCH .../represent`, `PATCH .../close` ("re-present returned checks", "mark returned checks as closed") |
| Unreferenced refund | `POST /api/v1/bankTransfer/refunds`; `GET`, `PATCH .../reverse` on `/refunds/{uniqueReference}` |

### Customer API - cards, accounts, tokens
| Capability | Operation | Notes |
|---|---|---|
| Card verify (no charge) | `POST /api/v1/customer/cards/verify` | |
| BIN lookup | `POST /api/v1/customer/cards/lookup` | |
| Balance inquiry | `POST /api/v1/customer/cards/balance` | "Currently ... only ... EBT cards" |
| Single-use payment token | `POST /api/v1/customer/cards/paymentTokens` | once-off, **30 minute** lifetime; `PaymentToken` is a 128-char value used via `PAYMENT_TOKEN` payload |
| Bank account verify | `POST /api/v1/customer/accounts/verify` | |
| Secure credentials (tokens) | `POST /api/v1/customer/credentials`, `GET` search, `GET|PATCH|DELETE /api/v1/customer/credentials/{merchantReference}`, `POST .../credentials/transactions` | Token "looks like a card number ... BIN `296753`" (tag description). Deleted `merchantReference` cannot be reused. History search supports only `MAG_STRIPE` and `EMV` payloads. |
| Payment plans | `GET|POST /api/v1/customer/terminals/{terminal}/paymentPlans`, `GET|PATCH|DELETE .../paymentPlans/{merchantReference}` | plan = reusable template; `merchantReference` unique per terminal (max 48). Partial update of orders not supported. |
| Subscriptions | `POST .../paymentPlans/{merchantReference}/subscriptions`, `GET .../subscriptions` (search), `GET|PATCH .../subscriptions/{merchantReference}`, `PATCH .../deactivate`, `PATCH .../reactivate`, `POST .../payment` (manual payment) | `startDate` required (YYYY-MM-DD); `endDate` wins over `length`; `pauseCollectionFor` supports free-trial style pauses. |

### Account API - terminals and devices (tag `settings`, `tokens`)
`GET /api/v1/account/terminals`, `GET|PATCH /api/v1/account/terminals/{terminalNumber}` (PATCH: **tips and taxes only**),
`PATCH .../terminals/{terminalNumber}/endOfDay` (manual-settle terminals), `GET .../terminals/{terminalNumber}/devices`
and `.../devices/{type}` (POS device types/capabilities). Spec guidance: read terminal/device capabilities first
to avoid calls to unsupported features.

### Device ("cloud") instructions - semi-integrated card-present
`POST /api/v1/transaction/devices/{serialNumber}/paymentInstructions|refundInstructions|signatureInstructions`,
then `GET /api/v1/transaction/{paymentInstructions|refundInstructions|signatureInstructions}/{id}` and `DELETE` to cancel.
Instruction `status` enum (`PaymentInstruction` schema): `CANCELED`, `COMPLETED`, `FAILURE`, `IN_PROGRESS`. On completion, follow the `links` to the resulting payment/refund/signature resource.
`PaymentInstructionRequest` mirrors `PaymentRequest` minus `customerAccount` (card data is read on the device), plus
`customizationOptions`.

### Reporting (tag `summaryReports`)
`GET /api/v1/reporting/terminals/{terminal}/batches/closed` (closed batch summaries per card type and currency),
`GET .../batches/{uniqueReference}/closed/transactions`. Open-batch data is reached via `transactions` search
with `batchType=OPEN`.

### DCC (tag `fxRates`)
`POST /api/v1/transaction/dcc/fxRates` - eligibility + offer; also performs a BIN lookup. Spec lists mandatory
decision-screen and receipt elements (exchange rate, both amounts, mark-up % with "over ECB rate" for EEA, disclaimer, provider).

### Wallets / Apple
`POST /api/v1/transaction/applePaySessions` (body: `terminal`, `appleDomainId`, `appleValidationUrl` matching `.*apple.com.*`),
`POST /api/v1/transaction/appleTapToPay/token` (reader token JWT). Google/Apple payments are sent as the `DIGITAL_WALLET`
payload (`serviceProvider` `GOOGLE`|`APPLE`, `encryptedData` 128..20480 chars). No Google Pay session endpoint appears in the spec.

### Webhooks (tag `webhooks`)
Only `POST /api/v1/webhook/bead` is in the spec: an **inbound** Bead payment-status callback (HMAC in
`x-webhook-signature`, IP allow-listed) - **not** a merchant-facing event subscription. Merchant-facing
notifications (receipt URL, validation URL, account-updater URL, subscription notifications) are configured
in Selfcare and documented under `hosted-pages.md`. No REST event-subscription API is in the snapshot.

## Cross-cutting behaviour (spec sections)

| Topic | What the spec says |
|---|---|
| Versioning | Major version in path (`/api/v1`, only v1 supported); minor, backward-compatible changes advertised in the `X-API-Version` response header (e.g. a date). |
| Headers | `Accept: application/json` only; `Content-Type: application/json` only; `Accept-Language` supports `en` and `fr`; `Authorization` Basic (once) then Bearer; `X-Integration-ID` for ISV merchant-level keys. |
| Request IDs | Every request gets an id returned in `X-Request-Id` and in error `debugIdentifier`; quote it to support. |
| Errors | Body `{debugIdentifier, details[{errorCode, errorMessage, source{location, resource, property, value, expected}}]}`; see `errors-and-response-codes.md`. |
| HATEOAS | `links[]` with `rel`, `method`, `href` (e.g. `capture`, `refund`, `update`, `self`, `reverse`). The token response carries an `enableHypermedia` flag (spec: HATEOAS is something you "have the possibility to enable"). Spec recommends following links. |
| Pagination | Cursor ("continuation token"): follow the `next` link; absent `next` = last page. `pageSize` default 10, max 100. List items are **compact** - follow `self`/`load` links for full resources. |
| Partial updates | `PATCH` with only changed properties; empty value clears a property. |
| Idempotency | **No `Idempotency-Key` header is documented in the spec** (grep finds none). Do not assume Payroc's header applies; use unique `orderId` and check `GET`/search before retrying. Confirm with Product. |
| Rate limits, SLAs, webhooks signing for merchants | Not documented in snapshot. |

## Common pitfalls found in the spec text

1. **Reverse verb mismatch.** Operations use `PATCH .../reverse`, but the HATEOAS example in the intro shows
   `"rel":"reverse","method":"DELETE"` on the payment URL. Follow the `links` actually returned and the
   operation list; flag if a partner relies on the example.
2. **JWT lifetime.** The JWT lifetime is `expiresIn` **hours**, "subject to change without prior notice" - never hard-code; 401 on expiry.
3. **403 is permission, not auth.** Re-authenticating will not help until permissions/terminals are added to the key (spec 403 row).
4. **Terminal scoping.** Keys are limited to selected terminals and per-sub-API permission modes (Selfcare -> Settings -> API Keys).
5. **Unreferenced refunds are gated** (support + acquirer approval).
6. **Pre-auth requires feature flag.** `autoCapture=false` creates a pre-auth only if "Allow Pre-Auth" is enabled; otherwise a PENDING regular transaction.
7. **`processAsSale` needs `autoCapture=true`.**
8. **Delete is logical** for credentials/payment plans; references cannot be reused.
9. **Compact list items** - do not read fees/amounts from list responses; fetch the resource.
10. **Sandbox shared accounts** have limited features (see `test-data-and-uat.md`).
11. **Currency-pair/limits, EBT, level 2/3 availability depend on the acquirer/processor** (Elavon, FDRC, TSYS...) - see `hosted-pages.md` notes.
12. **Webhook endpoint in spec is Bead-only**; do not present it as a general webhook API.

## Where to look next
- Spec text for any operation: search `merchant-api/openapi_worldnet.yaml` for the `operationId` (e.g. `payment`, `capturePayment`, `refundPayment`, `unreferencedRefund`, `getDccFxRates`, `bankTransferRefund`).
- Rendered docs (not snapshotted): https://developers.worldnetpayments.com/apis/merchant/
- 3DS for REST: `pages/selfcare/api_specification/3d_secure.md`; Apple/Google Pay availability: `pages/selfcare/api_specification/apple_pay.md`, `google_pay.md`.
