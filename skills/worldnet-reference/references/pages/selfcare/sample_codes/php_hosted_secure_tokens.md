<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_hosted_secure_tokens | synced: 2026-10-05 -->

# PHP Hosted SecureCards

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_secure_tokens?codeblock=0)

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

**SecureCard redirect (worldnet_securetokens.php):**  [worldnet_securetokens.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_secure_tokens?codeblock=1)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for integrating to the Gateway HPP in PHP.
require('worldnet_securetokens_functions.inc');
 
$secureCardAction = '';			# "register" or "update".
$secureCardMerchantRef = '';	# Unique Merchant Reference for this card. Length is limited to 48 chars.
$dateTime = requestDateTime();
 
# Verification string
$requestHash = secureCardRequestHash($secureCardMerchantRef, $dateTime, $secureCardAction);
 
# Request URL for the gateway
$requestURL = $gateway."/merchant/securecardpage";
 
# Write the HTML of the submission form
echo "<html><body><form id='gatewaysecuretokensform' action='" . $requestURL . "' method='post'>\n";
writeHiddenField("ACTION", $secureCardAction);
writeHiddenField("TERMINALID", $terminalId);
writeHiddenField("MERCHANTREF", $secureCardMerchantRef);
writeHiddenField("DATETIME", $dateTime);
writeHiddenField("HASH", $requestHash);
 
# Write the JavaScript that will submit the form to Gateway.
echo '</form>Submitting SecureCard request to Gateway...<script language="JavaScript">document.getElementById("gatewaysecuretokensform").submit();</script></body></html>';
 
?>
```

Secure Tokens URL (**worldnet_securetokens_response.php**) (URL for this page is setup as “**Secure Tokens URL**” through Terminal Setup in the Selfcare ):  [worldnet_securetokens_response.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_secure_tokens?codeblock=2)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for integrating to the Gateway HPP in PHP.
require('worldnet_securetokens_functions.inc');
 
if($_REQUEST["RESPONSECODE"] != "A") echo 'AN ERROR OCCURED! Your SecureCard request failed. Error message: ' . $_REQUEST["RESPONSETEXT"];
 
if(secureCardResponseHashIsValid($_REQUEST["RESPONSECODE"], $_REQUEST["RESPONSETEXT"], $_REQUEST["MERCHANTREF"], $_REQUEST["CARDREFERENCE"], $_REQUEST["DATETIME"], $_REQUEST["HASH"])) {
	switch($_REQUEST["RESPONSECODE"]) {
		case "A" :	# SecureCard registration suceeded. You should store the following details against the user account:
				$secureCardMerchantRef = $_REQUEST["MERCHANTREF"];
				$secureCardCardRef = $_REQUEST["CARDREFERENCE"];
				$secureCardCardType = $_REQUEST["CARDTYPE"];
				$secureCardMaskedCardNumber = $_REQUEST["MASKEDCARDNUMBER"];
				$secureCardCardCardExpiry = $_REQUEST["CARDEXPIRY"];
				echo "Success! Card Type: " . $secureCardCardType . ", Masked Card number: " . $secureCardMaskedCardNumber . ", expires (MMYY): " . $secureCardCardCardExpiry;
				break;
		default  :	# SecureCard registration failed.
				echo 'SECURECARD REGISTRATION FAILED! Error Code: ' . $_REQUEST["RESPONSECODE"] . ', Response text: ' . $_REQUEST["RESPONSETEXT"] . '.';
	}
} else {
	echo 'SECURECARD REGISTRATION FAILED: INVALID RESPONSE HASH. Please contact ' . $adminEmail . ' or call ' . $adminPhone . ' to inform them of this error.';
	if([isset](http://www.php.net/isset)($_REQUEST["ORDERID"])) echo 'Please quote Gateway Terminal ID: ' . $terminalId . ', and SecureCard Merchant Reference: ' . $_REQUEST["MERCHANTREF"] . ' when mailling or calling.';
}
 
?>
```

**Helper file (worldnet_securetokens_functions.inc):**  [worldnet_securetokens_functions.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_secure_tokens?codeblock=3)

```
<?php
 
# This simply reduces the PHP code required to build the form.
function writeHiddenField($fieldName, $fieldValue) {
	echo "<input type='hidden' name='" . $fieldName . "' value='" . $fieldValue . "' />";
}
 
# This generates a DATETIME value in the correct format expected in the request.
function requestDateTime() {
	return [date](http://www.php.net/date)('d-m-Y:H:i:s:000');
}
 
# This is used to generate the Authorisation Request Hash.
function secureCardRequestHash($secureCardMerchantRef, $dateTime, $secureCardAction) {
	global $terminalId, $secret;
	return [md5](http://www.php.net/md5)($terminalId . $secureCardMerchantRef . $dateTime . $secureCardAction . $secret);
}
 
# This function is used to validate that the MPI Response Hash from the server is correct.
#     If secureCardResponseHashIsValid(...) != $_REQUEST["HASH"] then an error should be shown and the SecureCard registration should fail.
function secureCardResponseHashIsValid($responseCode, $responseText, $secureCardMerchantRef, $secureCardCardRef, $dateTime, $responseHash) {
	global $terminalId, $secret;
	return ([md5](http://www.php.net/md5)($terminalId . $responseCode . $responseText . $secureCardMerchantRef . $secureCardCardRef . $dateTime . $secret)==$responseHash);
}
 
?>
```
