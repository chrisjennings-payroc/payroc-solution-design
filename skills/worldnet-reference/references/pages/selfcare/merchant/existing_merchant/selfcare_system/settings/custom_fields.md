<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:custom_fields | synced: 2026-10-05 -->

# Custom Fields

It is possible for the merchant to choose **Custom Fields** to appear on the Virtual Terminal and Hosted Payment Page.

The **Custom Fields** are accessible from **SETTINGS** menu. Custom Fields include: Field Name, Size, Display Order, mandatory flag and links to delete/edit the field.

Sample **Custom Fields** window:

The following attributes can be configured for each custom field:

- **Name** – the name of the custom field.
- **Display Name** – the name of the field which will appear on the Payment Page and Virtual Terminal.
- **Size** – the width of the field when it is displayed.
- **Display Order** – It is possible to set the order in which the fields appear on the payment pages using this setting. This value is between 1 and 100, with the lower number field displayed first on the payment pages.
- **Virtual Terminal** (check-box) – choose this option if this custom field should appear on the Virtual Terminal.
- **Payment Page** (check-box) – choose this option if the custom field should appear on the Hosted Payment Page.
- **Mandatory** (check-box) – Choose this option if the user MUST fill out this field before proceeding.
- **Bulk Payment** (check-box) - available only with if an additional agreement between the merchant and Worldnet Payments is in place.

Fill up all new fields or make all required changes and click the ‘**Save**’ button to store changes.

To customize another setting, select **Add Custom Field**. The **Add Custom Field** screen will request the Name of the field to be customized, the Language, the Display Name, the Field Type (String, Numeric or Boolean), the Display Order (1-20), and the option to use this feature for Virtual Terminal, Payment Page and Bulk Payment (check = yes, blank = no) and whether or not this is a Mandatory Field (check = yes, blank = no). Select **Save** to complete your customized field.

Before you leave this screen, select the language you wish to be used as the **Language Default** option. Click to **Save**.

**Deleting a Custom Field:**

Click the '**Delete**' link in the Custom Fields main page to delete a Custom Field. The chosen field will be marked as deleted *without a confirmation dialog*. This field will not appear in the terminal Custom Fields list but it will be displayed in the transaction details page for orders already processed using this custom field.
