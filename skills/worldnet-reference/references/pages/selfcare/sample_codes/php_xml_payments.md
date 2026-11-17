<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_xml_payments | synced: 2026-10-05 -->

# PHP XML Payments

Below you can find sample code for **Payments** page in **PHP**. You should also use this [Testing Guide](https://developers.worldnetpayments.com/selfcare/integration_docs/testing-guide), which also contains test card details.

The sample code below requires the **[PHP XML API](https://developers.worldnetpayments.com/_media/developer/sample_codes/gateway_xml_php_api.zip)**.

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments?codeblock=0)

```
<?php
 
# These values are used to identify and validate the account that you are using. They are mandatory.
$gateway = '';			# This is the Worldnet payments gateway that you should use, assigned to the site by Worldnet.
$terminalId = '';		# This is the Terminal ID assigned to the site by Worldnet.
$currency = '';			# This is the 3 digit ISO currency code for the above Terminal ID.
$secret = '';			# This shared secret is used when generating the hash validation strings.
						# It must be set exactly as it is in the Worldnet Selfcare system.
$testAccount = true;
 
# These are used only in the case where the response hash is incorrect, which should
# never happen in the live environment unless someone is attempting fraud.
$adminEmail = '';
$adminPhone = '';
 
?>
```

**Authorisation:**  [worldnet_xml_authorisation.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments?codeblock=1)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$cardNumber = '';		# This is the full PAN (card number) of the credit card OR the SecureCard Card Reference if using a SecureCard. It must be digits only (i.e. no spaces or other characters).
$cardType = '';			# See our Integrator Guide for a list of valid Card Type parameters
$cardExpiry = '';		# (if not using SecureCard) The 4 digit expiry date (MMYY).
$cardHolderName = '';		# (if not using SecureCard) The full cardholders name, as it is displayed on the credit card.
$cvv = '';			# (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.
$issueNo = '';			# (optional) Issue number for Switch and Solo cards.
$email = '';			# (optional) If this is sent then WorldNet will send a receipt to this e-mail address.
$mobileNumber = "";		# (optional) Cardholders mobile phone number for sending of a receipt. Digits only, Include international prefix.

# These values are specific to the transaction.
$orderId = '';			# This should be unique per transaction (12 character max).
$amount = '';			# This should include the decimal point.
$isMailOrder = false;		# If true the transaction will be processed as a Mail Order transaction. This is only for use with Mail Order enabled Terminal IDs.

# These fields are for AVS (Address Verification Check). This is only appropriate in the UK and the US.
$address1 = '';			# (optional) This is the first line of the cardholders address.
$address2 = '';			# (optional) This is the second line of the cardholders address.
$postcode = '';			# (optional) This is the cardholders post code.
$country = '';			# (optional) This is the cardholders country name.
$phone = '';			# (optional) This is the cardholders home phone number.

# eDCC fields. Populate these if you have retreived a rate for the transaction, offered it to the cardholder and they have accepted that rate.
$cardCurrency = '';		# (optional) This is the three character ISO currency code returned in the rate request.
$cardAmount = '';		# (optional) This is the foreign currency transaction amount returned in the rate request.
$conversionRate = '';		# (optional) This is the currency conversion rate returned in the rate request.

# 3D Secure reference. Only include if you have verified 3D Secure throuugh the WorldNet MPI and received an MPIREF back.
$mpiref = '';			# This should be blank unless instructed otherwise by WorldNet.
$deviceId = '';			# This should be blank unless instructed otherwise by WorldNet.

$autoready = '';		# (optional) (Y/N) Whether or not this transaction should be marked with a status of "ready" as apposed to "pending".
$multicur = false;		# This should be false unless instructed otherwise by WorldNet.

$description = '';		# (optional) This can is a description for the transaction that will be available in the merchant notification e-mail and in the Self Care system.
$autoReady = '';		# (optional) Y or N. Automatically set the transaction to a status of Ready in the batch. If not present the terminal default will be used.

# Set up the authorisation object
$auth = new XmlAuthRequest($terminalId,$orderId,$currency,$amount,$cardNumber,$cardType);
if($cardType != "SECURECARD") $auth->SetNonSecureCardCardInfo($cardExpiry,$cardHolderName);
if($cvv != "") $auth->SetCvv($cvv);
if($cardCurrency != "" && $cardAmount != "" && $conversionRate != "") $auth->SetForeignCurrencyInformation($cardCurrency,$cardAmount,$conversionRate);
if($email != "") $auth->SetEmail($email);
if($mobileNumber != "") $auth->SetMobileNumber($mobileNumber);
if($description != "") $auth->SetDescription($description);
 
if($issueNo != "") $auth->SetIssueNo($issueNo);
if($address1 != "" && $address2 != "" && $postcode != "") $auth->SetAvs($address1,$address2,$postcode);
if($country != "") $auth->SetCountry($country);
if($phone != "") $auth->SetPhone($phone);
 
if($mpiref != "") $auth->SetMpiRef($mpiref);
if($deviceId != "") $auth->SetDeviceId($deviceId);
 
if($multicur) $auth->SetMultiCur();
if($autoready) $auth->SetAutoReady($autoready);
if($isMailOrder) $auth->SetMotoTrans();
 
# Perform the online authorisation and read in the result
$response = $auth->ProcessRequestToGateway($secret,$testAccount, $gateway);
 
 
 
$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId . $response->UniqueRef() . ($multicur == true ? $currency : '') . $amount . $response->DateTime()
    . $response->ResponseCode() . $response->ResponseText() . $response->BankResponseCode() . $secret);
 
if($response->IsError()) echo 'AN ERROR OCCURED! You transaction was not processed. Error details: ' . $response->ErrorString();
elseif($expectedResponseHash == $response->[Hash](http://www.php.net/hash)()) {
    switch($response->ResponseCode()) {
        case "A" :	# -- If using local database, update order as Authorised.
            echo 'Payment Processed successfully. Thanks you for your order.';
            $uniqueRef = $response->UniqueRef();
            $responseText = $response->ResponseText();
            $approvalCode = $response->ApprovalCode();
            $avsResponse = $response->AvsResponse();
            $cvvResponse = $response->CvvResponse();
            break;
        case "R" :
        case "D" :
        case "C" :
        case "S" :
 
        default  :	# -- If using local database, update order as declined/failed --
            echo 'PAYMENT DECLINED! Please try again with another card. Bank response: ' . $response->ResponseText();
    }
} else {
    $uniqueReference = $response->UniqueRef();
    echo 'PAYMENT FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if you will get charged for this order.';
    if([isset](http://www.php.net/isset)($uniqueReference)) echo 'Please quote WorldNet Terminal ID: ' . $terminalId . ', and Unique Reference: ' . $uniqueReference . ' when mailing or calling.';
}
 
?>
```

**Perform a Refund** (standard refunds can only be performed against authorised sale transactions that have already been put through the same account system. Also, the Order ID of the original sale must be unique.):  [worldnet_xml_refund.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments?codeblock=2)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the transaction.
$uniqueRef = '';		# This is the unique reference returned in the response for the original sale transaction.
$amount = '';			# This should include the decimal point.
$operator = '';			# The administrative operator who is performing the refund.
$reason = '';			# This reason this refund is necessary.

# Optional fields
$autoReady = '';		# (optional) Y or N. Automatically set the transaction to a status of Ready in the batch. If not present the terminal default will be used.

# Set up the refund object
$refund = new XmlRefundRequest($terminalId,"",$amount,$operator,$reason);
$refund->SetUniqueRef($uniqueRef);
if($autoready) $refund->SetAutoReady($autoready);
 
# Perform the refund and read in the result
$response = $refund->ProcessRequestToGateway($secret,$testAccount, $gateway);
 
$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId . $response->UniqueRef() . ($multicur == true ? $currency : '') . $amount . $response->DateTime() . $response->ResponseCode() . $response->ResponseText() . $secret);
 
if($response->IsError()) echo 'AN ERROR OCCURED! You refund was not processed. Error details: ' . $response->ErrorString();
elseif($expectedResponseHash == $response->[Hash](http://www.php.net/hash)()) {
	switch($response->ResponseCode()) {
		case "A" :	# -- If using local database, update order as (partially) Refunded.
				echo 'Refund Processed successfully.';
				$responseText = $response->ResponseText();
				break;
		case "R" :
		case "D" :
		case "C" :
		case "S" :
		default  :	# -- If using local database, update order as declined/failed --
				echo 'REFUND DECLINED!';
	}
} else {
	echo 'REFUND FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if you will get refunded for this order.';
	$uniqueRef = $response->UniqueRef();
	if([isset](http://www.php.net/isset)($uniqueRef)) echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and Unique Reference: ' . $uniqueRef . ' when mailing or calling.';
}
 
?>
```
