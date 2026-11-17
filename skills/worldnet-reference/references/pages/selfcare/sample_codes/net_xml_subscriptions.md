<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:net_xml_subscriptions | synced: 2026-10-05 -->

# .NET XML Subscriptions

The sample code below requires the **[.NET XML API](https://developers.worldnetpayments.com/_media/developer/sample_codes/worldnet-api-dotnet.zip)**.

**Subscription registration:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class  SubscriptionRegistrationSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";        // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";                // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System
            Boolean testAccount = true;

            String subscriptionMerchantRef = "";    // Unique merchant identifier for the subscription. Length is limited to 48 chars.
            String storedSubscriptionMerchantRef = "";    // Merchant reference for the Stored Subscription under which this Subscription is to be created.
            String secureCardMerchantRef = "";        // Merchant reference for the SecureCard entry that you want to use to set up the subscription.
            String cardReference = "";        // Card Reference for the SecureCard entry that you want to use to set up the subscription.
            DateTime? subscriptionStartDate = new DateTime (2010, 4, 18);    // Date on which the subscription should start (setup payment is processed immediately, and does not obey this). Format: DD-MM-YYYY.

            DateTime? endDate = new DateTime (2018, 8, 18);                // (optional) set an end date for the subscription.  Format: DD-MM-YYYY.
            String eDCCDecision = "";            // (optional) if eDCC was offered and accepted, you should set this to 'Y'.

            String name = "";                // (optional)
            String description = "";            // (optional)
            String periodType = "";            // (optional)
            int length = -1;                // (optional)
            String currency = "EUR";            // (optional)
            double recurringAmount = -1.00;        // (optional)
            double initialAmount = -1.00;        // (optional)
            String type = "";                // (optional)
            String onUpdate = "";            // (optional)
            String onDelete = "";            // (optional)

            IList<CustomField> customFields = new List<CustomField> (); // CustomFields
            //customFields.Add (new CustomField ("name1", "value1"));
            //customFields.Add (new CustomField ("name2", "value2"));

            XmlSubscriptionRegRequest subreg = new XmlSubscriptionRegRequest (subscriptionMerchantRef, terminalId, storedSubscriptionMerchantRef, subscriptionStartDate.Value);

            if (!String.IsNullOrEmpty (secureCardMerchantRef)) {
                subreg.SetSecureCardMerchantRef (secureCardMerchantRef);
            } else {
                subreg.SetCardReference (cardReference);
            }

            if (!String.IsNullOrEmpty (name) || !String.IsNullOrEmpty (description) || !String.IsNullOrEmpty (periodType) || length > 0 || !String.IsNullOrEmpty (type) || !String.IsNullOrEmpty (onUpdate) || !String.IsNullOrEmpty (onDelete)) {
                subreg.SetNewStoredSubscriptionValues (name, description, periodType, length, currency, recurringAmount, initialAmount, type, onUpdate, onDelete);
            } else if (recurringAmount > 0 || initialAmount > 0) {
                subreg.SetSubscriptionAmounts (recurringAmount, initialAmount);
            }
            if (endDate.HasValue)
                subreg.SetEndDate (endDate.Value);
            if (!String.IsNullOrEmpty (eDCCDecision))
                subreg.SetEdccDecision (eDCCDecision);
            if (customFields != null && customFields.Count != 0) {
                subreg.SetCustomFields (customFields);
            }

            XmlSubscriptionRegResponse response = subreg.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantReference + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("Subscription successfully setup and setup payment processed succesfully.");
                //Handle Response
            }
        }
    }
}

```

**Subscription update:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class SubscriptionUpdateSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";        // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";                // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System
            Boolean testAccount = true;

            String subscriptionMerchantRef = "";    // Unique merchant identifier for the subscription. Length is limited to 48 chars.
            String secureCardMerchantRef = "";        // Merchant reference for the SecureCard entry that you want to use to set up the subscription.
            String cardReference = "";        // Card Reference for the SecureCard entry that you want to use to set up the subscription.

            DateTime? subscriptionStartDate = new DateTime (2010, 4, 18);    // (optional) Date on which the subscription should start (setup payment is processed immediately, and does not obey this). Format: DD-MM-YYYY.
            DateTime? endDate = new DateTime (2018, 8, 18);                // (optional) set an end date for the subscription.  Format: DD-MM-YYYY.
            String eDCCDecision = "";            // (optional) if eDCC was offered and accepted, you should set this to 'Y'.

            String name = "";                // (optional)
            String description = "";            // (optional)
            int length = -1;                // (optional)
            int skipPeriodCount = -1;   // (optional)
            double recurringAmount = -1.00;        // (optional)

            IList<CustomField> customFields = new List<CustomField> (); // CustomFields
            //customFields.Add (new CustomField ("name1", "value1"));
            //customFields.Add (new CustomField ("name2", "value2"));

            XmlSubscriptionUpdRequest subupd = new XmlSubscriptionUpdRequest (subscriptionMerchantRef, terminalId);

            if (!String.IsNullOrEmpty (secureCardMerchantRef)) {
                subupd.SetSecureCardMerchantRef (secureCardMerchantRef);
            } else {
                subupd.SetCardReference (cardReference);
            }
            if (!String.IsNullOrEmpty (name))
                subupd.SetSubName (name);
            if (!String.IsNullOrEmpty (description))
                subupd.SetDescription (description);
            if (length > 0)
                subupd.SetLength (length);
            if (skipPeriodCount > 0)
                subupd.SetSkipPeriodCount (skipPeriodCount);
            if (recurringAmount > 0)
                subupd.SetRecurringAmount (recurringAmount);
            if (subscriptionStartDate.HasValue)
                subupd.SetStartDate (subscriptionStartDate.Value);
            if (endDate.HasValue)
                subupd.SetEndDate (endDate.Value);
            if (!String.IsNullOrEmpty (eDCCDecision))
                subupd.SetEDCCDecision (eDCCDecision);
            if (customFields != null && customFields.Count != 0) {
                subupd.SetCustomFields (customFields);
            }

            XmlSubscriptionUpdResponse response = subupd.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantReference + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("Subscription successfully updated.");
                //Handle Response
            }
        }
    }
}
```

**Subscription deletion:**

```

using System;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class SubscriptionDeletionSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";       // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String secret = "";                // Shared Secret as configured in the Terminal Setup in your Worldnet Selfcare System
            Boolean testAccount = true;

            String subscriptionMerchantRef = "";    // Unique merchant identifier for the subscription. Length is limited to 48 chars.

            XmlSubscriptionDelRequest subdel = new XmlSubscriptionDelRequest (subscriptionMerchantRef, terminalId);
            XmlSubscriptionDelResponse response = subdel.ProcessRequest (secret, testAccount, gateway);
            String expectedResponseHash = Response.GetResponseHash (terminalId + response.MerchantReference + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("Subscription successfully deleted.");
                //Handle Response
            }
        }
    }
}

```
