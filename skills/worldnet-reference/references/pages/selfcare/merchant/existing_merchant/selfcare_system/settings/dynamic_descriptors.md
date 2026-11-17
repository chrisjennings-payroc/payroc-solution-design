<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:dynamic_descriptors | synced: 2026-10-05 -->

# Dynamic Descriptors

## How it Works

### Descriptors

Transaction descriptors describe a particular payment in order to help to identify that transaction on a bank statement or online bank interface. A good practice to help minimize the risk of charge-back and in turn, to save money! Provide your customers with your brand name and contact information to help them recognize their purchase, that’s all it takes to make descriptors work for your business.

### Dynamic Descriptors

These type of descriptors describe a specific product or service and can vary from one merchant to another. If your website sells applications or software services, this type of descriptor can be a great way to let your customers know what they bought. Usually customers know the name of an application they purchased and they will therefore recognize that name on their bank statement.

The text that appears on the cardholders statement will be made up of:

1. A “Prefix”, which is a static text value up to 12 characters long that is the same for every transaction followed by.
1. The dynamic value, which is sent in by the website with the transaction. Length is detailed in pseudo-code below.

If there is no dynamic value sent with the transaction then we also store a “default” value that will be displayed instead of the combination above.

### Support and Activation

Currently Dynamic Descriptors is only available on terminals with TSYS Saratoga acquirer. They are available on XML, Hosted Payment Page and Virtual Terminal transactions. The REST interface does not support this feature.

### Merchant Request

If required, the merchant must raise a support ticket to request that this feature be enabled on their Terminal ID. We will require 3 values to be able to enable this:

1. The Terminal ID that it is to be enabled on.
1. The “Prefix” string up to 12 characters long.
1. The “Default” string up to 25 characters long.

### Overview of Implementation

#### Merchant Access & Configuration

Dynamic Descriptors are implemented using Worldnet Payments s “custom fields” functionality. When the feature is enabled on the terminal ID any user that has “Terminal Setup” permissions, and therefore access to the Settings ⇒ Custom Fields control panel

A new section for the Dynamic Descriptors is shown on the Custom Fields control panel. This will allow the user to assign the desired custom field to be the Dynamic Descriptor. A single custom field may be used by all possible integrations (Example above), or a different custom field can be set per different integration method. Note that “Other” will cover the XML gateway.

#### Implementation/Integration

As stated above, the dynamic value for the transaction must be sent along with the transaction parameters as a custom fields with the correct name, as defined by the merchant when they configured the Dynamic Descriptors. Please refer to the Integrator Guide document for details about how to send custom fields with transactions.

#### Logic Flow

The logic of how Dynamic Descriptors are handled by our host is described in this pseudo-code:

```
if (Terminal ID allows Dynamic Descriptors)
    if (Correct custom field is sent and valid)
        Set the Dynamic Descriptor to the Prefix value followed by a “*” character and then the sent custom field value, and then truncated to a maximum of 29  characters.
    else if (custom field is no sent or valid)
        Set the Dynamic Descriptor to the Prefix value followed by a “*” character and then the defined Default value, and then truncated to a maximum of 29 characters.
end if
```

**PAYFAC**

When using PayFac, the Dynamic Descriptors become mandatory (prefix and default values also). For those terminals with payfac enabled, only the first 3 (three) characters of prefix are used with the Dynamic Descriptor.

A valid custom field value in not blank and contains only letters numbers and spaces.

#### Examples

Dynamic Descriptor Prefix= “**Order N**” Dynamic Descriptor Default = “StoreName” Custom Field value = “**1234**”

- a) If a transaction is sent with custom field “1234”, and Payfac is not enabled, the result would be: Order N*1234.
- b) If a transaction is sent with custom field “1234”, and Payfac is enabled, the result would be: Ord*1234.
- c) If a transaction is sent with no custom field, and Payfac is not enabled, the result would be: Order N*Storename.
- d) If a transaction is sent with no custom field, and Payfac is enabled, the result would be: Ord*Storename.

```
<html>
    </div>
  </div>
</html>
```
