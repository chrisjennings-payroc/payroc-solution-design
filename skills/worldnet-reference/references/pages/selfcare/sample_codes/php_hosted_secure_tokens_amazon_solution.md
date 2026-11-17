<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:php_hosted_secure_tokens_amazon_solution | synced: 2026-10-05 -->

# PHP Secure Tokens Amazon Solution

This solution requires our Card Storage solution called **SecureCard**. It's designed so that the checkout is like the Amazon checkout, in that the cardholder must register a card for their account and then they can use, update or delete the card info in their account settings. The integration is quite complex though, as there is a lot of functionality.

The first thing they will need to do is register their card. There are two ways of doing this:

**1.** Simply store the card without taking payment: You can find sample PHP code for this [here](https://developers.worldnetpayments.com/developer/sample_codes/php_hosted_secure_tokens).
**2.** Process a normal Hosted Payment Page transaction and store the card details afterwards: You can find sample PHP code for this [here](https://developers.worldnetpayments.com/developer/sample_codes/php_hosted_payment_with_secure_card_storage).

You should then store the card token details as per the sample code. You can then in the future update the card details using the standalone page (same sample code as 1 above). You can also delete it using the Delete sample code here.

When you want to pay using the card you can do this by using this XML sample code. Note that you will have to use the “Card Reference” from before in place of the Card Number, you will not need to send the Expiry Date, and the Card Type will be “**SECURECARD**”, but sample code takes care of all of this.
