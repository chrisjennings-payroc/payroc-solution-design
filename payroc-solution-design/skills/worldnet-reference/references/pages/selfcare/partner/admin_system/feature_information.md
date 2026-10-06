<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:partner:admin_system:feature_information | synced: 2026-10-05 -->

# Feature Information

The features presented here, although not always used or enabled, are also part of the Admin Portal. To be used, they must be enabled, so the next subsection will explain a little about them and how they function, if you need to use them.

## Amex OptBlue

**Amex OptBlue** is currently only supported with TSYS Saratoga.

In order to accept Amex, the merchant must enroll with Amex OptBlue. After ensuring the merchant is enrolled for Amex OptBlue, please follow these steps to enable it on the admin interface:

- **1**. After selecting the terminal, select **Amex OptBlue** in **Features** tab.
- **2**. Populate the “**Industry SE Number**” and “**Merchant Street Address**”
- **3**. Save the changes, then the Merchant will then be authorized to accept “**OptBlue**” on this terminal.

There is no changes on how the transaction is processed for the merchant point of view. The only change is how our system communicates with TSYS Saratoga.

## EMCP (Enhanced Multi Currency Processing)

### Description

EMCP is a method of MCP that applies currency conversion during the settlement only. The checkout is all done in the merchants currency and there is no merchant or cardholder facing currency information. When the settlement is performed though, the card currency is identified for each card, the amount is converted (and markup is applied at this stage) and each transaction is settled in the cardholders currency, so the cardholder will see it on their statement as already converted into their currency.

A transaction is determined to be EMCP eligible if Cardholder and Terminal countries and currencies are different.

EMCP workflow is mutually exclusive with regular MCP workflow. So a merchant that opts to deploy MCP cannot be opted in for 'Enhanced MCP' and vice-versa.

### Details

The following criterion are used to enable EMCP functionality for TSYSSaratoga merchants:

1. 'Allow EMCP' checkbox in the 'Bank Settings' block
1. Supported currencies in the 'Supported Currencies' block
1. Cardholder range in the 'BIN Ranges' page with selected country and checked 'DCC/MCP'.

Notes: 'Mark up percentage' field is used to calculate mark up

EMCP is available for the following transactions:

- Sale
- Refund
- Unreferenced Refund
- Pre-Authorization
- Pre-Auth Completion
- Pre-Auth Completion (difference between sent and confirmed amount is equal or more than 15%)

## Dynamic Descriptors

### General Descriptors

Transaction descriptors describe a particular payment in order to help to identify that transaction on a bank statement or online bank interface. A good practice to help minimize the risk of chargeback and in turn, to save money! Provide your customers with your brand name and contact information to help them recognize their purchase, that’s all it takes to make descriptors work for your business.

### Dynamic Descriptors

These type of descriptors describe a specific product or service and can vary from one merchant to another. If your website sells applications or software services, this type of descriptor can be a great way to let your customers know what they bought. Usually customers know the name of an application they purchased and they will therefore recognize that name on their bank statement.

The text that appears on the cardholders statement will be made up of:

1. A “Prefix”, which is a static text value up to 12 characters long that is the same for every transaction followed by
1. The dynamic value, which is sent in by the website with the transaction. Length is detailed in pseudo-code below.

n.b. If there is no dynamic value sent with the transaction then we also store a “default” value that will be displayed instead of the combination above.

n.b. The “Prefix” will be right space padded up to 2, 7 or 12 characters, whichever is the shortest.

### Support and Activation

Currently Dynamic Descriptors is only available on TSYS Saratoga terminal IDs. They are available on XML, Hosted Payment Page and Virtual Terminal transactions. The RESTful interface does not support this feature.

### Merchant Request

If required the merchant must raise a support ticket to request that this feature be enabled on their Terminal ID. We will require 3 values to be able to enable this

1. The Terminal ID that it is to be enabled on,
1. The “Prefix” string up to 12 characters long
1. The “Default” string up to 25 characters long

### Admin Setup

To enable this feature in the Admin interface you must go to the Terminal ID settings and tick “Allow Dynamic Descriptors” in the Features Panel.

When this is done two additional fields will appear: the Prefix and the Default Value.

feature_information

As stated above, the dynamic value for the transaction must be sent along with the transaction parameters as a custom fields with the correct name, as defined by the merchant when they configured the Dynamic Descriptors in the section above. Please refer to the Integrator Guide document for details about how to send custom fields with transactions.

Further information on Dynamic Descriptors can be found [Here](https://developers.worldnetpayments.com/merchant/existing_merchant/selfcare_system/settings/dynamic_descriptors)

## Routing and Balancing

Nearly all information and settings regarding Routing and Balancing are merchant facing. Information for these and general information about the feature can be found [here](https://developers.worldnetpayments.com/merchant/existing_merchant/selfcare_system/settings/routing_balancing).

The only Admin facing settings are in the Terminal Setup page, and relate to whether or not the terminal participates in balancing, and is therefore eligible for selection by the system when balancing is performed.

If you enable a terminal for balancing, by ticking “Participate in Balancing” checkbox, you will be prompted to set the “Balancing Priority”. This is a dropdown box that shows the list of terminals currently participating in balancing and the priority they are selected in. Each priority level can only be assigned to a single terminal ID, so you can either:

- Select the lowest priority (highest number) that will have no terminal ID beside it or
- Select the priority that another terminal is currently using; this will cause the existing terminal and lower priority terminals to be shifted down by 1 priority to allow for the new terminal.

Note that the terminals must always have a priority order, but this is only actually used if the Routing Type is set to “Terminal Priority”.

### System logic when selecting terminal during balancing

Balancing only is considered after the transaction is considered ineligible for routing, i.e. it does not match a routing rule.

When the system is deciding what terminal should be used for balancing if follows this logic:

1. Creates a list, ordered by Balancing Priority, of all terminals under the merchant that are participating in balancing
1. Filters out terminals that have reached their monthly transaction value limit
1. Filters out terminals the do not support the transaction currency
1. Filters out terminals that do not support the transaction Card Type
1. Gets the Balancing Type of the Routing Terminal that the transaction was submitted to (Round Robin, Processed Value Ratio, Value Processed, Terminal Priority)
1. Selects a single terminal based on this Balancing Type. If there are no longer any terminals in the list (they've all been filtered out above), then an error is returned to the merchant saying “Can't balance transaction”.

### Secure Tokens with Routing and Balancing

Secure Tokens are only supported for Routing and Balancing if using they are shared among terminals of its Merchant or Merchant's Merchant Portfolio. Currently, as there is no step in the terminal selection to filter by terminals that support processing that specific Secure Tokens, it should only be used for Secure Tokens that are supported by all terminals that are participating in balancing. If this is the case though, it will behave just like any other card.

## Multi-terminal Secure Tokens

Once a Secure Tokens have been saved on a terminal, it can be used on other terminals of the same Merchant or even by other Merchants under the same Merchant Portfolio.

**Merchant Portfolio Sharing**

At this level, when a Merchant Portfolio is configured (created or edited) with **Enable Token Auto Sharing** enabled, a Secure Tokens created within the Merchant Portfolio (all the Secure Tokens of all the Merchants' Terminals) is made available to be used for payment by all the Merchants' Terminals. Disabled, leaves the configuration to Merchant Level.

**Merchant Settings**

Any merchant can choose between sharing its Secure Tokens among all of its Terminals, or not, using the **Share all Secure Tokens** property. When enabled, allows any Terminal from this specific Merchant to use Secure Tokens of the its other Terminals to process transactions. When disabled, the sharing is not allowed and each Terminal can only use its own Secure Tokens.

However, if the Merchant is associated to a Merchant Portfolio with **Enable Token Auto Sharing** enabled, its **Share all Secure Tokens** configuration is automatically enabled.

For more details, check out the **[Secure Tokens](https://developers.worldnetpayments.com/merchant/existing_merchant/selfcare_system/secure_tokens)** page.

## Account Updater and Background Notifications

**Account Updater** refers to Secure Tokens saved on Worldnet Payments’s system, which have had their Cardholder details updated electronically via “Visa Account Updater” (VAU), and “Mastercard Automatic Billing Updater” (ABU) respectively. This is a process which helps to ensure a smooth automatic billing cycle by minimising payment disruptions due to account changes.

Example Use Case:

- Customers Secure Tokens is saved to the gateway
- A monthly subscription is created for the customer
- Time passes, and eventually the card expires
- Worldnet Payments sends a request to Mastercard or Visa asking for the new card details
- Visa/Mastercard sends the updated card details back to Worldnet Payments
- The customers card (Secure Tokens) is updated with new info
- Next months subscription won’t be affected because we now have the correct card details stored for the customer.

Account Updater **Background Notification** (AUBN) is a tool that enables merchants to receive the updated card details.

The merchants will receive the information below:

- New expiry date
- New card number, if it has been changed.

To enable this, on the Admin System,

- Select a terminal, and go to **Features** and check **Enable Account Updater Background Notifications**
- Add the **Account Updater Background Notification URL**
- In **Receipts and Notifications** you will also have to check **Enable Account Updater Background Notification Failure Email**

Further information on Account Updater and Background Notifications can be found [Here](https://developers.worldnetpayments.com/merchant/existing_merchant/selfcare_system/settings/account_updater), or contacting our support team.

## China UnionPay (CUP)

**Enabling CUP**

China UnionPay payment can be enabled only for selected processors.

To enabled CUP on a terminal you need to check **Enable** under the **UnionPay Processing** tab and provide the required data:

- Merchant ID
- Merchant Category Code
- Merchant Name
- Merchant Abbreviation

Additionally, details on the **Draft256 Billing** tab need to be entered as per merchant's Draft256.

**Usage of CUP**

To pay with CUP a cardholder will need to select this option from card list drop-down list on Worldnet Payments HPP. After selecting this option a cardholder will be redirected to CUP HPP.

Due to China UnionPay being a third party Hosted Payment Page, cardholders are not prompted for a credit card number on Worldnet Hosted Payment Page, but instead, they are redirected to the CUP hosted payment page where they enter card details.

All the payments processed with CUP can be check on Open or Closed Batch. The Card Type for CUP transaction is UNIONPAY and all declined transactions are going to show the card number as ‘0000’. This is an expected system behavior due to China UnionPay's handling of declined transactions.

Further information on CUP can be found [Here](https://developers.worldnetpayments.com/merchant/existing_merchant/tips_and_hints/what_is) or contact our support team.

## Recurring Override

Recurring Override has been introduced to flag transactions as recurring payments for merchants migrating to Worldnet Payments but using the same processor. It enables merchants to flag transactions as recurring even though the initial non-recurring transaction was performed on a gateway other than Worldnet Payments.

This feature can be enabled only for processors that support recurring payments e.g. Elavon or TSYS, and can only be used with XML integrations.

Recurring Override can be enabled or disabled on terminal level under **Bank Settings**. The default setting is to allow Recurring Override.

Once enabled on the terminal this feature is implemented by the merchant by sending the TRANSACTIONTYPE as “2” in the XML request. More info [Here](https://developers.worldnetpayments.com/selfcare/api_specification/xml_payment_features).

## PayFAC

Before you can enable PayFac into a Merchant's account, there are a few steps to be completed first.

**1) Create a Partner Portfolio and add PayFAC credentials:**

- Login to the Admin System and select **Billing System**.
- Select **Partners** and **Add** a new Partner.
- Inform the mandatory data. Select the **Enable PayFAC** and provide a **Processor** and a **Payment Facilitator Identifier**.

**2) Create a TPS User and Assign the Partner Portfolio:**

- Login to the Admin System and select **Platform Settings** and **TPS Users**.
- Add a new user or select a current user.
- In **Permissions**, assign the **Portfolio Administrator** role and select the applicable **Partner Portfolio**.

**3) Assign the Payment Facilitator to the Partner Portfolio:**

- Login to the Admin System and and select the desired Merchant account.
- You need to select **Merchant Portfolio Settings**
- Choose the respective **Partner Portfolio** from the drop down list and save the changes.

**4) Enable PayFAC on each applicable terminal:**

- Login to the Admin System and and select the desired Terminal.
- In **Features** tab, check the option **Allow PayFAC**.
- In **Terminal Location & Phone** tab, provide the **Sub-Merchant ID** and **Sub-Merchant Name**.

After that, PayFac is going to be enabled for the given terminal.
