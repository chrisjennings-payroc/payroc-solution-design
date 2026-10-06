<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:advanced_solutions:offline_mode | synced: 2026-10-05 -->

# Offline Mode

OFFLINE MODE is an Advanced Solution that changes the normal flow for a sale transaction using our Websockets SDK solution. As the terminal is not communicating with the bank until a later stage after the sale has taken place, we offer a way to configure your POS device to perform offline card expiration checks to help ensure the sale can be processed successfully when sent online to the bank.

To setup your terminal to process in OFFLINE MODE, there are two options available:

- (1) Set the terminal to OFFLINE MODE manually. You can add to your solution a “offline/online mode switch”, allowing you to set terminals to work in Offline Mode purposely. getOfflineMode(): Boolean method, which returns the offlineMode state of a specific terminal. When returns True, means that the terminal is in Offline Mode, otherwise returns False. setOfflineMode(Boolean offline): Boolean method, which changes the Offline Mode of a Terminal depending on the value informed on the offline argument – returns True when the Offline Mode of a terminal is successfully enabled or disabled, otherwise returns False.
- (2) Implement the HEALTH CHECKER which will perform a constant connectivity test. If Online, sales will process online as expected. If connectivity drops at any point and the terminal appears to be “OFFLINE”, the terminal will be switched to OFFLINE MODE to ensure transactions will still be processed. (TerminalHealth): this implementation should be added to your main class that controls the use of all the terminals.
- (3) Step 3 is processing these OFFLINE MODE sale requests.

> **Note**
> The implementation of both the above methods are explained in the SDK documentation where you can find out more about the TerminalHealth class.

For the responses, your application needs to add treatment for the callback defined by the CoreApiListener interface related to the Offline Sale responses. This result is received on a specific method (onOfflineSaleRequest), representing the data contained in the sale transaction that wasn’t submitted due to the Offline Mode as well as responses for other requests, needs to be implemented in the same class that implements the CoreApiListener interface.

Finally, your application needs to implement (based on time or other logic) a call to the gateway to send for processing all the offline responses received while terminals were working in Offline Mode. Differently to a normal sale, the submitting of an offline sale request is going to be done by a RestConnect, not by a terminal. There's no callback result, and instead a straightforward result with the sale response. To send offline sale requests, all you need to do is retrieve the transactions stored in your application that weren’t successfully sent, and send them to the Gateway using the sendSale method available at the RestConnector class.

> **Note**
> The implementation of the above method and class are further explained in the SDK documentation where you can find out more about the RestConnector class.
