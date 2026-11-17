<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:routing_balancing | synced: 2026-10-05 -->

# Routing and Balancing

Please note Routing and Balancing is only available if you have a routing terminal set up.

## Introduction

The Worldnet Payments system is a secure server-based transaction processing service that will enable your business to authorize and process credit/debit card transactions online in real-time. The information needed to process the transactions is sent over a secure, encrypted internet connection.

Large enterprise often have many strategies that require the use of multiple merchants accounts. This can be for:

- Geographical independence
- Authorization maximisation
- Load balancing
- Fraud/chargeback balancing & mitigation
- Interchange optimization
- Acquirer value capping
- Card scheme routing
- Currency management
- Affiliate management

The Worldnet Payments routing and balancing functionality can be used for automation of all of these tasks across all of the acquirers that Worldnet Payments support.

## Concepts

Worldnet Payments routing and balancing is based on the concepts of “Processing Terminals” and “Routing Terminals”. Both are 7-8 digit numbers beginning in your 4-5 digit Merchant ID.

### Processing Terminals

Processing terminals are the same as standard Terminals (Terminal IDs) if you are familiar with basic processing through Worldnet Payments.

They can be thought of as having a 1:1 relationship to an acquiring Merchant Account. It is possible to have multiple processing terminals pointing at one merchant account though, if required.

Processing terminals are where transactions actually belong to, and are available after authorization/settlement for reporting purposes.

Processing terminal Terminal IDs end in 001, 002, 003, etc.

### Routing Terminals

Routing terminals are pseudo terminals that you can send all of your transactions to and based on the “routing rules” and “balancing types” that are set up for that routing terminal it will choose the appropriate processing terminals (acquirer merchant account) and send the transaction through it for authorization/settlement.

Multiple Routing Terminals can be set up also, each with it's own set up processing terminals, routing rules and balancing configuration.

Routing terminal Terminal IDs end in 999, 998, 997, etc.

**If using routing or balancing all transactions must be submitted to us via a Routing Terminal.**

### Routing and Balancing

Routing and Balancing are two different but complimentary features in the Worldnet Payments system. A simple way to describe them is:

- Routing rules are purely based on the data in the transaction being processed. They look at the data and depending on the rules configured in the routing terminal they decide which processing terminal to use for the transaction. They can be based on the card or order details or any custom fields/data that the merchant chooses to send in with the transaction, such as Product SKU, affiliate ID, etc. The rules are boolean and prioritized. They can also be used to automatically authorize transactions only for later capture, or decline transactions immediately.
- Balancing is more concerned with the bigger picture of overall acquirer volume management, high volume load balancing and high availability.

### Priority

Routing rules take preference over balancing. If a rule a transaction to a processing terminal is a match then that rule will be applied. Otherwise balancing will be applied.

### Balancing

Balancing is not as granular as Routing. The choices made per transaction are made by the system, not by rules that a merchant can configure. There are 4 types of balancing:

1. Round Robin: Tries eligible processing terminals in sequential order (load balancing).
1. Processed Value Ratio: Prioritizes processing terminals based on their “processed value/value limit” ratio (in reverse). This method effectively sends a transaction to whichever eligible processing terminal has used up the lowest percentage of it's value limit.
1. Value Processed: Sends transactions to the processing terminal with the lowest value processed, regardless of limits.
1. Terminal Priority: Prioritizes one processing terminal. All eligible trans will get sent through this by default. If that terminal reaches it's value limit then the next highest priority eligible processing terminal will be used. Terminal Priority is configured to match your acquirer/processor maximum processing values (if they have maximum values, but most don't). To maintain consistency with the acquirer limits these values are only configurable by Worldnet Payments. For more information please contact our support help-desk at [ [email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection#<SAMPLE_HEX_VALUE>).

### Value Limits

Value limits are normally set at a processing terminal level, however greater granularity can be achieved by setting the limits at a card type (card scheme) level also, under that processing terminal. Card Type limits take precedence over processing terminal level limits.

### Balancing Eligibility

A processing terminal is only considered eligible to be considered in the group of balancing terminals for a specific transaction if:

- It is not deactivated
- Its card type value limit (if set) for the transactions card type has not been exceeded
- Its processing terminal level value limit (if set) has not been exceeded
- It supports the card type, base currency and transaction type of the transaction being processed

### System logic when selecting terminal during balancing

Balancing only is considered after the transaction is considered ineligible for routing, i.e. it does not match a routing rule.

When the system is deciding what terminal should be used for balancing if follows this logic:

1. Creates a list, ordered by Balancing Priority, of all terminals under the merchant that are participating in balancing.
1. Filters out terminals that have reached their monthly transaction value limit.
1. Filters out terminals that do not support the transaction currency.
1. Filters out terminals that do not support the transaction Card Type.
1. Gets the Balancing Type of the Routing Terminal that the transaction was submitted to (Round Robin, Processed Value Ratio, Value Processed, Terminal Priority).
1. Selects a single terminal based on this Balancing Type. If there are no longer any terminals in the list (they've all been filtered out above), then an error is returned to the merchant saying “Can't balance transaction”.

## Implementation

### Balancing

Balancing is purely configured by Worldnet Payments. If you have multiple merchant accounts and want to avail of our balancing functionality please contact our support help-desk at [ [email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection#<SAMPLE_HEX_VALUE>) with the details of the configuration you are looking for.

### Routing Rules

#### Access Permissions

To enable configuration of routing rules you will require:

1. Routing/Balancing enabled on the terminal by Worldnet Payments,
1. Access to a user login that has permission to modify the routing rules (“Allow Routing Terminal” permission).

Please contact us if you have any problems configuring these.

#### Navigating to the Rules Editor

To access the rules editor once you are logged in you will have to:

**1.** Switch to the appropriate Routing terminal from the Terminal Selection box in the top right of the Selfcare (see across).

**2.** Select Settings → Routing Rules from the menu. If either of these are not present then ensure that you have successfully selected a routing terminal (step 1) and that your user has “Allow Routing Terminal” permissions.

**3.** You will be displayed the rules editor page. Initially there may be “No rules defined”. To start creating a rule click “Add Routing Rule”.

#### Creating a rule

The images below and their descriptions describe how rules are created. The rules are boolean based and so should be very familiar in structure to anyone with any development experience at all, but even without that the interface is very straightforward.

As you can see from above the first thing you must do is give the rule a name. This allows for easy reference later on if multiple rules are configured.

Once a name is configured you must select the data field that you want the rule to act upon. *Note that the fields in the image above are always available. Any fields that you set up as Custom Fields (Settings → Custom Fields) under that routing terminal will also appear here and can be used as routing parameters.*

**Additionally to Custom Fields**, it also can be used other transaction data to define routing rules, like Currency, Amount, Country, Card (Brand and Program levels).

Custom Fields can be sent either via the XML or Hosted Payment Page integration methods (please see integration documentation for more information).

Next you must select the Operator that you need for the rule. That the list above are available for number based fields such as the Amount in this demonstration, but for strings another operator called LIKE is also available and operates the same way as the SQL LIKE string operator. Note that the IN operator will cause a preview to be shown in the value input box. Also note that strings are automatically converted to numbers and numbers to strings as necessary.

The next thing to do is to enter the string or amount or list that the transaction parameter you selected is to be compared to. Again this generally adheres to SQL comparison rules.

Once the comparison/identification part of the rule is complete you will see a logical synopsis of it in text at the bottom of the rule box. Now you need to define the action.

You can:

- Route To Terminal: This will use a specific Processing Terminal to process the transaction. The Processing Terminal should be selected from the dedicated drop down box next to it (right).

- Authorize Only: This will Authorize against a Processing Terminal chosen by the Balancing functionality. The transaction will not settle by default, but instead will appear in the Routing Terminals “Authorized Transaction Queue”. You will be able to see the Processing Terminal that was used in this list. This queue is used for merchants who need to manually flag transactions for settlement, such as merchants who perform delayed delivery of goods.
- Decline: Simply declines the transaction without going online. Again it will balance the transaction before declining it to determine which Processing Terminal it should be stored under.

Once a rule is complete click “Save Routing Rule” and it will appear as above. They can individually be edited, disabled or removed using the links next to them.

When multiple rules are configured you can re-order/prioritise then using *drag and drop.*

**Note that you must enable the “Enable Routing” checkbox is you want the ruleset to take affect!**

## Features Not Supported

### eDCC

Dynamic Currency Conversion relies on rates from a specific acquirer. As multiple rates may be available, and DCC is a two step process when invoked via XML, there is no way to currently ensure that the correct rate is used with the correct acquirer. Therefore eDCC or any other DCC or is not supported by Routing Terminals through XML. It is however supported via the Hosted Payment Page for Routing Terminals.

### 3D Secure

The same applies for 3D Secure and for eDCC above. It is not available via XML but is available for Hosted Payment Page transactions on the Routing Terminal.
