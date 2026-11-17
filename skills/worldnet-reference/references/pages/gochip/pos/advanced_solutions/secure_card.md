<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:advanced_solutions:secure_card | synced: 2026-10-05 -->

# Secure Tokens

> **Note**
> This feature is to be used along with our XML gateway to process transactions as our Websockets SDK Solution does not currently support the processing of transactions using the Secure Tokens Token.

The Secure Tokens feature is a special component of our platform that enables you to tokenize your client's cards so they can be used again later for subsequent single or recurring transactions. With your terminal configured to register Secure Tokens, a normal sale processed using our Websockets SDK Solution will return a “securecardmerchantref” to the merchant when a SECURE TOKEN REGISTRATION has been successful.

Using this Secure Tokens Merchant Reference, the merchant has the ability to process once-off or set up recurring sales without the card being present.

Although the uniqueRef is returned which can be used for a tip adjustment the secureCardReference is also returned if we have auto tokenisation enabled.The token is not required to perform the tip adjustment but you can use the token for subsequent payments.

There are two usages that we see in your solution for the secureCardReference

- If reservation is being performed online a tokenisation can happen there and that is what the pre-authorisation is created using, the adjustment would still happen using the uniqueRef
- If the guest is not available at checkout it would be possible to

  - Perform single payment for total bill using secureCardReference
  - On success, reverse original transaction fully using uniqueRef

Later usage at an arbitrary time the secureCardReference can be used via our XML Gateway for processing card holder not present once off payments and it can also be used to set up a subscription / recurring payment plan.
