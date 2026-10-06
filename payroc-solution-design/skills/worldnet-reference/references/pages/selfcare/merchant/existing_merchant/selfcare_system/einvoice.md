<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:einvoice | synced: 2026-10-05 -->

# eInvoice

The **eInvoice** feature provides merchants with the ability to create and send links to request payments from customers. The merchant “pre-configures” a payment providing the basic details and the elements that should appear on the customer's notification, identifies the customer, and then the merchant can send an e-mail using the Selfcare system, or manually (there's also the option of using our XML API for this) by its own means.

The Merchant needs to have a terminal configured to work with Hosted Payment Pages. Only terminals with this configuration enabled will allow the use of the eInvoice feature.

## Search and Manage Invoice Payment Requests

Each payment link generated can be found using the filter in the search. Among those filter options, you ca use:

- **Merchant Ref**
- **Customer Name**
- **Customer E-mail**
- **Status**
- - *Open* - still not paid successfuly
- - *Complete* - successfuly paid (or with a pending capture)
- - *Cancelled* - cancelled by the merchant before payment or expiration
- - *Expired* - passed the expiration date (automatically changes to expired)
- **Amount**
- **Creation Date**
- **Expiration Date**

All of those option allow the user to choose among different comparators (ranges for quantities, values and dates, or matching types for names and identifiers). Explore the filters and create your own searches - you can safe your searches using the SAVE option, on the left side below the filters.

Once your filters are as you need, just select the SEARCH option and the result is going to be paginates to your right below the search.

On the resulting list you see a few fields which are useful to identify the payment link.

- **Merchant ref**
- **Customer**
- **Creation Date**
- **Expiration Date**
- **Auth Type**
- **Status**
- **Amount**

If you want more details or perform a different action over an existing payment link, at the further right column of the search result you can find the ACTIONS list for each payment link. Depending on the status of the payment link, different actions are possible.

- **View**: Allows the user to check details but not change them. Might be achieve by clicking on the ACTION column and choosing the VIEW option for a specific payment link or by clicking on the MERCHANT REF (table link) of the same payment link. Applicable for COMPLETE, CANCELLED and EXPIRED payment links.
- **Edit**: Allows the user to check and edit details. Might be achieve by clicking on the ACTION column and choosing the EDIT option for a specific payment link or by clicking on the MERCHANT REF (table link) of the same payment link. Applicable only for OPEN payment links.
- **Cancel**: Allows the user to cancel. In the ACTION column, choose the CANCEL option for a specific payment link. Applicable only for OPEN payment links.
- **Send**: Allows the user to send (or resend). In the ACTION column, choose the SEND option for a specific payment link. Applicable only for OPEN payment links.
- **Copy**: Allows the user to create a new payment link from an existing one. In the ACTION column, choose the COPY. Applicable for all statuses. It only open a form copying most of the data of the selected payment link, so you can more easily create a new one from it.
- **Email Preview**: Allows the user to see how the e-mail send by the platform is going to look like in the customer's email. In the ACTION column, choose the EMAIL PREVIEW. Applicable for all statuses.

## Create an Invoice Payment Request

To create a new payment link, you only need to provide a few details.

Depending on your needs, you might want to break down the payment in items.

Also, if your terminal does allow the use of enhanced data, you might need to provide a few more information.

The enhanced data option is only going to be presented in your screen if your terminal does allow that feature. If you are not sure about this or want to know more about the benefits of using enhanced data in your payments, contact our support team.

About the fields:

- **Logo**: Field to inform any logo the Merchant desires to used on a invoice payment request e-mail.
- **Currency**: Currency in which the transaction will be processed (limited to the terminal's currencies). It's only going to be requested if the terminal has more than one currency enabled.
- **Merchant Ref**: Merchant reference used by the merchant to identify its payment links in its way.
- **Expiration Date**: Date in which the payment link ceases to be valid.
- **Description**: Description to inform what the payment link created is related to. Useful specially in cases where the merchant needs to provide context beyond the items for a payment link.
- **Customer Information**
- - *Name*: Name of the customer to which the payment link is addressed to.
- - *Email*: E-mail of the customer in which the payment link should be receive.
- **Enable Level II Data**: this option is going to appear only for terminals with enhanced data enabled (level II and level III). It's going to allow the user to define level II data for a customer. The shipping address details, if informed, will be editable at the Hosted Payment Page, so the customer can change, but the tax information is mandatory.
- - *Use tax for level II data*: this field indicates that the transaction is not exempt from tax and that the merchant wants to define a value, even if it's “0”.
- - *Add shipping address*: enables the fields to provide details on the shipping address to be used at level II. It's going to be editable by the customer when in the Hosted Payment Page.
- **Add Items**: this option allows the user to define if it's necessary to add a list of items to the payment link or if not.
- **Items** - In this list you can ADD or REMOVE items. This option is available after the user marks “Add Items”.
- - *Item*: Identification.
- - *Description*: Short description or name.
- - *Quantity*: Quantity of items.
- - *Price*: Unitary prive by item.
- - *Amount*: Quantity x Price.
- **Transaction Details**
- - *Subtotal*: SUM of all Items (Quantity x Price).
- - *Tax(%)*: Additional taxes the merchant might want or need to apply to a transaction.
- - *Total*: Subtotal + (Subtotal*Tax)
- **Footer Notes**: This area serves the purpose of additional descriptions, information or disclaimers.

## Send an Existing Invoice Payment Request

Once created, a payment link can be sent to a customer until it's completed, cancelled or expires. The user has two options to send the link to the customer:

- While creating the link (after saving is details).

- After the link is created, at any given time (even after editing the details or changing the customer), as long as the link is not COMPLETE, EXPIRED OR CANCELLED.

Understanding the fields:

- **E-mail Preview**: Represents the body build during the Invoice Payment Request creation, and how it is going to look like at the customer's e-mail box when opened.
- **Pay Now Button**: A fragment of HTML code already configured to redirect the customer to the merchant's hosted payment page.
- **Pay Now URL**: Also configured to redirect the customer to the merchant's hosted payment page, but just the URL, without the styling to look like a button.

If the user desires, the **Pay Now Button** is a functional fragment of HTML which can be used to any e-mail body to generate a button to redirect to the final payment page for the customer. Also, the **Pay Now URL** can be used for the same situation.
