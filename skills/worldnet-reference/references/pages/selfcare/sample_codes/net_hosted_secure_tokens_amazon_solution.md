<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:net_hosted_secure_tokens_amazon_solution | synced: 2026-10-05 -->

# .NET Hosted Secure Tokens Amazon Solution

This solution requires our Card Storage solution called **SecureCard**. It's designed so that the checkout is like the Amazon checkout, in that the cardholder must register a card for their account and then they can use, update or delete the card info in their account settings. The integration is quite complex though, as there is a lot of functionality.

The first thing they will need to do is register their card.

Full documentation can be found in **[API Specification](https://developers.worldnetpayments.com/developer/api_specification)**.

If you are using an ACH integration, full documentation can be found in **[API Specification - ACH JH](https://developers.worldnetpayments.com/developer/api_specification_ach_jh)**.

Here is some sample code to help in this integration:

**The code for generating a HASH is:**

```

using System.Security.Cryptography;
using System.Text;
protected static String GetHash(String plainString)
{
    byte[] toBeHashed = System.Text.Encoding.UTF8.GetBytes(plainString);
    MD5CryptoServiceProvider cryptHandler = new MD5CryptoServiceProvider();
    byte[] hash = cryptHandler.ComputeHash(toBeHashed);
    String hashed = "";
    foreach (byte i in hash)
    {
        if (i < 16)
            hashed += "0" + i.ToString("x");
        else
            hashed += i.ToString("x");
    }
    return hashed;
}

```

**You should generate the “datetime” value using:**

```

System.DateTime.Now.ToString("dd-MM-yyyy:HH:mm:ss:fff");

```

You should then store the card token details as per the sample code. You can then in the future update the card details using the same sample code. You can also delete it using the “**XmlSecureCardDelRequest**” method in our **XML API**.

You may also require 3D Secure - refer to the 3D Secure section on the integration guide. In this case you will implement the 3D secure before the XML payment, and then include the MPIREF in the payment request.

When you want to pay using a card, you can do this by using this XML sample code. Note that you will have to use the “Card Reference” from before in place of the Card Number - you will not need to send the Expiry Date - and the Card Type will be “**SECURECARD**”, but the sample code takes care of all of this.
