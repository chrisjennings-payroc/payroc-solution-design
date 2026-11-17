# Worldnet Hosted Pages (HPP) - derived summary

> Sources: `pages/hosted_pages/*.md` (payments, tokens, subscriptions, bank transfer, background validation) and
> `pages/selfcare/api_specification/*.md`. Paths below are relative to `references/`. All URLs in the snapshot are
> **sandbox** (`https://testpayments.worldnettps.com/merchant/...`); the wiki says to contact support for live URLs
> (`pages/selfcare/api_specification/bulk_payments_features.md`). Secrets are placeholders (`<TERMINAL_SECRET>`).

## What it is

Form POST (or iframe) from the merchant to a Worldnet-hosted page. Cardholder enters card data on Worldnet's
page (SAQ-A style scope reduction - `pages/selfcare/developer/understanding_the_integration.md`). Worldnet
posts/redirects the result to the **Receipt URL** and optionally to a **Validation URL** (server-to-server).
3DS, MaxMind, AVS, DCC, Apple Pay, Google Pay are enabled by terminal configuration, "no extra development"
(`pages/hosted_pages/introduction.md`).

## Request flow

1. Merchant server builds fields + `HASH` = SHA-512 of colon-joined fields + `<TERMINAL_SECRET>` (formulas below).
2. Browser POSTs to the page URL (or iframe `src`, with `INIFRAME=Y`).
3. Cardholder pays on the hosted page (styling from Selfcare -> Settings -> Pay Pages, `pages/selfcare/merchant/existing_merchant/selfcare_system/settings/pay_pages.md`).
4. Worldnet sends the result (with response `HASH`) to the **Receipt Page URL**; merchant **must verify the hash** and store `UNIQUEREF` for later reversals/refunds/capture.
5. Optionally Worldnet POSTs the same outcome to the **Validation URL** (background validation) and expects the plain text `OK`.

## Endpoints (sandbox)

| Feature | URL | Snapshot page |
|---|---|---|
| Payment | `/merchant/paymentpage` | `pages/hosted_pages/hpp_payment_features.md` |
| Pre-authorization | `/merchant/preauthpage` (same body as payment) | `pages/hosted_pages/hpp_payment_features.md` |
| Bank transfer (card + bank transfer on the same page) | `/merchant/paymentpage` | `pages/hosted_pages/hpp_bank_transfer.md` |
| Secure token register/update | `/merchant/securecardpage` (`ACTION=register|update`) | `pages/hosted_pages/hpp_secure_tokens_features.md` |
| Subscription register | `/merchant/subscriptionpage/register` | `pages/hosted_pages/hpp_subscription_features.md` |
| 3DS MPI | `/merchant/mpi` | `pages/selfcare/api_specification/3d_secure.md` |
| Bulk payments submit / result | `/merchant/bulkpayments/submit`, `/bulkpayments/result` | `pages/selfcare/api_specification/bulk_payments_features.md` |
| Account-updater reply | `/merchant/accountupdater/notification/reply` | `pages/selfcare/api_specification/account_updater.md` |

Page hosts: Worldnet sandbox `testpayments.worldnettps.com`. A Payroc-gateway variant of the 3DS page uses
`payments.uat.payroc.com/merchant/mpi` (`pages/selfcare/api_specification/3d_secure_payroc.md`) - see
`payroc-vs-worldnet.md`.

## Required fields (payment / pre-auth)

`TERMINALID` (1-50), `ORDERID` (1-24), `CURRENCY` (ISO 4217), `AMOUNT` (>0), `DATETIME` (`DD-MM-YYYY:HH:MM:SS:SSS`), `HASH`.
Common optional: `CARDHOLDERNAME`, `AUTOREADY` (Y|N), `DESCRIPTION`, `EMAIL`, `RECEIPTPAGEURL`, `VALIDATIONURL`,
`TERMINALTYPE` (1 MOTO, 2 eCommerce, 3 cardholder present), `TRANSACTIONTYPE` (4,5,6,7,9), billing address
(`ADDRESS1/2`, `POSTCODE`, `CITY`, `REGION`, `COUNTRY`, `PHONE`), `PAYMENTTYPE=CUP_SECUREPAY`, `CUSTOMFIELD`,
`OTHERFIELD`, `STOREDCREDENTIALUSE` (`UNSCHEDULED|INSTALLMENT|RECURRING`), `STOREDCREDENTIALTXTYPE`
(`FIRST_TXN|SUBSEQUENT_CARDHOLDER_INITIATED_TXN|SUBSEQUENT_MERCHANT_INITIATED_TXN`), `CARDREFERENCE` (use stored token;
customer cannot change card), `SECURECARDMERCHANTREF` (offers "store card" option), `BYPASS_SURCHARGE`,
`PAYMENTOPTIONS` (`CARD|BANK_TRANSFER|CARD_AND_BANK_TRANSFER`), `INIFRAME=Y`, Level 2/3 and convenience-fee fields
(`pages/hosted_pages/hpp_payment_features.md` notes ND009-ND011; FDRC/TSYS only).

## Hash formulas (`:` separator; no secret values here)

Rule (`pages/selfcare/api_specification/special_fields_and_parameters.md`): SHA-512, UTF-8, `:` between **elements that have values** only
(omit absent optional elements and their separator). Legacy MD5 is still accepted unless "Force SHA-512" is set; for
MD5 the same fields are used with **no separator**.

| Message | Formula |
|---|---|
| Payment/pre-auth request (single currency) | `TERMINALID:ORDERID:AMOUNT:DATETIME:RECEIPTPAGEURL:VALIDATIONURL:<SECRET>` |
| ... multi-currency terminal ("MC") | `TERMINALID:ORDERID:CURRENCY:AMOUNT:DATETIME:RECEIPTPAGEURL:VALIDATIONURL:<SECRET>` |
| Payment response | `TERMINALID:ORDERID:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:<SECRET>` (+ `:MERCHANTREF:CARDREFERENCE:CARDTYPE:CARDNUMBER:CARDEXPIRY` when a token was registered; multi-currency adds `CURRENCY` after `ORDERID`) |
| Bank transfer request | `TERMINALID:ORDERID:AMOUNT:DATETIME:RECEIPTPAGEURL:<SECRET>` |
| Secure token request | `TERMINALID:MERCHANTREF:DATETIME:ACTION:<SECRET>` |
| Secure token response | `TERMINALID:RESPONSECODE:RESPONSETEXT:MERCHANTREF:CARDREFERENCE:DATETIME:<SECRET>` |
| Subscription request (CARDREFERENCE) | `TERMINALID:MERCHANTREF:CARDREFERENCE:DATETIME:STARTDATE:<SECRET>` |
| Subscription request (SECURECARDMERCHANTREF) | `TERMINALID:MERCHANTREF:SECURECARDMERCHANTREF:DATETIME:STARTDATE:<SECRET>` |
| Subscription response | `TERMINALID:MERCHANTREF:DATETIME:RESPONSECODE:RESPONSETEXT:<SECRET>` |
| Background validation (to you) | `TERMINALID:ORDERID:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:<SECRET>` (+`CURRENCY` for MC) |
| 3DS MPI request / response | `TERMINALID:ORDERID:CARDNUMBER:CARDEXPIRY:CARDTYPE:AMOUNT:DATETIME:<SECRET>` / `RESULT:MPIREF:ORDERID:DATETIME:<SECRET>` |
| Bulk submit / bulk transaction / result | `TERMINALID:TRANSACTIONCOUNT:BATCHTOTAL:DATETIME:<SECRET>` / `TERMINALID:ORDERID:AMOUNT:DATETIME:<SECRET>` / `TERMINALID:BULKID:<SECRET>` |

Full detail: `auth-and-signatures.md`. Subscription page has a second request form (create plan + subscription) with
its own hash variants - read `pages/hosted_pages/hpp_subscription_features.md`.

## Response (receipt) fields - payment

`ORDERID`, `APPROVALCODE`, `RESPONSECODE` (`A` approval, `E` accepted CUP, `D` declined, `R` referral, `C` pick up), `RESPONSETEXT`,
`DATETIME`, `AVSRESPONSE`, `CVVRESPONSE`, `UNIQUEREF` (10 chars - **store it**), `EMAIL`, `PHONE`, `COUNTRY`, masked `CARDNUMBER`,
`CARDTYPE`, `HASH`, echoed custom/other fields, `BRANDTXIDENTIFIER`, `STOREDCREDENTIAL*`, `CONVENIENCE_FEE`, `SURCHARGE_FEE`,
`SURCHARGE_PERCENT`; token registration adds `ISSTORED`, `SCERROR`, `MERCHANTREF`, `CARDREFERENCE`, `CARDEXPIRY`;
DCC adds `FX_AMOUNT`, `FX_CURRENCY`, `FX_RATE`, `FX_MARKUP`, `FX_PROVIDER` (and the cardholder receipt must show them).
Bank transfer responses add `TRANSIT_NUMBER`, `ROUTING_NUMBER`, `ACCOUNT_NUMBER` (masked), `INSTITUTION_NUMBER`, `ACCOUNT_TYPE`.

## Feature sections

| Topic | Key points | Snapshot file |
|---|---|---|
| **Pre-auth** | Same body, different URL. Terminal must allow pre-auth (C001). Needs **completion/capture** via Selfcare or REST `PATCH .../payments/{uniqueReference}/capture` (C002); final amount adjustable (C003); un-captured pre-auths never settle and expire. Separately, `AUTOREADY=N` flags a payment `PENDING` (not settled until marked ready). 3DS does not support pre-auths. | `pages/hosted_pages/hpp_payment_features.md`, `pages/selfcare/merchant/existing_merchant/other_information/3d_secure.md` |
| **Secure tokens** | Hosted registration page; response returns `CARDREFERENCE` + `MERCHANTREF`; `ACTION=update` by `MERCHANTREF`; error codes E01-E44; token usable in HPP via `CARDREFERENCE`, in subscriptions and via REST credentials; sharing rules and auto-registration are Selfcare/portfolio settings. | `pages/hosted_pages/hpp_secure_tokens_features.md`, `pages/selfcare/important_integration_settings.md` |
| **Subscriptions** | Requires an existing secure token (`CARDREFERENCE` **or** `SECURECARDMERCHANTREF`, never both). Create from existing stored subscription (`STOREDSUBSCRIPTIONREF`) or create plan inline (`NAME`, `DESCRIPTION`, `PERIODTYPE` 2 weekly/3 fortnightly/4 monthly/5 quarterly/6 yearly, `LENGTH`, `RECURRINGAMOUNT`, `TYPE` 1 automatic/2 manual/3 automatic-without-amounts, `ONUPDATE`, `ONDELETE`). Response `A` or `C`; errors E01-E70. Subscription feature needs Secure Tokens first; suspension/notification rules are terminal settings. | `pages/hosted_pages/hpp_subscription_features.md`, `pages/selfcare/important_integration_settings.md` |
| **Bank transfer** | Same `paymentpage`; terminal config decides whether card, bank transfer or both show. `SECCODE` (`CCD|PPD|TEL|WEB`, default WEB for payments; PPD default for subscription payments). Not supported by background validation. | `pages/hosted_pages/hpp_bank_transfer.md`, `hpp_background_validation.md` |
| **Background validation** | Server-to-server POST to Validation URL for every HPP card transaction; reply body must be exactly `OK`; otherwise flagged "not validated"; if Worldnet cannot connect the transaction is flagged **expired** and the merchant is emailed; "retry policy" exists (interval/duration **not documented in snapshot**). Enable in Selfcare terminal setup or send `VALIDATIONURL`. | `pages/hosted_pages/hpp_background_validation.md` |
| **Custom fields** | Explicit (pre-configured in Selfcare -> Settings -> Custom Fields; stored, reportable, sent to validation URL) vs implicit (any other field; echoed to Receipt URL only; not stored; keep GET under ~2000 chars). Types boolean/numeric/string; size limit 100 (truncated). Used also for dynamic descriptors. | `pages/selfcare/api_specification/special_fields_and_parameters.md`, `pages/selfcare/merchant/existing_merchant/selfcare_system/settings/custom_fields.md` |
| **3D Secure** | HPP: handled by Worldnet when enabled on the terminal (email mandatory). Direct integrations (REST/XML): POST to MPI page, receive `RESULT/MPIREF/STATUS/ECI` on **MPI Receipt URL**, then put `MPIREF` into `threeDSecure` (`serviceProvider=GATEWAY`, `mpiReference`) of the REST payment; third-party 3DS (`THIRD_PARTY`: `eci`, `xid`, `cavv`, `protocolVersion`, `dsTransactionId`) also in the spec. | `pages/selfcare/api_specification/3d_secure.md`, `merchant-api/openapi_worldnet.yaml` (`ThreeDSecure`) |
| **Terminal types** | `TERMINALTYPE` 1 MOTO / 2 eCommerce / 3 cardholder present (HPP supports GENERIC_MSR or SRED_KEYED devices). Mail-order can have its own page layout/template. | `pages/hosted_pages/hpp_payment_features.md` |
| **iframe** | `INIFRAME=Y`; if using `sandbox` attribute include `allow-same-origin` (and allow-modals/forms/popups/scripts). Customer will not see the browser "green bar". | `pages/hosted_pages/hpp_payment_features.md` (ND002) |
| **Wallets** | Apple Pay and Google Pay appear as buttons on the HPP once support enables them; **Elavon terminals only**; Apple needs store name + certificate; Google needs the website domain. | `pages/selfcare/api_specification/apple_pay.md`, `google_pay.md`, `pages/selfcare/merchant/existing_merchant/selfcare_system/settings/apple_pay.md` |
| **DCC / international** | Gateway-hosted decision screen when terminal has a multi-currency/DCC feature; no extra integration; Elavon-only per terminal setup doc; MC (multi-currency) terminals change the hash. | `pages/hosted_pages/hpp_payment_features.md` (ND008), `pages/selfcare/api_specification/special_fields_and_parameters.md` |
| **Fraud / risk** | AVS (`ADDRESS1`, `POSTCODE`, `CITY`), MaxMind (needs `CITY`, `REGION`, `COUNTRY`), Sentinel Defence ("REVIEW" statuses block settlement until approved). | `special_fields_and_parameters.md` |
| **Bulk payments** | CSV file POST with per-row hash, async processing, result CSV fetched by `BULKID`; test URLs only. | `pages/selfcare/api_specification/bulk_payments_features.md` |
| **Account updater** | Visa VAU / Mastercard ABU updates pushed in CSV batches to terminal's notification URL (max 10,000 rows); merchant replies to the reply URL; row hash with MD5/SHA-256/384/512. | `pages/selfcare/api_specification/account_updater.md` |
| **Pay Link / eInvoice** | Selfcare features that email a link to an HPP; needs HPP-enabled terminal. The XML "Pay Link" API pages are **not in the snapshot**. | `pages/selfcare/merchant/existing_merchant/selfcare_system/pay_link.md`, `einvoice.md` |

## Terminal configuration dependencies (Selfcare -> Settings -> Terminal)

Receipt Page URL, Validation URL (+ Enable Validation), MPI Receipt URL, Secure Tokens URL, Subscription Receipt URL,
shared secret (16-48 chars per Payroc doc; the Worldnet page only says set + confirm), Auto Ready / Auto Ready limit,
"Allow Internet" (needed for HPP), Allow Secure Tokens Storage / Allow HPP Secure Tokens Storage, email-field behaviour
(Hidden/Optional/Mandatory), Force SHA-512 hashing. Sources: `pages/selfcare/merchant/existing_merchant/selfcare_system/settings/terminal.md`,
`pages/selfcare/partner/admin_system/terminal_setup.md`, `pages/selfcare/important_integration_settings.md`. Several of these
are gateway-administrator (support) settings, not merchant-editable.

## Open points not documented in snapshot
- Production URLs for each hosted page (only sandbox listed).
- Retry cadence/duration for validation webhooks and receipt redirects (Worldnet text says only "retry policy").
- Exact `RESPONSECODE` set for the subscription and token receipts beyond the E-code tables.
- `hpp_payment_features_applepay` / `..._googlepay` / XML feature pages referenced by the wiki index are **not** in the snapshot.
