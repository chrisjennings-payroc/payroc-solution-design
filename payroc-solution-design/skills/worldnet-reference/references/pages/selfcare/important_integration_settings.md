<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:important_integration_settings | synced: 2026-10-05 -->

# Important Integration Settings

 Each type of integration and each feature may require different settings to work under an integration. Here we are going to review the main settings you have to be aware of before you can start using your integration.

## By Integration Method

### Hosted Page (HP)

#### Enabling Method and Features for Terminal

When a Terminal is created or edited, a few permissions need to be set in place so it can operate with HP and its features, and before you can use this integration method, be sure these configuration are in place. Confirm with our support team if the Terminal you are trying to use allows the use of Hosted Payment Pages.

- **A hint**: Your Terminal needs to have “**Allow Internet**” enabled to start using the HPP.

> **Note**
> The present settings are to be performed by the **Gateway Administrator** - verify it before integrating.

#### Styling Your Hosted Pages

The Hosted Page integration method provides some additional settings regarding styling. This allows the pages to be highly styled, so they look more appealing to customers, besides helping to improve conversion rates and customers overall experience.

The configuration regarding this styling can be found at Selfcare System, under “Settings > Pay Pages”. There you can find templates for your hosted pages and see how they are going to appear to the customers.

For more information about the styling of Hosted Pages, visit the **[Pay Pages](https://developers.worldnetpayments.com/hosted_pages/introduction)** page in our Selfcare Guide.

> **Note**
> The present settings are to be performed by the **Merchant**.

## By Feature

A few features demand some configurations to work. Most of them are configured at Terminal Level, and you need to ensure they are accessible to the Terminal you are using. Below, we present a few mentions related to that, but depending on the features you are implementing, the setting might require other checkings, and in this case, contact our Support Team.

> **Note**
> The present settings are to be performed by the **Gateway Administrator** - verify it before integrating.

### Secure Tokens

**Merchant Portfolio Settings**

At this level, when a Merchant Portfolio is configured, three different settings can be used to define how the the Secure Tokens Registration and the Payment using a Secure Tokens should occur for its Merchants:

- **Enable Token Auto Registration**: when enabled, automatically attempts to create Secure Tokens when Payment transactions occur.
- **Enable Token Uniqueness**: when enabled, a Secure Tokens is unique within the Merchant Portfolio scope (all the Secure Tokens of all the Merchants' Terminals), but when disabled, a Secure Tokens is unique within the Terminal's scope.
- **Enable Token Auto Sharing**: when enabled, a Secure Tokens created within the Merchant Portfolio (all the Secure Tokens of all the Merchants' Terminals) is made available to be used for payment by all the Merchants' Terminals. Disabled, leaves the configuration to Merchant Level.

**Merchant Settings**

Any merchant can choose between sharing its Secure Tokens among all of its Terminals, or not, using the following property:

- **Share all Secure Tokens:** When enabled, allows any Terminal from this specific Merchant to use Secure Tokens of its other Terminals to process transactions. When disabled, the sharing is not allowed and each Terminal can only use its own Secure Tokens.

However, if the Merchant is associated to a Merchant Portfolio with **Enable Token Auto Sharing** enabled, its **Share all Secure Tokens** is automatically enabled.

**Terminal Settings**

The most basic configuration required to use Secure Tokens features is the enabling of this feature at Terminal Level.

> **Warning**
> **SHARING AND REUSING SECURE TOKENS FROM DEACTIVATE TERMINALS** In case a Merchant has deactivated terminals, the Secure Tokens registered on it, by default, won't be available from the moment the terminal is deactivated onward. To avoid that a "Share Secure Tokens from deactivated terminals" feature was introduced, and can be enabled at Merchant Portfolio or Merchant level, when using one of the mentioned sharing options for Secure Tokens. If you have deactivated terminals with Secure Tokens and want to reuse them, contact our support team.

### Subscription

First of all, the Subscription feature requires the enabling of the **Secure Tokens** features to be used (and actual Secure Tokens registered).

Secondly, the Subscription feature itself needs to be enabled and the following items need to be informed.

| FIELD | DESCRIPTION |
|---|---|
| Subscription max wait for payment, days | Defines the amount of days a subscription's payment can be delayed before the system suspends the given subscription. |
| Subscriptions max missed periods | Defines the amount of times a subscription can miss payments before being suspended by the system. |
| Subscriptions payment notification, days | Defines the amount of days the system waits until sending the notification warning for a subscription which couldn't be paid. |
| Subscription missed periods notification | Defines the amount of times a subscription can miss payments before the system starts sending warning notifications about it. |
| Subscription repeat notification, days | Defines the amount of days the system waits until sending the next notification warning about a subscription which is still not paid. |
| Subscription auth max attempts | Defines the amount of authorization attempts the system will try before suspending an automatic subscription. |
