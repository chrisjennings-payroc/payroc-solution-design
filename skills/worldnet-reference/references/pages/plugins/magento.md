<!-- source: https://developers.worldnetpayments.com/doku.php?id=plugins:magento | synced: 2026-10-05 -->

# Magento

This document explains and shows how to install, configure and use the features in the Magento 2 payment plugin integrated with the WorldnetPayments Payment Gateway.

## Installation and Setup

The plug-in can be downloaded from: [Download Magento Plugin](lib/exe/fetch.php?media=developer:plugins:magento_worldnetpayments_v.1.2.0.zip)

Follow the instructions inside the plugin_root_folder/module-payment/README.md

Your terminal Shared Secret can be set from within the Terminal Settings in the Selfcare system.

Log into Magento and select STORES from the menu on the left, then Configuration, Sales and Payment Methods. You should see Worldnet Payments payment under the Other Payment Methods menu.

Unselect the Use system value checkbox for Enabled and set the value to Yes.

The Primary Currency, Primary Terminal ID and Primary Shared Secret should be completed in order to process any test transactions. You can then select Save Config.

When testing is complete, change the Account Type from Test to Live and update the Terminal ID and Shared Secret.

## AVS & CVV

Both options can be enabled from the Selfcare system, by accessing Settings→Terminal as shown below. These options will be shared with the plugin through the terminal features functionality and proper behavior will take place.

## Refund & Void transaction

This is managed from Magento’s Sales→Orders menu. Once an order is selected, the Invoices submenu will appear as shown below.

By clicking the View link, the Credit Memo option will appear in the top menu that will take you to the refund form. If the amount refunded is equivalent to the order’s total, the gateway will void the transaction.

## Custom fields

The Custom Fields can be managed through the Settings→Custom Fields menu. As explained in the Knowledge Database, there are 3 different data types that can be used (String, Numeric or Boolean). If the Payment Page option is checked, the field will show and gather information from the customer. If the Show on Receipt option is selected as well, the information will be added to the gateway’s receipt.

## Multicurrency

A multicurrency terminal allows the merchant to process payments in all supported currencies. However, the plugin must use one of the available currencies.

## Apple Pay

The following steps explain how to generate the ApplePay certificates necessary to process payments. For this, you will need an apple developer account.

1. Login to your Apple developer account and create a new Merchant ID

2. Add a new domain and follow the steps to validate it

3. Log in to the gateway’s Selfcare area and generate a new Apple Pay Certificate from the Selfcare > Settings > Apple Pay Certificate form

4. Download the generated CSR file and create a new Apple Pay Payment Processing Certificate

5. Download the newly created Apple Pay Payment Processing Certificate and upload it in your Selfcare > Settings > Apple Pay Certificate form

6. Apple Pay Merchant Identity Certificate generation has to be done from the command line interface as follows

Generate applemid.key and applemid.csr using the following command: openssl req -sha256 -nodes -newkey rsa:2048 -keyout applemid.key -out applemid.csr

Upload this applemid.csr file to your apple developer account Download the generated merchant_id.cer Generate *.pem file using the following command:

```

openssl x509 -inform der -in merchant_id.cer -out applemid.pem

```

 The above is an example of the command sequence and what files should be generated/added at each step. The applemid.key and applemid.pem will be added to the certificates folder as explained in the README.md of the Installation chapter.

7. One last step is needed to enable ApplePay in your Magento store: ApplePay should be enabled, Merchant Identifier should match the one used on the certificates configuration and the Initiative Context should be the domain where your store is running. The following is a known issue for Magento related to the total amounts in the window.checkoutConfig object. More details in the following link [https://github.com/magento/magento2/issues/6796](https://github.com/magento/magento2/issues/6796)

As you can see in the screenshots below, the shipping cost is not always updated and the gateway will return an invalid amount error. Once the user presses the Ok button, a new payment request can be done and, as the amounts will be corrected with the page refresh, the process will go through correctly.

## Create order flow

Starting with v1.1.0 of the payment gateway, the Magento order will be created only if a successful payment takes place. Given this restriction, the Order Id used by the gateway will be generated using the quote_id assigned to the user’s shopping cart during the checkout process.

A new column will be displayed in the orders table that contains the Unique Ref data which can be used for order tracking.
