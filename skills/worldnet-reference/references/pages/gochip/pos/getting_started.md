<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:getting_started | synced: 2026-10-05 -->

# Getting Started

Our POS solution is aimed at the restaurant, counter top and unattended retail space. With a range of devices and development languages supported you’ll find a solution that fits!

## []POS Devices

First step in getting started is to pick your POS device from the following list of manufacturers. If you haven’t already, follow the links below to see details about your device.

### []IDTech

 [](doku.php?id=gochip:pos:devices:idtech)

#### [VP3300](doku.php?id=gochip:pos:devices:idtech)

 [](doku.php?id=gochip:pos:devices:idtech)

#### [VP5300](doku.php?id=gochip:pos:devices:idtech)

 [](doku.php?id=gochip:pos:devices:idtech)

#### [VP6300](doku.php?id=gochip:pos:devices:idtech)

 [](doku.php?id=gochip:pos:devices:idtech)

#### [VP6800](doku.php?id=gochip:pos:devices:idtech)

 [](doku.php?id=gochip:pos:devices:idtech)

#### [Augusta](doku.php?id=gochip:pos:devices:idtech)

 [](doku.php?id=gochip:pos:devices:idtech)

#### [Minismart II](doku.php?id=gochip:pos:devices:idtech)

### []Ingenico

 [](doku.php?id=gochip:pos:devices:ingenico)

#### [iPPC320](doku.php?id=gochip:pos:devices:ingenico)

 [](doku.php?id=gochip:pos:devices:ingenico)

#### [iPPC350](doku.php?id=gochip:pos:devices:ingenico)

 [](doku.php?id=gochip:pos:devices:ingenico)

#### [iUC285](doku.php?id=gochip:pos:devices:ingenico)

- **Note:** Our POS solution is currently only supported in North America.

## How to Integrate

## ** Websockets

Our Websockets solution lets you install our standalone local websockets service. This service provides a flexible API layer that let’s you control all aspects of the POS flow using your choice of programming language.

#### []Installation

1. Download the Websockets zip file <HERE>.
1. Extract the folder to a location of your choosing.
1. Run `ws-setup` and follow the instructions.
1. Run `start.bat` (Windows) or `start.sh` (Linux) to start the service.

Once started, follow the below steps to get your first transaction processed!

#### []Making your first transaction

1.

Authenticate.
Use the code shown to send an initialization request to the server. This will authenticate with the Worldnet gateway and retrieve settings required for operation.
1.

Initialize the device.
Once the service has returned a successful authentication you can now initialize the device. Use this code and wait for the device to connect.
1.

Perform a transaction.
Once the device has connected, simply send the amount to the Websockets that you wish to process for and the device should prompt for a card. Presenting a valid card should result in an online message being sent to the bank and your first transaction processed!

## SDK

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
