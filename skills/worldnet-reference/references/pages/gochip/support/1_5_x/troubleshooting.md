<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:1_5_x:troubleshooting | synced: 2026-10-05 -->

# Troubleshooting

1. [What's the minimum java version requirement?](#1)
1. [What's the minimum Android version requirement?](#2)
1. [What's the minimum IOS version requirement?](#3)
1. [What's the minimum Ubuntu version requirement?](#4)
1. [What's the minimum .NET C# version requirement?](#5)
1. [What should I use the sample app for?](#6)
1. [What are the options for collecting signature?](#7)
1. [What are all possible response codes?](#8)
1. [What does the response code mean?](#9)
1. [How can I test the different response codes?](#10)
1. [What is an Input method?](#11)
1. [How do I change my input method?](#12)
1. [What is a stored value card and how should I manage it?](#13)
1. [What is a KSN Error?](#14)
1. [What information do I need to supply to have my KSN added to the system?](#15)
1. [How do I report an issue to the integration team?](#16)
1. [What information should I provide when requesting help on an issue?](#17)
1. [What do I need to start testing?](#18)
1. [What is the payconfig file?](#19)
1. [What does the payconfig file contain?](#20)
1. [What RBA version is supported on Ingenico Devices?](#21)
1. [How do I check my firmware or RBA version?](#22)

#### What's the minimum java version requirement?

The SDK requires minimum java version 1.7.

#### What's the minimum Android version requirement?

The SDK requires minimum Android version 5.

#### What's the minimum IOS version requirement?

The SDK requires minimum IOS version 9.1.

#### What's the minimum Ubuntu version requirement?

The SDK requires minimum version 16.04.

#### What's the minimum .NET C# version requirement?

The SDK requires minimum .NET C# version 4.5.1.

#### What should I use the sample app for?

When downloading our SDK there is also an option to download our latest sample application along with it. Our sample application can be a good foundation for your integration as you can view the code to see how certain functions are expected to work. This can also be useful for comparing to your application and troubleshooting.

#### What are the options for collecting signature?

As part of the cardholder verification method some cards require signature to be collected. The SDK gives you 2 options to choose from.

1. Collect the signature automatically, this is the default option. It triggers the onSignatureRequired callback method which asks you to draw a signature in the app and submit the signature via the SDK. Once submitted, the transaction will continue.
`sale.setSignatureCollection(SignatureCollection.AUTOMATIC);`
1. Collect the signature manually, this option is usually used when collecting signature on the paper receipt. The onSignatureRequired callback won't be triggered.
`sale.setSignatureCollection(SignatureCollection. MANUAL);`

#### What are all possible response codes?

- `A - Approval` Transaction was approved.
- `D - Declined` Transaction was declined.
- `C - Pick Up` Transaction was declined. This type of decline means that the card has been marked as lost or stolen by the cardholder.
- `R - Referral` Transaction was declined. A referral means that the merchant should call the authorization center because more information is needed regarding the cardholder.

#### What does the response code mean?

When a transaction is approved, the response code of A is returned. Your solution **NEEDS TO VERIFY THE RESPONSE CODE** before continuing. Receiving any response doesn't indicate that the transaction was approved. **For the transaction to be approved, the response code must be A.**

#### How can I test the different response codes?

On a First Data terminal, transactions below $100.00 will receive an Approved response.

Transactions in the amount of $45.67 will receive No Host Response to simulate Time-out Reversal testing.

Transactions above $100.00 will receive a specific Error response (last three digits of amount, despite the decimal separator).

E.g., for the amount $101.23 response code 123 will be returned

On a TSYS Sierra terminal, the following cent values will trigger different responses:

| CENT VALUE | RESPONSE |
|---|---|
| 0.01 | Declined |
| 0.02 | Referral |
| 0.03 | CVV failure (Decline) |
| Any other | Authorised |

An American Express card and a value of $10.00 will trigger a timeout response.

#### What is an Input method?

Input method allows you to configure how a card is read using the device readers.

The following input methods are supported and should be self explanatory:

    - SWIPE
    - INSERT
    - TAP
    - SWIPE_OR_INSERT
    - SWIPE_OR_TAP
    - INSERT_OR_TAP
    - SWIPE_OR_INSERT_OR_TAP
    - SWIPE_OR_INSERT_OR_TAP_OR_KEYED
    - SWIPE_OR_INSERT_OR_KEYED
    - SWIPE_OR_KEYED

#### How do I change my input method?

You can choose the input method you would like to use for your integration by setting the following SALE object property. Eg. `sale.setTransactionInputMethod(CoreTransactionInputMethod.SWIPE_OR_INSERT_OR_TAP_OR_KEYED);`

#### What is a stored value card and how should I manage it?

Stored value cards are also referred as Gift cards. Unlike other bank cards where the monetary value is stored in a bank account, for gift cards monetary value is stored in the card itself.

Currently we don't support processing the gift card payments through our gateway however we will be able to send the gift card data to the merchant for them to process locally on their system for Ingenico devices. To use this option the merchants have to share the bin ranges of their gift cards to our integrations team and they will help configuring the devices with these bin ranges which will allow the device to send the unencrypted gift card data.

#### What is a KSN Error?

When a device is shipped with Worldnet Test/Live keys there is an extra step to add the KSN of the device to our HSM for decryption. This is a common error that is usually easily resolved by contacting %CompanyContact with the EMV and TRACK KSNs from your device.

#### What information do I need to supply to have my KSN added to the system?

The first 10 digits of the EMV and TRACK KSNs should be provided.

#### How do I report an issue to the integration team?

All issues should be reported to %CompanyContact

#### What information should I provide when requesting help on an issue?

When contacting our integrations team please include the following information:

    - Description of the issue and how to recreate it
    - Logs from our middleware

#### What do I need to start testing?

To begin your testing process you should have the following:

    1. **TEST credentials to the Worldnet platform - Terminal ID and Secret**

The Worldnet integration team will give you login credentials to the Virtual Terminal and SelfCare reporting system. These credentials should also be used to point your integration to our test host simulator.

You can use SelfCare to view transactions and perform actions such as Refunds/Voids etc.Training on SelfCare/ Virtual Terminal can provided by our support team on request.
    1. **TEST POS device supplied by our partner**

To work with our TEST system please note you must have a device with TEST firmware and TEST encryption keys injected in it. Please make sure the firmware is a version that we have validated.

> **Note**
> LIVE devices injected with LIVE Keys will not work on the Worldnet TEST system.

    1. **TEST Cards**

We recommend that you have test cards for each brand you want to use as part of your integration. We also recommend that the cards are capable of the features you wish to support. If needed, test cards can be purchased from ICC Solutions.

(Cards such as Live cards and expired cards should not be used as part of the testing stage of the integration)

#### What is the payconfig file?

The payconfig.xml file is the GoChip configuration file that contains URLs used to access the servers. This file should be added to your project.

#### What does the payconfig file contain?

The payconfig file contains the following configurations which are described below:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string name="gatewayLiveUrl">https://https://payments.worldnettps.com/merchant</string>
  <string name="gatewayTestUrl">https://https://testpayments.worldnettps.com/merchant</string>
  <string name="gatewayDevUrl">https://https://devpayments.worldnettps.com/merchant</string>
  <string name="isvToken"></string>
</resources>

```

    - gatewayTestUrl: URL that points to the TEST server.

By switching to test mode the SDK will point to gatewayTestUrl when communicating with the server. Test mode should be used for development. `terminal.setMode(CoreMode.TEST);`
    - gatewayLiveUrl: URL that points to the LIVE server.

After finishing the development of your app, don't forget to change the mode to Live which will point the SDK to gatewayLiveUrl defined in payconfig file. `terminal.setMode(CoreMode.LIVE);`
    - gatewayDevUrl : URL that points to the DEV server.

The Dev Mode is used to point to gatewayDevUrl defined in payconfig.xml file. This mode should only be used to test unreleased server features. `terminal.setMode(CoreMode.DEV);`
    - isvToken: Generated token used for identifying the ISV integration.

When you begin your integration we will provide you a generated test token to add to your payconfig file. You can then add this to the isvToken string which is located underneath the list of hosts.

Once the integration is finished you will be provided with a production token. This will need to replace the test token in the payconfig file.

#### What RBA version is supported on Ingenico Devices?

| Device | RBA 21.0.2 | RBA 23.0.2 | RBA 23044 |
|---|---|---|---|
| IUC285 | - | Supported | *Supported |
| IPP320 | Supported | Supported | *Supported |
| IPP350 | Supported | Supported | *Supported |

*Recommended RBA.

#### How do I check my firmware or RBA version?

The getDeviceInfo call will return your firmware or RBA version in the logs.
