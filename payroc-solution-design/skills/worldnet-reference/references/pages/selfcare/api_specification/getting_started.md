<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:getting_started | synced: 2026-10-05 -->

# API Specification

 Welcome to the API Specification. Here you will find all necessary information to help you understand your integration to our Payment gateway.

## Things You Should Know First

This section helps you to understand the elements for your solution's integration such as which integration method to use, how to configure your account to perform each integration, how to use the custom fields, how to calculate the hash parameters of requests and responses, etc.

 [ **

### Special Fields and Parameters

HASH Calculation, Card Types, Custom Fields, Dynamic Descriptors, Multi-currency Terminal ID, Signature Field ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:special_fields_and_parameters) [ **

### Response Codes and Messages

Specific response codes and messages which may be returned in different features... ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:response_codes_and_messages) [ **

### Account Updater Background Notification

A longer and more detailed explanation of how this important mechanism works... ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:account_updater)

## The Hosted Page Integration Method

The Hosted Page (HP) is an integration method where the entry of some sensitive data is handled by the Payment Gateway so the merchant’s servers are not exposed to this data. This is advisable so as to reduce the security overhead of the integrated solution. For this scenario, Worldnet Payments becomes the responsible party for maintaining the security and integrity of the sensitive data sent to these pages.

These Hosted Pages are also highly stylized so that they look more appealing to the customers and improves their overall experience. For more details on that consult **[Pay Pages](https://developers.worldnetpayments.com/merchant/existing_merchant/selfcare_system/settings/pay_pages)**.

Cardholders are redirected to a page at the Payment Gateway. Upon the customer clicking the ‘submit’ button on that page, all data are collected, processed and the Payment Gateway sends the processing result back to the Merchant's site, also redirecting the Account Holder to the Merchant's result page, in a transparent way.

The following features are available for this integration method:

 [ **

### Payment

Payment and pre-authorization ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:hpp_payment_features) [ **

### Background Validation

Checks the transaction ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:hpp_background_validation) [ **

### Payment

Payment using Apple Pay technology ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:hpp_payment_features_applepay) [ **

### Payment

Payment using Google Pay technology ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:hpp_payment_features_googlepay) [ **

### Secure Tokens

Secure token registration and update ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:hpp_secure_tokens_features) [ **

### Subscription

Subscription and stored subscription registration ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:hpp_subscription_features) [ **

### Bulk Payments

Large payment file submission and result request ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:bulk_payments_features)

## The RESTful Integration Method

Our APIs are built around REST principles and OpenAPI Specification definitions. Complying to such industry standards means that we can offer developers a much better experience by exposing predictable resource-oriented URL's as well as a comprehensive range of HTTP response codes and verbs. Moreover, you have the possibility to enable and take full advantage of HATEOAS controls to provide out-of-the-box Discoverability and Functional-Awareness for your integrations.

Get started on building full-featured payment applications and join us in the Revolution of Intelligent Retail.

 [ **

### Merchant API

Merchant API Documentation ](https://docs.worldnettps.com/apis/merchant/) [ **

### Boarding API

Boarding API Documentation ](https://docs.worldnettps.com/apis/boarding/)

## Other Information

 [ **

### Video Tutorials

Examples and tutorials on how to use our API ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:video_tutorials) [ **

### Changes

Change control history of the API ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:change_log) [ **

### Glossary

Guide's glossary ](https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:glossary)
