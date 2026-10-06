<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:troubleshooting | synced: 2026-10-05 -->

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
1. [What is the Integration ID?](#20)
1. [What does the payconfig file contain?](#21)
1. [What RBA version is supported on Ingenico Devices?](#22)
1. [What UPP version is supported on Ingenico Devices?](#23)
1. [How do I check my firmware or RBA version?](#24)
1. [How do I handle the new transaction cancellation flow introduced in Websocket 3.0.28 and SDK 1.6.28?](#25)
1. [I'm getting a network error during transactions, how do I handle this?](#26)
1. [What Axium Firmware version is supported on Ingenico Devices?](#27)

#### What's the minimum java version requirement?

The Java SDK requires Java 8 (1.8) or higher. The Android SDK requires Java 17 or higher. The Java WebSockets SDK requires Java 17 or higher.

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

    1. **TEST credentials to the Worldnet platform - Terminal ID**

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

#### What is the Integration ID?

An Integration ID is a key used to identify the business operating the terminal.

> **Note**
> The system will reject any transaction that is already associated to a partner and it is not using the correct Integration ID.

#### What does the payconfig file contain?

The payconfig file contains the following configurations which are described below:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="gatewayLiveUrl">https://payments.worldnettps.com/merchant</string>
    <string name="gatewayTestUrl">https://testpayments.worldnettps.com/merchant</string>
    <string name="gatewayDevUrl">https://devpayments.worldnettps.com/merchant</string>
    <string name="apiKey"></string>
    <string name="integrationId"></string>
    <string name="logFileAbsoluteDirPath"></string>
    <string name="logFileName">log_file.txt</string>
    <string name="logFileMaxLines">10000</string>
    <string name="logFileMaxFileSize">5MB</string>
    <string name="logFileMaxFileCount">0</string>
</resources>

```

    - gatewayTestUrl: URL that points to the TEST server.

By switching to test mode the SDK will point to gatewayTestUrl when communicating with the server. Test mode should be used for development. `terminal.setMode(CoreMode.TEST);`
    - gatewayLiveUrl: URL that points to the LIVE server.

After finishing the development of your app, don't forget to change the mode to Live which will point the SDK to gatewayLiveUrl defined in payconfig file. `terminal.setMode(CoreMode.LIVE);`
    - gatewayDevUrl : URL that points to the DEV server.

The Dev Mode is used to point to gatewayDevUrl defined in payconfig.xml file. This mode should only be used to test unreleased server features. `terminal.setMode(CoreMode.DEV);`
    - apiKey: Generated key used for identifying the API integration.

When you begin your integration we will provide you a generated test key to add to your payconfig file. You can then add this to the apiKey string which is located underneath the list of hosts.

Once the integration is finished you will be provided with a production key. This will need to replace the test key in the payconfig file.

Log files should be rotated properly based on the settings configured in payconfig.xml file.

    - active log file - the current log file which would be named to logFilename. The lines/size of this file is checked to determine if rotation is needed.
    - indexed/numbered log file - rotated files (i.e., if the logFileName is log_file.txt , a possible log file name would be log_file-0.txt

#### Rotation Policies:

    - Line-Based - logs are rotated when the active log file's number of lines goes above the configured maximum lines
    - Size-Based - logs are rotated when the active log file grows more than the maximum file size

#### Configuration:

    - **logFileAbsoluteDirPath** - absolute path to the preferred directory for the log files

default - project directory.
    - **logFileName** - preferred log file name

default - log_file.txt
    - **logFileMaxLines** - maximum log file lines to trigger line-based rotation. default - 10000.

min - 100.

    - **logFileMaxFileSizeM** - if this is set, we're gonna perform size-based log rotation. Otherwise, we'll do line-based rotation. default - 5MB if set to 0.

Sample values - 5000 (would be in bytes if no factor), 5KB, 5MB.

    - **logFileMaxFileCount** - number of indexed/numbered log files to keep (excluding the active log file). default - 0 (would only rotate the active log file).

max - 20 (to avoid rotating too many files).

#### What RBA version is supported on Ingenico Devices?

| Device | RBA 23.0.2 | RBA 2352 |
|---|---|---|
| IUC285 | Supported | *Supported |
| IPP320 | Supported | *Supported |
| IPP350 | Supported | *Supported |

*Recommended RBA.

#### What UPP version is supported on Ingenico Devices?

| Device | UPP 8.81.04 | UPP 8.81.12 |
|---|---|---|
| Lane3000 | *Supported | *Not Supported |
| Lane5000 | *Supported | *Not Supported |
| Lane7000 | *Supported | *Not Supported |
| Self 2000 | *Supported | *Not Supported |
| Self 3000 | *Not Supported | *Supported |
| Self 4000 | *Not Supported | *Supported |
| Self 5000 | *Supported | *Not Supported |
| Self 7000/8000 | *Supported | *Not Supported |

*Recommended UPP.

#### How do I check my firmware or RBA version?

The getDeviceInfo call will return your firmware or RBA version in the logs.

#### How do I handle the new transaction cancellation flow introduced in Websocket 3.0.28 and SDK 1.6.28?

We did a major refactoring on the way our SDK handles the cancellation of transactions. This introduced a new callback and status enum. We also had to remove a couple of errors and messages.

> **Note**
> For this release, the changes were only done for Android and Java SDK as well as Websocket.

### Pre-refactor Behavior

When you request for the transaction to be canceled by invoking the terminal method `cancelTransaction`, you always receive the `CoreMessage TRANSACTION_CANCELLED_BY_USER` regardless of the outcome of the cancellation.

The result could either be a successful cancellation request or a failed one in which performing the operation is not permitted.

You get the `CoreDeviceError TRANSACTION_CANCELLED` when the transaction cancellation is successfully executed and `CoreError/CoreDeviceError/CoreMessage TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE` when it's not allowed.

### Post-refactor Behavior

When you cancel the transaction, you either trigger the `onCancelTransactionAttempt` callback on the SDK or receive the message with type `RES_ON_CANCEL_TRANSACTION_ATTEMPT` on Websocket.

You get the `TransactionCancellationStatus` from both callback and Websocket message which describes the cancellation result. Please see the possible values below.

#### Transaction Cancellation Status

    - **CANCELLING** - cancellation is permitted and SDK is currently cancelling the transaction
    - **NOT_ALLOWED** - cancellation is not allowed, e.g. sale is already sent online and being authorized
    - **CANCELLED** - cancellation process has finished
    - **NOTHING_TO_CANCEL** - no transaction to be cancelled

> **Note**
> ### Scope
>
>
>
> Transaction cancellation coming from the device/device library or done by pressing the cancel button on the payment reader will not trigger the new callback/message.
>
> It's only when the you cancel by calling the terminal method `cancelTransaction` or sending the Websocket message with type `REQ_CANCEL_TRANSACTION`.

    - Java
    - Websocket

```

@Override
public void onCancelTransactionAttempt(TransactionCancellationStatus cancellationStatus) {
    AdminLogger.getInstance().log("onCancelTransactionAttempt - " + cancellationStatus, LogLevel.LEVEL_INFO);
    switch (cancellationStatus) {
        case CANCELLING:
            AdminLogger.getInstance().log("CANCELLING - The SDK is currently cancelling the transaction.", LogLevel.LEVEL_INFO);
            break;
        case NOT_ALLOWED:
            AdminLogger.getInstance().log("NOT_ALLOWED - Transaction cannot be cancelled at this stage. e.g. sale is being authorized online", LogLevel.LEVEL_INFO);
            break;
        case CANCELLED:
            AdminLogger.getInstance().log("CANCELLED - The transaction has been cancelled successfully.", LogLevel.LEVEL_INFO);
            break;
        case NOTHING_TO_CANCEL:
            AdminLogger.getInstance().log("NOTHING_TO_CANCEL - There is no transaction to be cancelled.", LogLevel.LEVEL_INFO);
            break;
    }
}

```

```

// CANCELLING
{
    "type": "RES_ON_CANCEL_TRANSACTION_ATTEMPT",
    "responseType": "RESPONSE_OK",
    "data": {
        "cancellationStatus": "CANCELLING"
    }
}

// NOT_ALLOWED
{
    "type": "RES_ON_CANCEL_TRANSACTION_ATTEMPT",
    "responseType": "RESPONSE_OK",
    "data": {
        "cancellationStatus": "NOT_ALLOWED"
    }
}

// CANCELLED
{
    "type": "RES_ON_CANCEL_TRANSACTION_ATTEMPT",
    "responseType": "RESPONSE_OK",
    "data": {
        "cancellationStatus": "CANCELLED"
    }
}

// NOTHING_TO_CANCEL
{
    "type": "RES_ON_CANCEL_TRANSACTION_ATTEMPT",
    "responseType": "RESPONSE_OK",
    "data": {
        "cancellationStatus": "NOTHING_TO_CANCEL"
    }
}

```

### Handling the Breaking Changes

As stated above, we added new callback and Websocket message and got rid of a couple of errors and messages. Please find below the details on how you should update your code.

#### TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE and TRANSACTION_CANCELLED_BY_USER

We have deleted the `TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE` and stopped sending them in the response with types `RES_ON_MESSAGE, RES_ON_DEVICE_ERROR` as it's deemed unnecessary.

Additionally, the `TRANSACTION_CANCELLED_BY_USER` message is now removed and will not be sent in the message with type `RES_ON_MESSAGE`.

If you are using the `TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE` message, you should now implement the new callback `onCancelTransactionAttempt` on the SDK and check for the `TransactionCancellationStatus.NOT_ALLOWED`.

On the Websocket, you should handle the response with type `RES_ON_CANCEL_TRANSACTION_ATTEMPT` and check for the `cancellationStatus - NOT_ALLOWED`

    - Old
    - New

```

// RES_ON_MESSAGE
{
    "type": "RES_ON_MESSAGE",
    "responseType": "RESPONSE_OK",
    "data": {
        "message": "TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE"
    }
}

// RES_ON_DEVICE_ERROR
{
    "type": "RES_ON_DEVICE_ERROR",
    "responseType": "RESPONSE_ERROR_GENERAL",
    "description": "string",
    "data": {
      "deviceError": "TRANSACTION_CANNOT_BE_CANCELED_AT_THIS_STAGE"
    }
}

```

```

{
    "type": "RES_ON_CANCEL_TRANSACTION_ATTEMPT",
    "responseType": "RESPONSE_OK",
    "data": {
        "cancellationStatus": "NOT_ALLOWED"
    }
}

```

For the `TRANSACTION_CANCELLED_BY_USER` message, you should now implement the new callback `onCancelTransactionAttempt` on the SDK and check for the `TransactionCancellationStatus.CANCELLED`.

On the Websocket, you now need to handle the response with type `RES_ON_CANCEL_TRANSACTION_ATTEMPT` and check for the `cancellationStatus - CANCELLED`

    - Old
    - New

```

{
    "type": "RES_ON_MESSAGE",
    "responseType": "RESPONSE_OK",
    "data": {
        "message": "TRANSACTION_CANCELLED_BY_USER"
    }
}

```

```

{
    "type": "RES_ON_CANCEL_TRANSACTION_ATTEMPT",
    "responseType": "RESPONSE_OK",
    "data": {
        "cancellationStatus": "CANCELLED"
    }
}

```

### SDK CoreAPISaleListener

We have introduced the new callback `onCancelTransactionAttempt` in the `CoreAPISaleListener` interface. This means you have to add the new method in your class that implements the `CoreAPISaleListener`.

> **Note**
> You are not forced to implement the new callback or handle the new Websocket message type if your current code doesn't care for the cancellation result or you are not using the deprecated errors and messages detailed above.

## Transaction Communication Error

> **Note**
> This feature is only available on Websocket version >=3.0.28 and SDK version >=1.6.28.

We added a new dedicated callback that is triggered whenever a network error occurs while a transaction is being authorized online.
This lets you know if you need to perform a reversal.

The new callback `onTransactionCommError` was added to the `CoreAPISaleListener` interface so you are required to implement it in the class that uses the said interface.

When callback is fired, you'll have access to the error as well as the transaction's `CoreSale` object.

    - C#
    - Java
    - ObjC
    - Websocket

```

public void OnTransactionCommError(CoreSale sale, CoreError error, string message)
{

}

```

```

@Override
public void onTransactionCommError(CoreSale sale, CoreError error, String message) {

}

```

```

- (void)onTransactionCommError:(CoreSale*)sale withError:(CoreError) error withMessage:(NSString*)message{

}

```

```

{
    "type": "RES_ON_TRANSACTION_COMM_ERROR",
    "responseType": "RESPONSE_ERROR_GENERAL",
    "data": {
        "sale": {
        // sale object
        },
        "error": "ERROR_TIMEOUT",
        "message": "timeout"
    },
    "description": "onTransactionCommError"
}

```

#### What Axium Firmware version is supported on Ingenico Devices?

| Device | FW v1.14.0 |
|---|---|
| DX4000 | *Supported |
| DX8000 | *Supported |
| EX8000 | *Supported |
| RX7000 | *Supported |

*Recommended Axium FW.
