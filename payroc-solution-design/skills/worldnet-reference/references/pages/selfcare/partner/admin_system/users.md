<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:partner:admin_system:users | synced: 2026-10-05 -->

# User Management

In this section we will learn to create and manage user accounts.

## Users

| Users Settings and Permissions | Definition |
|---|---|
| Username | Unique user account |
| Email | User email address |
| Allow Payment Pages | Permission to access templates available for Payment Page |
| Allow Terminal Setup | Permission to configure and setup terminal |
| Allow Refund | Permission to process refunds |
| Allow Virtual Terminal | Permission to process payments on Virtual Terminal |
| Allow CHP on Virtual Terminal | Permission to process payments on Virtual Terminal using CHP methods. <br>To be able to see this option, you user needs to have associated at least one Terminal. <br>This terminal must be CHP enabled and its acquirer should also allow this feature. <br>Contact our support team for more details. |
| Allow Users Setup | Permission to create new user |
| Allow Open Batch | Access to transactions that haven't been settled |
| Allow Closed Batch | Access to settled transactions |
| Allow Bulk Payments | Allows to process multiple transactions at once |
| Allow Billing | Access to billing section |
| Allow Secure Tokens Storage | Permission to store cards |
| Allow Subscriptions | Permission to process subscriptions |
| Allow Dashboard | Visualise statistics payments |
| Allow ACH Transactions | Automated Clearing House - available only in the US |

## Allow Processing Terminals

| Allow Processing Terminals | Definition |
|---|---|
| Processing Terminals | Select terminals that would be available for each user |

## Allow Routing Terminals

| Routing Terminals | Definition |
|---|---|
| Select All | Contact Support Team to check if this feature is available for you. |

## One Time Password Resetting

When necessary, it's possible to send a new password reset link for users using the **Resend welcome e-mail** option, as seen in the image below.

This action will send a 30 minute once valid link so the user can just enter a new password. Once used, the link only works as a “Forgot my Password” link, triggering more requests for a new password.
