# Worldnet errors and response codes (derived index)

> This file summarises and **points to** the full lists; do not paste the long tables into a Solution Design.
> Paths relative to `references/`. If a code is not in the linked file, say "not documented in snapshot".

## 1. Where each list lives

| List | Location | Size |
|---|---|---|
| Gateway response codes (`A`, `D`, `C`, `R`, `E`) | `pages/selfcare/api_specification/response_codes_and_messages.md` ("Gateway Response Codes"); also `pages/hosted_pages/hpp_payment_features.md` | 4-5 values |
| CVV result letters (`M`, `N`, `P`, `S`, `U`) | `response_codes_and_messages.md` ("CVV Results") | 5 |
| AVS result letters (`A E N R S U G W X Y Z`) | `response_codes_and_messages.md` ("AVS Results") | 11 |
| Bank (issuer) 2-digit codes `00`-`9x` | `response_codes_and_messages.md` ("Bank (Issuer) Response Codes") | ~90 rows |
| Plain-language transaction responses (Approved, Declined, Pick-up, Referral A / B...) | `pages/selfcare/merchant/existing_merchant/other_information/transaction_responses.md` | 9 sections |
| REST HTTP statuses + error body | `merchant-api/openapi_worldnet.yaml` (intro: "HTTP Status Codes", "Error Handling") | see 2 |
| REST validation `errorCode` values (e.g. `X_400_002`) | Only examples in the spec; **no full catalogue in snapshot** | - |
| HPP secure-token errors `E01`-`E44` | `pages/hosted_pages/hpp_secure_tokens_features.md` (ND002) | 19 |
| HPP subscription errors `E01`-`E70` | `pages/hosted_pages/hpp_subscription_features.md` (ND002) | ~45 |
| Bulk payments file codes `200`, `001`-`016` | `pages/selfcare/api_specification/bulk_payments_features.md` | 17 |
| Account-updater status codes | `pages/selfcare/api_specification/account_updater.md` ("Account Updater Status Codes") | table |
| gochip SDK errors / cancellation statuses | `pages/gochip/support/error_codes.md`, `pages/gochip/support/troubleshooting.md` | see 4 |
| 3DS `STATUS` / `ECI` | `pages/selfcare/api_specification/3d_secure.md` | see 5 |

## 2. REST API (Merchant API)

HTTP statuses documented: `200`, `201`, `204` (DELETE), `400` (malformed/schema), `401` (invalid/expired credentials, `WWW-Authenticate`),
`403` (insufficient permissions/terminals - re-auth will not help), `404`, `405`, `406` (bad `Accept`), `415` (bad `Content-Type`),
`422` (semantic/business-rule failure), `500`, `501`.
Wiki test guidance: "400 ... incorrect content in the JSON request", "422 ... business rule or constraint violation"
(`pages/selfcare/integration_docs/introduction.md`).

Error body (spec "Error Handling"):
```
{ "debugIdentifier": "<uuid>",
  "details": [ { "errorCode": "X_400_002", "errorMessage": "...",
                 "source": { "location": "BODY", "resource": "...", "property": "...", "value": "...", "expected": "..." } } ] }
```
`X-Request-Id` response header equals `debugIdentifier`; give it to support. Payment outcome is carried in the response body: `TransactionResult.status` enum is `READY, PENDING, VOID, DECLINED, COMPLETE, REFERRAL, PICKUP, REVERSAL, SENT, ADMIN, EXPIRED, ACCEPTED, OTHER` and `type` is `SALE, PREAUTH, COMPLETION, REFUND, OFFLINE_DECLINE, WITHDRAWAL`. Whether a decline returns `201` with `DECLINED` or an error status is **not stated in the intro** - confirm in sandbox.

## 3. Hosted-page / gateway response model

- `RESPONSECODE`: `A` Approval, `D` Declined, `R` Referral (only meaningful for MOTO/virtual terminal; eCommerce treats as decline - contact acquirer, authorise manually in Selfcare),
  `C` Pick Up (card reported lost/stolen), `E` Accepted (China Union Pay only; result pending).
- Always check `RESPONSECODE == A` before fulfilling ("Receiving any response doesn't indicate approved" - `pages/gochip/support/troubleshooting.md`).
- AVS and CVV results are **informational** unless the gateway admin enables "Auto decline on AVS/CVV failure".
- Decline reasons are the issuer's; Worldnet "is not sent the reason" (`transaction_responses.md`) - use the bank code if provided.
- HPP page-level problems (invalid hash, validation errors) are shown on the hosted page itself; token page returns E-codes in `RESPONSECODE`.
- Background validation: non-`OK` reply -> "not validated"; unreachable -> transaction flagged **expired** + merchant email.
- E-codes overlap in number between pages (token `E24` = "secure token is used in subscription"; subscription `E24` = "invalid recurringamount") - always read the table for the page you integrate.

## 4. gochip SDK / Websockets
- Families (`error_codes.md`): connection (`ERROR_NETWORK`, `ERROR_TIMEOUT`), decryption (`ERROR_INVALID_EMV_TAGS`, `ERROR_INVALID_KSN_RANGE` -> KSN must be added to the HSM by Worldnet),
  credentials (`INCORRECT_SETTINGS_TERMINAL`, `INCORRECT_SETTINGS_TOKEN`). The full error list is an external Google Doc link - **not in snapshot**.
- Cancellation (Websocket >= 3.0.28 / SDK >= 1.6.28): statuses `CANCELLING`, `NOT_ALLOWED`, `CANCELLED`, `NOTHING_TO_CANCEL`; relevant only when cancelling via `cancelTransaction` / `REQ_CANCEL_TRANSACTION`;
  also `TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE`, `TRANSACTION_CANCELLED_BY_USER` (`troubleshooting.md`).
- Communication error callback `onTransactionCommError` (same versions): fires on network error while authorising online -> decide whether to reverse.
- Simulated responses: First Data terminals - amounts < $100 approve, $45.67 = no host response, > $100 returns last three digits as code; TSYS - cents `.01` decline, `.02` referral, `.03` CVV failure; Amex $10.00 timeout (`troubleshooting.md`).

## 5. 3D Secure result codes
`RESULT` `A`/`D`; `STATUS` `Y` success, `A` attempted, `N` not performed, `U` unable; `ECI` `05` full auth, `06` not enrolled, `07` failed (Visa only). 3DS does not support pre-auths (`pages/selfcare/merchant/existing_merchant/other_information/3d_secure.md`).

## 6. How to use in a Solution Design
- Specify the **error-handling contract**: fulfil only on `A`; store `UNIQUEREF`/`uniqueReference`; log `debugIdentifier`/`X-Request-Id`; treat 422 as business-rule failures (surface message), 401 as re-auth, 403 as configuration.
- Specify **timeout handling**: HPP -> background validation; REST -> query `GET payments/{uniqueReference}` or search before retrying; SDK -> `onTransactionCommError` then reverse.
- Not documented in snapshot: complete REST `errorCode` catalogue; per-processor decline code mapping; webhook retry schedule; SLA/rate-limit errors (`429` is not in the spec's status list).
