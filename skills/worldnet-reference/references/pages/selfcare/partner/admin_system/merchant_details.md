<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:partner:admin_system:merchant_details | synced: 2026-10-05 -->

# Merchant Details

In this section, we will learn how to set up an account.

Let's start with the **Merchant Contact Details** as per screenshot below:

## Merchant Contact Details

| Merchant Contact Details | Description |
|---|---|
| DBA Name | Doing Business As - Business Name as it appears in the activation report |
| Contact Name | Main Business Contact |
| Phone | Merchant's Phone Number |
| Email | Invoice Email |
| Website | Merchant's website (if applicable) |
| City | As it appears in the activation report |
| MCC | Merchant Category Code (Provided in the activation report) |
| Address | Business address as it appears in the activation report |

## Merchant Portfolio Settings

| Merchant Portfolio Settings | Description |
|---|---|
| Gateway | Worldnet Payments or 3rd Party Gateway |
| Merchant Portfolio | This is available to group merchants under one portfolio and to create a portfolio administrator who can access, add and modify merchant groups under that portfolio. |
| Partner Portfolio | This is a filtering option for grouping merchants on the admin system. This option doesn't allow for any specific access or merchant modifications. |

## Merchant Pricing Details

| Merchant Pricing Details | Description |
|---|---|
| Pricing Type | If changed for terminal the price will be allocated |
| Pricing Templates | If the merchant is part of a partner portfolio, a template can be made to apply to all merchants and it will be applied for merchants included in the portfolio |
| Monthly Fee | Fixed Monthly Base Fee |
| Monthly Fee Type | Included transactions |
| Included Transactions | Monthly number of transactions included in Base Fee |
| Per Txn | Charge per transaction after included transaction limit reached |
| Transaction Classification | If “All” selected, the merchant will be charged for any transactions including approval, declined, referral or void whereas if “completed”, they will be charged only for approved transactions |
| Per 3DS (+) | Charge per 3DS transaction |
| Per eDCC (+) | Charge per eDCC transaction |
| Per Token (+) | Charge per Secure Token transaction |
| Per SMS | Charge per receipt or notification sent by SMS |
| Max Mind Request | Security feature - Contact Support Team for more information |

## Merchant Charging Details

| Merchant Charging Details | Description |
|---|---|
| Charging Currrency | Invoice's currency |
| VAT Exempt | Check this option if merchant is legally VAT exempt |
| VAT Number | Merchant VAT number |
| Billing Type | Invoice or Direct Debit Bank Details |
| Do not bill next month | Check this option if merchant should not be billed the following month |
| Reason | Reason for not bill |

## General Setup

| Merchant General Setup | Description |
|---|---|
| Share All Secure Tokens | This configuration enables a Merchant to define that all the Secure Tokens in its Terminals should be shared amount themselves or not. |
| Share Secure Tokens from deactivated terminals | Depends on enabling “Share All Secure Tokens”. Allows merchants to also use the Secure Tokens of Deactivated Terminals. In case the merchant is already associated to a Merchant Portfolio with this configuration enabled, this one is automatically enabled. |
| Enable Single Transaction Limits | Enables the Merchant to have general limits for single transactions on its terminals, regarding or not rules like: CVV and AVS verification. |
| Customize Register Secure Tokens Button Text | Enables a merchant to define the text for a Secure Tokens registration button at the Payment Gateway side for customers' interfaces. |

### Enable Single Transaction Limits

If selected, this option enables to configure a Merchant with limits for single transaction in all of the Merchant's Terminals.

This feature is useful in cases a Merchant needs, given risk policies or business rules, define limits to avoid charge backs or constant declines for purchases which are being normal limits.

Let's consider the following case:

- **I)** A Merchant wants to permit its terminals to allow transactions regardless the value, but
- **II)** In case the transaction can't verify AVS, limit each transaction to a maximum of EUR 1000.0, or
- **III)** In case the CVV can't be verified, limit each transaction to a maximum of EUR 100.0, or even
- **IV)** If none can be verified, limit each transaction to EUR 10.0
