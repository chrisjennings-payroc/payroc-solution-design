<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:mobile_pos:1_5_x:basic_solutions | synced: 2026-10-05 -->

> **Note**
> This documentation is a reference guide for 1_5_X and older versions. Please check the [new documentation](doku.php?id=gochip:pos:devices) for new implementations. If you're updating, please check our [update guide.](doku.php?id=gochip:support:update_guide_1_6_x)

# Basic Solutions

Here we can see the core physical elements for the Mobile Payment Solution:

- **POS APPLICATION:** represents the POS solution, developed and installed on a physical device, which is going to communicate with the SDK in its own platform (platform plugin) language to use diferent payment devices (device plugin) to read cards data and communicate with the payment gateway (gateway connector) to process diferent types of transactions.
- **PAYMENT DEVICE:** element that enables the POS to read cards' data using the certified industry standarts. Each Payment device has its own libs (libraries to integrate) and the SDK integrates them into the POS solution using the devices' plugins. The SDK already has a large set of market payment devices' plugins implemented, acquirer certified and available to use, and it's always expanding - contact our sales team to know the news about devices.
- **PAYMENT GATEWAY:** main business component of the whole solution. Responsible for processing the transactions requested by the POS solution. This component is going to execute the business rules, the communication with acquirers and other gateways, and finally, the mantainance of business data.

## General Solution Flows

Depending on the transaction type (sale, refund, consults, etc.), different flows are generated involving these three elements and its ‘interfaces’.

To make the SDK a simple and efficient experience for development, our architecture simplifies the communication, generating shorter flows where each request generates a callback for success or failure, abstracting the communication with the card reader devices.

The following diagrams represent different scenarios which may be applicable to your solution.

## Detailed Solution Flows

Depending on the solution you intend to implement, different flows need to be implemented.

The next diagrams show a more detailed interaction, closer to the implementation your application is going to reproduce in order to execute transactions - the example is based on a simple sale scenario.

### Basic SDK Transaction Flow
