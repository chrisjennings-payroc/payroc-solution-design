<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:account_updater | synced: 2026-10-05 -->

# Account Update and Background Notification

 “Account Updater” refers to Secure Tokens saved on Worldnet Payments’s system, which have had their Cardholder details updated electronically via “Visa Account Updater” (VAU) and “Mastercard Automatic Billing Updater” (ABU) respectively. This is a process which helps to ensure a smooth automatic billing cycle by minimizing payment disruptions due to account changes.

Case example:

- Customers Secure Tokens are saved to the gateway
- A monthly subscription is created for the customer
- As time passes, eventually, the cards expire
- Worldnet Payments sends a request to Mastercard or Visa asking for the new cards' details
- Visa/ Mastercard sends the updated card details back to Worldnet Payments
- The customers' cards (Secure Tokens) are updated with new info
- Next months subscription won’t be affected because we now have the correct card details stored for the customers.

The Account Updater operations run as a background task, constantly, and sends batches of Account Updater details to each terminal’s specified notification URL (Configured at Terminal Level for the specific purpose of notifying Terminals of this type of change).

This allows integrations with the Payment Gateway to keep their customers masked card details with valid data on their side - always updating whenever the card scheme sends new data.

Each request containing the Account Updater details will be stored until it has been accepted and validated by the specified notification host.

After receiving this request, the Merchant's Integration side should send a reply messages to:

https://testpayments.worldnettps.com/merchant/accountupdater/notification/reply

The live URL will be provided once merchant testing is completed.

> **Note**
> **Additionally**: a new report was added under the Reporting section of Selfcare System, where the Merchants can keep track of the updates performed by the Account Update feature. Take a look at the Selfcare Guide for more details.

## System Start-up

To enable the Account Updater Background Notifications(AUBN) it is required to set up your terminal to use the new AUBN feature.

Please note that as default the the number of cards sent for each notification will be set to 10,000. If you need to change this limit, please contact Worldnet Payments.

## Message Specification

The body of each message is in the format of Comma Separated Values (CSV). Each Account Updater Notification Request from the gateway will contain the following CSV headers and appropriate values.

### Request From Gateway

Format to HTTP Post:

- **Produces**:​ text/plain
- **Consumes**:​ text/plain

The request message size can be modified in a Gateway’s System Settings. The maximum size is 10,000. To ensure messages are not fragmented because of their Secure Tokens Custom Field names; the Secure Tokens custom fields are set as name/value pairs in the CSV string. More specifically, they are located under the SCCF1/2/3 columns, and have their names and values delimited by the String “<AUBN||MSG>”.

**The Gateway Sends this request to**: The ​Account Updater Background Notification URL​ set in Terminal Settings.

#### Request Body Fields

| HEADER | TYPE | DESCRIPTION |
|---|---|---|
| TERMINAL NUMBER | Numeric | Gateway terminal which the card belongs to |
| MASKED CARD DETAILS | String | Card Number with the first 6, and the last 4 digits visible. |
| MERCHANT REFERENCE | String | Merchant reference stored on the gateway |
| HASH | String | The hash of the current row of data. See **[Message Hash](https://developers.worldnetpayments.com/selfcare/api_specification/account_updater#message_hash)** subsection for more details. |
| CARD TYPE | String | Card type, e.g. Visa, Mastercard, etc. |
| STATUS | Integer | Status Code​ of the Secure Tokens Update. See **[Account Updater Status Codes](https://developers.worldnetpayments.com/selfcare/api_specification/account_updater#account_updater_status_codes)** for more details. |
| CURRENT EXPIRY | String | Card expiry date in the format of “MMYY”. |
| CARD MODIFICATION DATE | String | The date the Secure Tokens was last updated on the gateway via Account Updater. Date format = “yyyy-MM-dd:HH:mm:ss” |
| UUID | String | Unique ID to validate message authenticity |
| MSG EXPIRES IN | Numeric | Milliseconds. When the gateway will stop accepting merchant responses for this request. |
| SCCF1 | String | Any Secure Tokens custom fields will go here. The string will contain both name and value of the Secure Tokens custom field. For more information see **ND001** below |
| SCCF2 | String | Same as SCCF1 |
| SCCF3 | String | Same as SCCF1 |
| ALGORITHM | String | The hashing algorithm used for the hash string |

#### Notes and Details About the Request

**ND001 - Name and Value Format**

The name, and value will be delimited by the String “<AUBN||MSG>”.

**For example:**

- “name<AUBN|MSG>value”
- “exigoID<AUBN|MSG>213545”

### Received Reply From Merchant

Format to HTTP Post:

- **Produces**: text/plain
- **Consumes**: text/plain

Once the request is received by the merchant, they should reply with the String “OK” immediately, and a response code of 200.

The server expects a **OK** as the reply.

#### Processed Reply From Merchant

Format to HTTP Post:

- **Produces**: text/plain
- **Consumes**: text/plain
- **Reply URL:** https://testpayments.worldnettps.com/merchant/accountupdater/notification/reply

The live URL will be provided once merchant testing is completed.

After the ‘received reply’ is sent, the merchant server can proceed with processing the account updater background notification data received from the gateway. Once the CSV has been processed on the merchant side, it is required that the gateway be notified if it has been a success or failure.

The reply message must contain the following CSV Headers on the first line of the reply.

#### Response Body Fields

| HEADER | TYPE | DESCRIPTION |
|---|---|---|
| TERMINAL NUMBER | Numeric | Gateway terminal which the card belongs to |
| UUID | String | The original UUID from the original incoming request. Used for message authenticity |
| SUCCESS | Int - 0 or 1 | Flag that identifies if the card was processed successfully or not. Possible values: 0 or 1 |
| ERROR MSG | String | Error Message indicating why it failed. Empty String if successful. |
| HASH | String | Hash string of the previous values in the row. See **[Message Hash](https://developers.worldnetpayments.com/selfcare/api_specification/account_updater#message_hash)** subsection for more details. |
| ALGORITHM | String | The hashing algorithm used for the hash string. |

### Message Hash

To determine message authenticity on the merchant side, each row in the csv string of the request message has to be hashed along with the terminals secret passphrase. The hashing algorithm used will be specified in the “ALGORITHM” column in the CSV data. The default hashing algorithm used is “SHA-512”. Check section for valid algorithms. Each column in each row will be concatenated and hashed using the specified algorithm.

#### Hashing with Algorithm

- Firstly, the each value in the CSV row will need to be concatenated with the other values in the row.
- The terminal’s secret passphrase should be appended to the end of the string.
- The order in which this should be done is as follows:

The gerenal rule to build HASH field is given at the **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)** page. For this specific feature, you should use the following formats:

**For Request Row Hash**

TERMINALNUMBER:MASKEDCARDDETAILS:MERCHANTREF:CARDTYPE:STATUS:CURRENTEXPIRYDATE:CARDMODIFICATIONDATE:UUID:MSGEXPIRESIN:SCCF1:SCCF2:SCCF3:TERMINALSECRET

**For Response Row Hash**

TERMINALNUMBER:UUID:SUCCESS:ERRORMSG:TERMINALSECRET

#### Supported Hashing Algorithms

The hashing algorithms that the gateway supports are listed below; these algorithms are valid values for the “ALGORITHM” column in the CSV data.

| Algorithm | String Format |
|---|---|
| MD5 | Hexadecimal |
| SHA-256 | Hexadecimal |
| SHA-384 | Hexadecimal |
| SHA-512 | Hexadecimal |

## Additional Information

### Account Updater Status Codes

The message from the gateway contains a field called “STATUS”. This field reflects the gateways Secure Tokens account updater status. This means that the gateway has sent this Secure Tokens to Mastercard/Visa (ABU/VAU) and received an update status from their service.

The following table details the meaning of each status code.

| Code | Name | Description |
|---|---|---|
| 1 | UPDATE | Match made; update data provided / Account number change (the account number or account number and expiration date are updated). |
| 2 | EXPIRY | Match made; expiration date changed |
| 3 | VALID | Match made, account number and expiration date unchanged / No updates were found but the account is valid. |
| 4 | CONTACT_CLOSED | Match made; account closed / contact cardholder advice (the merchant should contact the cardholder for additional information on the account). |
| 5 | CONTACT | Contact cardholder advice |
| 6 | UNKNOWN | The account number could not be found |
| 7 | PARTICIPATING | No match, participating BIN/issuer |
| 8 | NON_PARTICIPATING | No match, non-participating BIN/issuer |
| 9 | ER_UNSUPPORTED_RESPONSE_CODE | Unsupported response code |
| 10 | IN_PROCESS | Deprecated. No longer sending this response code to merchants. |
| 101 | ER_000101 | Non-numeric Account Number |
| 102 | ER_000102 | Account Number is not in BIN Range |
| 103 | ER_000103 | Invalid Expiration Date |
| 104 | ER_000104 | Merchant Not Registered |
| 122 | ER_000122 | Unregistered Sub-merchant |
| -1 | UNDEFINED | STATUS_UNKNOWN status |

### Test Data

The following test data can be used to test your AUBN Service.

Note: The Terminal Secret used in the following data is: **secretpass**

**Request From Gateway:**

```
"TERMINAL NUMBER","MASKED CARD DETAILS","MERCHANT REFERENCE","HASH","CARD TYPE","STATUS","CURRENT EXPIRY","CARD MODIFICATION DATE","UUID","MSG EXPIRES IN","SCCF1","SCCF2","SCCF3","ALGORITHM"
"11001","448596******3864","1000029","<SAMPLE_HEX_VALUE>","VISA","1","1218","2016-09-20:20:00:34","5fa3e885-98f2-4e0b-9d29-8c6fe463ec33","150000","robsSCCF<AUBN||MSG>test123","","","SHA-256"
"11001","402400******8322","1000021","<SAMPLE_HEX_VALUE>","VISA","1","1218","2016-09-20:20:00:21","7bae3ecf-97c4-43b1-89a0-25797ca325e9","150000","robsSCCF<AUBN||MSG>testtest","","","SHA-256"
"11001","541022******0093","100002","<SAMPLE_HEX_VALUE>","MASTERCARD","1","1218","2016-09-20:20:00:07","18c78348-cd35-4e35-a817-7dd34dad955c","150000","robsSCCF<AUBN||MSG>tester1","","","SHA-256"
```

Service should immediately reply with “OK”, and process the CSV in a separate thread.

After CSV parsing/processing the service should respond to the URL specified in item **Processed Reply From Merchant**, under **[Received Reply From Merchant](https://developers.worldnetpayments.com/selfcare/api_specification/account_updater#received_reply_from_merchant)** subsection.

**Expected Reply From Service:**

```
"TERMINAL NUMBER","UUID","SUCCESS","ERROR MSG","HASH","ALGORITHM"
"11001","5fa3e885-98f2-4e0b-9d29-8c6fe463ec33","1","","<SAMPLE_HEX_VALUE>","SHA-256"
"11001","7bae3ecf-97c4-43b1-89a0-25797ca325e9","1","","<SAMPLE_HEX_VALUE>","SHA-256"
"11001","18c78348-cd35-4e35-a817-7dd34dad955c","1","","<SAMPLE_HEX_VALUE>","SHA-256"
```
