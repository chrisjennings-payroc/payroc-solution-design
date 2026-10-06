<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:f_a_q | synced: 2026-10-05 -->

# Frequently Asked Questions (F.A.Q.)

## My password doesn't work

In this case we would recommend to reset your password. You need to use “Forgot Password” option in the main Login screen. When you click on this, a new form will be displayed and you need to enter correct account's details.

## Can you send me my password?

Unfortunately, we do not have access to your password and we cannot reset it for you. In this case we would recommend to reset your password. You need to use “Forgot Password” option in the main Login screen. When you click on this, a new form will be displayed and you need to enter correct account's details.

## My account has been locked out

If you exceed your max failed login attempts then you will be forced to change your password using the “Forgot Password?” link. When you do this you will be prompted for the: Merchant ID, Username and the email address that is associated with the login account (the email address that originally received the login details). If these are entered correctly you will receive an email with a link that you can click to set a new password. This link will be valid for 30 minutes only. If you do not receive the email please check your spam filter, but you may have to contact your email administrator if you still do not receive it.

## How can I add a new user

Adding a new user is very simple and quick in the Selfcare and it takes only a few steps. When you create a new user, the log-in details are automatically emailed to them directly from the system. Two separate mails are sent (for security reasons) containing full instructions about how to set their initial password and log in.

## Funds have not been transferred into my account

Worldnet Payments do not deal with the merchant funding side or the payments. We deal with the data of the authorization and transaction daily settlement to the Merchant Bank only. For any funding queries please contact your Merchant Bank directly.

## How can I refund a transaction

Refunding a transaction is very simple in the Selfcare. It only takes the following steps:

- Find the original transaction in the Open Batch or Closed Batch section of our Selfcare. You can use one of the filters to find a transaction or click on a batch date stamp to open transactions if you know the exact date of the transaction.
- Click on a time stamp of a transaction you want to refund to see the full details and there is a “Refund” button at the bottom of the page.
- Click on the Refund button and fill both new fields: Amount and Reason. By default, you can refund up to 100% of the original transaction value (this is called the max refund percentage and it can be changed as needed by contacting Worldnet Payments Support).
- Click “Submit” button to confirm the refund.

## How can I void a transaction

A Void is the cancellation of a previous sale that has not yet been settled/batched. A void can only be performed on transactions in the Open Batch. The original sale transaction is effectively removed from the batch of transactions to be settled, but will still appear with a status of “Void”. Once a transaction has been voided this action cannot be undone.

## How to use Virtual Terminal

Processing sales transactions using Virtual Terminal is very simple and takes only a couple of seconds. To process any transaction you need:

- Ensure that you are using the correct Terminal ID. Terminal ID is displayed in the right top corner of the Selfcare, just beside Logout button.
- Then go to “Sale” section under Virtual Terminal menu Complete all the fields including drop-down lists for Card Type and Expiry Date.
- Ensure all details are correct and then click on “Perform Sale” button at the bottom of the form.

## How to set up a Pin Pad

Power on PIN Pad: Press power button for three seconds

To ensure Bluetooth is enabled on the PIN Pad:

- Press yellow button.
- Press 'arrow button down' twice to ‘Settings’, press 'OK'.
- Press 'arrow button down' twice to ‘Bluetooth’, press 'OK'.
- Ensure Mode is “Enabled”. If Disabled, press ‘OK’ to enable.
- Once enabled, press red button back to start.

## What does Referral B mean?

A Referral B means that the bank requires more information before they can approve the transaction. This is only relevant for Virtual Terminal (Telephone & Mail Order) transactions, and in the eCommerce environment it's treated as a decline.

If you are getting a “Referral B” response for a Virtual Terminal transaction then you should contact your acquiring bank immediately, because once these transactions settle, they can no longer be completed. They'll ask you for the transaction details and then give you an Authorization Code, which you can type into our Selfcare.

Your acquirer should have provided you with the relevant “referral phone number” to call them in regards to these queries. Please note that we do not have access to these contact numbers.

## Why a transaction has been declined?

Unfortunately,Worldnet Payments is not sent the reason for declines. This is due to information protection legislation. The “Declined” (or “Not Authorized”) text is actually sent by the cardholder’s bank and they do not provide any additional details. Only the cardholder can find out the reason for a decline.

## What is 3D Secure?

3D Secure (3DS) is a tool developed by Visa and used by MasterCard (called “Verified by Visa” and “MasterCard SecureCode” respectively) to combat eCommerce fraud.

It effectively consists of a prompt from the issuing bank for the cardholders to enter their password or some other authentication information during checkout.

3DS supports all Visa type cards including Electron, Visa Debit and Visa Credit (but not 3V vouchers) and all MasterCard type cards including Debit MasterCard, Maestro and MasterCard Credit (but not Laser cards).

## When am I covered by 3D Secure?

Merchants are protected by 3DS for all transactions that go through the process successfully. Some transactions can fail authentication, so all transactions should be checked in our Selfcare before fulfillment.

- If marked “Y” (Fully Authenticated) then the merchant is protected.
- If “A” (Attempted Authentication) then the merchant is protected for all but North American corporate/business cards.
- If marked “N” then no liability shift is in place. If a transaction is marked as “N” but is approved, this normally means that the card type does not support 3DS (such as American Express). It could also mean though there was some problem authenticating 3DS, but the acquirer decided to proceed with the transaction anyway.

## What does Pick-up mean?

Pickup is the same as a Referral A response and is a type of decline.

Pickup (or Referral A) means that the card has been marked as lost or stolen by the cardholder. In the customer present environment this would prompt the merchant to keep and cut up the card and send it back to your acquiring bank.

## What is Terminal ID (TID)?

Terminal Identification Number, also known as a TID, is a unique number assigned and linked to a specific point-of-sale (POS) terminal or workstation that can be used to identify the merchant operating the terminal during credit card sales transaction processing. This number is required to set up online processing through online payment gateways, and is created and provided by the bank or merchant service provider with which a company has set up a merchant account. The number not only identifies what company is using what specific terminal, but also tracks each POS transaction made at that specific location.

## What is Shared Secret?

A Shared Secret is a string used to create a digital signature (referred to as a “hash”) which is provided with every request to and from the system to ensure the integrity of the transaction data and to authenticate the sender as being the legitimate account holder. It is known by both sides communicating, but is never actually sent, hence why it is called a secret. It is known only to you (the merchant) and other parties involved and approved by you (i.e. your developer or a member of staff).

A Shared Secret can be a password, a paraphrase, a long number or a string of randomly chosen characters.

## How can I change my Shared secret?

To set up a new Shared Secret or to change an existing one, you need to:

- Go to Terminal under “Settings” Menu
- Find two fields called “Secret” and “Confirm Secret”
- Enter your new Shared Secret into both fields (those 2 strings must be identical)
- Accept changes by clicking on “Update Settings” at the bottom of the page
- Finally, please confirm that you are sure you want to change the Shared Secret

## Can you send me my last invoice?

We do not send out individual invoices to merchants. Monthly invoices can be downloaded from the “Billing” section, (however this section is only available to the users who have the “Allow Billing” permissions).

## Can I add additional charges to each payment made by credit cards?

This is not allowed by Visa and MasterCard.

## How can I add new card schemes to my account?

All available cards are visible under Settings → Cards. If you want to add a new card scheme, you must arrange this with your merchant bank first and then contact our Customer Support. We will add a new scheme for you as soon as it is confirmed by your merchant bank.

## How can I disable credit cards from my terminal?

All available cards are visible under Settings → Cards. If you want to disable any card scheme, which is currently available on your account, please contact our Customer Support and we will do it for you.
