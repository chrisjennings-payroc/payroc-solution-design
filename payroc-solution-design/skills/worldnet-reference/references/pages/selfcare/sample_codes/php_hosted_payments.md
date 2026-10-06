<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_hosted_payments | synced: 2026-10-05 -->

# PHP Hosted Payments

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_payments?codeblock=0)

```
<?php
 
# These values are used to identify and validate the account that you are using. They are mandatory.
$gateway = '';          # This is the Gateway payments URL that you should use, assigned to the site.
$terminalId = '';       # This is the Terminal ID assigned to the site by Gateway.
$currency = '';         # This is the 3 digit ISO currency code for the above Terminal ID.
$secret = '';           # This shared secret is used when generating the hash validation strings.
                        # It must be set exactly as it is in the Gateway SelfCare system.

# This should contain the URL of the receipt page and validation page
$host = '';	                   # This should be your host eg. http://localhost:8000
$receiptPageURL = $host.'';    # This should be the path to your receipt page
$validationURL = $host.'';     # This should be the path to your validation page

# These are used only in the case where the response hash is incorrect, which should
# never happen in the live environment unless someone is attempting fraud.
$adminEmail = '';
$adminPhone = '';
 
?>
```

**Payment page (worldnet_payment.php):**  [worldnet_payment.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_payments?codeblock=1)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for intgerating to the GatewayHPP in PHP.
require('worldnet_hpp_functions.inc');
 
# These values are specific to the transaction.
$orderId = '';			# This should be unique per transaction.
$amount = '';			# This should include the decimal point.
$dateTime = requestDateTime();
 
$autoReady = '';		# (optional) Y or N. Automatically set the transaction to a status of Ready in the batch. If not present the terminal default will be used.
$description = '';		# (optional) This is a decription for the transaction that will be available in the merchant notification e-mail and in the SelfCare system.

$email = '';			# (optional) If this is sent then Gatewaywill send a receipt to this e-mail address.
$cardholderName = '';    # (optional) This is the cardholder's name if available

$address1 = '';			# (optional) This is the first line of the cardholders billing address.
$address2 = '';			# (optional) This is the second line of the cardholders billing address.
$postcode = '';			# (optional) This is the postcode of the cardholders billing address.

 
# If there's no orderId set then generate a unique time-based order ID.
if(![isset](http://www.php.net/isset)($orderId) || $orderId == '') $orderId = generateUniqueOrderId();
 
# ------ Add order to the local database here if using one ------

# Verification string
$requestHash = authRequestHash($orderId, $amount, $dateTime);
 
# Request URL for the gateway
$requestURL = $gateway.'/merchant/paymentpage';
 
# Write the HTML of the submission form
echo "<html><body><form id='gatewayform' action='" . $requestURL . "' method='post'>\n";
writeHiddenField("TERMINALID", $terminalId);
writeHiddenField("CURRENCY", $currency);
writeHiddenField("ORDERID", $orderId);
writeHiddenField("AMOUNT", $amount);
writeHiddenField("DATETIME", $dateTime);
if([isset](http://www.php.net/isset)($cardholderName) && $cardholderName != '') writeHiddenField("CARDHOLDERNAME", $cardholderName);
if([isset](http://www.php.net/isset)($postcode) && $postcode != '') {
	writeHiddenField("ADDRESS1", $address1);
	writeHiddenField("ADDRESS2", $address2);
	writeHiddenField("POSTCODE", $postcode);
}
if([isset](http://www.php.net/isset)($email) && $email != '') writeHiddenField("EMAIL", $email);
if([isset](http://www.php.net/isset)($description) && $description != '') writeHiddenField("DESCRIPTION", $description);
if([isset](http://www.php.net/isset)($autoReady) && $autoReady != '') writeHiddenField("AUTOREADY", $autoReady);
if($receiptPageURL != '') writeHiddenField("RECEIPTPAGEURL", $receiptPageURL);
if($validationURL != '') writeHiddenField("VALIDATIONURL", $validationURL);
writeHiddenField("HASH", $requestHash);
 
# You can also include any other custom fields here. Their contents will for included in the response POST to the receipt page.
# writeHiddenField("Customer ID", '32856951');

# Write the JavaScript that will submit the form to Gateway.
echo '</form>Submitting order to Gateway for Payment...<script language="JavaScript">document.getElementById("gatewayform").submit();</script></body></html>';
 
?>
```

**Receipt page (worldnet_receipt_page.php):**  [worldnet_receipt_page.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_payments?codeblock=2)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for intgerating to the Gateway HPP in PHP.
require('worldnet_hpp_functions.inc');
 
if(authResponseHashIsValid($_REQUEST["ORDERID"], $_REQUEST["AMOUNT"], $_REQUEST["DATETIME"], $_REQUEST["RESPONSECODE"], $_REQUEST["RESPONSETEXT"], $_REQUEST["HASH"])) {
	# -- Do check to ensure that $_REQUEST["ORDERID"] is in the database
	if($_REQUEST["ORDERID"]) {
		switch($_REQUEST["RESPONSECODE"]) {
			case "A" :	# -- If using local database, update order as Paid/Successful
					echo 'Payment Processed successfully. Thanks you for your order.';
					break;
			case "R" :
			case "D" :
			case "C" :
			case "S" :
			default  :	# -- If using local database, update order as declined/failed --
					echo 'PAYMENT DECLINED! Please try again with another card. Bank response: ' . $_REQUEST["RESPONSETEXT"];
		}
	} else {
		echo 'Order ID: ' . $_REQUEST["ORDERID"] . ' not found. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify.';
	}
} else {
	echo 'PAYMENT FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if you will get charged for this order.';
	if([isset](http://www.php.net/isset)($_REQUEST["ORDERID"])) echo 'Please quote Gateway Terminal ID: ' . $terminalId . ', and Order ID: ' . $_REQUEST["ORDERID"] . ' when mailling or calling.';
}
 
?>
```

**Helper file (worldnet_hpp_functions.inc):**  [worldnet_hpp_functions.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_payments?codeblock=3)

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
 
# If you are not using your own Order ID's and need to use unique random ones, this function will generate one for you.
function generateUniqueOrderId() {
	$seconds = [date](http://www.php.net/date)('H')*3600+[date](http://www.php.net/date)('i')*60+[date](http://www.php.net/date)('s');
	return [date](http://www.php.net/date)('zy') . $seconds;
}
 
# This is used to generate the Authorisation Request Hash.
function authRequestHash($orderId, $amount, $dateTime) {
	global $terminalId, $secret, $receiptPageURL, $validationURL;
	return [md5](http://www.php.net/md5)($terminalId . $orderId . $amount . $dateTime . $receiptPageURL . $validationURL . $secret);
}
 
# This function is used to validate that the Authorisation Response Hash from the server is correct.
#     If authResponseHashIsValid(...) != $_REQUEST["HASH"] then an error should be shown and the transaction should not be approved.
function authResponseHashIsValid($orderId, $amount, $dateTime, $responseCode, $responseText, $responseHash) {
	global $terminalId, $secret;
	return ([md5](http://www.php.net/md5)($terminalId . $orderId . $amount . $dateTime . $responseCode . $responseText . $secret)==$responseHash);
}
 
?>
```

**Background Validation page (worldnet_validate.php):**  [worldnet_validate.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_payments?codeblock=4)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for intgerating to the Gateway HPP in PHP.
require('worldnet_hpp_functions.inc');
 
if(authResponseHashIsValid($_REQUEST["ORDERID"], $_REQUEST["AMOUNT"], $_REQUEST["DATETIME"], $_REQUEST["RESPONSECODE"], $_REQUEST["RESPONSETEXT"], $_REQUEST["HASH"])) {
	# -- Do check to ensure that $_REQUEST["ORDERID"] is in the database
	if($_REQUEST["ORDERID"]) {
		switch($_REQUEST["RESPONSECODE"]) {
			case "A" :	# -- Update order in database as paid/sucessful --
					echo 'OK';
					break;
			case "R" :
			case "D" :
			case "C" :
			case "S" :
			default  :	# -- Update order in database as declined/failed --
					echo 'OK';
		}
	} else {
		echo 'Order ID: ' . $_REQUEST["ORDERID"] . ' not found.';
	}
} else {
	echo 'Background validation hash incorrect.';
}
 
?>
```
