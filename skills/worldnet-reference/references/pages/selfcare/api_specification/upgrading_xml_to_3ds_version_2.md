<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:upgrading_xml_to_3ds_version_2 | synced: 2026-10-05 -->

# PSD2 - Upgrading your XML Integration to 3D Secure version 2

If your integration already supports XML 3D Secure (3DS) 1.0, to support the new directives within the PSD2 regulations it is necessary to make some small changes.

When using 3DS 1.0 it is not necessary to add the Cardholder Name in the REQUEST BODY for the 3D Secure Verification. For 3DS 2.0 it is necessary to add the CARDHOLDERNAME tag containing the Cardholder Name entered by the user when performing the transaction.

**PSD2 and Strong Customer Authentication (SCA)**

The Payment Services Directive 2 (PSD2) comes into force in 2020 (only applicable in EU) and you might need to be prepared to provide SCA for your payments. Take a closer look at our **[F.A.Q](https://resources.worldnetpayments.com/blog/psd2-faq)** if you have more questions.

The process is described in the flowchart below.

[](https://developers.worldnetpayments.com/_detail/selfcare/api_specification/xml_detailed_3_.png?id=selfcare%3Aapi_specification%3Aupgrading_xml_to_3ds_version_2)

1. A POST request is made to the Worldnet Payments server. The server will handle the user authentication.

2. After authentication, the server will redirect to the URL set in the MPI Receipt URL in the `Selfcare > Settings > Terminal` section with the authentication results passed in the URL.

3. In your integration add the MPIREF code to your XML payment and send a payment load to the XML Request URL. For further details, check [XML Payment Features](https://developers.worldnetpayments.com/selfcare/api_specification/xml_payment_features).

4. If the payment is successful, the server will return an approval message.

The following resources are the same for all the requests and responses you find in this page:

| **TYPE** | **URL** |
|---|---|
| Request URL | https://testpayments.worldnettps.com/merchant/mpi |

**3D SECURE LIVE**

This URL should be used in test mode only. Please contact the Worldnet Payments support team to receive the live URL.

## 3D Secure Check

### Request Body Fields

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TERMINALID | Y | A Terminal ID provided by Worldnet Payments. NB - Please contact Worldnet Payments to be issued with a test terminal ID. |
| CARDNUMBER | Y | The payment card number. |
| **CARDHOLDERNAME** | Y | Required for 3DS 2.0 - The name on the front of the credit card. |
| CARDEXPIRY | Y | 4 digit expiry field (MMYY). |
| CARDTYPE | Y | See **[ Card Types](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_card_types)** section. |
| AMOUNT | Y | The amount of the transaction as a 2 digit decimal or an Integer value for JPY amounts. |
| CURRENCY | Y | A 3 character currency code of the transaction. |
| ORDERID | Y | A unique identifier for the order created by the merchant (Max 24 characters). |
| CVV | N | The security code entered by the card holder. |
| DATETIME | Y | Request date and time. Format: DD-MM-YYYY:HH:MM:SS:SSS. |
| HASH | Y | A HASH code formed by part of the request fields. The formation rule is given at the **ND001 - Hash Formation**, in the next section. |

### Notes and Details About the Request

**ND001 - Hash Formation**

The general rule to build HASH field is given at the **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)** page. For this specific feature, you should use the following formats:

TERMINALID:ORDERID:CARDNUMBER:CARDEXPIRY:CARDTYPE:AMOUNT:DATETIME:SECRET

### Response Body Fields

The response body fields will be the same as from your previous integration. For details about the response, check the [XML 3D Secure](https://developers.worldnetpayments.com/selfcare/api_specification/xml_3d_secure) page.
