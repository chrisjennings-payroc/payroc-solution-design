<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:tips_and_hints:what_is | synced: 2026-10-05 -->

# What Is It?

## Closed Batch

A **Batch** is an accumulation of credit card transactions settled to the acquiring bank together, intended to be funded to your bank account in one “Batch”. The batch may contain sales transactions, refunds, voids, and other credit card transaction types. Typically, there are two types of batches: Open and Closed.

**Closed Batch**: This is a historical list of all previous batches for the Terminal. The date stamp listed is the exact date and time that the transactions were uploaded to the acquiring bank as a batch.

Please see the screenshot below with an example of a Closed Batch:

## eDCC (eCommerce Dynamic Currency Conversion)

**eCommerce Dynamic Currency Conversion**

- Worldnet Payments currently support eDCC only with Elavon bank.
- eDCC must be available in your Acquiring bank account and with Worldnet Payments, before it will be available to the site.
- eDCC cannot be used to provide multi currency pricing on your website. It comes into play during payment only, and not before. It cannot be used to provide exchange rates to your site, either.
- The wording of the eDCC offer is usually strictly controlled by the acquiring banks. We recommend using the text attached. The variable fields should all be available in the rate response you receive from us.
- You cannot add eDCC to a payment without prompting the cardholder for their decision.
- If you are using our Hosted pages to receive the cardholder data, then Worldnet Payments will process the eDCC.
- It is available for MOTO and e-commerce terminals.

**To add eDCC to your XML solution you must follow these steps**:

- After receiving the cardholder data (and before authenticating 3D Secure if relevant), you should process the XmlRateRequest(), XmlRateRequest.SetBaseAmount() and XmlRateResponse = XmlRateRequest.ProcessRequest() methods. If a rate is available for the card, this will provide you with all the information that you need for the DCC offer.
- If a rate was returned, prompt the cardholder for a DCC decision.
- If a rate is not available, or the cardholder decides to pay in the the base trans currency, the payment should be processed as normal.
- If the cardholder accepts the foreign currency (DCC) amount, when processing the XmlAuthRequest(), you should invoke the XmlAuthRequest.SetForeignCurrencyInformation() method.

People from all over the world make Internet bookings for international travel, accommodation, entertainment, and make payment for online goods and services. Typically, international credit card payments are made in the currency of the host merchant site, and converted subsequently by the card issuing bank to the buyer’s home currency, with the cardholder paying a foreign exchange conversion fee to the card issuer. E-commerce Dynamic Currency Conversion (eDCC) is a smart alternative which moves the exchange conversion to the front-end of the transaction, providing online merchants with a new revenue opportunity and additional value to their international customers.

**Improve service for international customers**

With eDCC, your international customers will know exactly what their total purchase is in their home currency at the time you process the transaction. Conversion rates are competitive and each online transaction shows the purchase amount in the merchant currency, the conversion rate, and the total amount in the cardholder’s home currency. This makes it simple for cardholders to reconcile purchases when they receive their credit card statements. The eDCC service instantly converts the purchase amount into 48 leading international currencies including:

- Euro
- British Pound
- Danish Krone
- U.S. Dollar
- Japanese Yen
- Australian Dollar
- Canadian Dollar
- Hong Kong Dollar
- Polish Złoty
- Swiss Franc
- South African Rand
- and many more

**How eDCC works**:

The eDCC process provides everything from direct treasury exchange rates and transaction processing to back-end reconciliation, settlement, funding and support. When the card details are entered on the merchant website, the system automatically determines if it is a foreign eDCC-qualified card from the Bank ID Number (BIN). If it is, the system will present the transaction for confirmation to the cardholder on the payment page including the transaction amount, conversion rate and payment amount in the cardholder currency for acceptance. The cardholder has the option of paying in their domestic currency or the merchant currency.

- Experience shows that over 90% of customers, when given the eDCC option, choose to pay in their own domestic currency.
- Funds are settled to the merchants in their own domestic currency as standard and the transaction reports and statements clearly indicate both currencies in the transaction details.
- eDCC carries no activation fees, monthly fees or monthly minimums .
- eDCC is also available for Mail Order & Telephone Order transactions, using Worldnet Payments`s Virtual Terminal product.

**eDCC pays you back**

Best of all, the merchant shares the income generated by processing foreign transactions in the form of a rebate of a percentage of the conversion rate on his monthly processing statement. The more international business the merchant processes, the more he improves his bottom line. In addition eDCC reduces the number of chargebacks, because the amount on the payment authorisation matches that on the cardholder’s statement. The eDCC service works for all MasterCard® and Visa® credit and debit card transactions from countries with approved settlement currencies. Conversion rates are competitive, transparent, and updated daily. The DCC system operates within the security and transparency requirements set by the card schemes.

**eDCC Benefits:**

*Benefits to your customers:*

- Convenience – prices are instantly converted to their own currency.
- Comfort – customer knows exactly how much the transaction costs in their own currency.
- Competitive rates – exchange rates are updated daily.

*Benefits to you:*

- New income stream – receive monthly rebates of the foreign exchange commission.
- Exchange rates are updated automatically on a daily basis.

## E-mail Alerts

**Email Alerts** are a part of “**Settings**” menu. Alerts allow you to set email notifications for different types of transactions such as daily sales, approved and declined sale or voids and refunds. Alerts can be sent depending on individual requirements. Also different email addresses can be used for each notification. Only one email address can be used for each alert though.

Each event can be triggered by choosing a monetary amount qualifier. For example, if the merchant wishes to be notified each time one of their system operators refunds a transaction for more than €1000 then select the ‘Sale Refunded’ event, choose ‘Greater than’ and enter 1000 in the value column.

Please see the screenshot below with the example of Email Alerts:

Alerts can be sent for email notification based on **current value** thresholds (less than/greater than the value entered) for each of the following:

**Daily Net Sales** - Choose this option if you wish to be notified daily of your processing totals. These totals are broken down into Net Total, Net Sales, Net Voids and Net Refunds.

- **Sale Approval** - Choose this option if you wish to be notified each time a sale is approved.
- **Sale Decline** - Choose this option if you wish to be notified each time a sale is declined.
- **Sale Pended** - Choose this option if you wish to be notified each time a sale is pended by the system or when an operator manually pends a transaction.
- **Sale Voided** - Choose this option if you wish to be notified each time a sale is pended by a system operator.
- **Sale Refunded** - Choose this option if you wish to be notified each time a sale is refunded by a system operator.

Please note that the alert can be turned **On/Off** at any time. Simply un-check the box if you want to to turn off the alert.

When data entry is complete, select **Update Email Alerts**.

## Merchant ID

**Merchant Identification Number** (MID) is a unique number issued by the acquiring bank to identify a merchant and the merchant's terminal(s) to a host computer in the credit card processing network.

**Worldnet Payments** use our own Merchant ID to identify merchants set-up on the Selfcare. Worldnet Payments MID is a four-digit code supplied to all merchants during the account activation process. Worldnet Payments MID is different to any acquiring bank's MID and those two MIDs are not related or linked in any way.

## Open Batch

A **Batch** is an accumulation of credit card transactions settled to the acquiring bank together, intended to be funded to your bank account in one “Batch”. The batch may contain: sales transactions, refunds, voids, and other credit card transaction types. Typically, there are two types of batches: Open and Closed.

**Open Batch**: These are transactions that have not yet settled. For most merchants they are “todays” transactions. Any Sale or Refund transactions will be settled the next time settlement is run for that Terminal ID as long as their status is Ready, Void, Declined, Pickup (lost or stolen card) or Referral.

Please see the screenshot below with the example of **Open Batch** in Selfcare:

## Pre- Authorization

A **Pre-Authorization** is a pre-approval for a future transaction. The pre-authorization is usually followed, within a specific time interval, by a “completion” that will be settled to the merchants account in a subsequent batch. Pre-authorizations are used primarily in situations where the merchant wishes to obtain “advance approval” or “verification” that sufficient funds are available on a card when the final amount of the transaction is not known (e.g. hotel check-in, ordering a tank of oil, cart order with unknown stock availability, etc.)

You can process a **Pre-Authorization using Virtual Terminal** in the Selfcare:

## Shared Secret

A **Shared Secret** is a string used to create a digital signature (referred to as a “hash”) which is provided with every request to and from the system to ensure the integrity of the transaction data and to authenticate the sender as being the legitimate account holder. It is known by both sides communicating, but is never actually sent, hence why it is called a secret. It is known only to you (the merchant) and other parties involved and approved by you (i.e. your developer or a member of staff).

A Shared Secret can be a password, a paraphrase, a long number or a string of randomly chosen characters (for example: ABCD, 2622Q5b5sv, John Smith, 5678, etc). It must be set up by you or a designated person after we create an account for you for the first time.

Also, please remember that no member of our staff has access to your Shared Secret and we are unable to provide you with your Shared Secret if you forgot it. In that case you must change the Shared Secret directly in the Selfcare and then update your sites/devices with the new Shared Secret.

If you have multiple TIDs, then each terminal has its own Shared Secret.

You can **change or set-up your Shared Secret** in the Selfcare within “**Terminal**” under “**Settings**” menu.

It is strongly recommended that the shared secret is kept safe and not shared with third-parties.

## SMS Alerts

**SMS Alerts** is a part of “Settings” menu. SMS Alerts allow for setting notifications, that are sent to a mobile phone, for different types of transactions such as daily sales, approved and declined sale or voided and refunded sale. Alerts can be sent depends on individual requirements. Also different phone numbers can be used for each notification.

Worldnet Payments provide the ability for merchants to be notified when specific events occur in their payment processing system. You can find “**SMS Alerts**” section under the **SETTINGS** tab in the Selfcare. This notification can be in the form of an eMail, an **SMS message**, or both.

Select **SMS Alerts** from the drop down menu under “SETTINGS” tab.

Each event can be triggered by choosing a monetary amount qualifier. For example, if the merchant wishes to be notified each time one of their system operators refunds a transaction for more than €1000 then select the ‘Sale Refunded’ event, choose ‘Greater than’ and enter 1000 in the value column.

Please see the screenshot below with the example:

Alerts can by sent for SMS notification based on current value thresholds (less than/greater than the value entered) for each of the following:

**Daily Net Sales** - Choose this option if you wish to be notified daily of your processing totals. These totals are broken down into Net Total, Net Sales, Net Voids and Net Refunds.

**Sale Approval** - Choose this option if you wish to be notified each time a sale is approved.

**Sale Decline** - Choose this option if you wish to be notified each time a sale is declined.

**Sale Pended** - Choose this option if you wish to be notified each time a sale is pended by the system or when an operator manually pends a transaction.

**Sale Voided** - Choose this option if you wish to be notified each time a sale is pended by a system operator.

**Sale Refunded** - Choose this option if you wish to be notified each time a sale is refunded by a system operator.

Enter a phone number capable of receiving SMS/text notification. Note that the alert can be turned On/Off at any time. When data entry is complete, select **Update SMS Alerts**.

## Terminal ID

**Terminal Identification Number**, also known as a **TID**, is a unique number assigned and linked to a specific point-of-sale (POS) terminal or workstation that can be used to identify the merchant operating the terminal during credit card sales transaction processing. This number is required to set up online processing through online payment gateways, and is created and provided by the bank or merchant service provider with which a company has set up a merchant account. The number not only identifies what company is using what specific terminal, but also tracks each POS transaction made at that specific location.

**Worldnet Payments Terminal ID** is also a unique number that is assigned to your merchant number when you apply for an account with us, and this ID is different from the TID provided by your merchant bank.

Worldnet Payments TID is always 7 digits long and starts with your 4 digit MID follow by sub-sequential numbers starting from 001 i.e.

- Worldnet Payments MID: 3211.
- Worldnet Payments TID: 3211001, 3211002, 3211003 etc.

Please note that you might have multiple TIDs under one MID, and you can switch between your TIDs using the drop-down list underneath the Worldnet Payments logo as per the example below.

## Void

A **Void** is the cancellation of a previous sale that has not yet been settled/batched. A void can only be performed on transactions in the Open Batch. The original sale transaction is effectively removed from the batch of transactions to be settled, but will still appear with a status of “Void”. Once a transaction has been voided this action cannot be undone.

**Note**: Worldnet Payments does not handle any actual funds and has no control over this process. Please contact your merchant bank for any further information.

Sample **Void** window:

You can void or this transaction by clicking on the “**Void**” button in the bottom right corner:

## Automated Clearing House (ACH)

Automated Clearing House (ACH) is an electronic network for financial transactions in the United States. ACH processes large volumes of credit and debit transactions in batches. ACH credit transfers include direct deposit, payroll and vendor payments. ACH direct debit transfers include consumer payments on insurance premiums, mortgage loans, and other kinds of bills.

The Worldnet Payments system is a secure server-based transaction processing service that will enable your business to authorise and process ACH transactions online in real-time. The information needed to process the transactions is sent over a secure, encrypted internet connection.

Once the customer has completed the payment form, the Worldnet Payments server connects with Sage for payment authorisation and if the sale is authorised, returns a receipt to the customer. Worldnet Payments settles the transactions automatically and the acquiring bank deposits the funds into your bank account. Worldnet Payments automatically archives sales that are finalised so that you can refer to them at a later date, if necessary.

## China UnionPay (CUP)

**Understanding**

China UnionPay, also known as UnionPay, or by its abbreviation CUP, is a Chinese financial services corporation headquartered in Shanghai, China. It provides bank card services and a major card scheme in mainland China. CUP has been founded in March 2002 and it is an association for China's banking card industry, operating under the approval of the central bank of China. It is also the only interbank network in China that links all the ATMs of all banks throughout the country. It is also an EFTPOS (Electronic Funds Transfer at Point of Sale) network.

UnionPay cards can be used in 141 countries and regions around the world. Some UnionPay credit cards are also affiliated with American Express, MasterCard or Visa, and they can be used abroad as an American Express, MasterCard or Visa. UnionPay debit cards, however, can only be used in the UnionPay network and other networks that have signed contracts with UnionPay. Since 2006, China UnionPay cards can be used in over 100 countries outside China.

**Using**

In order to use China UnionPay you will need to obtain a relevant merchant account with CUP. Once you have relevant documentation and approval, you need to contact our Customer Support and we will enable this payment option for you.

Using China UnionPay does not require any integration.

Once CUP is enabled on your account, a cardholder will be presented with a new option on your Hosted Payment Page under cards list. After selecting CUP as a payment option, a cardholder will be redirected to China UnionPay page where he needs to complete the payment.

All the payments processed with CUP can be check on Open or Closed Batch. The Card Type for CUP transaction is UNIONPAY. Note: all declined transactions show card number as ‘0000’. This is expected system behavior due to China UnionPay handling of declined transactions.
