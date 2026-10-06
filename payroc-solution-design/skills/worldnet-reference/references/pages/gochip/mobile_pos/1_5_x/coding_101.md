<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:mobile_pos:1_5_x:coding_101 | synced: 2026-10-05 -->

> **Note**
> This documentation is a reference guide for 1_5_X and older versions. Please check the [new documentation](doku.php?id=gochip:pos:devices) for new implementations. If you're updating, please check our [update guide.](doku.php?id=gochip:support:update_guide_1_6_x)

## []SDK

#### 1. Setup and Authenticate.

Setup the SDK using the `initialize` command. There are 2 ways to use this method.

- Pass an object that implements the `CoreAPIListener` interface. (the `this` in the code sample)
- Pass no argument and make subsequent calls to `register*Listener` to register callbacks in different locations depending on the structure of your application.

> **Note**
> Only one of these implementations should be used. i.e. don't register multiple listeners if you are using the `CoreAPIListener` this will lead to duplicate callbacks firing.

The `initWithConfiguration` call will authenticate with the Worldnet gateway and retrieve settings required for operation. The `onSettingsRetrieved` callback will fire on success. At this point we know that we have successful credentials and the SDK is ready to connect a device.

# <Code Samples>

- Android
- IOS

```

AndroidTerminal.getInstance().initialize(this);
AndroidTerminal.getInstance().setMode(CoreMode.TEST);
AndroidTerminal.getInstance().initWithConfiguration(MainActivity.this, TERMINAL_ID, SECRET);

```

```

[[WTPSTerminal singleton] init:self];
[[WTPSTerminal singleton] setMode:TEST];
[[WTPSTerminal singleton] initWithConfiguration:TERMINAL_ID withSecret:SECRET];

```

#### 2. Initialize the device.

You can now initialize the device. Use this code and wait for the device to connect. Change the device name and connection method to match your needs. The `onDeviceConnected` callback will fire on success. Once this fires the SDK and device are ready to use!

##

- Android
- IOS

```

AndroidTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, null);

```

```

[[WTPSTerminal singleton] initDevice:BBPOSDEVICE withConnectionType:BLUETOOTH withBluetoothAddress:nil];

```

#### 3. Perform a transaction.

Once the device is connected send the amount required via a `ProcessSale` call and the device should prompt for a card. Presenting a valid card should result in an online authentication being sent to the bank and the SDK processes the response. The `onSaleResponse` callback will fire on success. Here is where you can display receipts or do any other post transaction processing.

##

- Android
- IOS

```

CoreSale sale = new CoreSale(BigDecimal.valueOf(Double.parseDouble(2.22)));
AndroidTerminal.getInstance().processSale(sale);

```

```

CoreSale *sale =[[CoreSale alloc] init];
sale.amount = [NSNumber numberWithDouble: 2.22];
[[WTPSTerminal singleton] processSale:sale];

```

## Reversal and Refunds

## Overview

The purpose of this document is to provide a high level description of the changes made to the Worldnet System. The SDK is required to handle the situation where a reversal is performed on a transaction with a certain OrderID that may have been used in more than one transaction attempt. Transactions with the same OrderID are not guaranteed to be unique, and are therefore impossible to single out for a reversal on its own. In the event of performing a reversal using the OrderID field, the proposed solution is to include a new field in the request to identify what time the transaction occurred in the merchant’s timezone. This document reflects the changes made to the Gateway (server side) and the Mobile SDK.

#### Refund Flow

#### New Flow Refund

For the instances where the UniqueRef is not returned, the refund functionality is updated to allow refunds using OrderId + PreviousTransactionDateTime.
