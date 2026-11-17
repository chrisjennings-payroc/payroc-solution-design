<!-- source: https://developers.worldnetpayments.com/doku.php?id=hosted_pages:hpp_payment_features | synced: 2026-10-05 -->

# Accepting Payments & Pre-Auths

Worldnet-hosted payment page enables you to create secure and fully customized payment forms that let you accept payments on your website.

This solution works across devices and doesn't require much development work, all you need to do is send us a `POST` request with a set of pre-defined fields.

> **Note**
> The request body will be identical for payments and pre-auths, the distintion is made based on the request URL as you can see below.

| **TYPE** | **SANDBOX URL** |
|---|---|
| Payment | `https://testpayments.worldnettps.com/merchant/paymentpage` |
| Pre-Authorization | `https://testpayments.worldnettps.com/merchant/preauthpage` |

## Request

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TERMINALID | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| ORDERID | Y | <sup>string `[ 1 .. 24 ] characters`</sup> <br>A unique identifier for the order assigned by the merchant. |
| CURRENCY <br><sup>See notes: [ND008](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd008_-_international_payments)</sup> | Y | <sup>string `3-char ISO 4217 code`</sup> <br>The currency of the transaction. |
| AMOUNT | Y | <sup>number <double> `> 0`</sup> <br>The total amount to be authorized. |
| DATETIME | Y | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>The transaction date and time. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd001_-_hash_generation)</sup> | Y | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the request fields. |
| CARDHOLDERNAME | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The cardholder's name as it appears on the card. If provided, it will be used to pre-populate the cardholder name field on the payment page. |
| AUTOREADY | N | <sup>string <enum></sup><br>`Y` - The gateway will automatically set the transaction to `READY`, making it eligible to be batched in the next settlement run. <br>`N` - Flags the transaction with a `PENDING` status meaning that the transaction won't be settled until the merchant marks it as ready. <br>If not provided, the terminal default will take place. |
| DESCRIPTION | N | <sup>string `[ 1 .. 1024 ] characters`</sup> <br>A brief description of the transaction. |
| EMAIL <br><sup>See notes: [ND0012](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd0012_-_cardholder_email_field)</sup> | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The cardholder email address. <br>If **Email Cardholder Receipt** feature is enabled on the terminal, we will use this address to delivery transaction receipts to your customer. |
| RECEIPTPAGEURL | N | <sup>string <URI></sup> <br>This is the webhook that Worldnet will use to send you the result of the transactions. If provided, this will override the terminal setting in the Selfcare System. |
| VALIDATIONURL | N | <sup>string <URI></sup> <br>If the feature is enabled on your terminal, Worldnet will use this webhook to perform background validation. If provided, it will overwrite the default **Background Validation URL**. Check out the **[Background Validation](https://developers.worldnetpayments.com/hosted_pages/hpp_background_validation)** guide. |
| TERMINALTYPE | N | <sup>number <integer></sup><br>`1` - As Mail Order/Telephone Order.<br>`2` - eCommerce.<br>Defines how the transaction is to be processed. Mail Order transactions can have a separate payment Page Layout.<br>`3` - Cardholder Present.<br>HPP has support for GENERIC_MSR or SRED_KEYED terminal devices. |
| TRANSACTIONTYPE | N | <sup>number <integer></sup><br>`4` - Normal Mail order/Telephone Order trans (Mail Order for first Data Latvia).<br>`5` - 3DS fully authenticated trans.<br>`6` - 3DS attempted trans.<br>`7` - Normal eCommerce trans.<br>`9` - Telephone Order (First Data Latvia only). |
| ADDRESS1 <br><sup>See notes: [ND004](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd004_-_address_verification_system)</sup> | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The first line of the billing address. |
| ADDRESS2 | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The second line of the billing address. |
| POSTCODE <br><sup>See notes: [ND004](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd004_-_address_verification_system) \| [ND005](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd005_-_maxmind_minfraud)</sup> | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The postal code of the billing address. |
| CITY <br><sup>See notes: [ND004](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd004_-_address_verification_system) \| [ND005](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd005_-_maxmind_minfraud)</sup> | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The city of the billing address. |
| REGION <br><sup>See notes: [ND005](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd005_-_maxmind_minfraud)</sup> | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The region of the billing address. |
| COUNTRY <br><sup>See notes: [ND005](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd005_-_maxmind_minfraud)</sup> | N | <sup>string `2-char ISO 3166-1 code`</sup> <br>The country of the billing address. |
| PHONE | N | <sup>string `[ 5 .. 20 ] characters`</sup> <br>The cardholder phone number. International numeric format. |
| PAYMENTTYPE | N | `CUP_SECUREPAY` - To forward the transaction directly to China Union Pay. |
| CUSTOMFIELD | N | You can send any of the custom fields configured on your terminal. Otherwise, they will be displayed as inputs, so that the cardholder can populate them. All custom fields will be stored along with the transaction details and echoed back to the Receipt URL. Check **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)** for more details. |
| OTHERFIELD | N | Any other fields sent in the request will be treated as metadata. They are not going to be stored, but they'll be echoed back to the Receipt URL. Note that this is subject to the max length of a HTTP GET request which we would conservatively recommend considering to be 2000 characters. |
| ORIGINALBRANDTXIDENTIFIER | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>Reference provided by the card scheme. Only relevant to merchants using a third-party vault for tokenization. |
| STOREDCREDENTIALUSE | N | <sup>string <enum></sup> <br>`UNSCHEDULED`, `INSTALLMENT`, `RECURRING` <br>When cardholders authorize a merchant to store their card details, they must explicitly consent to how their credentials will be used in the future. |
| STOREDCREDENTIALTXTYPE | N | <sup>string <enum></sup> <br>`FIRST_TXN` - The first payment where the customer is signing up for a series of subsequent payments. <br>`SUBSEQUENT_CARDHOLDER_INITIATED_TXN` - A subsequent payment initiated by the cardholder (CIT). <br>`SUBSEQUENT_MERCHANT_INITIATED_TXN` - A subsequent payment initiated by the merchant (MIT) on behalf of the cardholder. |
| CARDREFERENCE | N | <sup>string `[ 12 .. 19 ] characters`</sup> <br>Token reference of an existing Secure Tokens. <br>If provided, your customer won't be able to change the card details or use a different payment method on the hosted page. |
| BYPASS_SURCHARGE | N | <sup>boolean</sup> <br>`true`, `false`. Send a value of 'true' to identify that surcharge has not been applied to this payment. Only applicable if surcharging is enabled for the terminal. |
| PAYMENTOPTIONS | N | <sup>string <enum></sup> <br>`CARD` <br>`BANK_TRANSFER` <br>`CARD_AND_BANK_TRANSFER` <br>Restricts payment options to either cards, bank transfer providers or both. Not providing a value is equivalent to the `CARD_AND_BANK_TRANSFER` option. |

### Request notes

##### ND001 - Hash generation

See how to generate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**. For this specific feature, you should use one of the following formats:

- *For single currency terminals*:

```
TERMINALID:ORDERID:AMOUNT:DATETIME:RECEIPTPAGEURL:VALIDATIONURL:SECRET
```

- *For multi-currency terminals*:

```
TERMINALID:ORDERID:CURRENCY:AMOUNT:DATETIME:RECEIPTPAGEURL:VALIDATIONURL:SECRET
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

##### ND003 - Storing card details

Give customers the option to store their card details during a payment. To display this option, you just need to include the field below in the request:

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| SECURECARDMERCHANTREF | Y | <sup>string `[ 1 .. 200 ] characters`</sup> <br>Unique Reference assigned by the merchant to identify the stored card details. |

##### ND004 - Address Verification System

Address Verification System (AVS) is a service provided by major credit card processors to enable merchants to authenticate ownership of a credit or debit card used by a customer.
It’s done as part of the authorization request where the bank checks the billing address provided by the cardholder against the billing address in its records.

The fields included in the verification process are:

- `ADDRESS1`
- `POSTCODE`
- `CITY`

> **Note**
> From your Selfcare account, you can enable the AVS feature and fully customize the way the address fields behave on the hosted page. For instance, it's possible to choose whether they should be required or optional as well as if they should be displayed to the cardholder or not.

##### ND005 - MaxMind MinFraud

MaxMind provides a score for each transaction between 0.01 and 100 (riskScore), effectively the percentage chance that it could be fraudulent.
Worldnet offers this service free of charge and it can be enabled in the terminal setup section of our Selfcare System. Check out more at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_maxmind_minfraud_fields)**.

Your request must contain at least the following fields to trigger a MaxMind check:

- `CITY`
- `REGION`
- `COUNTRY`

##### ND006 - Multi Language Support

Depending on your customer's browser definitions and if there's a language template defined for his/her language priority, Worldnet is going to send the payment receipt translated. If the language is not supported by the gateway, the receipt is going to be sent using the gateway's language.

##### ND007 - Stored Credential use field behavior and settings

This feature is currently available to TSYS Saratoga terminals and is configurable by customer support. These fields will only be used on a payment if you have Secure Tokens storage enabled. The fields will have the following behavior: Hidden - the gateway accepts the fields, if sent, and adds them to the transaction, but does not show it for the customer.

##### ND008 - International payments

If you want to accept international payments, make sure your account has one of the supported multi-currency processing features enabled.

One common feature is **Dynamic Currency Conversion (DCC)** — a service that allows cardholders to choose between paying in their home currency or the merchant's base currency at the point of transaction. When an international card is detected, the payment gateway will automatically handle the process by presenting a decision screen — hosted by Worldnet — that displays the exchange rate and both currency options. The customer can then select their preferred currency before finalizing the payment.

> **Note**
> No additional integration steps are required to support DCC. The detection of eligible cards and the display of the currency selection screen are handled entirely by the gateway.

##### ND009 - Enhanced Data - Level 2

Add Level 2 data to your transactions by including the following extra fields in the request.
Note that your terminal must support and be enabled to process enhanced data, otherwise these fields will just be ignored.
Make sure to send as much information as possible in order to have a better chance to qualify for the lower Level 2 fees with your bank.

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| CUSTOMER_REF_NUMBER | N | <sup>string `[ 1 .. 48 ] characters`</sup> <br>Sometimes referred to as customer code, it must be sent if provided by the cardholder. |
| TAX_AMOUNT | N | <sup>number <double> `>= 0`</sup> <br>Sales tax amount. <br>`0` - Indicates that the transactions is exempt of tax. |
| SHIPPING_FULL_NAME | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>Shipping address - contact name. |
| SHIPPING_ADDRESS1 | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>Shipping address - first line. |
| SHIPPING_ADDRESS2 | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>Shipping address - second line. |
| SHIPPING_CITY | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>Shipping address - city. |
| SHIPPING_REGION | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>Shipping address - region. |
| SHIPPING_POSTCODE | N | <sup>string `[ 1 .. 50 ] characters`</sup> <br>Shipping address - postal code. |
| SHIPPING_COUNTRY | N | <sup>string `2-char ISO 3166-1 code`</sup> <br>Shipping address - country. |

> **Note**
> This feature is only available for **FDRC** and **TSYS** terminals.

##### ND010 - Enhanced Data - Level 3

Add Level 3 data to your transactions by including the following extra fields in the request.
Note that your terminal must support and be enabled to process enhanced data, otherwise these fields will just be ignored.
Make sure to send as much information as possible and at least one line item in order to have a better chance to qualify for the lower Level 3 fees with your bank.

To include line items, you need to replace the `N` with a sequential count identifier, e.g., `LINE_ITEM_1_PRODUCT_CODE`, `LINE_ITEM_1_TOTAL_AMOUNT` and so on.

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TOTAL_DISCOUNT_AMOUNT | N | <sup>number <double> `>= 0`</sup> <br>Total discount amount applied to the sale. |
| TOTAL_FREIGHT_AMOUNT | N | <sup>number <double> `>= 0`</sup> <br>Total freight amount applied to the sale. |
| TOTAL_DUTY_AMOUNT | N | <sup>number <double> `>= 0`</sup> <br>Total duty amount applied to the sale. |
| LINE_ITEM_`N`_PRODUCT_CODE | N | <sup>string `[ 1 .. 45 ] characters`</sup> <br>This is the merchant’s identifier for the product, also known as Universal Product code (UPC). |
| LINE_ITEM_`N`_COMMODITY_CODE | N | <sup>string `[ 1 .. 45 ] characters`</sup> <br>Item's commodidy code, defined for trade tariff. Widely used by corporate purchasing organizations to segment and manage their total spend across diverse product lines. |
| LINE_ITEM_`N`_DESCRIPTION | N | <sup>string `[ 1 .. 250 ] characters`</sup> <br>This is the merchant’s description for the product. |
| LINE_ITEM_`N`_QUANTITY | N | <sup>number <double> `> 0`</sup> <br>Quantity of the specific item for the sale. |
| LINE_ITEM_`N`_UNIT_OF_MEASURE | N | <sup>string `[ 1 .. 45 ] characters`</sup> <br>Measure unit used for this specific item type to sell it in parts, units or sets. |
| LINE_ITEM_`N`_UNIT_PRICE | N | <sup>number `> 0`</sup> <br>Unit price applied for that specific type of item and measure unit, within the sale. |
| LINE_ITEM_`N`_DISCOUNT_RATE | N | <sup>number <double> `[ 0 .. 100 ]`</sup> <br>A % of discount applied to the item's total amount **before** taxes. |
| LINE_ITEM_`N`_TAX_RATE | N | <sup>number <double> `[ 0 .. 100 ]`</sup> <br>A % of tax applied to the item's total amount **after** discounts. |
| LINE_ITEM_`N`_TOTAL_AMOUNT | N | <sup>number <double> `> 0`</sup> <br>The item's total amount `quantity * unit price` after discounts and taxes. |

> **Note**
> This feature is only available for **TSYS** and **FDRC**.

##### ND011 - Convenience Fee - Line Items

Add Convenience Fee Line Items to your transactions by including the following extra fields in the request.
Note that your terminal must have Convenience Fee enabled, otherwise these fields will just be ignored.

To include line items, you need to replace the N with a sequential count identifier, e.g., LINE_ITEM_N_QUANTITY, LINE_ITEM_N_UNIT_PRICE and so on.

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| LINE_ITEM_N_QUANTITY | N | <sup>number <double> > `> 0`</sup> <br>Quantity of the specific item for the sale. |
| LINE_ITEM_N_UNIT_PRICE | N | <sup>number > `> 0` </sup> <br>Unit price applied for that specific type of item and measure unit, within the sale. |

> **Note**
> This feature is only available for **TSYS** and **FDRC**.

##### ND0012 - Cardholder email field

This field is available for all terminals, but depending on the **Hosted payment page email field setup** terminal setting, it might have one of the following behaviors:

- **Hidden** - the gateway accepts the field, if sent, and adds it to the transaction, but does not show it to the customer.
- **Optional** - an optional e-mail field is displayed to the cardholder. If you send the `EMAIL` parameter in the request, we'll use its value to pre-populate the field.
- **Mandatory** - a required e-mail field is displayed to the cardholder. If you send the `EMAIL` parameter in the request, we'll use its value to pre-populate the field.

> **Warning**
> The email address will be mandatory for transactions with 3-D Secure Authentication.

### Request sample

- **Scenario**: Minimum request containing only mandatory data.
- **Terminal Secret**: x4n35c32RT.

```
<[html](http://december.com/html/4/element/html.html)>
  <[body](http://december.com/html/4/element/body.html)>
    <[form](http://december.com/html/4/element/form.html) action="https://testpayments.worldnettps.com/merchant/paymentpage" method="post">
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="TERMINALID" value="6491002" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="ORDERID" value="3281" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="CURRENCY" value="EUR" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="AMOUNT" value="10.00" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="DATETIME" value="15-3-2023:10:43:01:673" />
       <[input](http://december.com/html/4/element/input.html) type="hidden" name="HASH" value="56083f2c6aa3d233dade436b1308805a" />
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
| APPROVALCODE | <sup>string `[ 0 .. 48 ] characters`</sup> <br>The authorization code assigned by the payment processor for approved transactions. |
| RESPONSECODE | <sup>string <enum></sup> <br>`A`: Approval <br>`E`: Accepted (China Union Pay only) <br>`D`: Declined <br>`R`: Referral <br>`C`: Pick Up <br>For more details, visit **[Transaction Responses](https://developers.worldnetpayments.com/selfcare/integration_docs/transaction_responses)**. |
| RESPONSETEXT | <sup>string `[ 0 .. 48 ] characters`</sup> <br>A brief description sent by the processor about the transaction result. |
| DATETIME | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>The processing date and time of the transaction. |
| AVSRESPONSE | <sup>string `1 character`</sup> <br>The result of the AVS check. See **[Transaction Responses](https://developers.worldnetpayments.com/merchant/existing_merchant/other_information/transaction_responses)** for a full list of AVS response codes. |
| CVVRESPONSE | <sup>string `1 character`</sup> <br>The result of the CVV check. See **[Transaction Responses](https://developers.worldnetpayments.com/merchant/existing_merchant/other_information/transaction_responses)** for a full list of CVV response codes. |
| UNIQUEREF | <sup>string `10 characters`</sup> <br>Unique reference number assigned by the gateway that should be stored to be able to perform follow up operations, such as reversals and refunds. |
| EMAIL | <sup>string `[ 1 .. 128 ] characters`</sup> <br>Echoed back from the request. |
| PHONE | <sup>string `[ 5 .. 20 ] characters`</sup> <br>Echoed back from the request. |
| COUNTRY | <sup>string `2-char ISO 3166-1 code`</sup> <br>Echoed back from the request. |
| CARDNUMBER | <sup>string `[ 12 .. 19 ] characters`</sup> <br>The card number masked as per PCI requirements. |
| CARDTYPE | Card type used for the transaction.<br>For more details on this, visit **[Special Fields and Parameters - Card Types](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_card_types)**. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_payment_features#nd001_-_hash_validation)</sup> | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the response fields. |
| CUSTOMFIELD | Echoed back from the request. |
| OTHERFIELD | Echoed back from the request. |
| BRANDTXIDENTIFIER | Echoed back from the request. |
| STOREDCREDENTIALUSE | Echoed back from the request. |
| STOREDCREDENTIALTXTYPE | Echoed back from the request. |
| ACCEPTTERMSANDCONDITIONS | <sup>string <enum></sup> <br>ON - The user accepted the convenience terms & conditions |
| CONVENIENCE_FEE | <sup>number <double> `> 0` </sup> <br>A service fee charged on the transaction |
| SURCHARGE_FEE | <sup>number <double> `> 0` </sup> <br>Surcharge amount. This field will be returned whenever a surcharge fee is applied to the transaction. |
| SURCHARGE_PERCENT | <sup>number <double> `[ 0 .. 100 ]` </sup> <br>Surcharge percentage. This field will be returned whenever a surcharge fee is applied to the transaction. |

### Response notes

##### ND001 - Hash validation

A hash string is also included in the response, so that you can implement a verification logic to make sure it was sent by Worldnet. See how to decode and validate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**.

For this specific feature, you should expect one of the following formats:

- *For single currency terminals*:

```
/**
 * The general case
 */
TERMINALID:ORDERID:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET
 
/**
 * When a secure token is registered as part of the transaction
 */
TERMINALID:ORDERID:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET:MERCHANTREF:CARDREFERENCE:CARDTYPE:CARDNUMBER:CARDEXPIRY
```

- *For multi-currency terminals*:

```
/**
 * The general case
 */
TERMINALID:ORDERID:CURRENCY:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET
 
/**
 * When a secure token is registered as part of the transaction
 */
TERMINALID:ORDERID:CURRENCY:AMOUNT:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET:MERCHANTREF:CARDREFERENCE:CARDTYPE:CARDNUMBER:CARDEXPIRY
```

##### ND002 - Secure token registration

By including the `SECURECARDMERCHANTREF` field in the request, you give customers the option to store their card details.
If a customer checks that option, the gateway automatically triggers a secure registration and adds the following extra parameters to the response:

| **FIELD** | **DESCRIPTION** |
|---|---|
| ISSTORED | <sup>boolean</sup> <br>`true`, `false` |
| SCERROR | If `ISSTORED = false`, check out this field for a brief description of the failure. |
| MERCHANTREF | <sup>string `[ 1 .. 200 ] characters`</sup> <br>The same `SECURECARDMERCHANTREF` you sent in the request. |
| CARDREFERENCE | <sup>string `[ 12 .. 19 ] characters`</sup> <br>The reference number assigned by Worldnet, this is the token that represents the card details. |
| CARDEXPIRY | <sup>string `MMYY`</sup> <br>Expiry date of the card. |

##### ND003 - Dynamic Currency Conversion (DCC)

If the cardholder accepts the DCC offer and chooses to complete the payment in their local currency, the gateway applies the agreed foreign exchange rate to the transaction amount. The response will include the following parameters, which reflect the final amount and conditions under which the transaction was processed.

| **FIELD** | **DESCRIPTION** |
|---|---|
| FX_AMOUNT | <sup>number <double> `> 0`</sup> <br>The transaction amount in the cardholder’s currency. |
| FX_CURRENCY | <sup>string `3-char ISO 4217 code`</sup> <br>The cardholder currency. |
| FX_RATE | <sup>number <double> `> 0`</sup> <br>The foreign exchange rate. |
| FX_MARKUP | <sup>number <double> `>= 0`</sup> <br>The markup fee (%) charged by the DCC provider. |
| FX_PROVIDER | <sup>string</sup> <br>The name of the DCC provider. |

##### Cardholder receipt requirements

To remain compliant with card scheme regulations, the **cardholder’s copy** of the receipt must clearly display the foreign exchange conversion details as part of the final transaction record, following the specific formatting and wording guidelines required by the schemes.

To meet these requirements, the following additional elements must be included on your receipts alongside the standard transaction details.

| **RECEIPT FIELD** | **FORMAT** | **EXAMPLE** |
|---|---|---|
| Transaction Amount | <sup>`{FX_CURRENCY}` `{FX_AMOUNT}`</sup> | GBP 9.03 |
| Exchange Rate | <sup>1`{CURRENCY}` = `{FX_RATE}{FX_CURRENCY}`</sup> | 1EUR = 0.903GBP |
| Markup | <sup>`{FX_MARKUP}`%</sup> <br>Note: The suffix “over ECB rate” must be appended for EEA currencies. | 3.73% over ECB rate |

In addition to the fields above, the receipt must include the following acceptance statement, as required by card schemes:

*I have been offered a choice of currencies and have chosen to accept DCC and pay in `{FX_CURRENCY}` at today’s exchange rate provided by `{FX_PROVIDER}`.*

##### Additional notes

- The DCC decision is fully handled by the gateway, and these fields are returned only when the cardholder has accepted the offer.

- Failure to display this information properly can result in non-compliance with card scheme rules, chargebacks, or disputes.

- Merchants are responsible for ensuring that their customer receipts comply with these requirements.

### General constraints and rules

| **CONSTRAINT** | **DESCRIPTION** |
|---|---|
| C001 | To use the hosted pre-auth page, your terminal must be enabled to process pre-auth transactions. |
| C002 | Pre-authorizations require an extra step called **completion** or **capture**, this operation can be done using our Selfcare System or via our [REST API](https://developers.worldnetpayments.com/apis/merchant/#operation/capturePayment). <br>If a pre-auth is not captured, it'll never settle and it'll expire after some time. |
| C003 | The final amount of a pre-auth transaction can be adjusted on completion. |
