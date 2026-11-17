<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:special_fields_and_parameters | synced: 2026-10-05 -->

# Special Fields and Parameters

 During the use of the features, a few fields have special considerations to be aware of. Here we list those fields, which your application should treat correctly to avoid inconsistencies on requests and responses, guaranteeing the right use of our API.

## Hash Parameter

Every request to and response from Worldnet Payments includes an SHA-512 HASH parameter. This is a security element to ensure that none of the sensitive request or response data has been modified by a “*man-in-the-middle*” attack. This is achieved by including all the sensitive fields into a string, which varies per request type, along with the shared secret, configured per terminal. This string is then used as the basis of an SHA-512 HASH.

When explaining the data structure for requests and responses, our **API Specification** is going to present for each feature the formation rule of its Request HASH and its Response HASH. Those rules are going to look like this:

```
TERMINALID:ORDERID:AMOUNT:DATETIME:SECRET
```

The “**:**” (colon) used in the example above is the separator used to concatenate the elements in a string and it **ALWAYS NEEDS TO BE ADDED** to define the separation of two elements.

It's important to understand that the separator should only be used to separate two elements with values.

- element[1]value
- element[1]value:element[2]value
- element[1]value:element[2]value:element[n]value

For example, if a HASH rule formation defines an element which your request doesn't have, you can't use the separator for that element.

Consider a HASH for the following data using the structure presented above:

- **TERMINALID**: 678002
- **ORDERID**: 300145858
- **AMOUNT**: 325.56
- **DATETIME**: 15-3-2006:10:43:01:673
- **SECRET**: x4n35c32RT
 Consider **sha512** your method to apply the SHA-512 encryption, which receives the string formed with the data elements separated by the colon.

```
[String](https://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) hash = sha512("678002:300145858:325.56:15-3-2006:10:43:01:673:x4n35c32RT");
```

 The final **hash** string variable would have the value of:

```
<SAMPLE_HEX_VALUE>
```

Note that the **sha512** method should always use a character encoding of UTF-8, when appropriate, as should all data sent to the payment gateway.

Remember to implement the specific hash rule for each request and response you decide to use from our solutions, exactly as they are described in their features. A few of them may seem similar, but they can differ in small details.

> **Warning**
> **HASH ALGORITHM AND TERMINAL INTEGRATION SETTINGS**
>
> The algorithm used to generate the HASH changed to **SHA-512**, but for older integrations, the platform still accepts HASH calculated with the **MD5** algorithm.
>
> Additionally, there's a configuration which can be used to force the SHA-512 algorithm for a specific terminal in **Integration > Force SHA-512 Hashing Algorithm**.
>
> If you are still using the MD5 algorithm and the SHA-512 is not forced in your terminal, the fields used for the HASH remain the same and no separator (as **:**) is necessary between them.

## The Card Types

The card types that your account supports are determined by your Acquiring Bank and your Merchant Account. The options our payment gateway provide are:

- VISA
- VISA DEBIT
- ELECTRON
- MASTERCARD
- DEBIT MASTERCARD
- MAESTRO
- AMEX
- DINERS
- JCB
- DISCOVER
- CUP SECUREPAY

- VISA
- VISA DEBIT
- ELECTRON
- MASTERCARD
- DEBIT MASTERCARD
- MAESTRO
- LASER
- AMEX
- DINERS
- JCB
- DISCOVER
- CUP SECUREPAY

All live accounts will be set up with the correct card types enabled as per the documentation that Worldnet Payments receive from your Acquiring Bank.

> **Warning**
> Please send any amendments to your merchant account to our support team so we may keep your account details up to date.

For testing purposes we recommend using the test card numbers in our **[Testing Guide - Test Resources](https://developers.worldnetpayments.com/selfcare/integration_docs/testing-guide#testing_resources)** document.

## The Currencies Supported

The following is a list of currency types supported by Worldnet. Other may be added upon request.

| **CURRENCY** | **CURRENCY CODE** | **CODE** |
|---|---|---|
| EURO | EUR | 978 |
| BRITISH POUNDS | GBP | 826 |
| UNITED STATES DOLLARS | USD | 840 |
| AUSTRALIAN DOLLARS | AUD | 36 |
| CANADIAN DOLLARS | CDN | 124 |
| SWISS FRANC | CHF | 756 |
| DANISH KRONE | DKK | 208 |
| HONG KONG DOLLAR | HDK | 344 |
| JAPANESE YEN | JPY | 392 |
| NORWEGIAN KRONE | NOK | 578 |
| NEW ZEALAND DOLLAR | NZD | 554 |
| SWEDISH KRONA | SEK | 752 |
| SOUTH AFRICAN RAND | ZAR | 710 |
| CZECH KORUNA | CZK | 203 |
| SINGAPORE DOLLAR | SGD | 702 |
| THAI BAHT | THB | 764 |
| ICELANDIC KRONA | ISK | 352 |
| HUNGARIAN FORINT | HUF | 348 |
| ARGENTINE PESO | ARS | 32 |
| BAHAMIAN DOLLAR | BSD | 44 |
| BAHRAINI DINAR | BHD | 48 |
| BARBADOS DOLLAR | BBD | 52 |
| BERMUDIAN DOLLAR | BMD | 60 |
| CHINESE YUAN | CNY | 156 |
| COLOMBIAN PESO | COP | 170 |
| INDIAN RUPEE | INR | 365 |
| ISRAELI SHEQEL | ILS | 376 |
| KENYAN SHILLING | KES | 404 |
| SOUTH KOREAN WON | KRW | 410 |
| KUWAITI DINAR | KWD | 414 |
| LATVIAN LATS | LVL | 428 |
| MALAYSIAN RINGGIT | MYR | 458 |
| MEXICAN PESO | MXN | 484 |
| MOROCCAN DIRHAM | MAD | 504 |
| OMANI RIAL | OMR | 512 |
| PANAMANIAN BALBOA | PAB | 590 |
| QUATARI RIAL | QAR | 634 |
| RUSSIAN RUBLE | RUB | 643 |
| SAUDI RIYAL | SAR | 682 |
| TRINIDAD AND TOBAGO DOLLAR | TTD | 780 |
| UAE DIRHAM | AED | 784 |
| NEW TAIWAN DOLLAR | TWD | 901 |
| VENEZUELAN BOLIVAR | VEF | 937 |
| ROMANIAN LEU | RON | 946 |
| TURKISH LIRA | TRY | 949 |
| UKRAINIAN HRYVNIA | UAH | 980 |
| POLISH ZLOTY | PLN | 985 |
| BRAZILIAN REAL | BRL | 986 |

## The Custom Fields

The Custom Fields allow you to send data to our systems with transactions in name-value pairs so that it is stored and can be included in reports, receipts and for other uses. There are two different types of custom fields: Explicit and Implicit.

- **Explicit Custom Fields**: All the custom fields that are mentioned in this document are explicit custom fields, all custom fields in the XML gateway are also. They must be pre-configured in the Selfcare System (**Settings** → **Custom Fields**) for the particular Terminal ID that you are sending the transaction through.
- **Implicit Custom Fields**: Any other fields that are sent to the Hosted Payment Page are considered to be implicit custom fields. These will be returned in the response to the Receipt Page, but will not be stored, sent to the Background Validation URL or available in any reporting features. Implicit custom fields are not supported by the XML gateway.

A Custom Field is set up to be one of three types:

- **1**. **Boolean:** Accepted values are “0”, “1”, “true” or “false”.
- **2**. **Numeric**: Any numeric only value.
- **3**. **String:** Any value containing only alphanumeric characters, spaces or the following characters: '-&*()_+:;@#|.,/

Additionally to that, each Custom Field also defines how it is going to be used:

- **1**. **Virtual Terminal**: defines it can be used on virtual terminal.
- **2**. **Payment Page**: defines it can be used on payment pages.
- **3**. **Bulk Payment**: defines it can be used with bulk payments.
- **4**. **Subscription**: defines it can be used with subscriptions.
- **5**. **Mandatory**: defines that, wherever is used, is mandatory.
- **6**. **Show on Receipt**: defines it should appear on receipts.

Each feature is going to give more details about the use of the Custom Fields in their requests and responses, but be aware that the use of a Custom Field is limited by its configuration.

The configuration of Custom Fields involve two main steps: one realized at the **Gateway** side and another done at the **Merchant** side.

- **1**. **Gateway Side**: The desired Terminal must be enabled with the Custom Fields feature.
- **2**. **Merchant Side**: The Merchant needs to configure the Terminal settings on Selfcare System with the list of Custom Fields which should be available for this Terminal, detailing the interfaces in which they should be used (XML, HPP, other) and the language in which that custom field is available for.

If your application requires to use Custom Fields with Subscriptions, there's still one more configuration step: under the relevant Stored Subscription, the Custom Field needs to be selected.

After that, you can use start using the Custom Fields in your integration, but be sure all the Custom Fields you use are still in place and configured as you expect before putting your integration live.

To use a custom field with a request, first verify if the request you want to use allows the custom fields. If it allows, all you have to do is to add to the request as many custom field tags as you need, using its original NAME at the NAME tag attribute, inform the value you desire, then send the request.

Custom fields size limit is 100 but they will not be rejected if they are bigger than 100, they will be shortened.

Example: registering a Secure Tokens with custom fields to inform the client's loyalty system id (custom field ClientLSID) and the current amount of accumulated points (custom field ClientLSCP).

```
<SECURECARDREGISTRATION>
    ...
    ...
    <CUSTOMFIELD NAME="ClientLSID">343f34fsg68laocaw</CUSTOMFIELD>
    <CUSTOMFIELD NAME="ClientLSCP">2650</CUSTOMFIELD>
    ...
</SECURECARDREGISTRATION>
```

## The Dynamic Descriptors

Transaction descriptors describe a particular payment transaction in order to help the Card Holder to identify this transaction on his/ her bank statement or online bank interface. It's a good practice which helps Merchants to minimize the risk of chargeback, saving money!

> **Note**
> We display the dynamic descriptor on the bank statement only after the processor settled the transaction.

Our **Dynamic Descriptor** feature provides this capability to our Merchants.

The text that appears on the Card Holders statements will be composed of:

- **1**. A **Prefix**, which is a static text value up to 12 characters long that is the same for every transaction followed by;
- **2**. The Dynamic Value, which can be, depending on the terminal settings and the transaction's data: sent in by the website with the transaction, as a Custom Field; adopt the default value defined at the terminal's configuration of the Dynamic Descriptor feature, or; the Terminal Name.

> **Warning**
> Not all Acquirer Banks/ Payment Processors allow this feature, so you need to know if your Terminal has the right one configured.

This feature works together with the **Custom Field** feature and has basically two main steps: one realized at the **Gateway** side and another done at the **Merchant** side.

- **1**. **Gateway Side**: The desired Terminal must be enabled with the Dynamic Descriptor feature and optionally it also can have a Dynamic Descriptor Prefix and a Default Value.
- **2**. **Merchant Side**: Optionally, the Merchant can configure the Terminal settings on Selfcare System pointing out the custom field to be used by each interface (XML, HPP, other) as the value for the Dynamic Descriptor.

See the example below:

| **PROPERTY** | **VALUE** |
|---|---|
| Dynamic Descriptor Prefix | “Order N.” |
| Dynamic Descriptor Default Value | “Purchase at Merchant Example” |
| Interface using the Dynamic Descriptor | Other |
| Associated Custom Field to the Dynamic Descriptor | “Order Number” |

If a Transaction is sent to the gateway with a custom field order number “1805000453”, the Card Holder would see in his/ her bank statement the following additional information for the purchase: “***Order N * 1805000453***”.

If a Transaction is sent to the gateway with no order number, the Card Holder would see in his/ her bank statement the following additional information for the purchase: “***Purchase at Merchant Example***”.

## The Multi-Currency Terminal IDs

Some Acquiring Banks support Multi-currency Terminals. They allow Merchants processing transactions in one of a number of pre-defined currencies for a Terminal. These Terminals have their own terminal ID and may be identified with the letters ‘MC’ after the terminal ID.

It's important to understand that, when processing transactions with one of those Terminals using an integration, your solution has to consider that the **Currency Type** must be added to the request HASH calculation and is going to be added to the response HASH calculation. Details on the HASH calculation for requests and responses involving Multi-currency Terminals are provided by each feature when explaining the HASH body field.

Worldnet Payments will inform you if your Terminal ID supports multi-currency. Contact our integration team if you have any questions relating to multi-currency terminals.

## The Signature Field Format

The signature field is used by some of the features' requests, and follows a set of rules to be formed, as such:

- **-** The SIGNATURE field is a string of characters. Each set of 4 characters represents a point on a 300 pixel wide x 100 pixel tall canvas.
- **-** Each set of 4 characters is comprised of 2 chars to represent the X value (pixel distance right from left side) and 2 chars to represent the Y value (pixel distance from down from top).
- **-** Each 2 char value is a base 28 encoded decimal number (similar to hex which is base 16). Possible values for each character are any numerical digit and the letters from “a” to “r” inclusive (“a” = 10, “b”= 11, etc. just like in hex, but up to “r” = 28). For example “**3bac**” can be calculated as: **(3 x 28<sup>1</sup>) + (11 x 28<sup>0</sup>) = 84 + 11 = 95** from the left and **(10 x 28<sup>1</sup>) + (12 x 28<sup>0</sup>) = 280 + 12 = 292** from the top, hence **3bac** is a point at 95×292 pixels from the top left.
- **-** To include a space between 2 points (no line drawn on signature canvas) include a 0x0 point (encoded as “0000”) in the string.
- **-** Points outside the bounds of the 300×100 pixel canvas will not be rendered, and should not be included.
- **-** The SIGNATURE string can be a minimum length of 4 characters (1 point) and a maximum of 1600 characters (400 points).
- **-** The recording canvas should always have a 3:1 width to height ratio.
- **-** If the canvas that the signature is recorded on is of a larger size, the magnitude of the X and Y values should be scaled down proportionately to a 300×100 boundaries respectively.
- **-** Example SIGNATURE string: “4i1m621m00005a125a2e” will draw a 40×40 pixel “plus” symbol in the middle of the canvas.

## The MaxMind MinFraud Fields

This feature is a complementary service to other features in HP and XML integration methods.

When used, this service provides a score for the transaction between 0.01 and 100 (riskScore), effectively the percentage chance that it could be fraudulent.

Certain fields are required for performing fraud scoring on the transaction using the MaxMind MinFraud service. There is no charge for this service, and it can be enabled in the Terminal Setup section of our Selfcare System.

Each feature of each integration method is going to present details on how to use it, if available, and all you have to do is make sure the terminal in use has this feature settings enabled at its Security & Fraud section, and that your integration is providing the data necessary for the verification.

> **Note**
> Read more about this service is available on the **[[https://www.maxmind.com/en/ccv_overview|MaxMind]]** website.

## The Sentinel Defence Fields

This feature is also an additional service to existing features in HP and XML integration methods.

Sentinel Defence provides software as a service (SaaS) technology that profiles online transactions and activities to determine whether they initiate from fraudsters or legitimate customers.

The Payment Gateway accepts or rejects transactions based on the Sentinel Defence's fraud analysis, enhancing the fraud prevention and threat detection for payment transactions on the Worldnet Payments platform.

Each feature of each integration method is going to present details on how to use it, if available, and all you have to do is make sure the terminal in use has this feature settings enabled at its Security & Fraud section, and that your integration is providing the data necessary for the verification.

> **Warning**
> **TERMINAL CONFIGURATION**: The terminal used to process the transaction must have the Sentinel Defence feature enabled and configured if you want it use on that transaction or any transaction processed by that terminal.

Transactions returned with “REVIEW”, when using Sentinel Defence, need to be manually reviewed by the Merchants. A new report feature on Selfcare System, allows Merchants to manually accept transactions marked as REVIEW by Sentinel Defence, and additionally, the XML gateway allows the use of the status update service to change a transaction to “APPROVE” or “REJECT”, depending on the merchant's needs.

Be aware that Transactions with REVIEW status are not going to be settled until it's rejected or approved by the merchant.
