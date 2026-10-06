<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:response_codes_and_messages | synced: 2026-10-05 -->

# Response Codes

 Here we present a list of possible responses your integration may receive and that your solution needs to be able to handle.

## CVV Results

- **M** - CVV Match
- **N** - CVV No Match
- **P** - Not Processed
- **S** - CVV should be on the card but the merchant indicates it is not.
- **U** - User is unregistered

> **Note**
> CVV result codes are for indication to the merchant only, and do not influence the overall authorisation result.
> If you intend to change this behaviour, ask your gateway adminstrator to enable the “Auto decline on CVV failure” option for your terminals.

## AVS Results

- **A** - Address matches, ZIP does not. The first five numerical characters contained in the address match those stored at the VIC or issuer's center. However, the ZIP code does not match.
- **E** - Ineligible transaction.
- **N** - Neither address nor ZIP matches. Neither the first five numerical characters contained in the address match with those stored at the VIC nor issuer's center nor the ZIP code match.
- **R** - Retry (system unavailable or timed out).
- **S** - Card type not supported. The card type for this transaction is not supported by AVS. AVS can verify addresses for Visa cards, MasterCard, proprietary cards, and private label transactions.
- **U** - Address information unavailable.
- **G** - Address information unavailable, International - Visa only, The address information was not available at the VIC or issuer's center.
- **W** - Nine-digit ZIP match, address does not. The nine-digit Postal ZIP code matches that stored at the VIC or card issuer's centre. However, the first five numerical characters contained in the address do not match.
- **X** - Exact match (nine digit ZIP and address). Both the nine-digit Postal ZIP code as well as the first five numerical characters contained in the address match.
- **Y** - Address and five-digit ZIP match. Both the five-digit Postal ZIP code as well as the first five numerical characters contained in the address match.
- **Z** - Five-digit ZIP matches, address does not. The five-digit Postal ZIP code matches that stored at the VIC or card issuer's centre.

> **Note**
> AVS result codes are for indication to the merchant only, and do not influence the overall authorisation result.
> If you intend to change this behaviour, ask your gateway adminstrator to enable the “Auto decline on AVS failure” option for your terminals.

## Gateway Response Codes

The gateway maps all responses into the following codes and, in addition to non-approval response codes, we will return a separate field containing a brief description of the failure.

- **A - Approval:** The transaction has been authorized. When an approval code is returned, a hold will be placed on cardholder funds in the amount of the sale (depending on the card issuing bank it might take a different number of days) and will guarantee funds to be transferred into a merchant’s account.
- **D - Declined:** The bank has declined the transaction and funds will not be transferred into the merchant's account.
- **C - Pick Up:** The card issuer has declined the transaction and requested that the card be retained as it may have been reported as lost or stolen.
- **R - Referral:** The bank requires more information before they can approve the transaction. This is only relevant when processing Mail/Telephone Order transactions through our Virtual Terminal.

> **Note**
> If you get an **R** (Referral) response code you should contact your acquiring bank immediately, because once these transactions settle, they can no longer be completed. They'll ask you for the transaction details and then give you an authorization code, which you can enter into our Selfcare.
>
> Your acquirer should have provided you with the a phone number, so you can contact them in regards to these queries. Please note that we do not have access to these contact numbers.

## Bank (Issuer) Response Codes

To help merchants understand better the cause of declines, our responses also include the bank response codes which is a 2-digit code that identifies the reason the payment was approved or declined.

The list below comprehends most of the response codes sent by issuers, but keep in mind that this list may vary depending on the bank.

| Code | Definition |
|---|---|
| 00 | Approved, authorized |
| 01 | Refer to card issuer |
| 02 | Refer to issuer's special conditions |
| 03 | Invalid merchant or service provider |
| 04 | Pick up card |
| 05 | Do not honor |
| 06 | Error |
| 07 | Pick up, special condition (other than lost/stolen) |
| 08 | Honor with ID |
| 09 | Request in progress |
| 10 | Partial amount approved |
| 11 | VIP Approval |
| 12 | Invalid or expired transaction |
| 13 | Invalid amount |
| 14 | Invalid card/account number |
| 15 | No such issuer |
| 16 | Approved, update track 3 |
| 17 | Customer cancellation |
| 18 | Customer dispute |
| 19 | Re-enter transaction |
| 20 | Invalid response |
| 21 | No action taken (no match) |
| 22 | Suspected malfunction |
| 23 | Unacceptable transaction fee |
| 24 | File update not supported by receiver |
| 25 | Unable to locate record on file |
| 26 | Duplicate file update record |
| 27 | File update field edit error |
| 28 | File update file locked out |
| 29 | File update not successful |
| 30 | Format error |
| 31 | Bank not supported by switch |
| 32 | Completed partially |
| 33 | Expired card - pick up |
| 34 | Suspected fraud - pick up |
| 35 | Contact acquirer - pick up |
| 36 | Restricted card - pick up |
| 37 | Call acquirer security - pick up |
| 38 | Allowable pin tries exceeded |
| 39 | No credit account |
| 40 | Requested function not supported |
| 41 | Lost card - pick up |
| 42 | No universal amount |
| 43 | Stolen card - pick up |
| 44 | No investment account |
| 46 | Closed account |
| 51 | Insufficient funds |
| 52 | No checking account |
| 53 | No savings account |
| 54 | Expired card or invalid expiration date |
| 55 | Incorrect pin |
| 56 | No card record |
| 57 | Transaction not permitted to cardholder |
| 58 | Transaction not permitted to terminal |
| 59 | Suspected fraud |
| 60 | Card acceptor contact acquirer |
| 61 | Exceeds withdrawal limit |
| 62 | Invalid service code, restricted |
| 63 | Security violation |
| 65 | Activity limit exceeded |
| 66 | Card acceptor call acquirer security |
| 67 | Hard capture - pick up card at ATM |
| 68 | Response received too late |
| 70 | PIN data required |
| 75 | PIN tries exceeded |
| 76 | Unable to locate, no match |
| 77 | Inconsistent data, rev., or repeat |
| 78 | No account |
| 79 | Already reversed at switch |
| 80 | Invalid date |
| 81 | Cryptographic failure |
| 82 | Incorrect CVV |
| 83 | Unable to verify PIN |
| 84 | Invalid authorisation life cycle |
| 85 | No reason to decline |
| 86 | ATM malfunction |
| 87 | No envelope inserted |
| 88 | Unable to dispense |
| 89 | Administration error |
| 90 | Cut-off in progress |
| 91 | Issuer or switch is unavailable |
| 92 | Destination not found |
| 93 | Violation, cannot complete |
| 94 | Duplicate transmission |
| 95 | Reconcile error |
| 96 | System malfunction |
| 97 | Reconciliation totals reset |
| 98 | MAC error |
| A1 | POS device authentication successful |
| A2 | POS device authentication not successful |
| A3 | POS device deactivation successful |
| B1 | Surcharge amount not permitted on Visa cards or EBT food stamps |
| B2 | Surcharge amount not supported by debit network issuer |
| CV | Card type verification error |
| E1 | Encryption not configured |
| E2 | Terminal not authenticated |
| E3 | Data could not be decrypted |
| EA | Account length error |
| EB | Check digit error |
| EC | CID format error |
| HV | Hierarchy verification failure |
| IA | Additional customer authentication required |
| K0 | Token request was processed |
| K1 | Tokenization Not Configured |
| K2 | Terminal not authenticated |
| K3 | Data could not be de-tokenized |
| N0 | Force STIP |
| N3 | Cash service is not available |
| N4 | Cash request exceeds issuer limit |
| N5 | Ineligible for re-submission |
| N7 | Decline for CVV2 failure |
| N8 | Transaction amount exceeds pre-authorized amount |
| P0 | Approved; PVID is missing, invalid or expired |
| P1 | Declined; PVID is missing, invalid or expired |
| P2 | Invalid biller information |
| P5 | PIN change unblock declined |
| P6 | Unsafe PIN |
| R0 | Customer requested stop of specific recurring payment |
| R1 | Revocation of authorization order |
| R3 | Revocation of all authorizations order |
| T0 | First check is OK and has been converted |
| T1 | Check is OK but cannot be converted - declined transaction |
| T2 | Invalid ABA number, not an ACH participant |
| T3 | Amount greater than the limit |
| T4 | Unpaid items, failed negative file check |
| T5 | Duplicate check number |
| T6 | MICR error |
| T7 | Too many checks (over merchant or bank limit) |
| V1 | Failure VM |
| Q1 | Card authentication failed |
| XA | Forward to issuer |
| XD | Forward to issuer |
| Z3 | Unable to go online |
