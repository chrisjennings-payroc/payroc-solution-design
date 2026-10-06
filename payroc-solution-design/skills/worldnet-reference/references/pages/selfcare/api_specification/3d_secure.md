<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:3d_secure | synced: 2026-10-05 -->

# 3D Secure and Strong Customer Authentication (SCA)

Strong Customer Authentication (SCA) came into force in 2019 as part of the PSD2 regulation in Europe. In order to meet SCA requirements, you'll be required to authenticate your customers via 3D Secure to make online payments. Merchants who do not meet the requirements are at risk of having transactions rejected.

Take a closer look at our **[F.A.Q](https://resources.worldnetpayments.com/blog/psd2-faq)** for more information on how PDS2 impacts merchants and customers.

The 3D Secure verification process requires the cardholder to pass an identity check. If you're using one of our shopping carts or our hosted pages solution, there's nothing to worry about as we'll handle everything for you. However, if you have a direct integration into one of our APIs, the implementation of an initial authentication step using our MPI services will be required.

The process is described in the flowchart below.

1. A `POST` request is sent to the MPI service provided by Worldnet which handles the user authentication.

2. After authentication, the server will send the results in the form of a redirect to the `MPI Receipt URL` webhook configured in your terminal.

3. If the authentication is successful, add the `MPIREF` code received from the response into the `threeDSecure` section of the [payment](https://developers.worldnetpayments.com/apis/merchant/#operation/payment) request.

## Creating MPI Request

To simplify 3D Secure for API integrations, Worldnet provides a simple MPI redirect.

> **Note**
> To be able to process 3D Secure transactions, this feature must be configured in your terminal. Please contact our support team if you need 3DS to be activated in your account.

### Request

| **TYPE** | **SANDBOX URL** |
|---|---|
| MPI Request | `https://testpayments.worldnettps.com/merchant/mpi` |

| **FIELD** | **REQUIRED** | **DESCRIPTION** |
|---|---|---|
| TERMINALID | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The terminal number assigned by Worldnet. |
| CARDNUMBER | Y | <sup>string `[ 12 .. 19 ] characters`</sup> <br>The payment card number. |
| CARDHOLDERNAME | Y | <sup>string `[ 1 .. 50 ] characters`</sup> <br>The cardholder's name as it appears on the card. |
| EMAIL | N | <sup>string `[ 1 .. 128 ] characters`</sup> <br>The cardholder email address. |
| CARDEXPIRY | Y | <sup>string `MMYY`</sup> <br>Expiry date of the card. |
| CARDTYPE | Y | Card type used for the transaction.<br>For more details on this, visit **[Special Fields and Parameters - Card Types](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters#the_card_types)**. |
| AMOUNT | Y | <sup>number <double> `> 0`</sup> <br>The total amount to be authorized including surcharge. |
| CURRENCY | Y | <sup>string `3-char ISO 4217 code`</sup> <br>The currency code of the transaction. |
| ORDERID | Y | <sup>string `[ 1 .. 24 ] characters`</sup> <br>A unique identifier for the order assigned by the merchant. |
| CVV | N | <sup>string `[ 3 .. 4 ] characters`</sup> <br>The card's security code. |
| DATETIME | Y | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>Request date and time. |
| CARDHOLDER_CHALLENGE | N | <sup>string <enum> `REQUIRED`, `OPTIONAL`</sup> <br>Inform whether the cardholder challenge is required or not. |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/selfcare/api_specification/3d_secure#nd001_-_hash_generation)</sup> | Y | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the request fields. |

### Request notes

##### ND001 - Hash generation

See how to generate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**. For this specific feature, you should the following format:

```
TERMINALID:ORDERID:CARDNUMBER:CARDEXPIRY:CARDTYPE:AMOUNT:DATETIME:SECRET
```

##### ND002 - Data Encoding for Requests

All data sent to us should be correctly encoded using `UTF-8` as the character encoding.

### Request sample

The HTML example below shows how to build a form to request Strong Customer Authentication (SCA) from Worldnet.

```
<[html](http://december.com/html/4/element/html.html)>
  <[body](http://december.com/html/4/element/body.html)>
    <[form](http://december.com/html/4/element/form.html) id="FormID" action="https://testpayments.worldnettps.com/merchant/mpi" method="post">
      <[label](http://december.com/html/4/element/label.html)>Terminal ID</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="TERMINALID" />
      <[label](http://december.com/html/4/element/label.html)>Terminal Secret</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="SECRET" />
 
      <[label](http://december.com/html/4/element/label.html)>Order ID</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="ORDERID" />
      <[label](http://december.com/html/4/element/label.html)>Currency</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="CURRENCY" value="EUR" />
      <[label](http://december.com/html/4/element/label.html)>Amount</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="AMOUNT" />
      <[label](http://december.com/html/4/element/label.html)>DateTime</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="DATETIME" value="26-03-2022:10:43:01:673" />
 
      <[label](http://december.com/html/4/element/label.html)>Cardholder Name</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="CARDHOLDERNAME" />
      <[label](http://december.com/html/4/element/label.html)>Email</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="EMAIL" />
      <[label](http://december.com/html/4/element/label.html)>Card Number</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="CARDNUMBER" />
      <[label](http://december.com/html/4/element/label.html)>Expiry Date</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="CARDEXPIRY" />
      <[label](http://december.com/html/4/element/label.html)>CVV</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="CVV" />
 
      <[label](http://december.com/html/4/element/label.html)>CardType</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="CARDTYPE" />
 
      <[label](http://december.com/html/4/element/label.html)>Hash</[label](http://december.com/html/4/element/label.html)> <[input](http://december.com/html/4/element/input.html) type="text" name="HASH" /><[br](http://december.com/html/4/element/br.html) />
      <[input](http://december.com/html/4/element/input.html) id="SubmitID" type="submit" value="Check 3D Secure" />
    </[form](http://december.com/html/4/element/form.html)>
 
    <[script](http://december.com/html/4/element/script.html) src="https://code.jquery.com/jquery-3.2.1.min.js"></[script](http://december.com/html/4/element/script.html)>
    <[script](http://december.com/html/4/element/script.html) src="https://cdnjs.cloudflare.com/ajax/libs/blueimp-md5/2.18.0/js/md5.min.js"></[script](http://december.com/html/4/element/script.html)>
    <[script](http://december.com/html/4/element/script.html)>
      // Generating HASH
      function calcHash() {
        var hash = md5($("input[name='TERMINALID']").val() + $("input[name='ORDERID']").val() + $("input[name='CARDNUMBER']").val() + $("input[name='CARDEXPIRY']").val() + $("input[name='CARDTYPE']").val() + $("input[name='AMOUNT']").val() + $("input[name='DATETIME']").val() + $("input[name='SECRET']").val());
        $("input[name='HASH']").val(hash);
      }
 
      $("input[type='text']").each(function (index) {
        $(this).on("keyup", calcHash);
      });
 
      calcHash();
    </[script](http://december.com/html/4/element/script.html)>
  </[body](http://december.com/html/4/element/body.html)>
</[html](http://december.com/html/4/element/html.html)>
```

> **Warning**
> Remember to change the `TERMINALID` and `SECRET` for valid values. Ready to try? **[Sign up](https://developers.worldnetpayments.com/selfcare/signup)** for a sandbox account.

## Handling MPI Response

Once the 3D Secure check is complete, the following parameters will be forwarded to the **MPI Receipt URL** configured in your terminal

### Response

The response body fields will be:

| **FIELD** | **DESCRIPTION** |  |
|---|---|---|
| RESULT | <sup>string <enum></sup> <br>`A`: Approved.<br>`D`: Declined. |  |
| MPIREF | <sup>string `20 characters`</sup> <br>MPI reference. If present, this value should be included in the payment request. |  |
| ORDERID | <sup>string `[ 1 .. 24 ] characters`</sup> <br>Echoed back from the request. |  |
| STATUS | <sup>string <enum></sup> <br>`A`: An attempt at authentication was performed.<br>`N`: Authentication attempt not performed.<br>`U`: Unable to authenticate.<br>`Y`: Authentication attempted and succeeded. |  |
| ECI | <sup>string `2 characters`</sup> <br>`05`: Full 3D Secure authentication.<br>`06`: Issuer and/or cardholder are not enrolled for 3D Secure.<br>`07`: 3D Secure authentication attempt failed - numerous possible reasons (Visa only). |  |
| DATETIME | <sup>string <date-time> `DD-MM-YYYY:HH:MM:SS:SSS`</sup> <br>Response date and time. |  |
| HASH <br><sup>See notes: [ND001](https://developers.worldnetpayments.com/selfcare/api_specification/3d_secure#nd001_-_hash_validation)</sup> | <sup>string <SHA-512> `[ 1 .. 128 ] characters`</sup> <br>A HASH code formed by part of the response fields. |  |

### Response notes

##### ND001 - Hash validation

A hash string is also included in the response, so that you can implement a verification logic to make sure it was sent by Worldnet. See how to decode and validate a hash string at **[Special Fields and Parameters](https://developers.worldnetpayments.com/selfcare/api_specification/special_fields_and_parameters)**.

For this specific feature, you should expect the following format:

```
RESULT:MPIREF:ORDERID:DATETIME:SECRET
```

### Response sample

A `GET` request will be sent to your webhook containing the response fields in the form of query parameters:

```
https://MPI_WEBHOOK_URL?RESULT=A&STATUS=A&ECI=06&MPIREF=d01656cf0ec3e62e3754&ORDERID=25&DATETIME=06-10-2020%3A13%3A19%3A10%3A239&HASH=3ea402c12f7a8cb0afac31cf0429a167
```

## Payment Request with 3D Secure

Now that you successfully acquired the `MPIREF` code, you just need to include it in your payment request within the `threeDSecure` section. Check out the sample below:

| **TYPE** | **SANDBOX URL** |
|---|---|
| Payment Request | `https://testpayments.worldnettps.com/merchant/api/v1/transaction/payments` |

```
{
    "channel": "WEB",
    "terminal": "4479001",
    "order": {
        "orderId": "25",
        "currency": "EUR",
        "totalAmount": "6.45"
    },
    "customerAccount": {
        "payloadType": "KEYED",
        "cardholderName": "Joe Bloggs",
        "cardDetails": {
            "cardNumber": "5480161234567897",
            "expiryDate": "1222",
            "cvv": "999"
        }
    },
    "threeDSecure": {
        "serviceProvider": "GATEWAY",
        "mpiReference": "d01656cf0ec3e62e3754"
    }
}
```
