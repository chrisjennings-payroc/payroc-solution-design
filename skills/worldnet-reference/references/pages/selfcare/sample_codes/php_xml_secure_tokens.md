<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_xml_secure_tokens | synced: 2026-10-05 -->

# PHP XML Secure Tokens

The sample code below required the **[PHP XML API](https://developers.worldnetpayments.com/_media/developer/sample_codes/gateway_xml_php_api.zip)**.

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_secure_tokens?codeblock=0)

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

**Secure Tokens registration:**  [worldnet_securetokens_registration.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_secure_tokens?codeblock=1)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$secureCardMerchantRef = '';	# Unique Merchant Reference. Length is limited to 48 chars.
$cardNumber = '';		# This is the full PAN (card number) of the credit card. It must be digits only (i.e. no spaces or other characters).
$cardType = '';			# See our Integrator Guide for a list of valid Card Type parameters
$cardExpiry = '';		# The 4 digit expiry date (MMYY)
$cardHolderName = '';		# The full cardholders name, as it is displayed on the credit card

$dontCheckSecurity = ''; 	# (optional) "Y" if you do not want the CVV to be validated online.
$cvv = '';			# (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.
$issueNo = '';			# (optional) Issue number for Switch and Solo cards.

# Set up the SecureCard addition object
$securereg = new XmlSecureCardRegRequest($secureCardMerchantRef, $terminalId, $cardNumber, $cardExpiry, $cardType, $cardHolderName);
 
if($dontCheckSecurity != "") $securereg->SetDontCheckSecurity($dontCheckSecurity);
if($cvv != "") $securereg->SetCvv($cvv);
if($issueNo != "") $securereg->SetIssueNo($issueNo);
 
$response = $securereg->ProcessRequestToGateway($secret,$testAccount,$gateway);
 
[unset](http://www.php.net/unset)($secureCardCardRef);
if($response->IsError()){
 
 echo 'AN ERROR OCCURED, Card details not registered. Error details: ' . $response->ErrorString();
} else {
	$merchantRef = $response->MerchantReference();
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->CardReference().$response->DateTime().$secret);
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		echo 'SECURECARD REGISTRATION FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if your card details were stored.';
		if([isset](http://www.php.net/isset)($merchantRef)) {
			 echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and SecureCard Merchant Reference: ' . $response->MerchantReference() . ' when mailling or calling.';
		}
	} else {
        echo "SecureCard successfully stored.";
	}
}
 
?>
```

**SecureCard record update:**  [worldnet_securetokens_update.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_secure_tokens?codeblock=2)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$secureCardMerchantRef = '';	# Unique Merchant Reference. Length is limited to 48 chars.
$cardNumber = '';		# This is the full PAN (card number) of the credit card. It must be digits only (i.e. no spaces or other characters).
$cardType = '';			# See our Integrator Guide for a list of valid Card Type parameters
$cardExpiry = '';		# The 4 digit expiry date (MMYY)
$cardHolderName = '';		# The full cardholders name, as it is displayed on the credit card
$recurringAmount = '';
$dontCheckSecurity = ''; 	# (optional) "Y" if you do not want the CVV to be validated online.
$cvv = '';			# (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.
$issueNo = '';			# (optional) Issue number for Switch and Solo cards.

# Set up the SecureCard update object
$secureupd = new XmlSecureCardUpdRequest($secureCardMerchantRef,$terminalId,$cardNumber,$cardExpiry,$cardType,$cardHolderName);
 
if($dontCheckSecurity != "") $secureupd->SetDontCheckSecurity($dontCheckSecurity);
if($cvv != "") $secureupd->SetCvv($cvv);
if($issueNo != "") $secureupd->SetIssueNo($issueNo);
 
$response = $secureupd->ProcessRequestToGateway($secret,$testAccount,$gateway);
 
if($response->IsError()) {
	echo 'AN ERROR OCCURED, Card details not updated. Error details: ' . $response->ErrorString();
}
 else {
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->CardReference().$response->DateTime().$secret);
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		echo 'SECURECARD UPDATE FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if your card details were updated.';
		$merchantRef = $response->MerchantReference();
		if([isset](http://www.php.net/isset)($merchantRef))
			{
				echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and SecureCard Merchant Reference: ' . $merchantRef . ' when mailling or calling.';
			}
	} else {
		echo "SecureCard successfully updated.";
	}
}
 
?>
```

**SecureCard record deletion:**  [worldnet_securetokens_delete.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_secure_tokens?codeblock=3)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$secureCardMerchantRef = '';	# Unique Merchant Reference. Length is limited to 48 chars.
$secureCardCardRef = '';	# This is the Worldnet generated 16 digit card number token

# Set up the SecureCard deletion object
$securedel = new XmlSecureCardDelRequest($secureCardMerchantRef,$terminalId,$secureCardCardRef);
$response = $securedel->ProcessRequestToGateway($secret,$testAccount,$gateway);
 
if($response->IsError()) {
	echo 'AN ERROR OCCURED, Card details not deleted. Error details: ' . $response->ErrorString();
} else {
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->DateTime().$secret);
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		echo 'SECURECARD DELETION FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if your card details were updated.';
		$merchantRef = $response->MerchantReference();
		if([isset](http://www.php.net/isset)($merchantRef)) {
			echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and SecureCard Merchant Reference: ' . $response->MerchantReference() . ' when mailling or calling.';
		}
	} else {
		echo "SecureCard successfully deleted.";
	}
}
 
?>
```

**SecureCard record search:**  [worldnet_securetokens_search.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_secure_tokens?codeblock=4)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$secureCardMerchantRef = '';	# Unique Merchant Reference. Length is limited to 48 chars.

# Set up the SecureCard addition object
$securesearch = new XmlSecureCardSearchRequest($secureCardMerchantRef,$terminalId);
$response = $securesearch->ProcessRequestToGateway($secret,$testAccount,$gateway);
 
if($response->IsError()){
 
 	echo 'AN ERROR OCCURED, Card details not found. Error details: ' . $response->ErrorString();
 
} else {
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->CardReference().$response->CardType().$response->CardExpiry().$response->CardHolderName().$response->DateTime().$secret);
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		echo 'SECURECARD SEARCH FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . ' or call ' . $adminPhone . ' to clarify if your card details were stored.';
		$getMerchantReference = $response->MerchantReference();
		if([isset](http://www.php.net/isset)($getMerchantReference)) {
 
			 echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and SecureCard Merchant Reference: ' . $response->MerchantReference() . ' when mailling or calling.';
		}
	} else {
		# Use/Save $response->MerchantReference(), $response->CardReference(), $response->CardType(), $response->CardExpiry(), $response->CardHolderName().
        echo "SecureCard successfull details found.";
	}
}
 
?>
```
