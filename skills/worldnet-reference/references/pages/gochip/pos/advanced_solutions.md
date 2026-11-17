<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:advanced_solutions | synced: 2026-10-05 -->

# Advanced Solutions

GoChip allows for flexible transaction flows so that applications have the ability to fit the transaction flow to the integrators needs. Before settling on a flow, a few things need to be considered:

- Is the POS solution attended or unattended?
- Do you need to tokenise the customer information for potential loyalty or subscription services?
- Is the transaction amount known prior to or after the customer presents the card?
- Should the terminal be allowed to operate if no internet is available?
- Is the card used at the beginning or at the end of the transaction?
- Should your cashier work at times when it's not possible to process a transaction online?

This and other questions represents challenges to a Merchant's business. The GoChip SDK solution provides a set of flow scenarios to help the Merchant to respond effectively to those situations. Depending on your answers to the above you may need to implement one or more of the advanced flows that are outlined below.

## What integration to choose?

Answer the questions below to find out what is the best solution for your business case.

Answer the questions below according to your application details:

-

Are you setting up an unattended retail payment system? (E.g. Parking systems, vending machine, user operated petrol stations)  Yes
-

Is the payment device always awaiting for a user to swipe the card to initiate a transaction?   Yes
-

Will the payment device have access to an internet connection at all times?   Yes
-

Is the Point Of Sale application designed to first capture the card's data before establishing the Sale amount?   Yes
 Previous Next Calculate Results

The solution(s) that best fit your needs:

- **Offline Mode
- **Polling Mode
- **Delayed Auth Mode

# Explore the Advanced Solutions

## Polling Mode

The Poling Mode allows your application to start the flow by making the card reader device wait until a card is presented. A default transaction value is established when setting this mode, and then before submitting the transaction your application needs to set the final amount for the sale.

Perfect solution for:

- **Laundromats
- **Car Parks
- **Car Wash
 [Learn More](doku.php?id=gochip:pos:advanced_solutions:polling_mode)

## Delayed Auth Mode

The Delayed Auth Mode allows your application to start the flow normally however instead of submitting the sale data it first asks the customer to present their card. Later your application should submit the final amount of the transaction.

Perfect solution for:

- **Gas Stations
- **Coffee Machines
- **Bar Tabs
 [Learn More](doku.php?id=gochip:pos:advanced_solutions:delayed_auth_mode)

## Offline Mode

The Offline Mode allows your application to work offline by choice, or based on the connectivity status with the payment gateway. This is done by storing the transaction in your application and submitting it to the gateway when you are able to process online.

Perfect solution for:

- **Taxis
- **Outdoor Events
- **Markets
 [Learn More](doku.php?id=gochip:pos:advanced_solutions:offline_mode)

## Secure Tokens

The Secure Tokens feature is a special component of our platform that enables you to tokenize your client's cards so they can be used again later for subsequent single or recurring transactions.

Perfect solution for:

- **Gym Memberships
- **Schools
- **Subscriptions
 [Learn More](doku.php?id=gochip:pos:advanced_solutions:secure_card)

## Authorisation

Authorisation is an advanced solution of a normal sale where the final amount is adjusted at a later stage after the sale has happened. Within the payment industry this type of solution can also often be referred to as pre-authorisation, auth & capture or tip flow adjustment.

Perfect solution for:

- **Hotels
- **Gas Stations
- **Car Rentals
 [Learn More](doku.php?id=gochip:pos:advanced_solutions:authorization)

## Loyalty Cards

The Loyalty Cards feature allows your application to read Google Smart TAP, Apple VAS or MIFARE cards, which integrates payments and loyalty in one solution.

Perfect solution for:

- **Laundromats
- **Markets
- **Car Wash
 [Learn More](doku.php?id=gochip:pos:advanced_solutions:loyalty_card)

Now, choose a flow and start implementing to your application's needs.

> **Note**
> Remember that all the flows defined above should be done only after the necessary steps from [Getting Started](doku.php?id=gochip:pos:getting_started) are done.
