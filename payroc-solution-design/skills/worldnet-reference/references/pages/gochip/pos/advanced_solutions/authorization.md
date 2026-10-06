<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:advanced_solutions:authorization | synced: 2026-10-05 -->

# Authorization

AUTHORISATION is an advanced solution of a normal sale where the final amount is adjusted at a later stage after the sale has happened. Within the payment industry this type of solution is also often referred to as Pre-Autorisation, Auth & Capture or Tip Flow Adjustment. This can be performed in either of 2 ways, an Authorisation for a LOW amount and an update Capture for a HIGHER amount (a tip for example). Or secondly, an Auth for a HIGH amount with a Capture for a LOWER amount. This will be processed as a partial void or a refund depending on if the sale has been captured (an example of this would be a petrol pump not dispensing the selected amount of gas - $50 selected, but only $30 pumped).

Process the sale (auth) with the lower amount, let's say $20, customer consumes and get the total amount, if the final amount is more than $20, use UpdateTransaction method to set the tip adjustment for the final amount (the tip will be added to the previous auth amount). To do this, you need to know the uniqueRef of the transaction you want to update:
