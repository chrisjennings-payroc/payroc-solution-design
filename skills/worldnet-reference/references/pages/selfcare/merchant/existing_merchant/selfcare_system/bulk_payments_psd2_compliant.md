<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:bulk_payments_psd2_compliant | synced: 2026-10-05 -->

# Bulk Payments (PSD2 Compliant)

**PSD2 and Strong Customer Authentication (SCA)**

The Payment Services Directive 2 (PSD2) comes into force in 2019 (only applicable in EU) and you might need to be prepared to provide SCA for your payments. Take a closer look at our **[F.A.Q](https://resources.worldnetpayments.com/blog/psd2-faq)** if you have more questions.

**Bulk Payments** allows merchants to process multiple transactions at once. The main use is for merchants that do not need to register transactions individually and can process a big volume of those transactions in a single batch.

The **Bulk Payments** was upgraded to allow merchants to process transactions in compliance with the PSD2 regulations introduced by the European Union. A few updates are required to make your transactions compliant. The new CSV file has to have a HEADER section like the example below:

```
ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,CARDEXPIRY,CARDHOLDERNAME,ADDRESS1,ADDRESS2,POSTCODE,DATETIME,HASH,AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE
```

3 new fields have been added to the original integration: ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE

Below you can find further details about the new fields.

The full CSV will look like this for a Cardholder initiated transaction:

```
ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,CARDEXPIRY,CARDHOLDERNAME,ADDRESS1,ADDRESS2,POSTCODE,DATETIME,HASH,AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE
"BLK4684020","USD","8.33","4787421513493733","VISA","1127","John Doe","10 Washington Street","Apt.21","10100","27-11-2020:18:38:12:000",<SAMPLE_HEX_VALUE>,"Y","Description","[[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection)","","SUBSEQUENT_CARDHOLDER_INITIATED_TXN",""
```

In case the transaction is Merchant Initiated, then the field STOREDCREDENTIALUSE should be sent either as UNSCHEDULED or RECURRING, depending on the scenario, but never empty. The full CSV will look like this for a Merchant initiated transaction:

```
ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,CARDEXPIRY,CARDHOLDERNAME,ADDRESS1,ADDRESS2,POSTCODE,DATETIME,HASH,AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE
"BLK4684020","USD","8.33","2969999961717430","SECURECARD","1127","John Doe","10 Washington Street","Apt.21","10100","27-11-2020:18:38:12:000",<SAMPLE_HEX_VALUE>,"Y","Description","[[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection)","","SUBSEQUENT_MERCHANT_INITIATED_TXN","RECURRING"
```

Sample **Getting Started with VT** window:

Sample **Bulk Payments** window:

Understanding the fields:

- **Batch Total**: The total value of the transactions present in the CSV file.
- **Transaction Count**: The quantity of transactions present in the CSV file.
- **Batch CSV File**: The CSV file used to submit the transactions for processing.
- **Transaction Type**: You have the option to submit CSV files with Normal Sale Transactions or ACH Transactions (in case the terminal has ACH enabled).

In this first part, the user only needs to inform the fields required above and click in SUBMIT. After that, the payment gateway is going to start the processing of the file.

When the file is submitted, if the batch total or the transaction count do not match the CSV file data, or if the file is not a CSV file, or even if the data informed for each transaction in the file is not consistent (wrong hashes for example), an error is generated and the payment gateway does not even starts to process the CSV file.

When the file is successfully submitted, the payment gateway processes the transactions and generate a response file, which is going to be presented on the table under the SUBMIT button.

- **Bulk Id**: When the file is submitted correctly, a bulkid is generated for that file to define the set of transactions processed from the given file.
- **Transaction Count**: quantity of transactions present in the file.
- **Bulk total**: total value for the transactions within the file.
- **Date**: The date of the submission.
- **Status (And Download Link)**: Status of the processing. When finalized, a status FINISHED appears, alongside a DOWNLOAD button to download the resulting CSV file which contains the processing details of each transaction.

Each time a bulk payment file is submitted, a new line on the results table is added.

## About the File Format

The file send by this request needs to be composed by the transactions you want to process. During the processing, each line informed in your file is going to be considered a transaction and each transaction (line) should be represented by the following fields in your CSV file.

**FOR SALE TRANSACTIONS**

| **FIELD NAME** | **REQUIRED** | **DESCRIPTION ** |
|---|---|---|
| ORDERID | Y | A unique reference generated by Merchant system to identify the transaction. Maximum of characters. |
| CURRENCY | Y | ISO 4217 Currency Code. |
| AMOUNT | Y | Amount formatted to two decimal places. E.g. 1653.00 |
| CARDNUMBER | Y | Card PAN.<br>If a SECURECARD is used (in CARDTYPE), this field should inform the CARDREFERENCE of the given Secure Tokens. |
| CARDTYPE | Y | Card Type used for the transaction.<br>For more details visit **[Special Fields and Parameters - Card Types](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_card_types)**.<br>This field can also admit the SECURECARD type, when using a Secure Tokens to perform the transaction. |
| CARDEXPIRY | Y | Expiry date of he card.A 4 digit expiry field (MMYY), required if the CARDTYPE is not SECURECARD.<br>If the CARDTYPE is SECURECARD this field shouldn't be informed. |
| CARDHOLDERNAME | Y | The cardholders name. Required if the CARDTYPE is not SECURECARD.<br>If the CARDTYPE is SECURECARD this field shouldn't be informed. |
| ADDRESS1 | Y | AVS Address Line 1. |
| ADDRESS2 | Y | AVS Address Line 2. |
| POSTCODE | Y | AVS Post Code. |
| DATETIME | Y | Format: DD-MM-YYYY:HH:MM:SS:SSS. |
| HASH | Y | A HASH code formed by part of the request fields. Take a look at **ND003 - Hash Formation For Transactions on Bulk File** for more details. |
| AUTOREADY | Y | Set to Y for setting auto ready or N to mark as pending. |
| DESCRIPTION | Y | Optional transaction description. |
| EMAIL | Y | Card holder email for notification. |
| ORIGINALBRANDTXIDENTIFIER | N | String, max length is 64. Merchant sends the transaction identifier got from acquirer through NetTraxion or another gateway in the request |
| STOREDCREDENTIALTXTYPE | N | Parameter describes the transaction type. Options: FIRST_TXN, SUBSEQUENT_MERCHANT_INITIATED_TXN, SUBSEQUENT_CARDHOLDER_INITIATED_TXN |
| STOREDCREDENTIALUSE | N | Parameter describes the Secure Tokens usage. Options: UNSCHEDULED, INSTALLMENT, RECURRING |

If you are not going to use one of the NOT MANDATORY fields for of or more of your transaction, don't forget to add the comma separating that field from the next one. The processing of your file is going to consider the order of fields in your CSV file based on the order presented above. If you fail on informing any of them (or add them in the wrong sequence), the processing is going to fail.

Also, each transaction of your CSV file also contains a HASH and they also should follow a formation rule.

The general rule to build HASH field is given at the **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_hash_parameter)** section. For this specific feature, you should use the following format:

TERMINALID:ORDERID:AMOUNT:DATETIME:SECRET

## Response File

In Bulk Payments version 2, the response file has a header with the following columns:

| **#** | **Header** |
|---|---|
| 1 | orderId |
| 2 | approvalCode |
| 3 | responseCode |
| 4 | responseText |
| 5 | brandTxIdentifier |
| 6 | datetime |
| 7 | hash |
