<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:account_updater | synced: 2026-10-05 -->

# Account Updater

“Account Updater” refers to Secure Tokens saved on Worldnet Payments’s system, which have had their Cardholder details updated electronically via “Visa Account Updater” (VAU), and “Mastercard Automatic Billing Updater” (ABU) respectively. This is a process which helps to ensure a smooth automatic billing cycle by minimising payment disruptions due to account changes.

Example Use Case:

- Customers Secure Tokens is saved to the gateway.
- A monthly subscription is created for the customer.
- Time passes, and eventually the card expires.
- Worldnet Payments sends a request to Mastercard or Visa asking for the new card details.
- Visa/Mastercard sends the updated card details back to Worldnet Payments.
- The customers card (Secure Tokens) is updated with new info.
- Next months subscription won’t be affected because we now have the correct card details stored for the customer.

## Account Updater Background Notification

Account Updater Background Notification (AUBN) is a tool that enables merchants to receive the updated card details.

The merchants will receive the information below:

- New expiry date.
- New card number, if it has been changed.

**Secure Tokens Custom Fields (SCCFs)**

At the moment, Secure Tokens custom fields are only useful with Account Updater Background Notifications. Because of this, SCCFs are only editable/viewable when Account Updater Background Notifications are Enabled.

**SCCFs Limit**

- Each terminal can have a maximum of 3 SCCFs.
- These fields are useful for any custom data the merchant wants to record about the customer for example: accounting software related data.

**To create SCCFs on the Selfcare System**

Once the Secure Tokens Custom Fields are set, they will be displayed when adding or editing a Secure Tokens in Selfcare system. To know more about how to create custom fields, visit the **[Custom Fields](https://developers.worldnetpayments.com/merchant/existing_merchant/selfcare_system/settings/custom_fields)** page.
