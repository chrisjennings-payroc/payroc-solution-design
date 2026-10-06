<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:mobile_pos:getting_started | synced: 2026-10-05 -->

# Getting Started

Our mPOS solution is aimed at people who may not have access to (or requirement for) traditional POS hardware. With support for Android and iOS it makes taking payments on the go simple and hassle free.!

## []mPOS Devices

The first step in getting started is to pick your mPOS device from the following list of manufacturers. If you haven’t already, follow the links below to see details about your device.

### []BBPos

 [](doku.php?id=gochip:mobile_pos:devices:bbpos)

#### [Wisepad 2](doku.php?id=gochip:mobile_pos:devices:bbpos)

 [](doku.php?id=gochip:mobile_pos:devices:bbpos)

#### [Chipper](doku.php?id=gochip:mobile_pos:devices:bbpos)

 [](doku.php?id=gochip:mobile_pos:devices:bbpos)

#### [Chipper BT](doku.php?id=gochip:mobile_pos:devices:bbpos)

 [](doku.php?id=gochip:mobile_pos:devices:bbpos)

#### [Chipper 2X](doku.php?id=gochip:mobile_pos:devices:bbpos)

 [](doku.php?id=gochip:mobile_pos:devices:bbpos)

#### [Chipper 2X BT](doku.php?id=gochip:mobile_pos:devices:bbpos)

- **Note:** BBPos is currently only supported in North America.

## []How to Integrate

### []SDK

#### []Installation

See Installation instructions for your corresponding device.

#### []Making your first transaction

1.

Authenticate.
Use the code shown to send an initialization request to the server. This will authenticate with the Worldnet gateway and retrieve settings required for operation.
1.

Initialize the device.
Once the service has returned a successful authentication via `OnSettingsRetrieved` you can now initialize the device. Use this code and wait for the device to connect.
1.

Perform a transaction.
Once the device has connected via `OnDeviceConnected`, simply send the amount required via a `processSale` call and the device should prompt for a card. Presenting a valid card should result in an online message being sent to the bank a response from the SDK via `onSaleResponse` and your first transaction processed!
