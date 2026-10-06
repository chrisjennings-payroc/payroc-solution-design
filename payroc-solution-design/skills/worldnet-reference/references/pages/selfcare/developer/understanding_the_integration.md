<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:developer:understanding_the_integration | synced: 2026-10-05 -->

# Understanding the Integration

## How the Gateway Works?

Our Platform offers a secure server-based transaction processing service which enables your business to authorize and process credit and debit card transactions online, in real-time. All the information necessary to process the transactions is sent over a secure, encrypted connection.

Once the transaction details have been provided and submitted to the payment gateway, the server connects with your acquiring bank to perform the authorization procedures and, depending on the transaction type and the acquirer's response, a receipt is returned to your customer.

The transactions are settled automatically by the Payment Gateway and the Acquiring Bank deposits the funds into your bank account.

Worldnet Payments automatically archives sales that are finalized so that you can refer to them at a later date.

This guide is going to provide instructions on how to integrate a website or application with the payment gateway and take automatic credit card payments.

## Choosing Your Integration Method

There are two integration methods available: **Hosted Payment Page** and **XML**. You can use one or a combination of them as required, but you should consider the integration method carefully before starting any development planning.

The following information is presented to help you decide on the most appropriate integration method for your solution with the Worldnet Payments gateway. It is intended for review after you have decided upon your merchant account but before you start integrating with us. All costs will be considered including integration cost, ongoing merchant costs, PCI DSS compliance costs and Worldnet Payments's own charges. Different technologies, languages, consumer industries, server environments and other technical considerations will also be addressed.

### The Hosted Page Integration Method

The Hosted Page (HP) has been created as a method for small-to-medium sized organisations to integrate their websites with our payment gateway. This is a hosted service with the highest levels of internet security, whose appearance can be customized to look just like your site. This is solely for use as a payment gateway for websites.

The benefits of the HP:

- **No cost for SSL certificate**: PCI DSS requires that web pages accepting credit card information must have SSLv3 128-bit minimum certificates. Our host has a 128-bit to 256-bit certificate with full “green bar” functionality for extra customer confidence. The equivalent certificate from VeriSign is the “Secure Site Pro with EV” which currently costs $1,499/year (March 2010).
- **No PCI considerations**: PCI also states that any site accepting card information must NEVER store the CVV, and if it does store the card number, it must be 256-bit AES encrypted. Most web servers log traffic to and from them which may include card numbers. These logs would have to be audited on a continual basis to ensure that card numbers are not being stored. Also, if you accept any sensitive card information on your site you jump up from a PCI SAQ A (Self Assessment Questionnaire) to an SAQ D. This means that you have to answer 30 pages of questions instead of 2!
- **Ease of integration**: As opposed to other integration methods, the HPP integration is VERY simple. You just have to submit a simple web form to us and then display the response that our host sends back.
- **Everything under one roof**: To enable features when using the Hosted Payment Page such as 3DSecure, eDCC, Mobile Payments etc., there is no extra development to do. We just flick a switch once we have all the data and your customers will then be offered the new feature(s).
- **Plug-in availability**: We have Hosted Payment Page plug-ins readily available for almost all our available shopping carts.
- **Can be implemented in an iframe**: If you do not want the customer to leave your site you can implement the HPP within an iframe. This is preferable for some merchants, but also means that the customer will not see the “green bar” that would be displayed otherwise.

### The XML Gateway Integration Method

The XML gateway is intended for much more elaborate integrations and for very large sites. It offers full access to all of our products and methods through a high speed, common platform gateway. This can be used as a payment gateway for a large website, but it can also be integrated into your existing corporate infrastructure. Companies using the XML gateway must maintain their own security and are subject to more rigorous PCI security assessment.

Benefits of the XML gateway:

- **Access**: All of our products can be controlled through the XML gateway, whether you want to process a payment, register card information for secure storage on our system, setup a recurring payment, check the status of existing subscriptions or refund a customer.
- **Site integration**: If you would like to integrate the card processing heavily into your site, then the XML gateway is the way to go. You can store card references on your site for loyal customers so that they don't have to put their card details in each time, or display the status of a customers subscription to your product, etc.

## Costs

### Small Business

For small businesses the Hosted Payment Page is nearly always the most cost effective route. There is an extra cost involved with using this service, but it is greatly outweighed by the savings made both directly because an SSL certificate does not have to be maintained and because the integration is very simple compared to other methods, and indirectly in that it removes the workload required to manage PCI compliance.

### Large Enterprise

For large enterprise the costs involved can be quite difficult to calculate. You must take into account development costs, opportunity costs during the development period, the value of customer loyalty due to having an easy to use site, etc.

## Testing Your Integrations

In order to integrate with the Payment Gateway, a few modifications are necessary to your solution.

Once you have completed your modifications, perform the relevant transaction types as listed in our **Merchant Validation Document**.

Please note that when testing you must supply at least TWO successful transactions per transaction type that you intend to use. Please refer to the functionality checklist in the **Merchant Validation Document**. Two transactions are necessary to ensure consistency when our Integration team analyses your transactions. Record all pertinent information relating to the testing and return the completed forms to our integration team via email. The integration team will contact you to confirm that you have successfully validated against the Payment Gateway.

For details on testing, please visit the **[Integration Docs](https://developers.worldnetpayments.com/selfcare/integration_docs/introduction)** and explore our guides.
