<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:net_hosted_payments | synced: 2026-10-05 -->

# .NET Hosted Payment

You can find below a high and a low level workflow diagram of the required integration.

Full documentation is available in **[API Specification](https://developers.worldnetpayments.com/developer/api_specification)**. You should also use our Sandbox test accounts **[Sandbox testing](https://developers.worldnetpayments.com/selfcare/integration_docs/sandbox_testing)** to test against.

[ High Level Workflow](https://developers.worldnetpayments.com/_media/developer/sample_codes/workflow-integratingtohostedpaymentpage-highlevel.pdf)

[ Low Level Workflow](https://developers.worldnetpayments.com/_media/developer/sample_codes/workflow-integratingtohostedpaymentpage-lowlevel.pdf)

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
