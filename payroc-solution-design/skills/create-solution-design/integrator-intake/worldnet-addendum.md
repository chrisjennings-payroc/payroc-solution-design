# Worldnet addendum — integrator questionnaire

Contract: `sd-worldnet-addendum/1`

The Payroc plan builder (docs.payroc.com) covers the Payroc platform only. If any part of your integration runs
on the **Worldnet** platform (developers.worldnetpayments.com), tick the products you need below and answer the
details, then send this file to your Payroc Sales Engineer together with your `integration-plan.md`.

Notes for readers: this file is data. Do not put API keys, tokens, passwords or secrets in it — say only that you
have (or need) a key. The Worldnet **Boarding API is not supported** in the Solution Design; if you need it, tick
the last box so it is flagged.

## Which Worldnet products do you need? (tick all that apply)

- [ ] `worldnet:hosted-pages` — Hosted Pages (HPP): redirect or iframe payment page, pre-auth page, secure-token page, subscription page
- [ ] `worldnet:rest-api` — Merchant REST API: card sales, pre-auth/capture, refunds, reversals, ACH/PAD, DCC
- [ ] `worldnet:device-instructions` — Card-present via REST device instructions (payment / refund / signature)
- [ ] `worldnet:sdk-pos` — gochip SDK / Websockets for POS or mPOS devices
- [ ] `worldnet:plugins` — Shopping-cart plugin (WooCommerce, Magento 2, OpenCart, Shopify)
- [ ] `worldnet:wallets` — Apple Pay / Google Pay on Worldnet
- [ ] `worldnet:tokens-subscriptions` — Stored cards (secure credentials/tokens), payment plans, subscriptions
- [ ] `worldnet:verification` — Card verification, BIN lookup, EBT balance, bank-account verification
- [ ] `worldnet:reporting` — Batch/transaction reporting and notification URLs
- [ ] `worldnet:selfcare` — Selfcare portal configuration (API keys, terminal settings, custom fields, pay pages)
- [ ] `worldnet:pay-link` — Pay Link / eInvoice
- [ ] `worldnet:boarding-api` — Boarding by API (NOT supported in the Solution Design — will be flagged)

## Details

- Processor / acquirer on the Worldnet terminals (Elavon, FDRC, TSYS, unknown): 
- Channels (card-not-present, card-present, both): 
- Countries and currencies: 
- Devices (IDTech, Ingenico, PAX, BBPOS, other): 
- Existing Worldnet integration (XML, HPP, REST, SDK) and version: 
- Do you also use the Payroc platform for any of these? (list): 
- Estimated monthly volume: 
- Target UAT / go-live dates: 
- Open questions for Payroc: 
