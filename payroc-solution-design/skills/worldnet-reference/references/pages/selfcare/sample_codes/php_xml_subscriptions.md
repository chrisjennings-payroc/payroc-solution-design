<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_xml_subscriptions | synced: 2026-10-05 -->

# PHP XML Subscriptions

The sample code below requires the **[PHP XML API](https://developers.worldnetpayments.com/_media/developer/sample_codes/gateway_xml_php_api.zip)**.

**Settings file (worldnet_account.inc):**  [worldnet_account.inc](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_subscriptions?codeblock=0)

```
<?php
 
# These values are used to identify and validate the account that you are using. They are mandatory.
$gateway = '';			# This is the Worldnet payments gateway that you should use, assigned to the site by Worldnet.
$terminalId = '';			# This is the Terminal ID assigned to the site by Worldnet.
$currency = '';				# This is the 3 digit ISO currency code for the above Terminal ID.
$secret = '';				# This shared secret is used when generating the hash validation strings.
					# It must be set exactly as it is in the Worldnet Selfcare system.
$testAccount = true;
 
# These are used only in the case where the response hash is incorrect, which should
# never happen in the live environment unless someone is attempting fraud.
$adminEmail = '';
$adminPhone = '';
 
?>
```

**Subscription registration:**  [worldnet_subscription_registration.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_subscriptions?codeblock=1)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$subscriptionMerchantRef = '';		# Unique merchant identifier for the subscription. Length is limited to 48 chars.
$storedSubscriptionMerchantRef = '';	# Merchant reference for the Stored Subscription under which this Subscription is to be created.
$secureCardMerchantRef = '';		# Merchant reference for the SecureCard entry that you want to use to set up the subscription.
$subscriptionStartDate = '';		# Date on which the subscription should start (setup payment is processed immediately, and does not obey this). Format: DD-MM-YYYY.

# These are all optiona fields
$endDate = '';				# (optional) set an end date for the subscription.  Format: DD-MM-YYYY.
$eDCCDecision = '';			# (optional) if eDCC was offered and accepted, you should set this to 'Y'.

$recurringAmount = '';			#
$initialAmount = '';			#
$periodType = '';
# Set up the stored subscription addition object
$subreg = new XmlSubscriptionRegRequest($subscriptionMerchantRef,$terminalId,$storedSubscriptionMerchantRef,$secureCardMerchantRef,$subscriptionStartDate);
	if($name != "" || $description != "" || $periodType != "" || $length != "" || $type != "" || $onUpdate != "" || $onDelete != "") $subreg->SetNewStoredSubscriptionValues($name, $description, $periodType, $length, $currency, $recurringAmount, $initialAmount, $type, $onUpdate, $onDelete);
	else if($recurringAmount != "" || $initialAmount != "") $subreg->SetSubscriptionAmounts($recurringAmount, $initialAmount);
	if($endDate != "") $subreg->SetEndDate($endDate);
	if($eDCCDecision != "") $subreg->EDCCDecision($eDCCDecision);
 
$response = $subreg->ProcessRequestToGateway($secret,$testMode,$gateway);
 
if($response->IsError())echo 'AN ERROR OCCURED, Subscription not created. Error details: ' . $response->ErrorString();
else {
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->DateTime().$secret);
	$merchantReference =$response->MerchantReference();
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		echo 'SUBSCRIPTION REGISTRATION FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if your card will be billed.';
		if([isset](http://www.php.net/isset)($merchantReference))echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and Subscription Merchant Reference: ' . $response->MerchantReference() . ' when mailling or calling.';
	} else echo "Subscription successfully setup and setup payment processed succesfully.";
}
 
?>
```

**Subscription update:**  [worldnet_subscription_update.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_subscriptions?codeblock=2)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$subscriptionMerchantRef = '';		# Merchant Reference of the subscription to be updated
$storedSubscriptionMerchantRef = '';	# Merchant reference for the Stored Subscription under which this Subscription is to be created.
$secureCardMerchantRef = '';		# Merchant reference for the SecureCard entry that you want to use to set up the subscription.
$subscriptionStartDate = '';		# Date on which the subscription should start (setup payment is processed immediately, and does not obey this).
$terminalId = '';
$recurringAmount = '';
# Set up the stored subscription update object
$subupd = new XmlSubscriptionUpdRequest($subscriptionMerchantRef,$terminalId,$secureCardMerchantRef);
	if($name != "") $subupd->SetSubName($name);
	if($description != "") $subupd->SetDescription($description);
	if($periodType != "") $subupd->SetPeriodType($periodType);
	if($length != "") $subupd->SetLength($length);
	if($recurringAmount != "") $subupd->SetRecurringAmount($recurringAmount);
	if($type != "") $subupd->SetSubType($type);
	if($startDate != "") $subupd->SetStartDate($startDate);
	if($endDate != "") $subupd->SetEndDate($endDate);
	if($eDCCDecision != "") $subupd->EDCCDecision($eDCCDecision);
 
$response = $subupd->ProcessRequestToGateway($secret,$testMode,$gateway);
 
if($response->IsError()) {
 
	echo 'AN ERROR OCCURED, Subscription not updated. Error details: ' . $response->ErrorString();
 
}
else {
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->DateTime().$secret);
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		echo 'SUBSCRIPTION UPDATE FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if your card will be billed.';
		$merchantRef = $response->MerchantReference();
		if([isset](http://www.php.net/isset)($merchantRef)) {
			echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and Subscription Merchant Reference: ' . $response->MerchantReference() . ' when mailling or calling.';
		}
	} else echo "Subscription successfully updated.";
 
}
 
?>
```

**Subscription deletion:**  [worldnet_subscription_delete.php](https://developers.worldnetpayments.com/_export/code/selfcare/sample_codes/php_xml_subscriptions?codeblock=3)

```
<?php
 
require('worldnet_account.inc');
require('gateway_tps_xml.php');
 
# These values are specific to the cardholder.
$subscriptionMerchantRef = '';		# Merchant Reference of the subscription to be deleted

# Set up the stored subscription update object
$subdel = new XmlSubscriptionDelRequest($subscriptionMerchantRef,$terminalId);
$response = $subdel->ProcessRequestToGateway($secret,$testMode,$gateway);
 
if($response->IsError())
{
 echo 'AN ERROR OCCURED, Subscription not deleted. Error details: ' . $response->ErrorString();
}
else {
	$expectedResponseHash = [md5](http://www.php.net/md5)($terminalId.$response->MerchantReference().$response->DateTime().$secret);
	if($expectedResponseHash != $response->[Hash](http://www.php.net/hash)()) {
		$merchantRef = $response->MerchantReference();
		echo 'SUBSCRIPTION DELETION FAILED: INVALID RESPONSE HASH. Please contact <a href="mailto:' . $adminEmail . '">' . $adminEmail . '</a> or call ' . $adminPhone . ' to clarify if your card will be billed.';
		if([isset](http://www.php.net/isset)($merchantRef)) {
			echo 'Please quote Worldnet Terminal ID: ' . $terminalId . ', and Subscription Merchant Reference: ' . $merchantRef . ' when mailling or calling.';
		}
	}
	else {
		echo "Subscription successfully deleted.";
	}
}
 
?>
```
