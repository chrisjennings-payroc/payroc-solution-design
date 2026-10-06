<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:secure_tokens | synced: 2026-10-05 -->

# Secure Tokens

**Secure Tokens** (Token) is useful for merchants which are required to perform regular payments without the card holders entering their information. This feature enables merchants to enter the payment card details and store them in a secure way, in order to use it in the future for recurring payments.

Considering that only PCI-DSS certified merchants are allowed to store card details, the **Secure Tokens** feature can remove this concern from the merchant's domain.

The **Secure Tokens** feature is located under the “**Customers**” tab in the **Selfcare** system.

Also:

- Secure Tokens can be shared with different terminals under the same Merchant or Merchant Portfolio, as long as those elements are configured to allow that.
- Our **Secure Tokens** feature works together with our **Subscription** feature, meaning that a Secure Tokens needs to be registered before you can set up a **Subscription** for regular payments.

The following subsections will present more details on each action regarding this feature.

## Secure Tokens Registration

To register a new Secure Tokens go to the “**Secure Tokens**” feature and choose “**Register New Secure Tokens**” button. Then fill in the card details and make sure that you complete all the fields.

- Merchant Ref - merchant's reference for the Secure Tokens.
- Card type - Master Card, Visa Debit, Visa, etc.
- Card number - complete card number
- CVV - this is going to be required depending on settings on your terminal.
- Expiry date - month and year.
- Cardholder name - complete card holder name printed on the card.

An error message will appear if there are any incomplete details, as shown by the next images.

Once all the details have been entered, click on the “**Register**” button in the bottom right corner to save the Secure Tokens details for future use. You can view the details of your new Secure Tokens in the list of all registered cards under “**Secure Tokens**” menu.

If your card requires CVV code or your Terminal is configured to perform Secure Tokens validation (CVV mandatory or not), the Payment Gateway performs an account verification before registering the Secure Tokens:

- If the CVV field is informed, the CVV response returned is verified and if it's positive the Secure Tokens is registered, if not, an error is generated.
- If the CVV field is not informed, the result of the transaction is verified and if it's successful the Secure Tokens is registered, if not, an error is generated.
-

Depending on the Payment Processor used by the Terminal, the account verification can be performed in two distinct ways:

- A 0.00 (zero) amount transaction or,
- A 1.00 (one) currency unit amount transaction followed, when successful, by its voiding (both transactions will appear in your batch).

If you would like to see the details of this transaction, go to “**Reporting**” tab and then to “**Open Batch**” section.

Please see below the examples of common **Error messages** occurring during new Secure Tokens registration process, due to *incomplete details* entered: “There are errors in your form. Please review and retry”.

## Secure Tokens Editing

When accessing the Secure Tokens option,all the previously registered Token are listed. You can also search for Secure Tokens by “Merchant reference” or by other criteria in the Advanced filter.

In order to edit the details of a Secure Tokens, click on the “Edit” link next to the required Secure Tokens's details.

Please note that you are not able to amend the Merchant Ref, modification date and Card Reference. (Please remember that you cannot use the same Merchant Ref which was already used for another card twice, to register or edit a new Secure Tokens, even if the previous card has been deleted).

Important Notes:

- **I**. You can choose a different **Card Type** from the available selection.
- **II**. If you wish to edit the card number, tick the box “**Update Card Number**” and then put the new card number. Then tick the box “**CVV required**” if your card requires CVV and enter the correct CVV code.
- **III**. You can also amend the cardholder's name, if needed.
- **IV**. If you do not want to make any changes, click on “**Cancel**” button in the bottom right corner and you will return to the all Secure Tokens list.
- **V**. When you make sure that all the new details are correct, click on the “**Update**” button to save the changes. This way, new updated **Secure Tokens** will be saved in the place of the old, incorrect one.

For example:

When you click on “**Update**”, the new Secure Tokens details are saved and they appear in the “**Secure Tokens**” list. Please note that if there is no 'tick' sign next to card reference number, it means that this card was not CVV validated.

**CVV Validation**: All Secure Tokens registered are validated.

- **a)** If the Token is registered without a CVV, our Gateway is going to submit a validation for the card number.
- **b)** If the CVV is informed, a CVV validation transaction is going to be performed.

Depending on your Acquirer, the validation may vary between a $ 1.00 currency unit authorization following by the voiding of the validation, or a $ 0.00 currency unit validation. If you would like to see the details of this transaction, go to “**Reporting**” tab and then to “**Open Batch**” section.

## Secure Tokens Deleting

In order to delete a Secure Tokens from the list, please click on “**Delete**” link next to the chosen card's details.

Please note that the system will not allow you to delete a Secure Tokens which has been already used to create a subscription.

In the case when a Secure Tokens is already used in a subscription, you will need to delete/finish the subscription first, before you will be able to delete that Secure Tokens.

The image below shows an error message, as an example.

## Secure Tokens Search

For Secure Tokens, you can “**Search by Merchant Reference**”, “**Search by Card**” or use “**Advanced Filter**”.

To search Secure Tokens by **Merchant Reference**, you just need to put the full merchant ref number in the field and click on “**Submit**” button.

To search Secure Tokens by **Card**, you can use the following criteria.

- Last 4 digits of the Card.
- First 6 digits and last 4 digits of the Card.
- Card expiry date.

This search is mostly used to find Secure Tokens details when you don't have the full card number.

The last search option, **Advanced Filter**, allows the following criteria:

- Start Date.
- End Date (the approximate date range of when the Secure Tokens was created , it's not the Secure Tokens's expiry date!).
- Card type (Master Card, Visa Debit, Visa, etc.).
- Cardholder name.
- Card reference - Secure Tokens unique reference used as the token.
- Merchant Holder - particularly useful when the Secure Tokens are shared between Merchants of a Merchant Portfolio.
- Terminal Holder - particularly useful when the Secure Tokens are shared between Terminals of a Merchant.

Please make sure that you put the complete reference - for example complete cardholder name (name and surname) and complete card ref - otherwise the search will not bring any results.

For example, if you would like to search by Card type, select it from the drop down menu, and click “**Submit**”.

Then all the Secure Tokens corresponding to this type will appear:

At any stage, if you would like to change the filter criteria, click on “Reset Search” button and you will go back to the main search page.

If you would like to search by Cardholder name, please put the full cardholder name as printed on the card. If you will put a partial name, then the search will not bring any results, as in the example below:

When you put the full cardholder name in the search field and click on “Submit”, then the cards will appear below:

When you search by Card Reference, only one Secure Tokens which corresponds to that reference will appear as a result of the search:
