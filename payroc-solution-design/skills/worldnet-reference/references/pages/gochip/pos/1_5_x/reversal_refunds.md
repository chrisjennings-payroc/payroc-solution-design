<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:1_5_x:reversal_refunds | synced: 2026-10-05 -->

> **Note**
> This is documentation for older versions 1_5_X if you want to go back to the newest version 1_6_0 click [here](doku.php?id=gochip:pos:1_5_X:devices)

## []Reversal and Refunds

#### Overview

The SDK is required to handle the situation where a reversal is performed on a transaction with a certain OrderID that may have been used in more than one transaction attempt. Transactions with the same OrderID are not guaranteed to be unique, and are therefore impossible to single out for a reversal on its own. In the event of performing a reversal using the OrderID field, add a timestamp indicating the time transaction occurred in the merchant’s timezone.

##

- Android
- IOS

```

CoreSale sale = new CoreSale(CoreUtil.parseStringToBigDecimal("1.00"));
sale.setDateTime("2020-01-01T10:00:00");
sale.setOrderId("TEST_ORDER_ID_001");
// The dateTime and orderId fields must be stored to be used in the Refund/Reversal request
AndroidTerminal.getInstance().processSale(sale);

```

```

CoreSale *sale = [[CoreSale alloc] init];
sale.amount = 1.00;
sale.orderId = "TEST_ORDER_ID_001";
sale.dateTime = "2020-01-01T10:00:00";
[[WTPSTerminal singleton] processSale:sale];

```

#### Refund Flow

For the instances where the UniqueRef is not returned, the refund functionality is updated to allow refunds using OrderId + PreviousTransactionDateTime.

##

- Android
- IOS

```

CoreRefund refund = new CoreRefund(BigDecimal.valueOf(0.5), "TEST_ORDER_ID_001");
refund.setPreviousTxnDateTime("2020-01-01T10:00:00");
AndroidTerminal.getInstance().processRefund(refund);

```

```

CoreRefund *refund = [[CoreRefund alloc] init];
refund.amount = 0.50;
refund.orderId = "TEST_ORDER_ID_001";
refund.previousTxnDateTime = "2020-01-01T10:00:00";
[[WTPSTerminal singleton] processRefund:refund];

```

#### Reversal Flow

Reversals on terminals that do not force unique OrderID, now require the new field PreviousTxnDateTime when attempting Reversals using OrderID. Transactions that have been settled between the time the first transaction occurs and the time the Reversal occurs are now Refunded instead of Reversed.

##

- Android
- IOS

```

CoreReversal reversal = new CoreReversal();
reversal.setOrderId("TEST_ORDER_ID_001");
reversal.setPreviousTxnDateTime("2020-01-01T10:00:00");
AndroidTerminal.getInstance().processReversal(reversal);

```

```

CoreReversal *reversal = [[CoreReversal alloc] init];
reversal.orderId = "TEST_ORDER_ID_001";
reversal.previousTxnDateTime = "2020-01-01T10:00:00";
[[WTPSTerminal singleton] processReversal:reversal];

```
