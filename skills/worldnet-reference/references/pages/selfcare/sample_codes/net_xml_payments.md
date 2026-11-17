<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:sample_codes:net_xml_payments | synced: 2026-10-05 -->

# .NET XML Payments

The sample code below requires the **[.NET XML API](https://developers.worldnetpayments.com/_media/developer/sample_codes/worldnet-api-dotnet.zip)**.

**Authorisation:**

```
using System;
using System.Globalization;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class AuthorisationSample
    {
        static void Main (string[] args)
        {
            String terminalId = "";                        // Terminal ID
            String secret = "";                            // Shared Secret as configured in the Terminal Setup in your WorldNet Self Care System
            String currency = "";                          // EUR/GBP/USD etc.

            // These values are specific to the cardholder.
            String cardNumber = "";                        // The cardholders PAN (or SecureCard Card Reference);
            String trackData = "";                         // Track Data
            String encryptedTrack = "";                    // Encrypted Track for DukptCardDetails
            String ksn = "";                               // ksn for DukptCardDetails
            int? formatId = null;                          // formatId for DukptCardDetails
            String applePayload = "";                      // Apple Payload
            String androidPayload = "";                    // Android Payload
            String cardType = "";                          // See our Integrator Guide for a list of valid Card Type parameters
            String email = "";                             // (optional) Cardholders e-mail address for sending of a receipt
            String mobileNumber = "";                      // (optional) Cardholders mobile phone number for sending of a receipt. Digits only, Include international prefix.
            String cardExpiry = "";                        // Format: MMYY
            String cardHolderName = "";                    // Cardholders name
            String cvv = "";                               // (optional) 3 digit (4 for AMEX cards) security digit on the back of the card.
            String issueNo = "";                           // (optional) Issue number for Switch and Solo cards.

            // These fields are for AVS (Address Verification Check). This is only appropriate in the UK and the US.
            String address1 = "";                          // (optional) This is the first line of the cardholders address.
            String address2 = "";                          // (optional) This is the second line of the cardholders address.
            String postcode = "";                          // (optional) This is the cardholders post code.
            String country = "";                           // (optional) This is the cardholders country name.
            String phone = "";                             // (optional) This is the cardholders home phone number.

            // These values are specific to the transaction.
            String orderId = "";                           // Unique Order ID for the transaction (max 12 chars). Used to identify the transaction in future.
            Double amount = 1.00;                          // Amount of transaction (should include the decimal point and decimal places)
            Boolean isMailOrder = false;                   // If true the transaction will be processed as a Mail Order transaction. This is only for use with Mail Order enabled Terminal IDs.

            String description = "";                       // (optional) Transaction description

            // eDCC fields. Populate these if you have retreived a rate for the transaction, offered it to the cardholder and they have accepted that rate.
            String cardCurrency = "";                      // (optional) This is the three character ISO currency code returned in the rate request.
            Double? cardAmount = null;                     // (optional) This is the foreign currency transaction amount returned in the rate request.
            Double? conversionRate = null;                 // (optional) This is the currency conversion rate returned in the rate request.

            // 3D Secure reference. Only include if you have verified 3D Secure throuugh the WorldNet MPI and received an MPIREF back.
            String mpiref = "";                            // This should be blank unless instructed otherwise by WorldNet.
            String deviceId = "";                          // This should be blank unless instructed otherwise by WorldNet.

            String autoReady = "";                         // (optional) Y or N. Automatically set the transaction to a status of Ready in the batch. If not present the terminal default will be used.
            Boolean multicur = false;                      // This should be false unless instructed otherwise by WorldNet.

            String billToFirstName = "";                   // BillTo FirstName
            String billTolastName = "";                    // BillTo LastName
            String xid = "";                               // XID
            String cavv = "";                              // CAVV
            String city = "";                              // CITY
            String region = "";                            // REGION
            String ipAddress = "";                         // IPADDRESS
            String signature = "";                         // SIGNATURE
            IList<CustomField> customFields = new List<CustomField> (); // CustomFields
            //customFields.Add ("name1", "value1"));
            //customFields.Add ("name2", "value2"));
            String recurringTxnRef = "";                   // RECURRING TXN REF

            Boolean testAccount = true;

            XmlAuthRequest request = new XmlAuthRequest (terminalId, orderId, currency, amount, cardType);

            if (!String.IsNullOrEmpty (trackData)) {
                request.SetTrackData (trackData);
            } else if (!String.IsNullOrEmpty (encryptedTrack) && !String.IsNullOrEmpty (ksn) && formatId.HasValue) {
                request.SetDukptCardDetails (encryptedTrack, ksn, formatId.Value);
            } else if (!String.IsNullOrEmpty (applePayload)) {
                request.SetApplePayload (applePayload);
            } else if (!String.IsNullOrEmpty (androidPayload)) {
                request.SetAndroidPayload (androidPayload);
            } else {
                request.SetCardNumber (cardNumber);
            }
            if (!String.IsNullOrEmpty (cardExpiry) && !String.IsNullOrEmpty (cardHolderName)) {
                request.SetNonSecureCardCardInfo (cardExpiry, cardHolderName);
            }
            if (!String.IsNullOrEmpty (cvv)) {
                request.SetCvv (cvv);
            }
            if (!String.IsNullOrEmpty (cardCurrency) && cardAmount.HasValue && conversionRate.HasValue) {
                request.SetForeignCurrencyInformation (cardCurrency, cardAmount.Value, conversionRate.Value);
            }
            if (!String.IsNullOrEmpty (email)) {
                request.SetEmail (email);
            }
            if (!String.IsNullOrEmpty (mobileNumber)) {
                request.SetMobileNumber (mobileNumber);
            }
            if (!String.IsNullOrEmpty (description)) {
                request.SetDescription (description);
            }

            if (!String.IsNullOrEmpty (issueNo)) {
                request.SetIssueNo (issueNo);
            }
            if (!String.IsNullOrEmpty (address1) && !String.IsNullOrEmpty (postcode)) {
                request.SetAvs (address1, address2, postcode);
            }
            if (!String.IsNullOrEmpty (country)) {
                request.SetCountry (country);
            }
            if (!String.IsNullOrEmpty (phone)) {
                request.SetPhone (phone);
            }

            if (!String.IsNullOrEmpty (deviceId)) {
                request.SetDeviceId (deviceId);
            }
            if (!String.IsNullOrEmpty (mpiref)) {
                request.SetMpiRef (mpiref);
            }
            if (!String.IsNullOrEmpty (billToFirstName)) {
                request.SetBillToFirstName (billToFirstName);
            }
            if (!String.IsNullOrEmpty (billTolastName)) {
                request.SetBillTolastName (billTolastName);
            }
            if (!String.IsNullOrEmpty (xid)) {
                request.SetXid (xid);
            }
            if (!String.IsNullOrEmpty (cavv)) {
                request.SetCavv (cavv);
            }
            if (!String.IsNullOrEmpty (city)) {
                request.SetCity (city);
            }
            if (!String.IsNullOrEmpty (region)) {
                request.SetRegion (region);
            }
            if (!String.IsNullOrEmpty (ipAddress)) {
                request.SetIpAddress (ipAddress);
            }
            if (!String.IsNullOrEmpty (signature)) {
                request.SetSignature (signature);
            }
            if (customFields != null && customFields.Count != 0) {
                request.SetCustomFields (customFields);
            }
            if (!String.IsNullOrEmpty (recurringTxnRef)) {
                request.SetRecurringTxnRef (recurringTxnRef);
            }

            if (isMailOrder) {
                request.SetMotoTrans ();
            }
            if (multicur) {
                request.SetMultiCur ();
            }
            if (!String.IsNullOrEmpty (autoReady)) {
                request.SetAutoReady (autoReady);
            }

            XmlAuthResponse response = request.ProcessRequest(secret, testAccount);

            String expectedResponseHash = Response.GetResponseHash(terminalId + response.UniqueRef + ((multicur) ? currency : "") + amount.ToString(CultureInfo.InvariantCulture) + response.DateTimeHashString + response.ResponseCode + response.ResponseText + response.BankResponseCode + secret);

            if (response.IsError == true)
            {
                Console.Out.WriteLine("ERROR : " + response.ErrorString);
                //Handle Error Response
            }
            else if (response.Hash != expectedResponseHash)
            {
                Console.Out.WriteLine("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            }
            else
            {
                Console.Out.WriteLine("RESPONSECODE : " + response.ResponseCode);
                if (response.ResponseCode.Equals("A"))
                {
                    //Handle success response
                }
                else
                {
                    //Handle declined response
                }
                Console.Out.WriteLine("RESPONSETEXT : " + response.ResponseText);
                Console.Out.WriteLine("APPROVALCODE : " + response.ApprovalCode);
                Console.Out.WriteLine("BANKRESPONSECODE : " + response.BankResponseCode);
                Console.Out.WriteLine("DATETIME : " + response.DateTimeHashString);
                Console.Out.WriteLine("AVSRESPONSE : " + response.AvsResponse);
                Console.Out.WriteLine("CVVRESPONSE : " + response.CvvResponse);
                Console.Out.WriteLine("UNIQUEREF : " + response.UniqueRef);
                Console.Out.WriteLine("HASH : " + response.Hash);
                //Handle Response
            }
        }
    }
}

```

**Perform a Refund** (standard refunds can only be performed against authorised sale transactions that have already been put through the same account system. Also, the Order ID of the original sale must be unique.):

```

using System;
using System.Globalization;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using $GatewayClient;

namespace ApiTest
{
    class RefundSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";        // Gateway that will process the transaction.
            String terminalId = "";        // Terminal ID
            String uniqueRef = "";  // Unique Reference of the transaction that you are looking to refund. This was returned in the auth response
            String orderId = "";        // Unique Order ID for the transaction (max 12 chars). Used to identify the transaction in future.
            Double amount = 10.0;            // Amount of transaction
            String operatorName = "";        // Administrative operator performing the refund
            String reason = "";            // The reason why the refund was necessary
            String autoReady = "";        // (optional) Y or N. Automatically set the transaction to a status of Ready in the batch. If not present the terminal default will be used.
            String secret = "";            // Shared Secret as configured in the Terminal Setup in your Worldnet SelfCare System

            Boolean testAccount = true;

            XmlRefundRequest request = new XmlRefundRequest (terminalId, amount, operatorName, reason);

            if (!String.IsNullOrEmpty (uniqueRef)) {
                request.SetUniqueRef (uniqueRef);
            } else {
                request.SetOrderID (orderId);
            }

            if (!String.IsNullOrEmpty (autoReady)) {
                request.SetAutoReady (autoReady);
            }

            XmlRefundResponse response = request.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (terminalId + response.UniqueRef + amount.ToString (CultureInfo.InvariantCulture) + response.DateTimeHashString + response.ResponseCode + response.ResponseText + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("RESPONSECODE : " + response.ResponseCode);
                if (response.ResponseCode.Equals ("A")) {
                    //Handle success response
                } else {
                    //Handle declined response
                }
                Console.Out.WriteLine ("RESPONSETEXT : " + response.ResponseText);
                Console.Out.WriteLine ("DATETIME : " + response.DateTimeHashString);
                Console.Out.WriteLine ("HASH : " + response.Hash);
                //Handle Response
            }
        }
    }
}

```

**Perform a eDCC rate request:**

```

using System;
using System.Globalization;
using System.Security.Cryptography;
using System.Collections.Generic;
using System.Text;
using WorldNetClient;

namespace ApiTest
{
    class EdccRateSample
    {
        static void Main (string[] args)
        {
			String gateway = "worldnet";        // Gateway that will process the transaction.
			String terminalId = "";        // Terminal ID
            String cardBin = "";        // First 6 digits of the card number
            Double? baseAmount = null;  // (optional) Amount of transaction in the base currency. If included the host will calculate and return the foreign currency amount
            String secret = "";         // Shared Secret as configured in the Terminal Setup in your Worldnet SelfCare System

            Boolean testAccount = true;

            XmlRateRequest request = new XmlRateRequest (terminalId, cardBin);

            if (baseAmount != null) {
                request.SetBaseAmount (baseAmount.Value);
            }

            XmlRateResponse response = request.ProcessRequest (secret, testAccount, gateway);

            String expectedResponseHash = Response.GetResponseHash (response.TerminalCurrency + response.CardCurrency + response.ConversionRate.ToString (CultureInfo.InvariantCulture) + response.DateTimeHashString + secret);

            if (response.IsError == true) {
                Console.Out.WriteLine ("ERROR : " + response.ErrorString);
                //Handle Error Response
            } else if (response.Hash != expectedResponseHash) {
                Console.Out.WriteLine ("ERROR : Response HASH parameter not as expected. If live possible man-in-the-middle attack.");
                //Handle Invalid Hash scenario - inform merchant that transaction may have to be voided.
            } else {
                Console.Out.WriteLine ("TERMINALCURRENCY : " + response.TerminalCurrency);
                Console.Out.WriteLine ("CARDCURRENCY : " + response.CardCurrency);
                Console.Out.WriteLine ("CONVERSIONRATE : " + response.ConversionRate.ToString (CultureInfo.InvariantCulture));
                Console.Out.WriteLine ("EXCHANGERATESOURCENAME : " + response.ExchangeRateSourceName);
                Console.Out.WriteLine ("MARGINPERCENTAGE : " + response.MargineRatePercentage);
                Console.Out.WriteLine ("COMMISSIONPERCENTAGE : " + response.CommissionPercentage);
                Console.Out.WriteLine ("FOREIGNAMOUNT : " + response.ForeignAmount.ToString (CultureInfo.InvariantCulture));
                Console.Out.WriteLine ("DATETIME : " + response.DateTimeHashString);
                Console.Out.WriteLine ("HASH : " + response.Hash);
                //Handle Response
            }
        }
    }
}

```
