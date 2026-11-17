<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:update_guide_1_6_0 | synced: 2026-10-05 -->

# SDK Version 1_6_0 - Update Guide

Please find below the detailed descriptions of the major changes we included in the new SDK Version 1_6_0.

### Summary

1. [API Key](#1)
1. [Date Time Type](#2)
1. [Reversals](#3)
1. [Reversals and Refunds](#4)
1. [Transaction Search](#5)
1. [Dependencies](#6)

## API Key

The first major change we made within Version 1_6_0 was to improve the security on our terminals. We have introduced a new authentication method in place of the `Terminal ID` and the `Secret`.

This is now done using an API Key which is a random 128 character string and grants you access to all functionalities of the SDK.

> **Note**
> Before proceeding, please check the [Authentication Guide](doku.php?id=gochip:support:authentication) to generate your API Key.

## Date | Time Type

The next change we have included is how we handle the Date and the Time. We have replaced a method where the date and time fields were stored within the SDK as a string. Instead now these fields are native date and time objects on each supported platform:

Using the new API this new method for the Date and Time can deliver results based on the user’s time zone.

Classes and fields affected by this changes:

- CoreResponse

  - dateTime
- CoreFilter

  - startDate
  - endDate
- CoreTransactionSummary

  - transactionDate
- CoreTransactionReports

  - dateTime
  - settlementDate

- C#
- Java
- ObjC

```

C# : System.DateTime

```

```

Java/Android : java.util.Date

```

```

ObjC (iOS) : NSDate

```

## Reversals

The next major change we have made is how the SDK handles transaction Reversals. Reversals will now return a `CoreSaleResponse`.

Within the payment industry there is a fundamental difference between Reversals and Refunds. **Reversals** update the initial transaction amount while **Refunds** are new transactions and return a specific amount to the cardholder.

This means that if a Reversal is processed the cardholder will see only one transaction in their statement with the final amount that the card has been charged.

If a Refund is processed then the cardholder will see 2 transactions on their statement, one with the original sale and then another transaction with the amount returned to the cardholder.

Therefore, our new approach to the handling of the Reversal callback **(`onReversalRetrieved`)** will return the same payment details from the original sale but with the final amount.

## Reversals and Refunds

With this new approach we also changed the Refund callback **(`OnRefundResponse`)** so that we could keep the same behavior from the previous versions:

- If a Refund is not possible, a Reversal will be processed instead.

This method will now receive either a CoreRefundResponse or a CoreSaleResponse based on the action taken. In other words, if a reversal is processed the callback will receive a CoreSaleResponse, if a refund is processed then CoreRefundResponse is received.

## Transaction Search

The handling of Transaction Reporting and Transaction Data has also seen a change within Version 1_6_0.

### Transaction Reporting

The Transaction Reporting is now done using the `UniqueRef` of the next transaction that will be delivered. This field is delivered on the callback **`onTransactionListResponse`** inside the CoreTransactions.next object.

For convenience, this field is also set in the `CoreFilter.next` object sent on the method` getTransactions`. So, to get the next page, you can just do another request to the` getTransactions` method with the same instance of the `CoreFilter`, as the field `next` will be populated with the correct value after the first one.

> **Note**
> It is up to the developer to keep track of the UniqueRef values sent on the CoreTransactions.next in case they want to go back for the previous page.

### Transaction Data

The information retrieved in the **CoreTransactionSummary** has been reduced so we can delivered more results per page without overloading the response message.

In addition to this change, we also provide a new method **getTransaction** which receives a transaction `UniqueRef` as parameter and returns a `CoreSaleResponse` on the callback `onTransactionRetrieved`.

Using both methods is possible to search and retrieve any transaction processed in the past 18 months.

Current information delivered on a `CoreTransactionSummary`:

- Terminal ID
- Order ID
- Unique Ref
- Amount
- Currency
- Cardholder Name
- Masked Card Number
- Transaction Date
- Transaction Status
- Transaction Type
- Description
- Result Code

## Dependencies

We have made changes to the SDK dependecies within Version 1_6_0.

In previous versions (1_5_x), the Java / Android version of the SDK was dependent on gson.jar and the C# version on NewtonJson and HashLib dlls.

Since Version 1_6_0 of the SDK is now based on the [OpenAPI](https://swagger.io/specification/) specification, we have had to introduce some additional dependencies.

- Java dependencies:

```
converter-gson-2.3.0.jar
converter-scalars-2.3.0.jar
gson-2.8.2.jar
gson-fire-1.8.0.jar
javax.annotation-api-1.3.2.jar
jsr305-3.0.2.jar
okhttp-3.8.0.jar
okio-1.13.0.jar
org.apache.oltu.oauth2.client-1.0.1.jar
retrofit-2.3.0.jar
slf4j-api-1.7.7.jar
swagger-annotations-1.5.22.jar
```

- C# dependencies

```
HashLib.dll 2.0.1
JsonSubTypes.dll 1.6.0
Newtonsoft.Json.dll 12.0.3
RestSharp.dll 105.1.0
```

All of the above dependencies can be found under `/dependencies` directory after extracting `gochipSDK.zip`. Once extracted, include them in your project.

If your project already contains one of the above libraries please make sure you are using the correct version.

> **Note**
> On Android and Java you might get duplicate classes error if any of your existing dependencies already contains the library.

To resolve the issue, you can exclude the affected `.jar` from your libs directory.   Alternatively, find the gradle dependency and exclude the duplicated modules. For example:

- Request

```

implementation ('com.squareup.retrofit2:retrofit:2.6.1') {
exclude module: 'okhttp'
}

```
