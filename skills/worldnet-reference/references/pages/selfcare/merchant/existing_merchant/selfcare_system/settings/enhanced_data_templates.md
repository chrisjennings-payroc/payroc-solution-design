<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:enhanced_data_templates | synced: 2026-10-05 -->

# Enhanced Data Templates

Once Enhanced Data feature is enabled for a Terminal, It's possible to configure Enhanced Data Templates.

The templates are an additional feature which allows merchants to predefined a set of generic data to be provided during authorization and settlement as part or all of a transaction's enhanced data.

The templates have four main ideas that you need to understand:

- **Platform default template**: you gateway might already have a default pre-defined template. You can see this template in your list (as above), but you can't change or deactivate this template. This template is going to be the base for the autofill feature.
- **The autofill feature**: when your terminal is configured with autofill, every transaction received by any channel (VT, Open Batch or Integrations) is going to receive the “default template”'s data where you din't inform anything. So say you sent a transaction without any enhanced data field and the terminal used has autofill enabled. In this case, the gateway is going to use the default teamplate's data (the platform's or yours, if you defined one for the terminal) to complete the missing data.
- **Terminal templates**: besides the platform default template (if existing), you can also define templates for terminals. If you define themplates, they are going to be available whenever you decide to sent or add enhanced data to a transaction. Also, you can define one of yout terminal's template as the default one for that terminal - in this case, the payment gateway is going to use the autofill with this template, instead of using the platform one.
- **Applying template manually before settlement**: anytime before settlement, during a transaction, using Virtual Terminal or XML Integrations, you can provide a template from which you want the data to be applied, if you don't use the autofill feature (or don't want to use it). You are going to be able to choose between the terminal's templates and even the platform template.

But before all of that, you need to define templates you might want to use for your transaction. So, here how It works:

- **1)** First you set up a name and define if this template is your default template or not.

**Template's General Details** Selfcaresettings-enhanceddatatemplates-general

- **2)** You define the details which go inside the template (the enhanced fields themselves, which can complement a transaction's enhanced data).

**Template's Enhanced Data Details** Selfcaresettings-enhanceddatatemplates-details

Once you provided these details, you can start using the template in Virtual Terminal, Open Batch or even XML Integrations.

If you have more question, please contact our support team.
