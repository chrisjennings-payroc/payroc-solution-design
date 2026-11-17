<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:3d_secure_payroc | synced: 2026-10-05 -->

# 3D Secure and Strong Customer Authentication (SCA)

Strong Customer Authentication (SCA) came into force in 2019 as part of the PSD2 regulation in Europe. In order to meet SCA requirements, you'll be required to authenticate your customers via 3D Secure to make online payments. Merchants who do not meet the requirements are at risk of having transactions rejected.

Take a closer look at our **[F.A.Q](https://resources.worldnetpayments.com/blog/psd2-faq)** for more information on how PDS2 impacts merchants and customers.

The 3D Secure verification process requires the cardholder to pass an identity check. If you're using one of our shopping carts or our hosted pages solution, there's nothing to worry about as we'll handle everything for you. However, if you have a direct integration into one of our APIs, the implementation of an initial authentication step using our MPI services will be required.

The process is described in the flowchart below.

1. A `POST` request is sent to the MPI service provided by Worldnet which handles the user authentication.

2. After authentication, the server will send the results in the form of a redirect to the `MPI Receipt URL` configured in your terminal.

3. If the authentication is successful, add the `mpiReference` code received from the response into the `threeDSecure` section of the [payment](https://docs.payroc.com/api/resources#payment) request.

## Creating MPI Request

To simplify 3D Secure for API integrations, Worldnet provides a simple MPI redirect.

> **Note**
> To be able to process 3D Secure transactions, this feature must be configured in your terminal. Please contact our support team if you need 3DS to be activated in your account.

### Request

| **TYPE** | **SANDBOX URL** |
|---|---|
| MPI Request | `https://payments.uat.payroc.com/merchant/mpi` |

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| processingTerminalId | Y | <sup>string `[ 4 .. 50 ] characters`</sup> <br>Unique identifier that gateway assigned to the terminal. |
| singleUseToken | Y | <sup>string `[ 128 ] characters`</sup> <br>Unique token that the gateway assigned to the payment details. |
| email | Y | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The cardholder email address. |
| amount | Y | <sup>number <double> `> 0`</sup> <br>The total amount to be authorized including surcharge. The value is in the currency’s lowest denomination, for example, cents. |
| currency | Y | <sup>string `3-char ISO 4217 code`</sup> <br>The currency code of the transaction. |
| orderId | Y | <sup>string `[ 1 .. 24 ] characters`</sup> <br>A unique identifier for the order assigned by the merchant. |
| cardholderChallenge | N | <sup>string <enum> `REQUIRED`, `OPTIONAL`</sup> <br>Inform whether the cardholder challenge is required or not. |

### Request notes

##### ND001 - Data Encoding for Requests

All data sent to us should be correctly encoded using `UTF-8` as the character encoding.

### Request sample

```
https://payments.uat.payroc.com/merchant/mpi?processingTerminalId=4479001&amount=100&currency=EUR&orderId=25&email=joe%40adomain.com&singleUseToken=<SAMPLE_HEX_VALUE>
```

> **Warning**
> Ready to try? **[Sign up](https://developers.worldnetpayments.com/selfcare/signup)** for a sandbox account.

## Handling MPI Response

Once the 3D Secure check is complete, the following parameters will be forwarded to the **MPI Receipt URL** configured in your terminal

### Response

The response body fields will be:

| **FIELD** | **DESCRIPTION** |
|---|---|
| result | <sup>string <enum></sup> <br>`A`: Approved.<br>`D`: Declined. |
| mpiReference | <sup>string `20 characters`</sup> <br>MPI reference. If present, this value should be included in the payment request. |
| orderId | <sup>string `[ 1 .. 24 ] characters`</sup> <br>Echoed back from the request. |
| status | <sup>string <enum></sup> <br>`A`: An attempt at authentication was performed.<br>`N`: Authentication attempt not performed.<br>`U`: Unable to authenticate.<br>`Y`: Authentication attempted and succeeded. |
| eci | <sup>string `2 characters`</sup> <br>`05`: Full 3D Secure authentication.<br>`06`: Issuer and/or cardholder are not enrolled for 3D Secure.<br>`07`: 3D Secure authentication attempt failed - numerous possible reasons (Visa only). |

### Response sample

A `GET` request will be sent to your receipt endpoint containing the response fields in the form of query parameters:

```
https://MPI_RECEIPT_URL?result=A&status=A&eci=06&mpiReference=d01656cf0ec3e62e3754&orderId=25
```

## Payment Request with 3D Secure

Now that you successfully acquired the `mpiReference` code, you just need to include it in your payment request within the `threeDSecure` section. Check out the sample below:

| **TYPE** | **SANDBOX URL** |
|---|---|
| Payment Request | `https://api.payroc.com/v1/payments` |

```
{
    "channel": "WEB",
    "processingTerminalId": "4479001",
    "order": {
        "orderId": "25",
        "currency": "EUR",
        "totalAmount": "100"
    },
    "paymentMethod": {
        "type": "singleUseToken",
        "token": "<SAMPLE_HEX_VALUE>"
    },
    "threeDSecure": {
        "serviceProvider": "gateway",
        "mpiReference": "d01656cf0ec3e62e3754"
    }
}
```
