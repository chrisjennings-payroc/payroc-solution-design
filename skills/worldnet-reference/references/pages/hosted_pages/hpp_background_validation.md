<!-- source: https://developers.worldnetpayments.com/doku.php?id=hosted_pages:hpp_background_validation | synced: 2026-10-05 -->

# Background Validation

The background validation is an asynchronous webhook-based mechanism used to confirm wheher a transaction was processed or not. It comes in handy when the connection between the gateway and your application fails while you're still waiting for the response. This would leave the website in a hanging state, meaning that it'd be unable to give a feedback to the customer since it doesn't know whether the payment was processed or not.

To use this feature, you need to enable it for your terminal. This can be done via our Selfcare System in the terminal setup section. Once enabled, all transactions processed through the hosted payment page will be validated. Additionally, you can also configure the **Validation URL** webhook in your terminal, so that you don't have to send it every time as part of the payment requests.

If for some reason, the gateway is unable to establish a connection with your application and the validation fails, the transaction will be flagged as **expired** and a notification e-mail will be sent to the merchant. Please, keep in mind that Worldnet has a retry policy for background validations and this communication will be attempted multiple times.

> **Note**
> This feature does not support bank transfers.

## Request

Worldnet will use the validation webhook to send you an `HTTP POST` request containing the parameters below:

| **FIELD** | **DESCRIPTION** |
|---|---|
| TERMINALID | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| UNIQUEREF | <sup>string `10 characters`</sup> <br>Unique reference number assigned by the gateway that should be stored to be able to perform follow up operations, such as reversals and refunds. |
| AMOUNT | <sup>number <double> `> 0`</sup> <br>The transaction's total amount. |
| ORDERID | <sup>string `[ 1 .. 24 ] characters`</sup> <br>Echoed back from the request. |
| APPROVALCODE | <sup>string `[ 0 .. 48 ] characters`</sup> <br>The authorization code assigned by the payment processor for approved transactions. |
| RESPONSECODE | <sup>string <enum></sup> <br>`A`: Approval <br>`E`: Accepted (China Union Pay only) <br>`D`: Declined <br>`R`: Referral <br>`C`: Pick Up <br>For more details, visit **[Transaction Responses](https://developers.worldnetpayments.com/selfcare/integration_docs/transaction_responses)**. |
| RESPONSETEXT | <sup>string `[ 0 .. 48 ] characters`</sup> <br>A brief description sent by the processor about the transaction result. |
| DATETIME | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>Same as the one generated for the transaction's response. |
| AVSRESPONSE | <sup>string `1 character`</sup> <br>The result of the AVS check. See **[Transaction Responses](https://developers.worldnetpayments.com/merchant/existing_merchant/other_information/transaction_responses)** for a full list of AVS response codes. |
| CVVRESPONSE | <sup>string `1 character`</sup> <br>The result of the CVV check. See **[Transaction Responses](https://developers.worldnetpayments.com/merchant/existing_merchant/other_information/transaction_responses)** for a full list of CVV response codes. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_background_validation#nd001_-_hash_validation)</sup> | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the fields. |
| CUSTOMFIELD | Echoed back from the request. |

> **Warning**
> The gateway expects your application to respond to this request with a plain `OK` string. Any other response will lead to the transaction being flagged as **not validated**.

### Request notes

**ND001 - Hash validation**

A hash string is also included in the request, so that you can implement a verification logic to make sure it was sent by Worldnet. See how to decode and validate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**.

For this specific feature, you should expect one of the following formats:

- *For single currency terminals*:

```
TERMINALID:ORDERID:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET
```

- *For multi-currency terminals*:

```
TERMINALID:ORDERID:CURRENCY:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET
```
