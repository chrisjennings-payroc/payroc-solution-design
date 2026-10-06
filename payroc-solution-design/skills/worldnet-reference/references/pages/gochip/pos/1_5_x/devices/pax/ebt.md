<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:1_5_x:devices:pax:ebt | synced: 2026-10-05 -->

# EBT Sample requests [BACK TO PAX](doku.php?id=gochip:pos:devices:pax)

EBT sample requests are described below. For more information please check our sample app.

### EBT Cash

- **Operator** and **deviceID** fields are required and can be used later on for reporting.
- **DeviceID** can be set as “serial number” of the device which will be returned in **onDeviceConnected** callback method
-

Once the card has been swiped, **onRequestPin** callback will be triggered whenever the device asks for PIN with the following enum types, which can be used to display dialog with edit text field (to display * whenever the pin character was added).

```

/**
* Display prompt
*/
PIN_STARTED,
/**
* Pin character was added
*/
CHARACTER_ADDED,
/**
* Pin character was removed
*/
CHARACTER_REMOVED,
/**
* Dismiss prompt
*/
PIN_FINISHED;

```

 Once the pin gets confirmed the transaction gets processed and the transaction response will be returned in **onSaleResponse** callback method.

- Request

```

CoreSaleEbt ebt = new CoreSaleEbt(amount);
ebt.setCardAccount(CardAccount.CASH);
ebt.setOperator("operator");
ebt.setDeviceId("1234567");
ebt.setSaleRequestType(SaleRequestType.PURCHASE);
AndroidTerminal.getInstance().processSale(ebt);

```

#### Keyed

1. Once the transaction has been started, the card number should be submitted using the following method: `AndroidTerminal.getInstance().submitCardNumber(cardNum);`
1. **onRequestExpiryDate** callback method will be triggered. The expiry date should be submitted using the following method: `AndroidTerminal.getInstance().submitExpiryDate(expiryDate);`
1.

**onRequestPin** callback will be triggered whenever the device asks for PIN with the following enum types, which can be used to display dialog with edittext (to display * whenever the pin character was added).

```

                /**
                * Display prompt
                */
                PIN_STARTED,
                /**
                * Pin character was added
                */
                CHARACTER_ADDED,
                /**
                * Pin character was removed
                */
                CHARACTER_REMOVED,
                /**
                * Dismiss prompt
                */
                PIN_FINISHED;

```

- Request

```

CoreSaleEbt ebt = new CoreSaleEbt(amount);
ebt.setCardAccount(CardAccount.CASH);
ebt.setOperator("operator");
ebt.setDeviceId("1234567");
ebt.setSaleRequestType(SaleRequestType.PURCHASE);
AndroidTerminal.getInstance().processSale(ebt);

```

   Once the pin gets confirmed the transaction gets processed and the transaction response will be returned in **onSaleResponse** callback method.

### Cash Back

To process EBT cash back transaction the CoreSaleEbt request should contain ` **Cashback** field: ebt.setCashBackAmount(BigDecimal.ONE); `

### EBT Food

#### Swipe/ Keyed

EBT Food Swipe/Keyed To process EBT food transaction, the CoreSaleEbt request **cardAccount** field should ` be set to **FOOD_STAMP**: coreSale.setCardAccount(CardAccount.FOOD_STAMP); `

### Cash Withdraw

#### Swipe/ Keyed

- To process EBT cash withdrawal transaction, the CoreSaleEbt request **cardAccount** field should be set to **CASH** and **saleRequestType** should be set to **CASH_WITHDRAWAL**. ` coreSale.setCardAccount(CardAccount.CASH); coreSale.setSaleRequestType(SaleRequestType.CASH_WITHDRAWAL); `

```

```

### EBT Food Voucher

#### Purchase

This EBT payment type doesn’t involve card processing but it is a type of a transaction which requires to input the voucher details and process the purchase transaction using the SDK.}

- Request

```

CoreVoucher voucher = new CoreVoucher();
voucher.setCardAccount(CardAccount.FOOD_STAMP);
voucher.setVoucherApprovalCode("123456");
voucher.setVoucherNumber("123456789012345");
voucher.setCardNumber("6007602801003837968");
((CoreSaleEbt) coreSale).setVoucher(voucher);
coreSale.setSaleRequestType(SaleRequestType.PURCHASE);
AndroidTerminal.getInstance().processSale(coreSale);

```

### Refund Unreferenced

##### Swipe/ Keyed

Once the pin gets confirmed the transaction gets processed and the transaction response will be returned in OnRefundResponse callback method.

- Request

```

Refund Unreferenced
Swipe/ Keyed
CoreUnreferencedRefundEbt ebt = new
CoreUnreferencedRefundEbt(amount));
ebt.setCardAccount(CardAccount.FOOD_STAMP);
ebt.setReason("reason");
ebt.setOperator("android-operator");
ebt.setDeviceId("12345678");
AndroidTerminal.getInstance().processUnreferencedRefund(ebt);

Once the pin gets confirmed the transaction gets processed and the transaction
response will be returned in **onRefundResponse** callback method.
Voucher

```

### Voucher

- Request

```

CoreUnreferencedRefundEbt ebt = new
CoreUnreferencedRefundEbt(amount));
ebt.setOperator("android-operator");
ebt.setDeviceId("12345678");
CoreVoucher voucher = new CoreVoucher();
voucher.setCardAccount(CardAccount.FOOD_STAMP);
voucher.setCardNumber("6007602801003837968");
voucher.setVoucherApprovalCode("123456");
voucher.setVoucherNumber("123456789012345");
ebt.setVoucher(voucher);
ebt.setReason("reason");
AndroidTerminal.getInstance().processUnreferencedRefund(ebt);

```

### Void

This is usually used during the transaction if something goes wrong. Only applies to transactions which are not settled yet. The uniqueRef from the previous transaction is required. The transaction response will be returned in **onReversalRetrieved** callback method.

- Request

```

CoreReversalEbt
CoreReversalEbt reversal = new
CoreReversalEbt("PAX_A920_ATTENDED",
transaction.getUniqueRef(), "reason");
reversal.setDeviceId("PAX_A920_ATTENDED");
reversal.setOperator("android_operator");
AndroidTerminal.getInstance().processReversal(reversal);

```

### CoreRefund

This will void the transaction no matter if it's settled or not. The uniqueRef from the previous transaction is required. The transaction response will be returned in **onRefundResponse** callback method.

- Request

```

CoreRefund
CoreRefund refund = new CoreRefund(transaction.getAmount());
refund.setUniqueRef(transaction.getUniqueRef());
refund.setReason("reason");
AndroidTerminal.getInstance().processRefund(refund);

```

### Balance Inquiry

Once the pin gets confirmed the transaction gets processed and the transaction response will be returned in **onBalanceInquiryRetrieved** callback method. Reporting

- Request

```

Balance Inquiry
Swipe/ Keyed
CoreBalanceInquiryEbt ebt = new CoreBalanceInquiryEbt();
ebt.setCardAccount(CardAccount.FOOD_STAMP);
ebt.setOperator("android-operator");
ebt.setDeviceId("12345678");
AndroidTerminal.getInstance().processBalanceInquiry(ebt);

```

### Reporting

##### Close Batch

Reporting request requires settlementDate, criterionType and criterionValue fields to be set. criterionType can be set to OPERATOR with the value of operator field being used in sale requests or DEVICE_ID with the value of deviceId field being used in sale requests.

settlementDate needs to be in the following format dd-MM-yyyy ` AndroidTerminal.getInstance().getTransactionReports("25-11-2 019", "OPERATOR", "android-operator");`

The reporting response will be returned in **onTransactionReportRetrieved** callback method.

### External PinPad - SP30

To enable SP30 device, set externalPinpad flag to **true** during the device initialization.

if the device is not plugged in, the SDK will return EXTERNAL_PINPAD_NOT_DETECTED error.

- Request

```

HashMap data = new HashMap<>();
data.put("externalPinpad", true);
AndroidTerminal.getInstance().initDevice(DeviceEnum.PAX,
DeviceConnectionType.AIDL, null, data);

```

### EBT+EMV

In situations where the same device will support both EBT and Credit / Debit transactions through the Worldnet gateway, a Gateway terminal will have to be set up for each one. One for EBT and another for credit / debit. Once configured in the Gateway, one of the terminals will be the primary terminal, and that’s the terminal the integration will use for all EBT and Credit/debit transactions. (Terminal number + secret).
