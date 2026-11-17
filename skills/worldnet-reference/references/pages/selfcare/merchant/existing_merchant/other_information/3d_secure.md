<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:other_information:3d_secure | synced: 2026-10-05 -->

# Getting Started with 3DS

**3D Secure** (3DS) works by confirming that the buyer is the cardholder. If the cardholder has not set up 3DS yet or if their bank doesn't support it yet, it's not the merchant's fault, and therefore the merchant is not liable for fraud for the transaction (n.b. there are some rare exceptions to this, e.g. for corporate cards).

If the cardholder has not yet set up 3DS they will have the option to skip set up and proceed with the payment (they can do this a maximum of 3 times on their account) or set up 3DS during the payment (this will not abandon the payment).

3DS is completely integrated into the Worldnet Payments Hosted Payment Page, so if your site is using this, all you have to do is ask us to turn it on! There's no set up charge either. Sometimes it can take a while to set up with Visa, MasterCard and the acquiring bank though, so do give us as much notice as possible.

3DS does not actually have to be displayed during checkout for the merchant to be protected.

3DS protects against fraud, not charge-backs. You can still get charge-backs for non-fraud related reasons, such as if the customer doesn't receive the goods or if the customer refutes the quality of the goods, etc.

3DS does not support pre-authorizations.

**PSD2 and String Customer Authentication (SCA)**

The Payment Services Directive 2 (PSD2) comes into force in 2019 (only applicable in EU) and you might need to be prepared to provide SCA for your payments. Take a closer look at our **[F.A.Q](https://resources.worldnetpayments.com/blog/psd2-faq)** if you have more questions.

## What is 3D Secure?

**3D Secure** (3DS) is a tool developed by Visa and used by MasterCard (called “Verified by Visa” and “MasterCard SecureCode” respectively) to combat eCommerce fraud.

It effectively consists of a prompt from the issuing bank for the cardholders to enter their password or some other authentication information during checkout.

3DS supports all Visa type cards including Electron, Visa Debit and Visa Credit (but not 3V vouchers) and all MasterCard type cards including Debit MasterCard, Maestro and MasterCard Credit (but not Laser cards).

## Do I need 3D Secure?

If you wish to accept Maestro eCommerce transactions, then yes, as it is mandatory. If not, check with your acquiring bank. Some require it and others don’t. Even if they don’t require it, we would recommend enabling it as it provides the merchant with peace of mind. Many merchants don’t consider fraud an issue until they get their first fraudulent chargeback, and then they want 3DS ASAP!

## Integrating with 3D Secure

In order to get 3DS all you have to do is request it of Worldnet Payments ([[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection)). If you are using our Hosted Payment Page integration method then there is no extra development work. If using XML then we will forward you or your developer the necessary documentation to integrate into our separate MPI page for performing the 3D Secure request separately, before the XML transaction. We will also supply you with the logos that are required to be on your site.

## Going Live

In order to get **3D Secure**, all you have to do is request it of Worldnet Payments (email: [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection)).

If you are using our **Hosted Payment Page integration method** then there is no extra development work.

If using **XML** then we will forward you, or your developer, the necessary documentation to integrate into our separate MPI page for performing the 3D Secure request separately, before the XML transaction. We will also supply you with the logos that are required to be on your site.

**Going live with 3D Secure**: Once Worldnet Payments have fully registered 3DS for you with Visa, MasterCard, your acquiring bank and ourselves, we will let you know that we are ready to go live. To go live we will ask you to have a live Visa card and MasterCard ready to test once we enable it.

## Monitoring & Responses

Merchants are protected by 3DS for all transactions that go through the process successfully. Some transactions can fail authentication, so all transactions should be checked in our Selfcare System before fulfilment.

**1.** If marked “**Y**” (**Fully Authenticated**) then the merchant is protected.
**2.** If “**A**” (**Attempted Authentication**) then the merchant is protected for all but North American corporate/business cards.
**3.** If marked “**N**” then no liability shift is in place. If a transaction is marked as “N” but is approved, this normally means that the card type does not support 3DS (such as American Express). It could also mean though there was some problem authenticating 3DS, but the acquirer decided to proceed with the transaction anyway.

## Some more information about 3D Secure

- 3DS works by confirming that the buyer is the cardholder. If the cardholder has not set up 3DS yet or if their bank doesn’t support it yet, it’s not the merchant’s fault, and therefore the merchant is not liable for fraud for the transaction (n.b. there are some rare exceptions to this, e.g. for corporate cards).
- If the cardholder has not yet set up 3DS they will have the option to skip set up and proceed with the payment (they can do this a maximum of 3 times on their account) or set up 3DS during the payment (this will not abandon the payment).
- 3DS is completely integrated into the Worldnet Payments Hosted Payment Page, so if your site is using this, all you have to do is ask us to turn it on! There’s no set up charge either. Sometimes it can take a while to set up with Visa, MasterCard and the acquiring bank though, so do give us as much notice as possible.
- 3DS does not actually have to be displayed during checkout for the merchant to be protected.
- 3DS protects against fraud, not chargebacks. You can still get chargebacks for non-fraud related reasons, such as if the customer doesn’t receive the goods or if the customer refutes the quality of the goods, etc.
- 3DS does not support pre-authorisations.

## Cart Abandonment

Some merchants are reluctant to set up 3D Secure because they believe that it will cause high cart abandonment. This used to be the case, but recently some acquirers have been mandating 3DS for a lot of sites. This means that the public are a lot more aware and accepting of 3DS. It does depend on your customer demographic though; a computer parts retailer will have almost no abandonment whereas a book retailer may have less customer awareness about it.

The best way to combat this is to inform customers before they get to the checkout that 3DS will be prompted for. A trial week is also advisable, to get a feel for it and maybe feedback from your customers.
