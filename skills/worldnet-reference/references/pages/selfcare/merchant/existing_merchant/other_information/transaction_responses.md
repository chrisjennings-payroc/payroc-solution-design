<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:other_information:transaction_responses | synced: 2026-10-05 -->

# Transaction Responses

## Approved

An **Approved** or **Authorized** response means that the amount of the sale is within the cardholder's credit limit. When an approval code is returned, a hold will be placed on cardholder funds in the amount of the sale (depending on the card issuing bank it might take a different number of days) and will guarantee funds to be transferred into a merchant’s account.

## Authorised

An **Authorised** or **Approved** response means that the amount of the sale is within the cardholder's credit limit. When an approval code is returned, a hold will be placed on cardholder funds in the amount of the sale (depending on the card issuing bank it might take a different number of days) and will guarantee funds to be transferred into a merchant’s account.

## AVS Responses

Note that transactions can still be authorised, even if the AVS response is no match or if there is a failed response. AVS responses are for indication to the merchant only and usually they do not influence the overall authorisation result. This can vary per the cardholders bank though (i.e. the issuing bank).

- **A - Address matches, ZIP does not**. The first five numerical characters contained in the address match with those stored at the VIC or issuer’s center. However, the zip code does not match.
- **E - Ineligible** transaction.
- **N - Neither address nor ZIP matches**. Neither the first five numerical characters contained in the address match with those stored at the VIC nor the issuer’s center, nor the zip code match.
- **R - Retry** (system unavailable or timed out).
- **S - Card type not supported**. The card type for this transaction is not supported by AVS. AVS can verify addresses for Visa cards, MasterCard, proprietary cards, and private label transactions.
- **U - Address information unavailable**.
- **G - Address information unavailable**, International - Visa Only. The address information was not available at the VIC or the issuer’s center.
- **W - Nine-digit zip match, address does not match**. The nine-digit Postal zip code matches that stored at the VIC or the card issuer's center. However, the first five numerical characters contained in the address do not match.
- **X - Exact match** (nine-digit zip and address). Both the nine-digit zip and postal code.

## CVV Responses

Note that transactions can still be authorised even if the CVV response is no match or if there is a failure in response. CVV responses are for indication to the merchant only, and they usually do not influence the overall authorisation result. This can vary per the cardholder's bank, though (i.e. the issuing bank).

- **M** - CVV Match.
- **N** - CVV No Match.
- **P** - Not Processed.
- **S** - CVV should be on the card but the merchant indicates it is not.
- **U** - User is unregistered.

## Declined

The **Declined** or **Not Authorized** response means that the bank has declined the transaction and funds will not be transferred into the merchant's account.

There can be many reasons for a card being declined and it is not possible to list all of them.

Unfortunately, Worldnet Payments is not sent the reason for declines. This is due to information protection legislation. The “Declined” (or “Not Authorized”) text is actually sent by the cardholder’s bank and they do not provide any additional details. Only the cardholder can find out the reason for a decline.

## Not Authorised

The **Not Authorised** or **Declined** response means that the bank has declined the transaction and funds will not be transferred into a merchant’s account.

There are many reasons for a card being declined and they are not possible to be listed.

Unfortunately Worldnet Payments is not sent the reason for declines. This is due to information protection legislation. The “Not Authorised” (or “Declined“) text is actually send by the cardholder’s bank, and that's all they send. Only the cardholder can find out reasons for declines.

## Pick-up

**Pickup** is the same as a Referral A response and is a type of decline.

Pickup (or Referral A) means that the card has been marked as **lost or stolen by the cardholder**. In the customer present environment this would prompt the merchant to keep and cut up the card and send it back to your acquiring bank.

## Referral A

**Referral A** is the same as a Pickup response and is a type of a Decline.

Referral A (or Pickup) means that the card has been marked as **lost or stolen by the cardholder**. In the customer present environment, it is advisable that the merchant should retain the card, cut it and send it back to merchant's acquiring bank.

## Referral B

A **Referral B** means that the bank requires more information before they can approve the transaction. This is only relevant for **Virtual Terminal** (Telephone & Mail Order) transactions, and in the eCommerce environment it's treated as a decline.

If you are getting a “Referral B” response for a Virtual Terminal transaction then you should contact your acquiring bank immediately, because once these transactions settle, they can no longer be completed. They'll ask you for the transaction details and then give you an Authorization Code, which you can type into our Selfcare.

Your acquirer should have provided you with the relevant “referral phone number” to call them in regards to these queries. Please note that we do not have access to these contact numbers.
