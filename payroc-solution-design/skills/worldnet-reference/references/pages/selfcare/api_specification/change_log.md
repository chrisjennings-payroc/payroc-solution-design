<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:api_specification:change_log | synced: 2026-10-05 -->

# API Version Control

| **Version** | **Date** | **Element** | **Description** |
|---|---|---|---|
| 5.2 | 13/06/2018 | Developer > XML Integration Method > Payment Link | New feature designed to provide Merchants with capability of sending a payment link for Customers to perform a payment on a Hosted Payment Page. Additionally, the feature will enable Merchants to send the payment link by e-mail. Take a look: **[XML Payment Link Features](https://developers.worldnetpayments.com/selfcare/api_specification/xml_payment_features_paymentlink)**. |
| 5.1 | 03/04/2018 | Developer > XML Integration Method > Terminal | New feature added to allow integrations to consult Terminal Settings. Take a look: **[XML Terminal Features](https://developers.worldnetpayments.com/selfcare/api_specification/xml_terminal_features)**. |
| 5.1 | 03/04/2018 | New Knowledge Base is live! | The new version of our Knowledge Base is now live. |

| **Author** | **Version** | **Date** | **Changes** |
|---|---|---|---|
| - | 3.0 | 03/04/2018 | New version of our Knowledge Base is now live. |
| - | 3.0 | 03/04/2018 | New feature added to allow integrations to consult Terminal Settings. Take a look: **[XML Terminal Features](https://developers.worldnetpayments.com/selfcare/api_specification/xml_terminal_features)**. |
| Raj Sandhu | 2.7 | 20/01/2016 | Updated TOC, re-branding, updated 3.2 Card Type added CUP SecurePay. Added new section 3.4 Custom Fields and section 3.5 Dynamic Descriptors. Under section 7.1, updated new response codes added, E14: CVV Validation Failed. Added Appendix B. Signature Filed Format |
| Raj Sandhu | 2.6.3 | 14/07/2015 | Updated TOC; Added new section 4 Hosted Pages, 4.1 Hosted Page Styling, 4.2 Basic Mode Styling, 4.3, Advanced Mode Styling; Update under XML Payments section 6.3.1 added Recurring Payment Flagging and uththannder PreAuthorization Request. Updated Test Card details under section 6.1.2. Updated under Request File Submission added /submit to test link |
| Raj Sandhu | 2.6.1 | 07/11/2014 | Under XML Payments section 5.6.1 added MSR/CHP to TRACKDATA added new terminal type #3 Cardholder Present & #0 Cardholder Present (CHP) transaction, also added new note #4. Added +BANKRESPONSECODE+ to hash return in section 5.6.1 under note #2b; Updated glossary with MSR & CHP description |
| Raj Sandhu | 2.6 | 06/10/2014 | Removed Section 2.4.1, added new notes #2 Under Section 5.3.2 added +BANKRESPONSECODE+, Added new Section 5.7, Added Appendix C for response codes, under Section 6.3.1 modified & added new Field Names; XID,CAVV,MPIREF,DEVICEID,CUSTOMFIELD also added BANKRESPONSECODE. Under Section 6.3.1 Notes #2a added BANKRESPONSECODE and added new note #3. Under Section 6.3.2 under Field Name added BANKRESPONSECODE, modified note #2 under section 6.3.4.2 also corrected the respond hash calculation; and under Section 7.1 removed MERCHANT and replaced with REFERENCE, removed AVSONLY Under Section 5.3.1 XML Payments table, & updated TOC |
| Raj Sandhu | 2.5 | 11/08/2014 | Changed ORDERID to UNIQUEREF in Section 4.3 Section4.5 and section 7.2.6.Added new section 5.4.3 Transaction Status Updated |
| Kevin Goddard | 2.4 | 22/07/2014 | Added note about pre-auths, added information to card expiry and cardholdername in sect 5 XML Payment Integration, added processing terminal sect 5, Deleted reference and added payment request fields section under Pre-Auth Requests, added section under unreferenced refunds, carddetails tag in XML requests. |
| Kevin Goddard | 2.3 | 17/04/2014 | Changed references to UTF8 to UTF-8, Added section 5.4.3 FX Terminal Rates Lookup, Added 7.2.7 Subscription Notifications, added user setup section added currency table |
| Kevin Goddard | 2.2 | 11/03/2014 | Added section on Testing Guide and merchant Validation, added two successful trx per trx type required. Removed reference to MCP in hash for preauth. Update URL to GlobalOnePay.com. Changed GlobalONE to GlobalOnePay |
| Kevin Goddard | 2.1 | 24/02/2014 | Added Development team modifications |
| Kevin Goddard | 2.0 | 17/02/2014 | Revised Version |
