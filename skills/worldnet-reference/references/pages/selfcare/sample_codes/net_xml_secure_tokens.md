<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:net_xml_secure_tokens | synced: 2026-10-05 -->

# .NET XML Secure Tokens

The sample code below requires the **[.NET XML API](https://developers.worldnetpayments.com/_media/developer/sample_codes/worldnet-api-dotnet.zip)**.

**SecureCard registration:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class SecureCardRegistrationSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";       // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";            // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System

            String secureCardMerchantRef = "";    // Unique Merchant Reference. Length is limited to 48 chars.
            String cardNumber = "";        // The cardholders PAN (or SecureCard Card Reference);
            String cardType = "";        // See our Integrator Guide for a list of valid Card Type parameters
            String cardExpiry = "";        // Format: MMYY
            String cardHolderName = "";        // Cardholders name

            String dontCheckSecurity = "";    // (optional) "Y" if you do not want the CVV to be validated online.
            String cvv = "";            // (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.
            String issueNo = "";        // (optional) Issue number for Switch and Solo cards.

            IList<String> permittedTerminals = new List<String> (); // PERMITTED TERMINALS
            //permittedTerminals.Add ("1002");
            //permittedTerminals.Add ("1009");
            IList<CustomField> customFields = new List<CustomField> (); // CustomFields
            //customFields.Add ("name1", "value1"));
            //customFields.Add ("name2", "value2"));

            Boolean testAccount = true;

            XmlSecureCardRegRequest securereg = new XmlSecureCardRegRequest (secureCardMerchantRef, terminalId, cardNumber, cardExpiry, cardType, cardHolderName);

            if (!String.IsNullOrEmpty (dontCheckSecurity)) {
                securereg.SetDontCheckSecurity (dontCheckSecurity);
            }
            if (!String.IsNullOrEmpty (cvv)) {
                securereg.SetCvv (cvv);
            }
            if (!String.IsNullOrEmpty (issueNo)) {
                securereg.SetIssueNo (issueNo);
            }
            if (permittedTerminals != null && permittedTerminals.Count != 0) {
                securereg.SetPermittedTerminals (permittedTerminals);
            }
            if (customFields != null && customFields.Count != 0) {
                securereg.SetCustomFields (customFields);
            }

            XmlSecureCardRegResponse response = securereg.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantRef + response.CardRef + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("SecureCard successfully stored.");
                Console.Out.WriteLine ("CARDREFERENCE : " + response.CardRef);
                //Handle Response
            }
        }
    }
}
```

**SecureCard record update:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class  SecureCardRecordUpdateSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";       // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";            // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System

            String secureCardMerchantRef = "";    // Unique Merchant Reference. Length is limited to 48 chars.
            String cardNumber = "";        // The cardholders PAN (or SecureCard Card Reference);
            String cardType = "";        // See our Integrator Guide for a list of valid Card Type parameters
            String cardExpiry = "";        // Format: MMYY
            String cardHolderName = "";        // Cardholders name

            String dontCheckSecurity = "";    // (optional) "Y" if you do not want the CVV to be validated online.
            String cvv = "";            // (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.
            String issueNo = "";        // (optional) Issue number for Switch and Solo cards.

            IList<String> permittedTerminals = new List<String> (); // PERMITTED TERMINALS
            //permittedTerminals.Add ("1003");
            //permittedTerminals.Add ("1013");
            IList<CustomField> customFields = new List<CustomField> (); // CustomFields
            //customFields.Add (new CustomField ("name1", "value1"));
            //customFields.Add (new CustomField ("name2", "value2"));

            Boolean testAccount = true;

            XmlSecureCardUpdRequest secureupd = new XmlSecureCardUpdRequest (secureCardMerchantRef, terminalId, cardNumber, cardExpiry, cardType, cardHolderName);

            if (!String.IsNullOrEmpty (dontCheckSecurity)) {
                secureupd.SetDontCheckSecurity (dontCheckSecurity);
            }
            if (!String.IsNullOrEmpty (cvv)) {
                secureupd.SetCvv (cvv);
            }
            if (!String.IsNullOrEmpty (issueNo)) {
                secureupd.SetIssueNo (issueNo);
            }
            if (permittedTerminals != null && permittedTerminals.Count != 0) {
                secureupd.SetPermittedTerminals (permittedTerminals);
            }
            if (customFields != null && customFields.Count != 0) {
                secureupd.SetCustomFields (customFields);
            }

            XmlSecureCardUpdResponse response = secureupd.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantRef + response.CardRef + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("SecureCard successfully updated.");
                //Handle Response
            }
        }
    }
}

```

**SecureCard record deletion:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using $GatewayClient;

namespace ApiTest
{
    class SecureCardRecordDeletionSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";        // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";            // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System

            String secureCardMerchantRef = "";    // Unique Merchant Reference. Length is limited to 48 chars.
            String secureCardCardRef = "";    // This is the Worldnet generated 16 digit card number token

            Boolean testAccount = false;

            XmlSecureCardDelRequest securedel = new XmlSecureCardDelRequest (secureCardMerchantRef, terminalId, secureCardCardRef);
            XmlSecureCardDelResponse response = securedel.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantRef + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("SecureCard successfully deleted.");
                //Handle Response
            }
        }
    }
}

```

**SecureCard Search:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class SecureCardSearchSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";        // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";            // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System

            String secureCardMerchantRef = "";    // Unique Merchant Reference. Length is limited to 48 chars.

            Boolean testAccount = true;

            XmlSecureCardSearchRequest securesearch = new XmlSecureCardSearchRequest (secureCardMerchantRef, terminalId);
            XmlSecureCardSearchResponse response = securesearch.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantRef + response.CardRef + response.CardType + response.CardExpiry + response.CardHolderName + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("SecureCard successfully found.");
                Console.Out.WriteLine ("MERCHANTREF : " + response.MerchantRef);
                Console.Out.WriteLine ("CARDREFERENCE : " + response.CardRef);
                Console.Out.WriteLine ("CARDTYPE : " + response.CardType);
                Console.Out.WriteLine ("CARDEXPIRY : " + response.CardExpiry);
                Console.Out.WriteLine ("CARDHOLDERNAME : " + response.CardHolderName);
                //Handle Response
            }
        }
    }
}
```
