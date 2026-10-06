<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:mobile_pos:coding_101 | synced: 2026-10-05 -->

> **Note**
> This documentation is a reference guide for 1_6_0 and later versions. Please check the [previous documentation](doku.php?id=gochip:pos:1_5_X:coding_101) for 1_5_X and older versions.

## []SDK

#### 1. Setup.

Setup the SDK using the `initialize` command. There are 2 ways to use this method.

- Pass an object that implements the `CoreAPIListener` interface. (the `this` in the code sample)
- Pass no argument and make subsequent calls to `register*Listener` to register callbacks in different locations depending on the structure of your application.

> **Note**
> Only one of these implementations should be used. i.e. don't register multiple listeners if you are using the `CoreAPIListener` this will lead to duplicate callbacks firing.

> **Note**
> Before proceeding, please check the [Authentication Guide](doku.php?id=gochip:support:authentication) to generate your API Key.

The `initWithConfiguration` call will authenticate with the Worldnet gateway and retrieve settings required for operation. The `onSettingsRetrieved` callback will fire on success. At this point we know that we have successful credentials and the SDK is ready to connect a device.

# <Code Samples>

- Android
- IOS

```

AndroidTerminal.getInstance().initialize(this);
AndroidTerminal.getInstance().setMode(CoreMode.TEST);
AndroidTerminal.getInstance().initWithConfiguration(MainActivity.this, TERMINAL_ID);

```

```

[[WTPSTerminal singleton] init:self];
[[WTPSTerminal singleton] setMode:TEST];
[[WTPSTerminal singleton] initWithConfiguration:TERMINAL_ID];

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
