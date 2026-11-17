<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:integration_docs:sandbox_testing | synced: 2026-10-05 -->

## What is a sandbox

The Worldnet sandbox is a shared testing account where you can validate the initial phases of your integration. These accounts (one per currency) are publically available on our test host and they provide very basic functionality and no access to the back-end ‘Merchant Selfcare’

## What can you test

Sandbox accounts provide the ability to perform basic sales and refunds through our test host with any of the three integration methods, including DCC. In order to be able to test pre-authorisations, completions, SecureCard functionality, subscriptions, unreferenced refunds or any other feature or currency, you must request a full test account by e-mailing [ [email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection#<SAMPLE_HEX_VALUE>). In order to test a Hosted Payment Page customization you need to obtain access to a full test account first.

## API Keys & Account Details

### Sandbox EU (ID: 4479)

Merchant API Key:

```
<REDACTED: sandbox API key - see Worldnet developer portal>
```

**Terminal 4479001 (EUR)**
Processor: Elavon
Secret: <REDACTED>
Shopify Password: <REDACTED>
**Terminal 4479002 (GBP)**
Processor: Elavon
Secret: <REDACTED>
Shopify Password: <REDACTED>
### Sandbox US (ID: 4480)

Merchant API Key:

```
<REDACTED: sandbox API key - see Worldnet developer portal>
```

**Terminal 4480001 (USD)**
Processor: FDRC
Secret: <REDACTED>
Shopify Password: <REDACTED>
> **Note**
> API Keys are only relevant for **[REST API](https://developers.worldnetpayments.com/apis/merchant/)** integrations.
