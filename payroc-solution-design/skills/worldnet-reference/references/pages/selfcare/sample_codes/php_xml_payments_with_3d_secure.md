<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_xml_payments_with_3d_secure | synced: 2026-10-05 -->

# PHP XML Payments with 3D Secure

In this section, you can find sample code for the **3D Secure** redirect before the payment.

Once you receive the response to the “MPI Receipt URL” you will have an MPIREF parameter. You should then process a payment and include that parameter. The sample code for the **XML payment stage** is [here](https://developers.worldnetpayments.com/developer/sample_codes/php_xml_payments).

You should also use this [Testing Guide](https://developers.worldnetpayments.com/selfcare/integration_docs/testing-guide) that also contains test card details.

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments_with_3d_secure?codeblock=0)

```
<?php
 
# These values are used to identify and validate the account that you are using. They are mandatory.
$gateway = '';			# This is the Worldnet payments gateway that you should use, assigned to the site by Worldnet.
$terminalId = '';       # This is the Terminal ID assigned to the site by Worldnet.
$currency = '';			# This is the 3 digit ISO currency code for the above Terminal ID.
$secret = '';			# This shared secret is used when generating the hash validation strings.
						# It must be set exactly as it is in the Worldnet Selfcare system.
#$testAccount = true;   # Commented out as there is no functional test MPI page

# These are used only in the case where the response hash is incorrect, which should
# never happen in the live environment unless someone is attempting fraud.
$adminEmail = '';
$adminPhone = '';
 
?>
```

**3D Secure redirect (worldnet_payment.php):**  [worldnet_payment.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments_with_3d_secure?codeblock=1)

```
<?php
 
# This is the file that contains the account settings for Worldnet.
require('worldnet_account.inc');
 
# This is a helper file for intgerating to the Worldnet HPP in PHP.
require('worldnet_hpp_functions.inc');
 
# These values are specific to the cardholder.
$cardNumber = '';		# This is the full PAN (card number) of the credit card. It must be digits only (i.e. no spaces or other characters).
$cardType = '';			# This can only be one of a set number of values (VISA,DELTA,MASTERCARD,MAESTRO,UK MAESTRO,LASER,AMEX,DINERS,JCB,SECURECARD for example). Check with Worldnet what values you can send.
$cardExpiry = '';		# The 4 digit expiry date (MMYY)
$cvv = '';			# (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.

# These values are specific to the transaction.
$orderId = '';			# This should be unique per transaction.
$amount = '';			# This should include the decimal point.
$host = '';				# This is your host eg. http://localhost:8000
$dateTime = requestDateTime();
 
# If there's no orderId set then generate a unique time-based order ID.
if(![isset](http://www.php.net/isset)($orderId) || $orderId == '') $orderId = generateUniqueOrderId();
 
# Verification string

$requestHash = mpiRequestHash($orderId, $cardNumber, $cardExpiry, $cardType, $amount, $dateTime);
$requestURL = $host.'/merchant/mpi';
 
# Write the HTML of the submission form
echo "<html><body><form id='worldnetmpiform' action='" . $requestURL . "' method='post'>\n";
writeHiddenField("TERMINALID", $terminalId);
writeHiddenField("CARDNUMBER", $cardNumber);
writeHiddenField("CARDTYPE", $cardType);
writeHiddenField("CARDEXPIRY", $cardExpiry);
writeHiddenField("AMOUNT", $amount);
writeHiddenField("CURRENCY", $currency);
writeHiddenField("ORDERID", $orderId);
if([isset](http://www.php.net/isset)($cvv) && $cvv != '') writeHiddenField("CVV", $cvv);
writeHiddenField("DATETIME", $dateTime);
writeHiddenField("HASH", $requestHash);
 
# Write the JavaScript that will submit the form to Worldnet.
echo '</form>Submitting order to Worldnet for Payment...<script language="JavaScript">document.getElementById("worldnetmpiform").submit();</script></body></html>';
 
?>
```

Response page (**worldnet_mpi_response.php**) (URL for this page is setup as “MPI Receipt URL” through Terminal Setup in the Selfcare):  [worldnet_mpi_response.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments_with_3d_secure?codeblock=2)

```
<?php
 
# This is the file that contains the account settings for Worldnet.
require('worldnet_account.inc');
 
# This is a helper file for intgerating to the Worldnet HPP in PHP.
require('worldnet_hpp_functions.inc');
 
if(mpiResponseHashIsValid($_REQUEST["RESULT"], $_REQUEST["MPIREF"], $_REQUEST["ORDERID"], $_REQUEST["DATETIME"], $_REQUEST["HASH"])) {
	switch($_REQUEST["RESULT"]) {
		case "A" :	# 3D Secure validation successfully attempted. Proceed with transaction including the below reference in the authorisation request:
				$mpiRef = $_REQUEST["MPIREF"];
				break;
		default  :	# 3D Secure validation failed. Do not proceed with the transaction.
				echo '3D SECURE VALIDATION FAILED! Please try again with another card.';
	}
} else {
	echo '3D SECURE VALIDATION FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to inform them of this error.';
	if([isset](http://www.php.net/isset)($_REQUEST["ORDERID"])) echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and Order ID: ' . $_REQUEST["ORDERID"] . ' when mailling or calling.';
}
 
?>
```

**Helper file (worldnet_hpp_functions.inc):**  [worldnet_hpp_functions.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_payments_with_3d_secure?codeblock=3)

```
<?php
 
# This function returns the URL that should be used as the "action" for the form posting the Worldnet's servers.
function mpiURL() {
	global $gateway, $testAccount;
	$url = 'https://';
	# if($testAccount) $url .= 'test';       # Commented out as there is no functional test MPI page
	switch ([strtolower](http://www.php.net/strtolower)($gateway)) {
		default :
		case 'worldnet'  : $url .= 'payments.worldnettps.com'; break;
		case 'cashflows' : $url .= 'cashflows.worldnettps.com'; break;
		case 'payius' : $url .= 'payments.payius.com'; break;
		case 'pago' : $url .= 'payments.pagotechnology.com'; break;
	}
	$url .= '/merchant/mpi';
	return $url;
}
 
# This simply reduces the PHP code required to build the form.
function writeHiddenField($fieldName, $fieldValue) {
	echo "<input type='hidden' name='" . $fieldName . "' value='" . $fieldValue . "' />\r";
}
 
# This generates a DATETIME value in the correct format expected in the request.
function requestDateTime() {
	return [date](http://www.php.net/date)('d-m-Y:H:i:s:000');
}
 
# If you are not using your own Order ID's and need to use unique random ones, this function will generate one for you.
function generateUniqueOrderId() {
	$seconds = [date](http://www.php.net/date)('H')*3600+[date](http://www.php.net/date)('i')*60+[date](http://www.php.net/date)('s');
	return [date](http://www.php.net/date)('zy') . $seconds;
}
 
# This is used to generate the Authorisation Request Hash.
function mpiRequestHash($orderId, $cardNumber, $cardExpiry, $cardType, $amount, $dateTime) {
	global $terminalId, $secret;
	return [md5](http://www.php.net/md5)($terminalId . $orderId . $cardNumber . $cardExpiry . $cardType . $amount . $dateTime . $secret);
}
 
# This function is used to validate that the MPI Response Hash from the server is correct.
#     If mpiResponseHashIsValid(...) != $_REQUEST["HASH"] then an error should be shown and the 3D Secure should not be validated.
function mpiResponseHashIsValid($result, $mpiRef, $orderId, $dateTime, $responseHash) {
	global $secret;
	return ([md5](http://www.php.net/md5)($result . $mpiRef . $orderId . $dateTime . $secret)==$responseHash);
}
 
?>
```
