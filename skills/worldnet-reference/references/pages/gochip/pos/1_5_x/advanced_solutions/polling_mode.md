<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:1_5_x:advanced_solutions:polling_mode | synced: 2026-10-05 -->

# Polling Mode

POLLING MODE changes the normal flow of a sale transaction using our Websockets SDK solution. In a basic transaction flow we need to call the method processSale to start a sale. With POLLING MODE enabled, your terminals POS device will be ready to process the sale with no command required to be sent to start the transaction. The POS device will be “listening” for a card to be presented to process a sale at all times. When a sale finishes (onSaleResponse is received from the bank) the terminals POS device will return to a “listening” state ready to process the next sale. POLLING MODE is mostly applied to situations where a terminal is unattended, and needs to wait until a card is presented to execute a sale based on predefined value - parking lots, stadiums, etc.

> **Note**
> POLLING MODE requires QUICK CHIP to be enabled to process the sales.

- **(1) Configuring Device** Your application requires the POS device to be connected, and this is when you will set the flags needed to configure the POS device to enable POLLING MODE
- **(2) Start Sale – Present Card** In POLLING MODE the request for a card to be presented will happen before your application submits any information of the sale. The POS device will always be “listening” for a card to be presented.
- **(3) Start Sale – Process Sale** At this point your application needs to set an amount for the sale before processing. You will need to consider that the onRequestSetAmount(CoreSale coreSale) callback method is going to be called for more than one mode, so inside the method when treating the response you received, remember to verify if the terminal is on Polling Mode.
- **(4) Cardholder Confirmation** When the transaction method requires a signature (or PIN entry), the SDK is going to require that from your application. After your application submits the captured signature, the SDK will add it to the sale and submit it to the gateway.
- **(5) Submit Sale** The last part of the sale transaction is the submission itself and the receiving of the response. Depending on the result, your application might need to treat the information and send some feedback to the final user. Afterwards you can request the user to remove the card.
- **(6)** As POLLING MODE is enabled the POS device will then return to STEP 3.
