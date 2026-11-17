<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_hosted_subscriptions | synced: 2026-10-05 -->

# PHP Hosted Subscriptions

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_subscriptions?codeblock=0)

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

**Subscription redirect (worldnet_subscription.php):**  [worldnet_subscription.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_subscriptions?codeblock=1)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for integrating to the Gateway HPP in PHP.
require('worldnet_subscription_functions.inc');
 
$subscriptionAction = '';             # "register" or "update".
$subscriptionMerchantRef = '';        # Unique Merchant Reference for this subscription. Length is limited to 48 chars.
$storedSubscriptionMerchantRef = '';  # The Merchant Reference for the Stored Subscription (Subscription template/payment plan) that you would like this subscription to run under.
$secureCardMerchantRef = '';          # The Merchant Reference of the SecureCard that the Subscription is to be set up on.
$startDate = '';                      # The date the Subscription is to start on (note the setup payment will still be taken immediately if it is >0). Format: DD-MM-YYYY
$dateTime = requestDateTime();
 
# Verification string
$requestHash = subscriptionRequestHash($subscriptionMerchantRef,$secureCardMerchantRef, $dateTime, $startDate);
 
# Request URL for the Gateway
$requestURL = $gateway."/merchant/subscriptionpage/".$subscriptionAction;
 
# Write the HTML of the submission form
echo "<html><body><form id='gatewaysubscriptionform' action='" . $requestURL . "' method='post'>\n";
writeHiddenField("TERMINALID", $terminalId);
writeHiddenField("MERCHANTREF", $subscriptionMerchantRef);
writeHiddenField("STOREDSUBSCRIPTIONREF", $storedSubscriptionMerchantRef);
writeHiddenField("SECURECARDMERCHANTREF", $secureCardMerchantRef);
writeHiddenField("DATETIME", $dateTime);
writeHiddenField("STARTDATE", $startDate);
writeHiddenField("HASH", $requestHash);
 
# Write the JavaScript that will submit the form to Gateway.
echo '</form>Submitting Subscription setup request to Gateway...<script language="JavaScript">document.getElementById("gatewaysubscriptionform").submit();</script></body></html>';
 
?>
```

Subscription URL **(worldnet_subscription_response.php)** (URL for this page is setup as “**Subscription URL**” through Terminal Setup in the Selfcare ):  [worldnet_subscription_response.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_subscriptions?codeblock=2)

```
<?php
 
# This is the file that contains the account settings for Gateway.
require('worldnet_account.inc');
 
# This is a helper file for integrating to the Gateway HPP in PHP.
require('worldnet_subscription_functions.inc');
 
if($_REQUEST["RESPONSECODE"] != "A") echo 'AN ERROR OCCURED! Your Subscription setup request failed. Error message: ' . $_REQUEST["RESPONSETEXT"];
 
if(subscriptionResponseHashIsValid($_REQUEST["RESPONSECODE"], $_REQUEST["RESPONSETEXT"], $_REQUEST["MERCHANTREF"], $_REQUEST["DATETIME"], $_REQUEST["HASH"])) {
	switch($_REQUEST["RESPONSECODE"]) {
		case "A" :	# Subscription setup suceeded. You should store the following details against the user account:
				$subscriptionMerchantRef = $_REQUEST["MERCHANTREF"];
				echo "Subscription successfully registered.";
				break;
		default  :	# Subscription registration failed.
				echo 'SUBSCRIPTION REGISTRATION FAILED! Error Code: ' . $_REQUEST["RESPONSECODE"] . ', Response text: ' . $_REQUEST["RESPONSETEXT"] . '.';
	}
} else {
	echo 'SUBSCRIPTION REGISTRATION FAILED: INVALID RESPONSE HASH. Please contact ' . $adminEmail . ' or call ' . $adminPhone . ' to inform them of this error.';
	if([isset](http://www.php.net/isset)($_REQUEST["ORDERID"])) echo 'Please quote Gateway Terminal ID: ' . $terminalId . ', and Subscription Merchant Reference: ' . $_REQUEST["MERCHANTREF"] . ' when mailling or calling.';
}
 
?>
```

**Helper file (worldnet_subscription_functions.inc):**  [worldnet_subscription_functions.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_hosted_subscriptions?codeblock=3)

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
function subscriptionRequestHash($merchantRef, $secureCardMerchantRef, $dateTime, $startDate) {
	global $terminalId, $secret;
	return [md5](http://www.php.net/md5)($terminalId . $merchantRef . $secureCardMerchantRef . $dateTime . $startDate . $secret);
}
 
# This function is used to validate that the MPI Response Hash from the server is correct.
#     If subscriptionResponseHashIsValid(...) != $_REQUEST["HASH"] then an error should be shown and the Subscription registration should fail.
function subscriptionResponseHashIsValid($responseCode, $responseText, $subscriptionMerchantRef, $dateTime, $responseHash) {
	global $terminalId, $secret;
	return ([md5](http://www.php.net/md5)($terminalId . $responseCode . $responseText . $subscriptionMerchantRef . $dateTime . $secret)==$responseHash);
}
 
?>
```
