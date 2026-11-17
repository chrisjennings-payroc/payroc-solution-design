<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:error_codes | synced: 2026-10-05 -->

# Error Codes

While integrations are expected to run smoothly with our SDK there is some common errors customers may run into which can be resolved by reporting them to our team. Below are some common errors that may occur during the integration:

### Connection errors:

`ERROR_NETWORK`
`ERROR_TIMEOUT`

This could mean that your internet connection has been interrupted. If you have checked that your internet connection is working then contact our team with logs from our SDK. We can then further investigate to get you back up and running.

### Decryption errors:

`ERROR_INVALID_EMV_TAGS`
`ERROR_INVALID_KSN_RANGE`

When a device is shipped with Worldnet Test/Live keys there is an extra step to add the KSN of the device to our HSM for decryption. This is a common error that is usually easily resolved by contacting %CompanyContact with the EMV and TRACK KSNs from your device.

### Credential errors:

`INCORRECT_SETTINGS_TERMINAL`
`INCORRECT_SETTINGS_TOKEN`

This usually means the credentials you are using for your virtual terminal are incorrect. If you are sure your credentials are correct it is best to contact our integrations team for further investigation.

You can view a list of our errors with general descriptions [here.](https://docs.google.com/document/d/1apiRcguFm6npljNp7YZWkAAjJCvRM69cE25KEP6dOXs/edit?usp=sharing)
