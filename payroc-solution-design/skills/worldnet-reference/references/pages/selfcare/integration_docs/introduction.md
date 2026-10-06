<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:integration_docs:introduction | synced: 2026-10-05 -->

# Testing Guide

 This page is intended to guide you through the best practices for testing your integration with Worldnet.

## Test environment

Make sure all the testing is done against one of our sandbox accounts. Testing on a live account can cause problems such as:

1. Unnecessary downtime
1. Live transaction corruption/loss
1. Chargebacks
1. PCI DSS implications

## Setting up the test environment

You should ensure that your test environment is configured as close as possible to your live environment, particularly:

1. Web server (IIS/Apache) version
1. Web server configuration, especially the language interface (PHP/ASP etc.) and session timeout
1. Database connectivity
1. Firewall
1. Latest versions of our shopping carts and SDKs

## Background validation

If you're using our **[Hosted Pages](https://developers.worldnetpayments.com/hosted_pages/introduction)** solution, you should seriously consider implementing **[Background Validation](https://developers.worldnetpayments.com/hosted_pages/hpp_background_validation)**.

With background validation you can provide a webhook to which our host will send the result of every transaction in addition to the response you already get from the page. This ensures that your order system accurately reflects the transaction result even in the case where the cardholder redirect fails.

## Security concerns

The PCI DSS states that you should never use live cards in a test environment, otherwise this environment is also subject to PCI audit and DSS rules.

> **Note**
> Worldnet cannot be held accountable for live cards being put through our test systems and sandbox accounts.

## What to test

### All cases

1. Host is unavailable (i.e. use invalid sandbox URL)
1. Incorrect parameters in the request
1. The hash string sent by the gateway in the response is properly validated
1. Make sure your application is able to handle the different types of responses
1. Refreshing the receipt page does not re-perform the transaction/resend the receipts
1. PCI DSS guidelines are met in all scenarios
1. All required currencies are processed correctly

### Per integration method

#### Hosted Payment Page

1. Customer doesn't complete transaction (e.g. closes browser window)
1. The Receipt Page URL is misconfigured in your terminal
1. Customer takes over 60 mins to complete transaction
1. Simultaneous transactions do not interfere with each other
1. Background validation is successful for all transactions and responses, if applicable

#### REST API

1. API Key is valid
1. Access tokens are re-generated before they expire
1. Only digits with no spaces are sent into Card number/CVV fields
1. Host returns a Bad Request error due to incorrect content in the JSON request
1. Host returns an Unprocessable Entity error to indicate a business rule or constraint violation

#### When using shopping carts

Testing will be quite specific depending on the shopping cart and plug-in being used. You should cover all the relevant test above for your integration method, even though the functionality is obscured by the plug-in you are using, the issues outlined above can still occur.

Other shopping cart issues that should be tested are:

1. Only digits with no spaces are sent into Card number/CVV fields
1. Order status is updated correctly in shopping cart
1. Customer e-mails are populated correctly
1. Customers get the right number of e-mails (our host may also send an e-mail to the customer depending on the plug-in)
1. Session timeouts do not cause transactions to be dropped
1. Transactions over 1,000 and 1,000,000 Euro/Pounds/Dollar etc. are handled correctly

## Testing resources

### Sandbox

Initial testing doesn't require a dedicated test account, you can use our sandbox to get started. Ready to play around? **[Sign up](https://developers.worldnetpayments.com/selfcare/signup)** for a sandbox account.

### Credit Cards

Test cards that can be used on our host are:

| **CARD SCHEME** | **CARD NUMBER** | **REQUIRES CVV** |
|---|---|---|
| American Express | 3400000000000000 | Y |
| Debit MasterCard | 5100270000000007 | Y |
| Diners | 3600000000000008 | N |
| Discover | 6011000000000004 | Y |
| JCB | 3528000000000007 | Y |
| Maestro | 5000330000000000 | Y |
| MasterCard | 5001650000000000 | Y |
| Switch | 6301144000000009 | N |
| Visa Credit | 4539858876047062 | Y |
| Visa Debit | 4000060000000006 | Y |
| Visa Electron | 4001020000000009 | N |

### Electronic Benefit Transfer (EBT) Cards

Currently, EBT processing is only supported by **FiServ** and **TSYS** processors.

| **CARD NUMBER** | **BENEFIT CATEGORY** | **PIN** |
|---|---|---|
| 6007602801003837964 | Food Stamp | 1234 |
| 6007602801003837965 | Food Stamp | 1234 |
| 6007602801003837967 | Cash Only | 1234 |
| 6007602801003837968 | Cash Only | 1234 |
| 6007602801003837969 | Cash Only | 1234 |
| 6007602801003837971 | Inactive card | 1234 |

> **Note**
> You can use any **CVV** and **Expiry Date** as long as the expiry date is a valid future date and the CVV is either a `4-digit` (Amex) or `3-digit` (other brands) numeric code.

### Response Codes

Simulate responses by using different cent amounts for transactions. The cent values and their respective responses are:

| **Cent Value** | **Response** |
|---|---|
| 0.01 | Declined |
| 0.02 | Referral |
| 0.03 | CVV failure (Decline) |
| Any other | Authorised |

Meaning that if you enter `5.01`, `99.01` or `1754.01` you will get a decline, for example.

## Advanced solutions

For large merchants, Worldnet will be happy to provide you with specialized test scripts and help with any struggle you may go through during integration. Feel free to **[contact](https://www.worldnetpayments.com/contact/)** our team of experts.
