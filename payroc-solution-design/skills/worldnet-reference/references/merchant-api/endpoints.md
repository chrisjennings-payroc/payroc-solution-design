<!-- source: https://developers.worldnetpayments.com/apis/merchant/openapi_worldnet.yaml | synced: 2026-10-05 -->

# Merchant REST API — endpoint index

Generated from the public OpenAPI spec (`openapi_worldnet.yaml`, same folder). Rendered docs: https://developers.worldnetpayments.com/apis/merchant/

| Method | Path | Summary | Tag |
|---|---|---|---|
| GET | `/api/v1/account/authenticate` | Authenticate | tokens |
| GET | `/api/v1/account/terminals` | List Terminals | settings |
| POST | `/api/v1/bankTransfer/payments` | Make a Payment | bankTransferPayments |
| POST | `/api/v1/bankTransfer/refunds` | Unreferenced Refund | bankTransferRefunds |
| POST | `/api/v1/customer/accounts/verify` | Account Verification | accounts |
| POST | `/api/v1/transaction/dcc/fxRates` | DCC Rates Inquiry | fxRates |
| POST | `/api/v1/transaction/payments` | Make a Payment | payments |
| POST | `/api/v1/transaction/devices/{serialNumber}/paymentInstructions` | Submit payment instruction | paymentInstructions |
| POST | `/api/v1/transaction/refunds` | Unreferenced Refund | refunds |
| POST | `/api/v1/transaction/devices/{serialNumber}/refundInstructions` | Submit refund instruction | refundInstructions |
| POST | `/api/v1/transaction/devices/{serialNumber}/signatureInstructions` | Submit signature instruction | signatureInstructions |
| GET | `/api/v1/transaction/transactions` | Search Transactions | transactions |
| POST | `/api/v1/webhook/bead` | Receive Bead payment-status webhook | webhooks |
| GET | `/api/v1/account/terminals/{terminalNumber}` | Load Terminal | settings |
| PATCH | `/api/v1/account/terminals/{terminalNumber}` | Update Terminal | settings |
| GET | `/api/v1/bankTransfer/payments/{uniqueReference}` | Get a Payment | bankTransferPayments |
| GET | `/api/v1/bankTransfer/refunds/{uniqueReference}` | Get a Refund | bankTransferRefunds |
| POST | `/api/v1/customer/cards/verify` | Account Verification | cards |
| GET | `/api/v1/customer/terminals/{terminal}/paymentPlans` | List Payment Plans | subscriptions |
| POST | `/api/v1/customer/terminals/{terminal}/paymentPlans` | Create Payment Plan | subscriptions |
| GET | `/api/v1/customer/credentials/{merchantReference}` | Get Credentials | credentials |
| DELETE | `/api/v1/customer/credentials/{merchantReference}` | Delete Credentials | credentials |
| PATCH | `/api/v1/customer/credentials/{merchantReference}` | Update Credentials | credentials |
| GET | `/api/v1/reporting/terminals/{terminal}/batches/closed` | Closed Batch Summary | summaryReports |
| GET | `/api/v1/transaction/payments/{uniqueReference}` | Get a Payment | payments |
| PATCH | `/api/v1/transaction/payments/{uniqueReference}` | Update a Payment | payments |
| GET | `/api/v1/transaction/paymentInstructions/{paymentInstructionId}` | Retrieve payment instruction | paymentInstructions |
| DELETE | `/api/v1/transaction/paymentInstructions/{paymentInstructionId}` | Cancel payment instruction | paymentInstructions |
| GET | `/api/v1/transaction/refunds/{uniqueReference}` | Get a Refund | refunds |
| PATCH | `/api/v1/transaction/refunds/{uniqueReference}` | Update a Refund | refunds |
| GET | `/api/v1/transaction/refundInstructions/{refundInstructionId}` | Retrieve refund instruction | refundInstructions |
| DELETE | `/api/v1/transaction/refundInstructions/{refundInstructionId}` | Cancel refund instruction | refundInstructions |
| GET | `/api/v1/transaction/signatureInstructions/{signatureInstructionId}` | Retrieve signature instruction | signatureInstructions |
| DELETE | `/api/v1/transaction/signatureInstructions/{signatureInstructionId}` | Cancel signature instruction | signatureInstructions |
| PATCH | `/api/v1/bankTransfer/payments/{uniqueReference}/reverse` | Reverse a Payment | bankTransferPayments |
| PATCH | `/api/v1/bankTransfer/refunds/{uniqueReference}/reverse` | Reverse a Refund | bankTransferRefunds |
| POST | `/api/v1/customer/cards/lookup` | BIN Lookup | cards |
| GET | `/api/v1/customer/terminals/{terminal}/paymentPlans/{merchantReference}` | Get Payment Plan | subscriptions |
| DELETE | `/api/v1/customer/terminals/{terminal}/paymentPlans/{merchantReference}` | Delete Payment Plan | subscriptions |
| PATCH | `/api/v1/customer/terminals/{terminal}/paymentPlans/{merchantReference}` | Update Payment Plan | subscriptions |
| GET | `/api/v1/reporting/terminals/{terminal}/batches/{uniqueReference}/closed/transactions` | Closed Batch Transactions | summaryReports |
| PATCH | `/api/v1/transaction/payments/{uniqueReference}/reverse` | Reverse a Payment | payments |
| PATCH | `/api/v1/transaction/refunds/{uniqueReference}/reverse` | Reverse a Refund | refunds |
| PATCH | `/api/v1/account/terminals/{terminalNumber}/endOfDay` | End Of Day | settings |
| PATCH | `/api/v1/bankTransfer/payments/{uniqueReference}/represent` | Re-present a Payment | bankTransferPayments |
| POST | `/api/v1/customer/cards/balance` | Balance Inquiry | cards |
| GET | `/api/v1/account/terminals/{terminalNumber}/devices` | List POS Device Types | settings |
| POST | `/api/v1/bankTransfer/payments/{uniqueReference}/refunds` | Refund a Payment | bankTransferPayments |
| POST | `/api/v1/customer/cards/paymentTokens` | Single Use Payment Token | cards |
| POST | `/api/v1/customer/credentials/transactions` | Search Latest Transactions | credentials |
| PATCH | `/api/v1/transaction/payments/{uniqueReference}/capture` | Capture a Payment | payments |
| GET | `/api/v1/account/terminals/{terminalNumber}/devices/{type}` | Load POS Device Type | settings |
| PATCH | `/api/v1/bankTransfer/payments/{uniqueReference}/close` | Close a Payment | bankTransferPayments |
| POST | `/api/v1/customer/terminals/{terminal}/paymentPlans/{merchantReference}/subscriptions` | Create Subscription | subscriptions |
| GET | `/api/v1/customer/credentials` | Search Credentials | credentials |
| POST | `/api/v1/customer/credentials` | Store Credentials | credentials |
| POST | `/api/v1/transaction/payments/{uniqueReference}/refunds` | Refund a Payment | payments |
| POST | `/api/v1/transaction/applePaySessions` | Apple Pay Session | payments |
| POST | `/api/v1/transaction/appleTapToPay/token` | Payment Card Reader Token for Apple TapToPay | payments |
| GET | `/api/v1/customer/terminals/{terminal}/subscriptions` | Search Subscriptions | subscriptions |
| GET | `/api/v1/customer/terminals/{terminal}/subscriptions/{merchantReference}` | Get Subscription | subscriptions |
| PATCH | `/api/v1/customer/terminals/{terminal}/subscriptions/{merchantReference}` | Update Subscription | subscriptions |
| PATCH | `/api/v1/customer/terminals/{terminal}/subscriptions/{merchantReference}/deactivate` | Deactivate Subscription | subscriptions |
| PATCH | `/api/v1/customer/terminals/{terminal}/subscriptions/{merchantReference}/reactivate` | Re-activate Subscription | subscriptions |
| POST | `/api/v1/customer/terminals/{terminal}/subscriptions/{merchantReference}/payment` | Subscription Payment | subscriptions |
| GET | `/api/v1/transaction/signatures/{uniqueReference}` | Retrieve Signature | signatures |
