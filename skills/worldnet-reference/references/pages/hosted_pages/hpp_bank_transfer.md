<!-- source: https://developers.worldnetpayments.com/doku.php?id=hosted_pages:hpp_bank_transfer | synced: 2026-10-05 -->

# Accepting Bank Transfer Payments

Worldnet-hosted payment page enables you to create secure and fully customized payment forms that let you accept bank transfer payments on your website.

This solution works across devices and doesn't require much development work, all you need to do is send us a `POST` request with a set of pre-defined fields.

> **Note**
> The request body will be identical for bank transfers and payments, but it's the terminal setting that determines which form will be displayed first.
>
>
>
> - Case 1 - The terminal supports card processing and bank transfer
>
>   - Payment Type displays card brands and bank transfers as an option of payment.
> - Case 2 - The terminal supports only card processing
>
>   - Payment Type displays card brands as an option of payment only.
> - Case 3 - The terminal supports only bank transfer
>
>   - Payment Type displays bank transfers as an option of payment only.

| **TYPE** | **SANDBOX URL** |
|---|---|
| Payment | `https://testpayments.worldnettps.com/merchant/paymentpage` |

## Request

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TERMINALID | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| ORDERID | Y | <sup>string `[ 1 .. 24 ] characters`</sup> <br>A unique identifier for the order assigned by the merchant. |
| CURRENCY  | Y | <sup>string `3-char ISO 4217 code`</sup> <br>The currency of the bank transfer. |
| AMOUNT | Y | <sup>number <double> `> 0`</sup> <br>The total amount to be authorized. |
| DATETIME | Y | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>The transaction date and time. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd001_-_hash_generation)</sup> | Y | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the request fields. |
| ACCOUNTHOLDER_NAME | N | <sup>string `[ 1 .. 29 ] characters`</sup> <br>Client's bank account name . If provided, it will be used to pre-populate the account holder name field on the payment page. |
| DESCRIPTION | N | <sup>string `[ 1 .. 1024 ] characters`</sup> <br>A brief description of the transaction. |
| EMAIL <br><sup>See notes: [ND004](https://developers.worldnetpayments.com/hosted_pages/hpp_bank_transfer#nd004_-_cardholder_email_field)</sup> | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The cardholder email address. <br>If **Email Cardholder Receipt** feature is enabled on the terminal, we will use this address to delivery transaction receipts to your customer. |
| RECEIPTPAGEURL | N | <sup>string <URI></sup> <br>This is the webhook that Worldnet will use to send you the result of the transactions. If provided, this will override the terminal setting in the Selfcare System. |
| ADDRESS1  | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The first line of the billing address. |
| ADDRESS2 | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The second line of the billing address. |
| POSTCODE  | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The postal code of the billing address. |
| CITY  | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The city of the billing address. |
| REGION  | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The region of the billing address. |
| COUNTRY  | N | <sup>string `2-char ISO 3166-1 code`</sup> <br>The country of the billing address. |
| PHONE | N | <sup>string `[ 5 .. 20 ] characters`</sup> <br>The cardholder phone number. International numeric format. |
| CUSTOMFIELD | N | You can send any of the custom fields configured on your terminal. Otherwise, they will be displayed as inputs, so that the cardholder can populate them. All custom fields will be stored along with the transaction details and echoed back to the Receipt URL. Check **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)** for more details. |
| PAYMENTOPTIONS | N | <sup>string <enum></sup> <br>`CARD` <br>`BANK_TRANSFER` <br>`CARD_AND_BANK_TRANSFER` <br>Restricts payment options to either cards, bank transfer providers or both. Not providing a value is equivalent to the `CARD_AND_BANK_TRANSFER` option. |
| OTHERFIELD | N | Any other fields sent in the request will be treated as metadata. They are not going to be stored, but they'll be echoed back to the Receipt URL. Note that this is subject to the max length of a HTTP GET request which we would conservatively recommend considering to be 2000 characters. |
| CARDREFERENCE | N | <sup>string `[ 12 .. 19 ] characters`</sup> <br>Token reference of an existing Secure Token.<br>If provided, your customer won't be able to change the account details or use a different payment method on the hosted page. |
| SECCODE | N | <sup>string <enum></sup> <br>`CCD` <br>`PPD` <br>`TEL` <br>`WEB` <br>The SEC Code to use for ACH bank transfer. If provided, it will override the default value of `WEB`. |

### Request notes

##### ND001 - Hash generation

See how to generate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**. For this specific feature, you should use one of the following formats:

```
TERMINALID:ORDERID:AMOUNT:DATETIME:RECEIPTPAGEURL:SECRET
```

##### ND002 - Hosted page in an iFrame

> **Warning**
> When embedding the hosted page inside an iframe and using the `sandbox` attribute, ensure that `allow-same-origin` is included in the list of allowed tokens.
> Without this, browser security policies may block scripts from executing properly, leading to CORS-related errors and preventing the page from functioning correctly.
>
> Recommended sandbox configuration:
> `sandbox=“allow-modals allow-forms allow-popups allow-scripts allow-same-origin”`
>
> For more details on the `sandbox` attribute, refer to the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#sandbox)

You can embed our hosted pages within an iframe if you don't want the customer to leave your site. There are two ways to do that:

1. Build and submit the form as with standard integration, but within the iFrame.
1. Construct the request URL, including the parameters as query strings, and set it as the `src` of the iFrame.

Either way, the following extra parameter should also be included in the request:

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| INIFRAME | Y | `Y` - Ensures that all redirects performed by our system do not break out of the iFrame. |

##### ND003 - Storing account details

Give customers the option to store their account details during a payment. To display this option, you just need to include the field below in the request:

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| SECURECARDMERCHANTREF | Y | <sup>string `[ 1 .. 200 ] characters`</sup> <br>Unique Reference assigned by the merchant to identify the stored account details. |

##### ND004 - Cardholder email field

This field is available for all terminals, but depending on the **Hosted payment page email field setup** terminal setting, it might have one of the following behaviors:

- **Hidden** - the gateway accepts the field, if sent, and adds it to the transaction, but does not show it to the customer.
- **Optional** - an optional e-mail field is displayed to the cardholder. If you send the `EMAIL` parameter in the request, we'll use its value to pre-populate the field.
- **Mandatory** - a required e-mail field is displayed to the cardholder. If you send the `EMAIL` parameter in the request, we'll use its value to pre-populate the field.

### Request sample

- **Scenario**: Minimum request containing only mandatory data.
- **Terminal Secret**: x4n35c32RT.

```
<[html](http://december.com/html/4/element/html.html)>
  <[body](http://december.com/html/4/element/body.html)>
    <[form](http://december.com/html/4/element/form.html) action="https://testpayments.worldnettps.com/merchant/paymentpage" method="post">
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="TERMINALID" value="6491003" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="ORDERID" value="1478" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="CURRENCY" value="USD" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="AMOUNT" value="10.00" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="DATETIME" value="28-8-2023:10:20:15:225" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="HASH" value="2eccef7c0a499bf3b1ebed56a59c595c" />
       <[input](http://december.com/html/4/element/input.html) type="submit" value="Pay Now" />
    </[form](http://december.com/html/4/element/form.html)>
  </[body](http://december.com/html/4/element/body.html)>
</[html](http://december.com/html/4/element/html.html)>
```

> **Warning**
> Remember to change the `TERMINALID` and `SECRET` for valid values. Ready to try? **[Sign up](https://developers.worldnetpayments.com/signup)** for a sandbox account.

## Response

Assuming valid details were sent, the hosted page will be displayed to the cardholder and he'll be prompted to enter his card details. Once the payment is processed, the following parameters will be forwarded to the **Receipt URL** configured in your terminal:

| **FIELD** | **DESCRIPTION** |
|---|---|
| ORDERID | <sup>string `[ 1 .. 24 ] characters`</sup> <br>Echoed back from the request. |
| UNIQUEREF | <sup>string `[ 10 ] characters`</sup> <br>Unique reference assigned by the gateway that identifies the transaction on both platforms. **Note:** Clients must be able to store this value in order to eventually perform follow up operation on existing transactions. |
| TRANSIT_NUMBER | <sup>string `[ 5 ] characters`</sup> <br>Client's bank branch/transit number. |
| ROUTING_NUMBER | <sup>string `[ 9 ] characters`</sup> <br>The 9-digit ABA routing transit number of the account. |
| ACCOUNT_NUMBER | <sup>string</sup> <br>Client's bank account number masked with the character `*` except last four digits. |
| INSTITUTION_NUMBER | <sup>string `[ 3 ] characters`</sup> <br>Client's institution number. |
| ACCOUNT_TYPE | <sup>string <enum></sup> <br>`CHECKING` <br>`SAVINGS` <br>The account type of the client's bank account. |
| RESPONSECODE | <sup>string <enum></sup> <br>`A`: Approval <br>`D`: Declined  |
| RESPONSETEXT | <sup>string `[ 0 .. 48 ] characters`</sup> <br>A brief description sent by the processor about the transaction result. |
| DISCOUNT_AMOUNT | <sup>number <double> `> 0`</sup> <br>The discount amount. |
| DATETIME | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>The processing date and time of the transaction. |
| EMAIL | <sup>string `[ 1 .. 128 ] characters`</sup> <br>Echoed back from the request. |
| PHONE | <sup>string `[ 5 .. 20 ] characters`</sup> <br>Echoed back from the request. |
| COUNTRY | <sup>string `2-char ISO 3166-1 code`</sup> <br>Echoed back from the request. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd001_-_hash_validation)</sup> | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the response fields. |
| CUSTOMFIELD | Echoed back from the request. |

### Response notes

##### ND001 - Hash validation

A hash string is also included in the response, so that you can implement a verification logic to make sure it was sent by Worldnet. See how to decode and validate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**.

For this specific feature, you should expect one of the following formats:

```
/**
 * The general case
 */
TERMINALID:ORDERID:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET
```

##### ND002 - Secure Token registration

By including the SECURECARDMERCHANTREF field in the request, you give customers the option to store their account details.
If a customer checks that option, the gateway automatically triggers a secure registration and adds the following extra parameters to the response:

| **FIELD** | **DESCRIPTION** |
|---|---|
| ISSTORED | <sup>boolean</sup> <br>`true`, `false` |
| SCERROR | If `ISSTORED = false`, check out this field for a brief description of the failure. |
| MERCHANTREF | <sup>string `[ 1 .. 200 ] characters`</sup> <br>The same `SECURECARDMERCHANTREF` you sent in the request. |
