<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:terminal | synced: 2026-10-05 -->

# Terminal

You can find the “**TERMINAL**” section under the “**SETTINGS**” tab in the Selfcare.

Select **Terminal** from the drop down box to view the terminal settings. If the current user has the correct permission level, they can view and modify some of the virtual terminal (VT) settings that best accommodate your business practices. Several “default” field selections will appear but can be revised. Use the scroll down bar to view all of the setting options.

*Note:* If more than (4) taxes are to be collected, you can select **Add new tax** to implement them or **remove** them as needed. Also, additional Terminal Tips can be preset by selecting **Add new tip** or deleted by selecting **remove**. When finished, select **Update Settings** to save.

The following settings can be configured in this section:

**Show CVV** - This option indicates whether the merchant chooses to have the CVV field shown on the Hosted Payment Page and Virtual Terminal. This field is supported by Visa, MasterCard and Delta cards only.

**Auto Decline CVV failures** - This option is chosen if the merchant decides to force all CVV non-matches to a transaction decline. This is sometimes desirable as not all card issuers will decline a transaction that has failed a CVV check.

**Show Issue No** - This option enables / disables the ‘Issue No’ field being shown on the Hosted Payment Page and Virtual Terminal. This field is for Switch and Solo cards only.

**Enable AVS** - This option enables the Address Verification System (AVS) and two new fields will be shown: **AVS Compulsory** (check field) and If **AVS sent** (list of options). This setting, when enabled, shows three address fields at the Virtual Terminal and at the Hosted Payment Page – the fields are Street, City and Postcode. With that, the cardholder will be able to provide a card billing address, but that is not mandatory. If informed, this entered address fields will be sent to the bank for validation.

**AVS Compulsory** - When selected, this option enables a new field **API AVS Type**, and ensures that before finishing a transaction cannot be processed without filling in the address fields.

**API AVS Type** - This field defines a configuration for the execution of AVS in API integrations – REST, XML and HPP. Depending on the value selected, the AVS will consider a specific set of fields to be sent to the bank for validation.

- *Exact:* The fields shown and expected are all three.
- *Postal:* The only field shown and expected is Postcode.

**If AVS sent** - This field defines a configuration for the Hosted Payment Page (HPP). When an application integrated to a HPP already has the cardholder’s billing address, it’s possible to send this data to the HPP and selecting one of the options in this field you can:

- *Hide* – selecting “Hide”, the HPP is going to use the address internally on the AVS, but the data is not going to be shown on the HPP.
- *Display* – selecting “Display”, the address receive by the HPP will be shown and used to execute the AVS, but It’ll not be editable by the user.
- *Editable* – selecting “Editable”, the address receive by the HPP will be shown and used to execute the AVS, but the user will be able to edit the fields before submiting the payment.

**Auto Ready** - This option specifies if transactions, not exceeding a specified limit, should automatically be set in the READY state. This means that all transactions will immediately be put in the queue for settlement without any intervention needed. Auto Ready setting for the terminal can be replaced by the Auto Ready at a transaction level, please check Merchant Integration Guide for details.

**Auto Ready Limit** - The merchant may choose to limit the value of transactions that should be automatically set to READY. For example if the average transaction value is EUR20, the merchant may need to be aware if a transaction arrives which is substantially outside this range. This field has effect only when ‘Auto Ready’ is enabled. Limit setting of 0 means that transaction amounts will not be checked.

**Notification Email** - This value is set if the merchant wishes to receive an email every time the system processes a transaction.

**Notification Language** - This value defines the default language to be used for receipts' notifications and printing.

**Receipt Page URL** - The cardholder browser is redirected to this URL after the transaction is completed. The merchant decides what to do/display based on the fields received. Please check the Hosted Payment Page section in the Merchant Integration Guide for a description of the fields sent to this URL.

**MPI Receipt URL** - This should be used if your website uses our hosted 3D Secure page for XML payments. The cardholder browser is redirected to this URL after the 3D Secure verification is completed.

**SecureCard URL** - This should be used if your website uses our hosted SecureCard registration/update page. The cardholder browser is redirected to this URL after the card details are registered/updated.

**Subscription Receipt URL** - This should be used if your website uses our hosted Subscription registration/update page. The cardholder browser is redirected to this URL after the subscription details are registered/updated.

**Enable Validation** - Check this box if your site is configured to validate all transactions before allowing them to settle.

**Validation URL** - This should be used if your website uses background validation for transactions. Our server will post a server side message to this URL containing the result of every transaction/subscription payment attempt.

**Secret and Confirm Secret** - A new terminal shared secret can be set here; both fields should have an identical value. Terminal secret will be changed only if secret fields are populated, secret will not be modified when these fields are empty.

**Show Email on VT** - This will include an e-mail field for Virtual Terminal transactions. If populated with an e-mail address this will send a receipt for the transaction to that address.

**Show Phone on VT** - This will include a phone number field for Virtual Terminal transactions.

**Show Country on VT** - This will include a country drop down box for Virtual Terminal transactions.

**Disable Cardholder Receipt** - This will prevent Worldnet Payments from sending the cardholder an email even if the e-mail address is included in the transaction.

Clicking the ‘**Update Settings**’ button will save changes made to the General Section. Data modified in the other sections will be lost without alert.
