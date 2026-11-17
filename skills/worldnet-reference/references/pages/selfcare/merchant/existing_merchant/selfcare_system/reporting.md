<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:reporting | synced: 2026-10-05 -->

# Reporting

After logging on Selfcare system, access the “**Reporting**” tab for the following features.

## Open Batch

All the transaction performed by your terminals which were not settled yet can be found in the open batch. The **Open Batch** report provides Merchants with the ability to:

- **I)** Search and list the transactions processed and still not settled for a terminal, or all terminals.
- **II)** Export transactions at open batch to a CSV file.
- **III)** Mark a set of transactions as “Pending” before they are settled.

1. This will prevent them from being settled until set to “Ready”.
1. Transactions cannot be altered from “Ready” to “Pending” after the terminal batch time.

- **IV)** Mark a set of transactions as “Void” before they are settled.

1. This will cause them to not be settled and moved to the closed batch at the settlement time.
1. A transaction cannot be voided after the terminal batch time.

- **V)** Mark a set of transactions as “Ready”, instructing the payment gateway to settle this transactions.
- **VI)** View general transactions' data.
- **VII)** View a transaction's details.
- **VIII)** Resend a cardholder's receipt copy.
- **IX)** Reprint the merchant's or the cardholder's receipt copy.
- **X)** And, depending on the Terminal's Acquirer and Enabled/ Allowed Features:
- * **a)** Refund a transaction
- * **b)** Perform a partial capture
- * **c)** Create a Secure Tokens out of the cardholder details within the transaction
- * **d)** Create a subscription out of the transaction's details if a Secure Tokens was already generated
- * **e)** Add enhanced data to the transaction before settlement

The Open Batch list is set to 10 transactions per page. If the transactions found cannot fit on one page, the list will be spread between several pages and a page navigator will appear below the transactions' list, on the right side.

**Open Batch** Selfcarereportingopenbatch-general

### Open Batch Search Filter Options

To search transactions, you can use many different filter options. Transaction data can be combined with filter that allow you to create matches based on quantity, amount, value match, ranges, among others. Explore and learn more about what you can do with the search filters.

**Search** Selfcarereportingopenbatch-search

### Export transactions at open batch to a CSV file

Based on the result of your searches, you can generate a CSV report, exporting the data you desire, depending on the data available in your transactions.

**Export to CSV** Selfcarereportingopenbatch-exportcsv

### Mark a set of transactions as "Pending", "Ready" or "Void"

A few actions can be performed for a set of transactions. To do this, select the desired transactions then choose the action by clicking in one of the available buttons on the left bottom side of your visible transaction list.

**Change Status of Transaction Group** Selfcarereportingopenbatch-changestatusoftransactiongroup

### Transactions Inidividual Management

Each transaction has its own status and details, therefore, you might need to take a closer look at them or treat them individually. Clicking anywhere on a transaction line from open batch (except the Order ID - this opens the transaction details), the table expands that line with more information.

**Transaction Line Details** Selfcarereportingopenbatch-transactionline-details

If you want to know the action options for that transaction, just click at the end of each line on the “**…**” option. A list of possible actions is going to be presented.

**Transaction Actions** Selfcarereportingopenbatch-transactionline-actions

Each action represents a specific feature, which might or not be available depending on:

- Transaction status (specific actions can only be applied to specific statuses)
- User Permissions
- Terminal features and settings
- Terminal's Acquirer settings

If you don't have access to one of the following features and want to kknow more about it, contact our suppor team.

Below in can see a few examples for those actions.

**Create a Secure Tokens from Transaction Details** Selfcarereportingopenbatch-actions-securecard

**Create a Subscription from Transaction Details** Selfcarereportingopenbatch-actions-subscription

**Add Enhanced Data to Transaction** Selfcarereportingopenbatch-actions-enhanceddata

**Perform Partial Capture of Transaction Value** Selfcarereportingopenbatch-actions-partialcapture

**Refund Transaction** Selfcarereportingopenbatch-actions-refund

**Void Transaction** Selfcarereportingopenbatch-actions-void

**Resend Cardholder Receipt Copy by Email** Selfcarereportingopenbatch-actions-resendreceiptemail

**Consult Sentinel Defend Events** Selfcarereportingopenbatch-actions-sentineldefend

## Closed Batch

After performing a transaction, the transaction will appear in Open Batch. After settlement, the transaction is moved to Closed Batch and grouped by settlement date.

Closed Batch is located within the Reporting section on Selfcare. The [Closed Batch documentation](doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:reporting:closed_batch) covers all functionalities available in Selfcare.

## Scheduled Report

Scheduled Reports is a feature designed to facilitate the production of reports from past transactions processed by your terminals. You can create multiple Scheduled Reports to suit your needs and the reports can be delivered by email or FTP. The Scheduled Report feature can be found after logging into the Selfcare system and is located under the Reporting section on the main menu and the [Scheduled Report documentation](doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:reporting:scheduled_report) covers how to prepare a Scheduled Report.

## Account Updater

The **Account Updater** report enables you to keep track of the updated Secure Tokens in your Terminals, making possible:

- **I)** To track the changes made to the accounts associated to your Secure Tokens.
- **II)** Understand changes which may be causing transaction decline (based on statuses).
- **III)** Export those “updates” to a CSV file.
- **IV)** See the amount of changes already updated to your Secure Tokens.

This features allows you to filter your search by the card details, the provider of the Account Update service or the change type, as you can see in the next two images.

**Account Updater Report - Search By Card**

**Account Updater Report - Advanced Filter**

**Account Updater Report - Search Result**

Following the result of the report, when applied any search, you would be able to see the list of changes already registered by the Account Updater feature, as shown in the next image. Among the data informed, you are going to find the provider or the account update service (vendor), the Secure Tokens and card details (card reference, merchant holder, terminal holder, merchant reference, card, masked card number, expiration date, cardholder), the card update details (las update date and status) and payment details (total and volume of sales, refunds, voids and total deposit on that Secure Tokens).

It's important to understand that, besides the informative function, the Merchant should understand what each status mean and if they have any impact in its future transactions.

**Statuses for Each Registered Update**

| **NAME** | **DESCRIPTION** |
|---|---|
| VALID | No updates performed. Token details are still valid. |
| UPDATE | Account number or account number, plus expiration date were updated. |
| EXPIRY | Just expiration date was updated. |
| CONTACT_CLOSED | Account was closed (Secure Tokens invalid). Merchant should contact the cardholder. |
| UNKNOWN | Account number could not be found. Token details are not valid anymore. |
| IN_PROCESS | The updating of this Token details is still in progress. It will change to one of the other statuses as soon as it's finished. |
| CONTACT | Merchant should contact the cardholder. |
| PARTICIPATING | No Match from participating bin issuer (not sure what merchant should do). |
| NON_PARTICIPATING | No Match from non-participating bin issuer (I think this card is not eligible for account updater). |
| UNDEFINED | VAU or ABU returned status_unknown. |
| ER_000101 | Error while updating: Non-numeric Account Number. The Token Details are not valid anymore. |
| ER_000102 | Error while updating: Account Number is not in BIN Range. The Token Details are not valid anymore. |
| ER_000103 | Error while updating: Invalid Expiration Date. The Token Details are not valid anymore. |
| ER_000104 | Error while updating: Merchant Not Registered. The Token Details are not valid anymore. |
| ER_000122 | Error while updating: Un-registered Sub-merchant. The Token Details are not valid anymore. |
| ER_UNSUPPORTED_RESPONSE_CODE | Error while updating: Unsupported response code from the updater service. The Token Details are not valid anymore. In this case, you should contact the Payment Gateway Support team to open an investigation to see what the response code is, and update possible valid responses. |

## ACH

If you are using a terminal which can perform ACH Transactions, a separated report option is made available under **Reporting > ACH**, with those transactions, as you can see at the menu on the following images.

Each report focuses on a specific transaction state, such as:

### Pending Transactions

This report presents all the ACH pending transactions for the used terminal:

- **I**. Grouped by **Date**.
- **II**. With a link (click on the date) to show the detailed list of transactions on that date.
- **III**. Detailed in five summarizing lines for the transactions performed on that date:

1. **a)** The first top line (aligned with the date) represents the sum of the remaining 4 lines (that's why its SEC Code column is always empty).
1. **b)** Each of the four remaining lines represents the total volumes for transactions of each one of the Sec Codes - CCD, PPD, TEL and WEB (refer **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)** to know a little bit more about SEC Codes). Additionally, a link is also provided for each SEC Code to the list of transactions with that code on that date.
1. **c)** Additionally, each line also groups the transactions as **Sales**, **Refunds** and **Voids** by quantity, represented by the value between “**()**”, followed by its total resulting amount. The **Total Deposit** totalizes those three types (Sales - Refunds - Voids).

### Submitted Transactions

This report presents all the ACH submitted transactions for the used terminal:

- **I**. Grouped by **Date**.
- **II**. With a link (click on the date) to show the detailed list of transactions on that date.
- **III**. Detailed in five summarizing lines for the transactions performed on that date:

1. **a)** The first top line (aligned with the date) represents the sum of the remaining 4 lines (that's why its SEC Code column is always empty).
1. **b)** Each of the four remaining lines represents the total volumes for transactions of each one of the Sec Codes - CCD, PPD, TEL and WEB (refer **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)** to know a little bit more about SEC Codes). Additionally, a link is also provided for each SEC Code to the list of transactions with that code on that date.
1. **c)** Additionally, each line also groups the transactions as **Sales**, **Refunds** and **Voids** by quantity, represented by the value between “**()**”, followed by its total resulting amount. The **Total Deposit** totalizes those three types (Sales - Refunds - Voids).

### Settled Transactions

This report presents all the ACH settled transactions for the used terminal:

- **I**. Grouped by **Date**.
- **II**. With a link (click on the date) to show the detailed list of transactions on that date.
- **III**. Detailed in five summarizing lines for the transactions performed on that date:

1. **a)** The first top line (aligned with the date) represents the sum of the remaining 4 lines (that's why its SEC Code column is always empty).
1. **b)** Each of the four remaining lines represents the total volumes for transactions of each one of the Sec Codes - CCD, PPD, TEL and WEB (refer **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)** to know a little bit more about SEC Codes). Additionally, a link is also provided for each SEC Code to the list of transactions with that code on that date.
1. **c)** Additionally, each line also groups the transactions as **Sales**, **Refunds** and **Voids** by quantity, represented by the value between “**()**”, followed by its total resulting amount. The **Total Deposit** totalizes those three types (Sales - Refunds - Voids).

### Closed Transactions

This report presents all the ACH closed transactions for the used terminal:

- **I**. Presenting an option to search the transaction based on a simple filter.
- **II**. Grouped by **Date**.
- **III**. With a link (click on the date) to show the detailed list of transactions on that date.
- **IV**. Detailed in five summarizing lines for the transactions performed on that date:

1. **a)** The first top line (aligned with the date) represents the sum of the remaining 4 lines (that's why its SEC Code column is always empty).
1. **b)** Each of the four remaining lines represents the total volumes for transactions of each one of the Sec Codes - CCD, PPD, TEL and WEB (refer **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)** to know a little bit more about SEC Codes). Additionally, a link is also provided for each SEC Code to the list of transactions with that code on that date.
1. **c)** Additionally, each line also groups the transactions as **Sales**, **Refunds** and **Voids** by quantity, represented by the value between “**()**”, followed by its total resulting amount. The **Total Deposit** totalizes those three types (Sales - Refunds - Voids).

If you desire to see more details or simple look for a specific transaction from a specific data, whenever you click on a date you are going to be presented to the image below, and if you click on the date link once more, te transaction details are presented.

### Returned Transactions

This report presents all the ACH returned transactions for the used terminal:

- **I**. Presenting two search options for transactions: simple and advanced - with filters.
- **II**. Grouped by **Date**.
- **III**. With a link (click on the date) to show the detailed list of transactions on that date.
- **IV**. Detailed in five summarizing lines for the transactions performed on that date:

1. **a)** The first top line (aligned with the date) represents the sum of the remaining 4 lines (that's why its SEC Code column is always empty).
1. **b)** Each of the four remaining lines represents the total volumes for transactions of each one of the Sec Codes - CCD, PPD, TEL and WEB (refer **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)** to know a little bit more about SEC Codes). Additionally, a link is also provided for each SEC Code to the list of transactions with that code on that date.
1. **c)** Additionally, each line also groups the transactions as **Sales**, **Refunds** and **Voids** by quantity, represented by the value between “**()**”, followed by its total resulting amount. The **Total Deposit** totalizes those three types (Sales - Refunds - Voids).

### Transactions' Re-presentations

This report presents all the ACH re-presentrations of returned transactions for the used terminal:

- **I**. Grouped by **Date**.
- **II**. With a link (click on the date) to show the detailed list of transactions on that date.
- **III**. Detailed in five summarizing lines for the transactions performed on that date:

1. **a)** The first top line (aligned with the date) represents the sum of the remaining 4 lines (that's why its SEC Code column is always empty).
1. **b)** Each of the four remaining lines represents the total volumes for transactions of each one of the Sec Codes - CCD, PPD, TEL and WEB (refer **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)** to know a little bit more about SEC Codes). Additionally, a link is also provided for each SEC Code to the list of transactions with that code on that date.
1. **c)** Additionally, each line also groups the transactions as **Re-initiation First Date** and **Re-initiation Second Date** by quantity, represented by the value between “**()**”, followed by its total resulting amount.

## Customers

The “**Customers**” section under the **Reporting** tab enables merchants to view and manage “**Outstanding Subscriptions with Payment Due**” and “**Expiring Secure Tokens**”.

The “**Subscription**” option shows all the details related to outstanding subscriptions.

It also provides the option to filter and search those subcriptions and export the details on this report to CSV.

The “**Expiring Secure Tokens**” shows only the Secure Tokens which are going to expire within the 2 months. This section includes the following details: Card type, Merchant Ref, Card Number, Cardholder Name and Expiry Date. You can search for expiring Secure Tokens by “Merchant Reference” or by “Month Range” for up to 12 months.

It is possible also to export the details to CSV, if needed.
