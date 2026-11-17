<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:1_5_x:advanced_solutions:delayed_auth_mode | synced: 2026-10-05 -->

# Delayed Auth Mode

DELAYED AUTH MODE changes the normal flow of a sale transaction using our Websockets SDK solution. A transaction is started using QUICK CHIP with a default initial amount set. After the card is presented and the data has successfully been read, we request the real DELAYED AUTH amount of the sale to be entered before sending online. This mode is mostly applied to situations where the POS application is designed to first capture the card’s data before establishing the sale’s value.

- **(1) Configuring Device** Your application requires the POS device to be connected, and here you will set the flags needed to configure the POS device to enable DELAYED AUTH MODE.
- **(2) Start Sale – Process Sale** This is the normal sale execution. Your application must send a basic sale requiring it to be processed. Before actually sending the sale to the Gateway your Application will be able to set the (delayed auth) amount.
- **(3) Start Sale – Present Card** the card is detected and the required information is provided.
- **(4) Start Sale – Submit Amount** At this point your application needs to set the final amount to the sale. Before using the submitAmount() method, the received CoreSale object, from the OnRequestSetAmount(CoreSale coreSale) method, has an amount defined as “0” (zero). Here you will need to consider that the onRequestSetAmount(CoreSale coreSale) callback method is going to be called for more than one Mode, so inside the method, when treating the response you received, remember to verify if the terminal is on DELAYED AUTH MODE.
- **(5) Cardholder Confirmation** When the transaction method requires a signature (or PIN entry), the SDK is going to require that from your application. After your application submits the captured signature, the SDK will add it to the sale and submit it to the Gateway.
- **(6) Submit Sale** The delayed auth amount is submitted as the final amount for the transaction. Depending on the result of the bank’s response, your application might need to treat the information and send some feedback to the final user. If everything is ok, you can request the user to remove the card.
