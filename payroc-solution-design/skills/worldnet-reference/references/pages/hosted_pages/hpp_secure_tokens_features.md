<!-- source: https://developers.worldnetpayments.com/doku.php?id=hosted_pages:hpp_secure_tokens_features | synced: 2026-10-05 -->

# Registering Secure Tokens

This feature enables you to store your customers' card details using a hosted page.

- Sandbox URL: `https://testpayments.worldnettps.com/merchant/securecardpage`

## Request

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| ACTION | Y | <sup>string <enum> `register`, `update`</sup> <br>The action that determines whether you're trying to store or update a Secure Tokens. |
| TERMINALID | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| MERCHANTREF | Y | <sup>string `[ 1 .. 200 ] characters`</sup> <br>Unique Reference assigned by the merchant to identify the stored card details. |
| EMAIL <br><sup>See notes: [ND004](https://developers.worldnetpayments.com/hosted_pages/hpp_secure_tokens_features#nd004_-_cardholder_email_field)</sup> | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The cardholder email address. |
| DATETIME | Y | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>Date and time of the request. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_secure_tokens_features#nd001_-_hash_generation)</sup> | Y | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the request fields. |
| STOREDCREDENTIALUSE | N | <sup>string <enum> `UNSCHEDULED`, `INSTALLMENT`, `RECURRING`</sup> <br>When cardholders authorize a merchant to store their card details, they must explicitly consent to how their credentials will be used in the future. |
| PAYMENTOPTIONS | N | <sup>string <enum></sup> <br>`CARD` <br>`BANK_TRANSFER` <br>`CARD_AND_BANK_TRANSFER` <br>Restricts payment options to either cards, bank transfer providers or both. Not providing a value is equivalent to the `CARD_AND_BANK_TRANSFER` option. |

### Request notes

##### ND001 - Hash generation

See how to generate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**. For this specific feature, you should use the following format:

```
TERMINALID:MERCHANTREF:DATETIME:ACTION:SECRET
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

##### ND003 - Updating Secure Tokens

To initiate card details updating, the value of the ACTION parameter should be changed to `update`. Updates are performed based on the `MERCHANTREF` field.

##### ND004 - Cardholder email field

This field is available for all terminals, but depending on the **Hosted token page email field setup** terminal setting, it might have one of the following behaviors:

- **Hidden** - the gateway accepts the field, if sent, and adds it to the transaction, but does not show it to the customer.
- **Optional** - an optional e-mail field is displayed to the cardholder. If you send the `EMAIL` parameter in the request, we'll use its value to pre-populate the field.
- **Mandatory** - a required e-mail field is displayed to the cardholder. If you send the `EMAIL` parameter in the request, we'll use its value to pre-populate the field.

> **Warning**
> The email address will be mandatory for terminals that have 3-D Secure Authentication enabled.

### Request sample

- **Scenario**: Minimum request containing only mandatory data.
- **Terminal Secret**: mySharedSecretUSD

```
<[html](http://december.com/html/4/element/html.html)>
  <[body](http://december.com/html/4/element/body.html)>
    <[form](http://december.com/html/4/element/form.html) action="https://testpayments.worldnettps.com/merchant/securecardpage" method="post">
        <[input](http://december.com/html/4/element/input.html) type="hidden" name="ACTION" value="register" />
        <[input](http://december.com/html/4/element/input.html) type="hidden" name="TERMINALID" value="4480001" />
        <[input](http://december.com/html/4/element/input.html) type="hidden" name="MERCHANTREF" value="1234321" />
        <[input](http://december.com/html/4/element/input.html) type="hidden" name="DATETIME" value="15-3-2023:10:43:01:673" />
        <[input](http://december.com/html/4/element/input.html) type="hidden" name="HASH" value="<SAMPLE_HEX_VALUE>" />
        <[input](http://december.com/html/4/element/input.html) type="submit" value="Register" />
    </[form](http://december.com/html/4/element/form.html)>
  </[body](http://december.com/html/4/element/body.html)>
</[html](http://december.com/html/4/element/html.html)>
```

> **Warning**
> Remember to change the `TERMINALID` and `SECRET` for valid values. Ready to try? **[Sign up](https://developers.worldnetpayments.com/signup)** for a sandbox account.

## Response

Assuming valid details were sent, the hosted page will be displayed to the cardholder and he'll be prompted to enter his card details. Once the registration is complete, the following parameters will be forwarded to the **Secure Tokens URL** configured in your terminal:

| **FIELD** | **DESCRIPTION** |
|---|---|
| RESPONSECODE <br><sup>See notes: [ND002](https://developers.worldnetpayments.com/hosted_pages/hpp_secure_tokens_features#nd002_-_response_error_codes)</sup> | `A` - Approval |
| RESPONSETEXT | <sup>string `[ 1 .. 48 ] characters`</sup> <br>The text of the response. |
| MASKEDCARDNUMBER | <sup>string `[ 12 .. 19 ] characters`</sup> <br>The registered or updated card number masked as per PCI requirements. |
| MERCHANTREF | <sup>string `[ 1 .. 200 ] characters`</sup> <br>The `MERCHANTREF` provided in the request. |
| CARDREFERENCE | <sup>string `[ 12 .. 19 ] characters`</sup> <br>The reference number assigned by Worldnet, this is the token that represents the card details. |
| CARDTYPE | Card type used for the transaction. <br>For more details on this, visit **[Special Fields and Parameters - Card Types](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_card_types)**. |
| CARDEXPIRY | <sup>string `MMYY`</sup> <br>Expiry date of the card. |
| TRANSITNUMBER | <sup>string `[ 5 ] characters`</sup> <br>Client's bank branch/transit number. |
| ROUTINGNUMBER | <sup>string `[ 9 ] characters`</sup> <br>The 9-digit ABA routing transit number of the account. |
| ACCOUNTNUMBER | <sup>string</sup> <br>Client's bank account number masked with the character `*` except last four digits. |
| INSTITUTIONNUMBER | <sup>string `[ 3 ] characters`</sup> <br>Client's institution number. |
| ACCOUNTTYPE | <sup>string <enum></sup> <br>`CHECKING` <br>`SAVINGS` <br>The account type of the client's bank account. |
| DATETIME | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>The time of the registration. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/hosted_pages/hpp_secure_tokens_features#nd001_-_hash_validation)</sup> | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the response fields. |
| STOREDCREDENTIALUSE | <sup>string <enum> `UNSCHEDULED`, `INSTALLMENT`, `RECURRING`</sup> <br>The same value you provided in the request will be echoed back here. |
| STOREDCREDENTIALTXTYPE | <sup>string <enum> `FIRST_TXN`, `SUBSEQUENT_MERCHANT_INITIATED_TXN`, `SUBSEQUENT_CARDHOLDER_INITIATED_TXN`</sup> <br>Since this is registration, the gateway will always return `FIRST_TXN`. |
| BRANDTXIDENTIFIER | <sup>string `[ 1 .. 64 ] characters`</sup> <br>Reference provided by the card scheme. It's the link to the payment history between a customer and a merchant. |

### Response notes

##### ND001 - Hash validation

A hash string is also included in the response, so that you can implement a verification logic to make sure it was sent by Worldnet. See how to decode and validate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**.

For this specific feature, you should expect the following format:

```
TERMINALID:RESPONSECODE:RESPONSETEXT:MERCHANTREF:CARDREFERENCE:DATETIME:SECRET
```

##### ND002 - Response error codes

| **Error Code** | **Description** |
|---|---|
| E01 | SYSTEM ERROR – TRY AGAIN |
| E03 | OPERATION NOT ALLOWED |
| E04 | INVALID REFERENCE DETAILS |
| E05 | INVALID CARD TYPE |
| E06 | INVALID TERMINALID |
| E07 | METHOD NOT SUPPORTED |
| E08 | INVALID MERCHANTREF |
| E09 | INVALID DATETIME |
| E10 | INVALID CARDNUMBER |
| E11 | INVALID CARDEXPIRY |
| E12 | INVALID CARDHOLDERNAME |
| E13 | INVALID HASH |
| E14 | CVV VALIDATION FAILED |
| E24 | SECURE TOKEN IS USED IN SUBSCRIPTION |
| E32 | SECURE TOKEN ALREADY EXISTS |
| E33 | INVALID ENCRYPTION METHOD |
| E42 | INAPPROPRIATE CARD NUMBER USAGE |
| E43 | APPROVED BUT ACCOUNT NOT VALIDATED |
| E44 | BANK ACCOUNT VALIDATION FAILED |
