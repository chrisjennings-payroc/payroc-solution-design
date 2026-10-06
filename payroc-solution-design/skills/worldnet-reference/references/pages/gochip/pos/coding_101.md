<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:coding_101 | synced: 2026-10-05 -->

> **Note**
> This documentation is a reference guide for 1_6_0 and later versions. Please check the [previous documentation](doku.php?id=gochip:pos:1_5_X:coding_101) for 1_5_X and older versions.

# Getting Started

Our POS solution is aimed at the restaurant, counter top and unattended retail space. With a range of devices and development languages supported you’ll find a solution that fits!

## []POS Devices

First step in getting started is to pick your POS device from the list of [supportive manufacturers](doku.php?id=gochip:pos:devices).

> **Note**
> Before proceeding, please make sure your device is setup successfully. Check the [Devices section](doku.php?id=gochip:pos:devices) to learn how to setup your device.

> **Note**
> Before proceeding, please check the [Authentication Guide](doku.php?id=gochip:support:authentication) to generate your API Key.

## []How to Integrate

## ** []Websockets

Our Websockets solution lets you install our standalone local websockets service. This service provides a flexible API layer that let’s you control all aspects of the POS flow using your choice of programming language.

#### []Installation

1. Download the Websockets zip file [here](doku.php?id=gochip:downloads:websockets).
1. Extract the folder to a location of your choosing.
1. Run `ws-setup` and follow the instructions.
1. Run `start.bat` (Windows) or `start.sh` (Linux) to start the service.

Once started, follow the below steps to get your first transaction processed!

#### []Making your first transaction

# <Code Samples>

#### 1. Initialize the SDK.

Use the code shown to send an initialization request to the server. This will authenticate with the Worldnet gateway and retrieve settings required for operation.

- Request
- Response

```

{
    "type": "REQ_INIT_WITH_CONFIGURATION",
    "data": {
        "terminalId": "136007"
    }
}

```

```

{
    "type": "RES_ON_SETTINGS_RETRIEVED",
    "data": {
    "settings": {
        "currencySymbol": "$",
        "currency": "USD",
        "features": {
            "allowMsrFallback": true,
            ...
        },
        "merchantDetails": {
            "name": "Merchant",
            "city": "Dublin",
            "address1": "11 MyChoiceMerchant",
            "address2": "SomePlace",
            ...
        }
        }
    },
    "responseType": "RESPONSE_OK"
}

```

#### 2. Initialize the device.

Once the service has returned a successful authentication you can now initialize the device. Use this code and wait for the device to connect.

- Request
- Response

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
        "device": "IDTECH",
        "connectionType": "USB",
        "inputMethod": "SWIPE_OR_INSERT"
    }
}

```

```

{
    "type": "RES_ON_DEVICE_CONNECTED",
    "data": {
        "deviceType": "Idtech",
        "deviceInfo": {
        "serialNumber": "824T844193",
        "kernelVersion": "EMV Common L2 V1.10.037",
        "firmwareVersion": "ID TECH Augusta USB-HID V1.03",
        "connectionType": "USB"
    }
},
    "responseType": "RESPONSE_OK"
}

```

#### 3. Perform a transaction.

Once the device has connected, simply send the amount to the Websockets that you wish to process for and the device should prompt for a card. Presenting a valid card should result in an online message being sent to the bank and your first transaction processed!

- Request
- Response

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
          "amount": "12.50",
    }
}

```

```

{
    "type": "RES_ON_SALE_RESPONSE",
    "data": {
        "saleResponse": {
        "cardHolderName": "Test Card 12 Uat Usa",
        "cardNumber": "374245*****1006",
        "expiryDate": "0120",
        "authorizedAmount": 12.5,
        "currency": "USD",
        "uniqueRef": "EX3QVJ56L6",
        "dateTime": "2019-11-08T11:19:30.794Z",
        "description": "APPROVAL",
        "code": "A",
        "cardType": "American Express",
        "emvTags": [],
        "orderId": "KQK9Z8",
        ...
        }
    },
    "responseType": "RESPONSE_OK"
}

```

## []SDK

#### 1. Setup and Authenticate.

Setup the SDK using the `initialize` command. There are 2 ways to use this method.

- Pass an object that implements the `CoreAPIListener` interface. (the `this` in the code sample)
- Pass no argument and make subsequent calls to `register*Listener` to register callbacks in different locations depending on the structure of your application.

> **Note**
> Only one of these implementations should be used. i.e. don't register multiple listeners if you are using the `CoreAPIListener` this will lead to duplicate callbacks firing.

The `initWithConfiguration` call will authenticate with the Worldnet gateway and retrieve settings required for operation. The `onSettingsRetrieved` callback will fire on success. At this point we know that we have successful credentials and the SDK is ready to connect a device.

##

- Java
- C#

```

JavaTerminal.getInstance().initialize(this);
JavaTerminal.getInstance().setMode(CoreMode.TEST);
JavaTerminal.getInstance().initWithConfiguration(MainActivity.this, TERMINAL_ID);

```

```

Terminal.Instance.Initialize(this);
Terminal.Instance.SetMode(CoreMode.TEST);
Terminal.Instance.InitWithConfiguration(TERMINAL_ID);

```

#### 2. Initialize the device.

You can now initialize the device. Use this code and wait for the device to connect. Change the device name and connection method to match your needs. The `onDeviceConnected` callback will fire on success. Once this fires the SDK and device are ready to use!

##

- Java
- C#

```

JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, null);

```

```

Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, null);

```

#### 3. Perform a transaction.

Once the device is connected send the amount required via a `ProcessSale` call and the device should prompt for a card. Presenting a valid card should result in an online authentication being sent to the bank and the SDK processes the response. The `onSaleResponse` callback will fire on success. Here is where you can display receipts or do any other post transaction processing.

##

- Java
- C#

```

CoreSale sale = new CoreSale(BigDecimal.valueOf(Double.parseDouble(2.22)));
JavaTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale(Math.Round(12.3, 2, MidpointRounding.ToEven));
Terminal.Instance.ProcessSale(sale);

```
