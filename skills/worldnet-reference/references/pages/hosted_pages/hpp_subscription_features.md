<!-- source: https://developers.worldnetpayments.com/doku.php?id=hosted_pages:hpp_subscription_features | synced: 2026-10-05 -->

# Creating Subscriptions

This feature enables you to set up subscription payments using a hosted page.

- Sandbox URL: `https://testpayments.worldnettps.com/merchant/subscriptionpage/register`

## Request

#### To create a new subscription based on an existing payment plan (stored subscription):

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TERMINALID | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| MERCHANTREF | Y | <sup>string `[ 1 .. 48 ] characters`</sup> <br>Unique reference assigned by the merchant to identify the subscription. |
| STOREDSUBSCRIPTIONREF | Y | <sup>string `[ 1 .. 48 ] characters`</sup> <br>Reference of an existing payment plan (stored subscription). <br>You can also create a payment plan while creating the subscription, check out the next section. |
| SECURECARDMERCHANTREF | Y | <sup>string `[ 1 .. 200 ] characters`</sup> <br>Merchant reference of an existing Secure Token which will be used in the initial and all subsequent payments. <br>When using this field, please do **not** include the `CARDREFERENCE`. |
| CARDREFERENCE | Y | <sup>string `[ 12 .. 19 ] characters`</sup> <br>Token reference of an existing Secure Token.<br>When using this field, please do **not** include the `SECURECARDMERCHANTREF`. |
| SUBSCRIPTIONRECURRINGAMOUNT | N | <sup>number <double> `>= 0`</sup> <br>Cost of each payment to be processed for the subscription. |
| SUBSCRIPTIONINITIALAMOUNT | N | <sup>number <double> `>= 0`</sup> <br>Initial (set-up) payment to be taken off card. Payment will not be taken if it is 0. |
| DATETIME | Y | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>Date and time of the request. |
| STARTDATE | Y | <sup>string <date> `dd-MM-yyyy`</sup> <br>Subscription start date. |
| ENDDATE | N | <sup>string <date> `dd-MM-yyyy`</sup> <br>Subscription end date. If not provided, subscription will continue until manually canceled or length reached (if it is set). |
| SECCODE | N | <sup>string <enum></sup> <br>`CCD` <br>`PPD` <br>`TEL` <br>`WEB` <br>The SEC Code which will be used in the initial and all subsequent ACH bank transfer payments. If provided, it will override the default value of `PPD`. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_subscription_features#nd001_-_hash_generation)</sup> | Y | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the request fields. |

#### To create a new subscription, and at the same time, create a new payment plan (stored subscription):

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TERMINALID | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| MERCHANTREF | Y | <sup>string `[ 1 .. 48 ] characters`</sup> <br>Unique reference assigned by the merchant to identify the subscription. |
| SECURECARDMERCHANTREF | Y | <sup>string `[ 1 .. 200 ] characters`</sup> <br>Merchant reference of an existing Secure Token which will be used in the initial and all subsequent payments. <br>When using this field, please do **not** include the `CARDREFERENCE`. |
| CARDREFERENCE | Y | <sup>string `[ 12 .. 19 ] characters`</sup> <br>Token reference of an existing Secure Token.<br>When using this field, please do **not** include the `SECURECARDMERCHANTREF`. |
| DATETIME | Y | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>Date and time of the request. |
| STARTDATE | Y | <sup>string <date> `dd-MM-yyyy`</sup> <br>Subscription start date. |
| ENDDATE | N | <sup>string <date> `dd-MM-yyyy`</sup> <br>Subscription end date. If not provided, subscription will continue until manually canceled or length reached (if it is set). |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_subscription_features#nd001_-_hash_generation)</sup> | Y | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the request fields. |
| NEWSTOREDSUBSCRIPTIONREF | N | <sup>string `[ 1 .. 48 ] characters`</sup> <br>Merchant Ref to be assigned for the payment plan (stored subscription) being created. |
| NAME | Y | <sup>string `[ 5 .. 128 ] characters`</sup> <br>Display name for subscription. |
| DESCRIPTION | Y | <sup>string `[ 0 .. 128 ] characters`</sup> <br>A brief description of the subscription. |
| PERIODTYPE | Y | <sup>string <enum></sup> <br>The frequency of which payments are collected. <br>`2` - WEEKLY<br>`3` - FORTNIGHTLY<br>`4` - MONTHLY<br>`5` - QUARTERLY<br>`6` - YEARLY. |
| LENGTH | Y | <sup>number <integer> `>= 0`</sup> <br>Total number of billing cycles. <br>Send a value of `0` to set the subscription's billing cycle to never expire (Unlimited). |
| RECURRINGAMOUNT | Y | <sup>number <double> `>= 0`</sup> <br>Cost of each payment (will be ignored if manual). |
| INITIALAMOUNT | Y | <sup>number <double> `>= 0`</sup> <br>Initial (set-up) payment to be taken off card. Payment will not be taken if it is 0. Setup fails if setup payment declines. |
| TYPE | Y | <sup>string <enum></sup> <br>The type by which payments are collected. <br>`1` - AUTOMATIC <br>`2` - MANUAL <br>`3` - AUTOMATIC (WITHOUT AMOUNTS). |
| ONUPDATE | Y | <sup>string <enum></sup> <br>`1` - CONTINUE <br>`2` - UPDATE |
| ONDELETE | Y | <sup>string <enum></sup> <br>`1` - CONTINUE <br>`2` - CANCEL |
| CURRENCY | N | <sup>string 3-char ISO 4217 code</sup> <br>The currency of the payment plan. |
| OTHERFIELD | N | Any other fields sent in the request will be treated as metadata. They are not going to be stored, but they'll be echoed back to the Receipt URL. Note that this is subject to the max length of a HTTP GET request which we would conservatively recommend considering to be 2000 characters. |

### Request notes

##### ND001 - Hash generation

See how to generate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**. For this specific feature, you should use one of the following formats:

```
/**
 * If your request contains the {@code CARDREFERENCE} field
 */
TERMINALID:MERCHANTREF:CARDREFERENCE:DATETIME:STARTDATE:SECRET
```

```
/**
 * If your request contains the {@code SECURECARDMERCHANTREF} field
 */
TERMINALID:MERCHANTREF:SECURECARDMERCHANTREF:DATETIME:STARTDATE:SECRET
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

##### ND003 - International customers

If you want to accept international payments, make sure your account has one of the supported multi-currency processing features enabled.

One common feature is **Dynamic Currency Conversion (DCC)** — a service that allows cardholders to choose between paying in their home currency or the merchant's base currency at the point of transaction. When setting up a subscription for a foreign card, the payment gateway will automatically handle the process by presenting a decision screen — hosted by Worldnet — that displays the exchange rate and both currency options. The customer can then select their preferred currency before finalizing the payment.

##### ND004 - Enhanced Data - Level 2

You can add Level 2 data to your subscriptions by including the following extra fields in the request.
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
> This feature is only available for **FDRC** terminals.

### Request sample

- **Scenario**: Minimum request containing only mandatory data and using an existing payment plan (stored subscription).
- **Stored Subscription Ref**: 6523423
- **Secure Tokens Reference**: 237498
- **Terminal Secret**: x4n35c32RT

```
<[html](http://december.com/html/4/element/html.html)>
  <[body](http://december.com/html/4/element/body.html)>
    <[form](http://december.com/html/4/element/form.html) action="https://testpayments.worldnettps.com/merchant/paymentpage" method="post">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="TERMINALID" value="6491002">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="MERCHANTREF" value="26352">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="STOREDSUBSCRIPTIONREF" value="6523423">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="SECURECARDMERCHANTREF" value="237498">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="DATETIME" value="03-08-2023:17:32:18:329">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="STARTDATE" value="04-08-2023">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="ENDDATE" value="03-08-2010">
      <[input](http://december.com/html/4/element/input.html) type="hidden" name="HASH" value="d880c3e63d5acf0c23737c742ad63e7b">
      <[input](http://december.com/html/4/element/input.html) type="submit" value="Register">
    </[form](http://december.com/html/4/element/form.html)>
  </[body](http://december.com/html/4/element/body.html)>
</[html](http://december.com/html/4/element/html.html)>
```

> **Warning**
> Remember to change the `TERMINALID` and `SECRET` for valid values. Ready to try? **[Sign up](https://developers.worldnetpayments.com/signup)** for a sandbox account.

## Response

Assuming valid details were sent, the subscription registration hosted page will be displayed, clicking on “Accept & Subscribe” button will create the subscription. Once the registration is complete, the following parameters will be forwarded to the **Subscription Receipt URL** configured in your terminal:

| **FIELD** | **DESCRIPTION** |
|---|---|
| RESPONSECODE <br><sup>See notes: [ND003](https://developers.worldnetpayments.com/hosted_pages/hpp_subscription_features#nd002_-_response_codes_-_errors)</sup> | <sup>string <enum></sup> <br>`A`: Approval. <br>`C`: Cancelled. |
| RESPONSETEXT | <sup>string `[ 1 .. 48 ] characters`</sup> <br>The text of the response. |
| MERCHANTREF | <sup>string `[ 1 .. 48 ] characters`</sup> <br>The `MERCHANTREF` provided in the request. |
| DATETIME | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>The time of the registration. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_subscription_features#nd001_-_hash_validation)</sup> | A HASH code formed by part of the response fields. |

### Response notes

##### ND001 - Hash validation

A hash string is also included in the response, so that you can implement a verification logic to make sure it was sent by Worldnet. See how to decode and validate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**.

For this specific feature, you should expect the following format:

```
TERMINALID:MERCHANTREF:DATETIME:RESPONSECODE:RESPONSETEXT:SECRET
```

##### ND002 - Response Codes - Errors

| **Error Code** | **Description** |
|---|---|
| E01 | SYSTEM ERROR - TRY AGAIN |
| E03 | OPERATION NOT ALLOWED |
| E06 | INVALID TERMINALID |
| E07 | METHOD NOT SUPPORTED |
| E08 | INVALID MERCHANTREF |
| E09 | INVALIDE DATETIME |
| E13 | INVALID HASH |
| E20 | INVALID LENGTH |
| E21 | INVALID PERIOD TYPE |
| E22 | INVALID NAME |
| E23 | INVALID DESCRIPTION |
| E24 | INVALID RECURRINGAMOUNT |
| E25 | INVALID INTIALAMOUNT |
| E26 | INVALID TYPE |
| E27 | INVALID ONUPDATE |
| E28 | INVALID ONDELETE |
| E29 | INVALID TERMINAL CURRENCY |
| E30 | INVALID STORED SUBSCRIPTION REF |
| E31 | INVALID STORED SUBSCRIPTION MERCHANT REF |
| E32 | INVALID SECURE TOKEN MERCHANT REF |
| E33 | INVALID STARTDATE |
| E34 | INVALID ENDDATE |
| E35 | INVALID EDCCDESICION |
| E36 | SETUP PAYMENT PROCESSING ERROR |
| E37 | INVALID SUBSCRIPTIONRECURRINGAMOUNT |
| E38 | INVALID SUBSCRIPTIONINITIALAMOUNT |
| E39 | SECURE TOKEN NOT VALIDATED |
| E41 | PASS ONLY ONE OF CARDREFERENCE OR SECURECARDMERCHANTREF OR SECUREACHACCOUNTMERCHANTREF |
| E42 | INVALID SECURE ACH ACCOUNT MERCHANT REF |
| E43 | AMOUNT IS NOT VALID |
| E45 | MULTIPLE PAYMENTS FOR ONE PERIOD IS NOT ALLOWED |
| E46 | SUBSCRIPTION HAS SKIP PERIOD |
| E47 | INVALID BANK IDENTIFIER |
| E48 | INVALID SECURE TOKEN REFERENCE |
| E60 | INVALID SECURE ACH MERCHANT REF |
| E61 | INVALID SECURE ACH REFERENCE |
| E65 | INVALID RECEIPT SUBSCRIPTION URL |
| E67 | INVALID HOST |
| E68 | UNSUPPORTED PAYMENT NETWORK FOR BANK TRANSFERS |
| E69 | UNSUPPORTED CURRENCY FOR CARD PROCESSING |
| E70 | UNSUPPORTED CURRENCY FOR BANK TRANSFER PROCESSING |

### General constraints and rules

| **CONSTRAINT** | **DESCRIPTION** |
|---|---|
| C001 | To create a subscription, you need to provide a valid, existing Secure Token. You may either use the `SECURECARDMERCHANTREF` or the `CARDREFERENCE` field for that, but never both. |
| C002 | When requesting the creation of a new subscription, you may also create your payment plan (stored subscription), or use an existing one. |
| C003 | When requesting the creation of a new subscription based on an existing payment plan (stored subscription), you need to provide a valid `STOREDSUBSCRIPTIONREF`. |
