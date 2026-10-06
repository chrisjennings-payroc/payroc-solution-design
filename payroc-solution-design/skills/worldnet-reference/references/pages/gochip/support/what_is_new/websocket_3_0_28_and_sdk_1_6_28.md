<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:what_is_new:websocket_3_0_28_and_sdk_1_6_28 | synced: 2026-10-05 -->

# What's New in Websocket 3.0.28 & SDK 1.6.28

> **Note**
> This release has required changes to the interface which are not backwardly compatible. Please see below for details.

### Breaking Changes and New Flows

1. [Secure Card to Secure Token Rebranding](#1)
1. [Transaction Cancellation](#2)
1. [Transaction Communication Error](#3)

### New Features

1. [Frictionless Payment Feature](#4)
1. [Configurable Host Request Timeout](#5)
1. [IDTech Card Removal Timeouts](#6)
1. [IDTech MiniSmart II APDU Command Exchange](#7)

## ** Breaking Changes and New Flows

## Secure Card to Secure Token Rebranding

For the rebranding, we had to update all of the Secure Card references in the Websocket and SDK.

Please see below the breaking changes on Websocket and SDK.

### Websocket Breaking Changes

#### Message Types

- REQ_SET_DELAYED_AUTH_WITH_SECURE_CARD_ENABLED → REQ_SET_DELAYED_AUTH_WITH_SECURE_TOKEN_ENABLED
- REQ_SET_POLLING_WITH_SECURE_CARD_ENABLED → REQ_SET_POLLING_WITH_SECURE_TOKEN_ENABLED
- REQ_REGISTER_SECURE_CARD → REQ_REGISTER_SECURE_TOKEN
- REQ_UPDATE_SECURE_CARD → REQ_UPDATE_SECURE_TOKEN
- REQ_DELETE_SECURE_CARD → REQ_DELETE_SECURE_TOKEN
- REQ_LOAD_SECURE_CARD → REQ_RETRIEVE_SECURE_TOKEN
- REQ_RETRIEVE_SECURE_CARD_HISTORY → REQ_RETRIEVE_SECURE_TOKEN_HISTORY
- RES_ON_SECURE_CARD_RESPONSE → RES_ON_SECURE_TOKEN_RESPONSE

#### Messages

**Secure Token Response fields**

- secureCard → secureTokenResponse
- secureCardReference → secureTokenCredentialsNumber
- secureCardMerchantReference → secureTokenMerchantReference
- coreSecureCard → coreSecureToken
- cardReference → credentialsNumber

- Old
- New

```

{
    "type": "RES_ON_SECURE_CARD_RESPONSE",
    "data": {
        "secureCard": {
                "secureCardReference": "123456",
                "secureCardMerchantReference": "MREF"
                "coreSecureCard": {
                    "cardReference": "123456",
                    ...
                }
        }
    }
}

```

```

{
    "type": "RES_ON_SECURE_TOKEN_RESPONSE",
    "data": {
        "secureTokenResponse": {
                "secureTokenCredentialsNumber": "12356",
                "secureTokenMerchantReference": "MREF",
                "coreSecureToken": {
                    "credentialsNumber": "123456",
                    ...
                }
        }
    }
}

```

   **Init Device - Secure Token history flag**

- secureCardHistory → secureTokenHistory

- Old
- New

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
            ...
            "secureCardHistory": true
            ...
    }
}

```

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
            ...
            "secureTokenHistory": true
            ...
    }
}

```

   **Process Sale - merchant reference**

- secureCardMerchantRef → secureTokenMerchantRef

- Old
- New

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
            ...
            "secureCardMerchantRef": "MREF1"
            ...
    }
}

```

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
            ...
            "secureTokenMerchantRef": "MREF1"
            ...
    }
}

```

   **Sale Response - merchant and card reference**

- cardReferenceNumber → secureTokenCredentialsNumber
- secureCardMerchantRef → secureTokenMerchantRef

- Old
- New

```

{
    "type": "RES_ON_SALE_RESPONSE",
    "responseType": "RESPONSE_OK",
    "data": {
        "saleResponse": {
                "cardReferenceNumber": "123456",
                "secureCardMerchantRef": "MREF",
                ...
            }
    }
}

```

```

{
    "type": "RES_ON_SALE_RESPONSE",
    "responseType": "RESPONSE_OK",
    "data": {
        "saleResponse": {
                "secureTokenCredentialsNumber": "123456",
                "secureTokenMerchantRef": "MREF",
                ...
            }
    }
}

```

### SDK Breaking Changes

#### Classes, Fields

- CoreSecureCard → CoreSecureToken
(field) cardReference → credentialsNumber
- CoreSecureCardResponse → CoreSecureTokenResponse
- CoreEmvSecureCard → CoreEmvSecureToken
- CoreKeyedSecureCard → CoreKeyedSecureToken
- CoreOCRSecureCard → CoreOCRSecureToken
- CoreTrackSecureCard → CoreTrackSecureToken
- CoreAPISecureCardListener → CoreAPISecureTokenListener
(callback) onSecureCardResponse → onSecureTokenResponse
- CoreSale
(field) coreSecureCard → coreSecureToken
- CoreResponse
(field) cardReferenceNumber → secureTokenCredentialsNumber
(field) secureCardMerchantRef → secureTokenMerchantRef

#### Terminal InitDevice Data Map Field

- secureCardHistory → secureTokenHistory

- Old
- New

```

// Old Android
HashMap data = new HashMap();
data.put("secureCardHistory", true);
AndroidTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

// Old C#
Dictionary data = new Dictionary();
data.Add("secureCardHistory", true);
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

// Old Java
HashMap data = new HashMap();
data.put("secureCardHistory", true);
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

// Old Android
HashMap data = new HashMap();
data.put("secureTokenHistory", true);
AndroidTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

// Old C#
Dictionary data = new Dictionary();
data.Add("secureTokenHistory", true);
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

// Old Java
HashMap data = new HashMap();
data.put("secureTokenHistory", true);
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

#### Terminal Methods

We have updated all of the available Terminal methods related to Secure Token such as ones for callback registration, toggling polling/delayed auth, and Secure Token CRUD operations.

- C#
- Java
- ObjC

```

registerCoreAPISecureCardListener → registerCoreAPISecureTokenListener

unRegisterCoreAPISecureCardListener → unRegisterCoreAPISecureTokenListener

enableDelayedAuthWithSecureCard → enableDelayedAuthWithSecureToken

enablePollingWithSecureCard → enablePollingWithSecureToken

isSecureCardModeEnabled → isSecureTokenModeEnabled

registerSecureCard → registerSecureToken

editSecureCard → editSecureToken

deleteSecureCard → deleteSecureToken

retrieveSecureCard → retrieveSecureToken

retrieveSecureCardHistory → retrieveSecureTokenHistory

```

```

RegisterCoreAPISecureCardListener → RegisterCoreAPISecureTokenListener

UnRegisterCoreAPISecureCardListener → UnRegisterCoreAPISecureTokenListener

EnableDelayedAuthWithSecureCard → EnableDelayedAuthWithSecureToken

EnablePollingWithSecureCard → EnablePollingWithSecureToken

IsSecureCardModeEnabled → IsSecureTokenModeEnabled

RegisterSecureCard → RegisterSecureToken

EditSecureCard → EditSecureToken

DeleteSecureCard → DeleteSecureToken

RetrieveSecureCard → RetrieveSecureToken

RetrieveSecureCardHistory → RetrieveSecureTokenHistory

```

```

registerCoreAPISecureCardListener → registerCoreAPISecureTokenListener

unRegisterCoreAPISecureCardListener → unRegisterCoreAPISecureTokenListener

registerSecureCard → registerSecureToken

editSecureCard → editSecureToken

deleteSecureCard → deleteSecureToken

retrieveSecureCard → retrieveSecureToken

```

## Transaction Cancellation

[This ](https://developers.worldnetpayments.com/doku.php?id=gochip:support:troubleshooting#25) section in the Troubleshooting page details the new transaction cancellation flow.

## Transaction Communication Error

[This ](https://developers.worldnetpayments.com/doku.php?id=gochip:support:troubleshooting#26) section in the Troubleshooting page further describes the new callback and Websocket response.

## ** New Features

## Frictionless Payment Feature

This feature aims to simplify the customer identification for merchants during Polling and Delayed Auth. With a properly configured SDK and Terminal, it is possible to track all transactions done with a specific card. This will help merchants identify their customers and associate transactions to the appropriate account.

> **Note**
> The Frictionless Payment feature is fully supported only on IDTech plugins for now.

### Settings

This feature requires a few settings to work.

#### Terminal

1. Set a Merchant Portfolio to the terminal.
1. Make sure that the following settings are selected on the Merchant Portfolio:

  - `Enable Token Uniqueness`
  - `Enable Token Auto Sharing`
1. Enable the `Allow Internet` setting of the terminal.

#### SDK

Enable Secure Token with Polling or Delayed Auth.

- Android
- Java
- C#
- Websocket

```

// Delayed auth with Secure Token
AndroidTerminal.getInstance().enableDelayedAuthWithSecureToken(BigDecimal.valueOf(10.0);

// Polling with Secure Token
AndroidTerminal.getInstance().enablePollingWithSecureToken(BigDecimal.valueOf(10.0));

```

```

// Delayed auth with Secure Token
JavaTerminal.getInstance().enableDelayedAuthWithSecureToken(BigDecimal.valueOf(10.0);

// Polling with Secure Token
JavaTerminal.getInstance().enablePollingWithSecureToken(BigDecimal.valueOf(10.0));

```

```

// Delayed auth with Secure Token
Terminal.Instance.EnableDelayedAuthWithSecureToken(10.0m);

// Polling with Secure Token
Terminal.Instance.EnablePollingWithSecureToken(10.0m);

```

```

// Delayed auth with Secure Token
{
    "type": "REQ_SET_DELAYED_AUTH_WITH_SECURE_TOKEN_ENABLED",
    "data": {
    "enabled": true,
        "initialAmount": 10.0
    }
}

// Polling with Secure Token
{
    "type": "REQ_SET_POLLING_WITH_SECURE_TOKEN_ENABLED",
    "data": {
    "enabled": true,
        "initialAmount": 10.0
    }
}

```

### Flow

When the above settings are enabled the following flow will take place for each transaction.

1. A card is read using a payment device.
1. A Secure Token is registered on the Gateway.
1. The transaction is processed against the Secure Token.

If all the settings above are correctly configured then the server will always return the same Secure Token Merchant Reference for the same card details. This can be used to link or group transactions to the same customer.

> **Note**
> #### Limitation
>
>
>
> - If one card is registered multiple times on the Gateway, the first registration will be returned. This can happen when an terminal is used to register cards before the option `Enable Token Uniqueness` is enabled.

### Secure Token History

The Secure Token history lets you to retrieve the last transactions processed with a Secure Token. This could be done during a Secure Token Registration/Update, Polling/Delayed Auth with Secure Token, or Secure Token History Retrieval.

### Availability

| Request | Plugin |
|---|---|
| Secure Token Registration | IDTech, BBPos |
| Secure Token Update | IDTech, BBPos |
| Secure Token History Retrieval | IDTech |
| Polling | IDTech |
| Delayed Auth | IDTech |

### Enabling the Feature

To enable the feature, add the `secureTokenHistory` field to the `initDevice` request data and set its value to `true`.

- Android
- C#
- ObjC
- Java
- Websocket

```

HashMap data = new HashMap<>();
data.put("secureTokenHistory", true);
AndroidTerminal.getInstance().initDevice(DeviceEnum.BBPOSDEVICE, DeviceConnectionType.BLUETOOTH,  data);

```

```

Dictionary data = new Dictionary();
data["secureTokenHistory"] = true;
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB,  data);

```

```

NSMutableDictionary *data = [[NSMutableDictionary alloc] init];
[data setObject:[NSNumber numberWithBool:YES] forKey:@"secureTokenHistory"];
[[WTPSTerminal singleton] initDevice:BBPOSDEVICE withConnectionType:BLUETOOTH withBluetoothAddress:nil withDeviceData:data];

```

```

HashMap data = new HashMap<>();
data.put("secureTokenHistory", true);
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB,  data);

```

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
        "device": "IDTECH",
        "inputMethod": "INSERT",
        "connectionType": "USB",
        "emvType": "QUICK_CHIP",
        "secureTokenHistory": true
    }
}

```

### Usage

After the Secure Token History feature is enabled, the history is added to the field `history` as a list of `CoreTransactionSummary`.   **Secure Token Registration/Update/History Retrieval**

When the Secure Token response callback, `onSecureTokenResponse/OnSecureTokenResponse`, is triggered or the Websocket message `RES_ON_SECURE_TOKEN_RESPONSE` is received for these actions, you could get the history from the Secure Token response object.

- Android
- C#
- ObjC
- Java
- Websocket

```

public void onSecureTokenResponse(CoreSecureTokenResponse secureTokenResponse) {
    CoreSecureToken secureToken = secureTokenResponse.getCoreSecureToken();
    ArrayList secureTokenHistory = secureToken.getHistory();
}

```

```

public void OnSecureTokenResponse(CoreSecureTokenResponse response)
{
    CoreSecureToken secureToken = response.coreSecureToken;
    List history = secureToken.history;
}

```

```

-(void)onSecureTokenResponse: (CoreSecureTokenResponse*)secureTokenResponse {
    CoreSecureToken * secureToken = secureTokenResponse.coreSecureToken;
    NSMutableArray* secureTokenHistory = secureToken.history;
}

```

```

public void onSecureTokenResponse(CoreSecureTokenResponse secureTokenResponse) {
    CoreSecureToken secureToken = secureTokenResponse.getCoreSecureToken();
    ArrayList secureTokenHistory = secureToken.getHistory();
}

```

```

{
    "type": "RES_ON_SECURE_TOKEN_RESPONSE",
    "responseType": "RESPONSE_OK",
    "data": {
        "secureTokenResponse": {
        "coreSecureToken": {
            "history": [
            {
                "amount": 1.00,
                "orderId": "3543DF06CA0F",
                "transactionDate": "2023-01-19T15:55:35.000+0000",
                "transactionState": "",
                "transactionStatus": "COMPLETE",
                "transactionType": "REFUND",
                "uniqueRef": "FKNS9P2NAK",
                "cardHolderName": "Test Card 13 Uat Usa",
                "cardNumber": "374245*****1003",
                "cardType": "American Express",
                "expiryDate": "",
                "currency": "USD",
                "code": "A",
                "approvalCode": "",
                "description": "reason",
                "terminalId": "432001"
            }
            ]
        }
        }
    }
}

```

   **Delayed Auth/Polling with Secure Token (only for IDTech plugin)**

The history is returned on the callback `onRequestSetAmount/OnRequestSetAmount` and Websocket message `RES_ON_REQUEST_SET_AMOUNT`

- C#
- Java
- Websocket

```

public void OnRequestSetAmount(CoreSale coreSale)
{
    CoreSecureToken secureToken = coreSale.coreSecureToken;
    List history = secureToken.history;
}

```

```

public void onRequestSetAmount(CoreSale coreSale) {
    CoreSecureToken secureToken = coreSale.getCoreSecureToken();
    ArrayList secureTokenHistory = secureToken.getHistory();
}

```

```

{
    "type": "RES_ON_REQUEST_SET_AMOUNT",
    "responseType": "RESPONSE_OK",
    "data": {
        "sale": {
        "className": "WSCoreSaleEmv",
        "amount": 6.66,
        "deviceType": "IDTECH_MINISMART",
        "cardHolderName": "UAT USA/Test Card 12      ",
        "maskedPAN": "3742*******1006",
        "expiryDate": "241231",
        "debitAccountType": "NOTSPECIFIED",
        "serial": "712T377686",
        "firstDigitOfPan": 0,
        "transactionInputMethod": "INSERT",
        "coreSecureToken": {
            "merchantReference": "MREF_b61e396f-1252-4639-85e2-242a7822c6bd",
            "credentialsNumber": "2967530708538866",
            "customFields": [],
            "securityCheck": "CVV_VALIDATED",
            "history": [
            {
                "amount": 22,
                "orderId": "2454A4815635",
                "transactionDate": "2022-01-27T15:16:38.000+0000",
                "transactionState": "",
                "transactionStatus": "READY",
                "transactionType": "SALE",
                "uniqueRef": "GP7BFAJ0GB",
                "cardHolderName": "Test Card 12 Uat Usa",
                "cardNumber": "374245*****1006",
                "cardType": "American Express",
                "expiryDate": "",
                "currency": "USD",
                "code": "A",
                "approvalCode": "",
                "description": "",
                "terminalId": "136007"
            },
            ...
            ...
            ...
            ],
            "coreTokenMethod": {
            "emvSecureToken": {
                "ksn": "62994900840002200CC3",
                "emvTags": {},
                "tlvString": "..."
            }
            },
            "maskedPan": "374245*****1006"
        },
        "terminalCategory": "ATTENDED_TERMINAL",
        "deviceFirmware": "ID TECH MiniSmart II V2.01.008",
        "emvType": "STANDARD",
        "cardRequestTimeout": 0,
        "ctlsWalletType": "UNAVAILABLE",
        "ksn": "62994900840002200CC3",
        "emvTags": {},
        "tlvString": "...",
        "delayedAuthEnabled": false,
        "signatureRequired": false,
        "giftCard": false
        }
    }
}

```

## Configurable Host Request Timeout

On previous releases, the host connection timeout could only be set via the SDK terminal method (setter). Now, you could configure it in the `payconfig.xml` file using the field `connectionTimeoutInMillis`.

### payconfig.xml

```

<?xml version='1.0' encoding='UTF-8'?>
<resources>
  <string name="gatewayLiveUrl">https://payments.worldnettps.com/merchant</string>
  <string name="gatewayTestUrl">https://testpayments.worldnettps.com/merchant</string>
  <string name="gatewayDevUrl">https://devpayments.worldnettps.com/merchant</string>
  <string name="apiKey"></string>
  <string name="integrationId"></string>
  <!-- absolute path to the preferred log directory -->
  <string name="logFileAbsoluteDirPath"></string>
  <!-- preferred file name including the extension -->
  <string name="logFileName">log_file.txt</string>
  <!--
            maximum log file lines to trigger line-based rotation
            - defaults to 10000 if set to a value less than 100
            -->
  <string name="logFileMaxLines">10000</string>
  <!--
            active log file's maximum size to trigger size-based rotation
            - overrides line-based rotation if set
            - defaults to 5MB if set to 0
            -->
  <string name="logFileMaxFileSize">5MB</string>
  <!-- maximum file count to keep excluding the active log file, MAX: 20 -->
  <string name="logFileMaxFileCount">0</string>
  <!--
        sets the connection timeout between SDK and host. Default: 30,000 milliseconds
        - if the value set is <1000 ms, default value will be used
        -->
  <string name="connectionTimeoutInMillis">30000</string>
</resources>

```

## IDTech Card Removal Timeouts

During Quick Chip transactions, you are prompted for card removal up to two times.

1. After the card data has been read by the device
1. When the card is left inserted on the first case up until the online sale response is retrieved

### Setting the Timeouts

In this release, we added the support to specify the prompt timeout for each cases.

To configure the timeout for the first case, pass the field `quickChipCardRemovalTimeoutInMillis` with a value in milliseconds.

For the second case, use the field `postTransactionCardRemovalTimeoutInMillis`.

**Minimum: ** 1000ms
**Maximum: ** 255000ms

- C#
- Java
- Websocket

```

Dictionary data = new Dictionary();
data["quickChipCardRemovalTimeoutInMillis"] = 30000;
data["postTransactionCardRemovalTimeoutInMillis"] = 30000;
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB,  data);

```

```

HashMap data = new HashMap<>();
data.put("quickChipCardRemovalTimeoutInMillis", 30000);
data.put("postTransactionCardRemovalTimeoutInMillis", 30000);
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB,  data);

```

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
        "device": "IDTECH",
        "inputMethod": "INSERT",
        "connectionType": "USB",
        "emvType": "QUICK_CHIP",
        "quickChipCardRemovalTimeoutInMillis": 30000,
        "postTransactionCardRemovalTimeoutInMillis": 30000
    }
}

```

## IDTech MiniSmart II APDU Command Exchange

The MiniSmart II device is capable of exchanging APDU commands with a smartcard but performing such feature requires direct calls to the IDTech library.

On the websocket solution, this is achievable through the device passthrough call messages.

Device Passthrough Request

```
{
  "type": "REQ_DEVICE_PASSTHRU",
  "data": {
    "methodName": "method_to_call",
    "parameters": {
            "someParamName": "someValue"
    }
  }
}

```

Device Passthrough Response

```
{
  "type": "RES_ON_DEVICE_PASSTHRU_RESPONSE",
  "responseType": "RESPONSE_OK",
  "data": {
        "someResponseDataName": "someValue"
  }
}

```

### Performing the APDU Command Exchange

To perform the APDU command exchange, please see the steps below.

1. Make sure the device is connected and initialized.
1.

Set the card type option to ISO (”00”).

Request

```
 {
           "type": "REQ_DEVICE_PASSTHRU",
           "data": {
             "methodName": "setCardTypeOption",
             "parameters": {
               "cardType": "00"
             }
           }
         }

```

Response

```
 {
           "type": "RES_ON_DEVICE_PASSTHRU_RESPONSE",
           "responseType": "RESPONSE_OK",
           "data": {
             "responseCodeString": "no error, beginning task.",
             "responseData": "06",
             "responseCode": 0
           }
         }

```

1.

Insert a card into the device.
1.

Send a device passthrough call message to power on the reader.

Request

```
 {
           "type": "REQ_DEVICE_PASSTHRU",
           "data": {
             "methodName": "icc_powerOnICC",
           }
         }

```

Response

```
 {
           "type": "RES_ON_DEVICE_PASSTHRU_RESPONSE",
           "responseType": "RESPONSE_OK",
           "data": {
             "responseCodeString": "no error, beginning task.",
             "atr": "<SAMPLE_HEX_VALUE>",
             "responseCode": 0
           }
         }

```

1.

To exchange APDU command, send the device passthrough call message below.

Request

```
 {
           "type": "REQ_DEVICE_PASSTHRU",
           "data": {
             "methodName": "icc_exchangeEncryptedAPDU",
             "parameters": {
               "commandAPDU": "00A40400",
               "outputBufferSize": 4096
             }
           }
         }

```

Response

```
 {
           "type": "RES_ON_DEVICE_PASSTHRU_RESPONSE",
           "responseType": "RESPONSE_OK",
           "data": {
             "responseCodeString": "no error, beginning task.",
             "responseData": "<SAMPLE_HEX_VALUE>",
             "responseCode": 0
           }
         }

```

1.

Power off the reader.

Request

```
 {
           "type": "REQ_DEVICE_PASSTHRU",
           "data": {
             "methodName": "icc_powerOffICC"
           }
         }

```

Response

```
 {
           "type": "RES_ON_DEVICE_PASSTHRU_RESPONSE",
           "responseType": "RESPONSE_OK",
           "data": {
             "responseCodeString": "no error, beginning task.",
             "responseCode": 0
           }
         }

```
