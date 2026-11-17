<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:authentication | synced: 2026-10-05 -->

# API Key

> **Note**
> You will need to contact [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection#<SAMPLE_HEX_VALUE>) or have a pre existing account to obtain a key.

API keys are used to manage authentication with the gateway. Details of creating a key can be found [here](https://docs.worldnettps.com/apis/merchant/#section/Authentication).

> **Note**
> For integrations managing multiple merchant accounts you may need an ISV account that can use an API key for multiple merchants.

## Setting an API Key

### Setting via Payconfig

This applies for both SDK and Websockets

- Setting it in the `payconfig.xml` file as your `apiKey`, for more information click [here](doku.php?id=gochip:support:troubleshooting#19).

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string name="gatewayLiveUrl">https://https://payments.worldnettps.com/merchant</string>
  <string name="gatewayTestUrl">https://https://testpayments.worldnettps.com/merchant</string>
  <string name="gatewayDevUrl">https://https://devpayments.worldnettps.com/merchant</string>
  <string name="apiKey"></string>
</resources>
```

### Setting via Code

#### For SDK

Set it programatically using this code in the Request. This will set the API key to be used.

- Request

```

AndroidTerminal.getInstance().setApiKey("<SAMPLE_HEX_VALUE>");
AndroidTerminal.getInstance().initWithConfiguration(currentContext, "136007");

```

#### For Websockets

set the APIKey programatically using `request_setAPIKey` payload message.

- Request

```

{
  "type": "REQ_SET_API_KEY",
  "data": {
    "key": "API_KEY"
  }
}

```

# Integration ID

> **Note**
> You will need to contact [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection#<SAMPLE_HEX_VALUE>) or have a pre existing account to obtain a Integration ID.

## Setting an Integration ID

### Setting via Payconfig

This applies for both SDK and Websockets

- Setting it in the `payconfig.xml` file as your `integrationID`,for more information click[ here](doku.php?id=gochip:support:troubleshooting#20).

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string name="gatewayLiveUrl">https://https://payments.worldnettps.com/merchant</string>
  <string name="gatewayTestUrl">https://https://testpayments.worldnettps.com/merchant</string>
  <string name="gatewayDevUrl">https://https://devpayments.worldnettps.com/merchant</string>
  <string name="apiKey"></string>
  <string name="integrationId"></string>
</resources>
```

### Setting via Code

#### For SDK

Set it programatically using this code in the Request. This will set the IntegrationID to be used.

- Request

```

AndroidTerminal.getInstance().setIntegrationId("<SAMPLE_HEX_VALUE>");
AndroidTerminal.getInstance().setApiKey("<SAMPLE_HEX_VALUE>");
AndroidTerminal.getInstance().initWithConfiguration(currentContext, "136007");

```

#### For Websockets

Set the integration ID programatically using `request_setIntegrationID` payload message.

- Request

```

{
    "type": "REQ_SET_INTEGRATION_ID",
    "data": {
    "key": "INTEGRATION_ID"
    }
}

```
