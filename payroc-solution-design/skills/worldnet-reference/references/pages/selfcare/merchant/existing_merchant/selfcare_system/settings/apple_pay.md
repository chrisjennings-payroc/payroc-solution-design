<!-- source: https://developers.worldnetpayments.com/doku.php?id=selfcare:merchant:existing_merchant:selfcare_system:settings:apple_pay | synced: 2026-10-05 -->

# Apple Pay Certificate

Once the Apple Pay is enabled for a Terminal, It's possible to configure a certificate to start using it.

To set it up, you only need to follow the instruction at the screen after creating the .CSR file.

Once those elements are configured, the only additional step is left to the integrations with the Payment Gateway. The integrations will add the **APPLEPAYLOAD** instead of the card data or the track to perform transactions.
