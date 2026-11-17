<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:advanced_solutions:loyalty_card | synced: 2026-10-05 -->

# Loyalty Cards

There are 3 loyalty card features available for IDTech VP3300.

# <Code Samples>

## Configuration

### Apple VAS

Use the `CoreLoyaltyConfig` builder to configure the Apple VAS settings before initializing the device.

Required fields:

- Apple VAS Merchant ID
- Apple VAS Private Key

> **Note**
> Note: We support up to 6 Apple VAS Merchants ID but only one Private Key.

- Java
- Android
- C#
- Websocket

```

HashMap data = new HashMap();
data.put("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .addAppleVasMerchant("pass.com.pronto.id-tech.demo", "www.idtechproducts.com")
    .setAppleVasPrivateKey( "<SAMPLE_HEX_VALUE>")
    .build());
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

HashMap data = new HashMap();
data.put("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .addAppleVasMerchant("pass.com.pronto.id-tech.demo", "www.idtechproducts.com")
    .setAppleVasPrivateKey( "<SAMPLE_HEX_VALUE>")
    .build());
AndroidTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

Dictionary data = new Dictionary();
data.Add("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .AddAppleVasMerchant("pass.com.pronto.id-tech.demo", "www.idtechproducts.com")
    .SetAppleVasPrivateKey("<SAMPLE_HEX_VALUE>")
    .Build());
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
        "device": "IDTECH",
        "connectionType": "USB",
        "loyaltyConfig": {
            "appleVasPrivateKey": "<SAMPLE_HEX_VALUE>",
            "appleVasMerchants": [
                {
                    "merchantId": "pass.com.pronto.id-tech.demo",
                    "merchantUrl": "www.idtechproducts.com"
                }
            ]
        }
    }
}

```

### Google Smart TAP

Use the `CoreLoyaltyConfig` builder to configure the Google Smart TAP settings before initializing the device.

Required fields:

- Google Smart TAP Collector ID
- Google Smart TAP Private Key
- Google Smart TAP Private Key Version

- Java
- Android
- C#
- Websocket

```

HashMap data = new HashMap();
data.put("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .setGoogleSmartTapCollectorId(87133300)
    .setGoogleSmartTapPrivateKeyVersion(10)
    .setGoogleSmartTapPrivateKey( "<SAMPLE_HEX_VALUE>")
    .build());
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

HashMap data = new HashMap();
data.put("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .setGoogleSmartTapCollectorId(87133300)
    .setGoogleSmartTapPrivateKeyVersion(10)
    .setGoogleSmartTapPrivateKey( "<SAMPLE_HEX_VALUE>")
    .build());
AndroidTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

Dictionary data = new Dictionary();
data.Add("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .SetGoogleSmartTapCollectorId(87133300)
    .SetGoogleSmartTapPrivateKeyVersion(10)
    .SetGoogleSmartTapPrivateKey("<SAMPLE_HEX_VALUE>")
    .Build());
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
        "device": "IDTECH",
        "connectionType": "USB",
        "loyaltyConfig": {
            "googleSmartTapCollectorId": 87133300,
            "googleSmartTapPrivateKeyVersion": 10,
            "googleSmartTapPrivateKey": "<SAMPLE_HEX_VALUE>"
        }
    }
}

```

### MIFARE

We only support **MIFARE Classic** and **MIFARE Ultralight** cards.

#### Write Data

Before using the MIFARE cards the merchant must write their own data to the MIFARE card. This can be done using IDTech uDemo.

The example below will show how to write a simple "Hello world!" using uDemo:

1. Enabled Passthrough Mode.

  - Command: 2C
  - Sub-Command: 01
  - Data: 01
1. Place the MIFARE card on top of the reader.

  - NOTE: DO NOT REMOVE UNTIL THE PROCESS IS FINISHED
1. Read card:

  - Command: 2C
  - Sub-Command: 02
  - Data: 0A 00
1. Auth Command:

  - Command: 2C
  - Sub-Command: 06
  - Data: 01 01 FF FF FF FF FF FF
1. Write Block 1:

  - Command: 2C
  - Sub-Command: 08
  - Data: 31 01 48 65 6C 6C 6F 00 77 6f 72 6c 64 21 00 00 00 00
  - Data translation:

    - 31 : Command
    - 01 : Block to be written
    - 48 65 6C 6C 6F 00 77 6F 72 6C 64 21 00 00 00 00 : 16 bytes of data - Hello word + padding of 0s for remaining 4 bytes
1. Disable Passthrough Mode:

  - Command: 2C
  - Sub-Command: 01
  - Data: 00
1. Remove card from the reader.

#### Read Data

Card information can be read using the Android app [NFC TagInfo by NXP](https://play.google.com/store/apps/details?id=com.nxp.taginfolite).

1. Install and open the app on the link above
1. Place the MIFARE card on the phone's reader
1. Select "FULL SCAN"
1. The written information should be displayed as in the image below

#### SDK Configuration

Use the `CoreLoyaltyConfig` builder to configure the MIFARE settings before initializing the device.

Required field:

- Array of block indexes to be read. IDTech limits it to 10 blocks per reading request.

Optional field:

##### MIFARE Classic authentication configuration

You could specify a global or multiple sector key configurations based on your MIFARE Classic card settings.

> **Note**
> If your MIFARE Classic cards use the default key `FFFFFFFFFFFF`, there's no need to declare any authentication configurations.

When setting up a global MIFARE Classic key, the assumption is that all of the sectors use the same key or at least the blocks requested belong to the sectors protected by the key. Use the method `setMiFareClassicAuthGlobalKeyConfig` to configure it.

In case you have sectors with different keys, use the method `addMiFareClassicAuthSectorKeyConfig` to add a sector key configuration.

- Java
- Android
- C#
- Websocket

```

HashMap data = new HashMap();
data.put("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .setMiFareBlocksToRead(new byte[] { 1, 2, 3 })
    .setMiFareClassicAuthGlobalKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF") // replace key
    .addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 0, 1 }) // replace key
    .addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 2, 3 }) // replace key
    .build());
JavaTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

HashMap data = new HashMap();
data.put("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .setMiFareBlocksToRead(new byte[] { 1, 2, 3 })
    .setMiFareClassicAuthGlobalKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF") // replace key
    .addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 0, 1 }) // replace key
    .addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 2, 3 }) // replace key
    .build());
AndroidTerminal.getInstance().initDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

Dictionary data = new Dictionary();
data.Add("loyaltyConfig", new CoreLoyaltyConfig.Builder()
    .SetMiFareBlocksToRead(new byte[] { 1, 2, 3 })
    .SetMiFareClassicAuthGlobalKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF") // replace key
    .AddMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 0, 1 }) // replace key
    .AddMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 2, 3 }) // replace key
    .Build());
Terminal.Instance.InitDevice(DeviceEnum.IDTECH, DeviceConnectionType.USB, data);

```

```

{
    "type": "REQ_INIT_DEVICE",
    "data": {
        "device": "IDTECH",
        "connectionType": "USB",
        "loyaltyConfig": {
            "miFareBlocksToRead": [ 1, 2, 3 ],
            "miFareClassicAuthConfig": {
                "globalKeyMode": "KEY_A",
                "globalKeyValue": "FFFFFFFFFFFF",
                "sectorKeyConfigs": [
                    {
                        "keyMode": "KEY_A",
                        "keyValue": "FFFFFFFFFFFF",
                        "sectors": [ 0, 1 ]
                    },
                    {
                        "keyMode": "KEY_A",
                        "keyValue": "FFFFFFFFFFFF",
                        "sectors": [ 2, 3 ]
                    }
                ]
            }
        }
    }
}

```

## Usage

After the device is initialized with the correct configuration you can set the parameter Loyalty Mode in a `CoreSale` to process a Loyalty and/or Payment Card.

> **Note**
> MIFARE only supports Loyalty Mode `CoreLoyaltyMode.LOYALTY_ONLY`.

- Java
- Android
- C#
- Websocket

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_AND_PAYMENT);
JavaTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_AND_PAYMENT);
AndroidTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.amount = 1.00m;
sale.loyaltyMode = CoreLoyaltyMode.LOYALTY_AND_PAYMENT;
Terminal.Instance.ProcessSale(saleDevice);

```

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
        "amount": 1.5,
        "loyaltyMode": "LOYALTY_ONLY"
    }
}

```

### Re-defining Google Smart TAP Collector ID

It is possible to change the Google Smart TAP Collector ID on a per transaction basis. This can be done on the `CoreSale` object using the method `setGoogleSmartTapCollectorId`:

- Java
- Android
- C#
- Websocket

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setGoogleSmartTapCollectorId(87133300);
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_AND_PAYMENT);
JavaTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setGoogleSmartTapCollectorId(87133300);
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_AND_PAYMENT);
AndroidTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.amount = 1.00m;
sale.googleSmartTapCollectorId = 87133300;
sale.loyaltyMode = CoreLoyaltyMode.LOYALTY_AND_PAYMENT;
Terminal.Instance.ProcessSale(saleDevice);

```

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
        "amount": 1.5,
        "loyaltyMode": "LOYALTY_ONLY",
        "googleSmartTapCollectorId": 12345678
    }
}

```

### Re-defining MIFARE Blocks

It is possible to change the MIFARE blocks to read on a per transaction basis. This can be done on the `CoreSale` object using the method `setMIFAREBlocksToRead`:

- Java
- Android
- C#
- Websocket

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setMiFareBlocksToRead(new byte[] { 1, 2 });
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_ONLY);
JavaTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setMiFareBlocksToRead(new byte[] { 1, 2 });
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_AND_PAYMENT);
AndroidTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.amount = 1.00m;
sale.miFareBlocksToRead = new byte[] { 1, 2 };
sale.loyaltyMode = CoreLoyaltyMode.LOYALTY_AND_PAYMENT;
Terminal.Instance.ProcessSale(saleDevice);

```

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
        "amount": 1.5,
        "loyaltyMode": "LOYALTY_ONLY",
        "miFareBlocksToRead": [ 1, 2 ]
    }
}

```

### Re-defining MIFARE Classic Authentication Configuration

It is possible to change the MIFARE Classic authentication configuration per sale. Use the methods `setMiFareClassicAuthGlobalKeyConfig` and `addMiFareClassicAuthSectorKeyConfig`:

- Java
- Android
- C#
- Websocket

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setMiFareBlocksToRead(new byte[] { 1, 2 });
sale.setMiFareClassicAuthGlobalKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF"); // replace key
sale.addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 0, 1 }); // replace key
sale.addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 2, 3 }); // replace key
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_ONLY);
JavaTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.setAmount(BigDecimal.valueOf(1.00));
sale.setMiFareBlocksToRead(new byte[] { 1, 2 });
sale.setMiFareClassicAuthGlobalKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF"); // replace key
sale.addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 0, 1 }); // replace key
sale.addMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 2, 3 }); // replace key
sale.setLoyaltyMode(CoreLoyaltyMode.LOYALTY_AND_PAYMENT);
AndroidTerminal.getInstance().processSale(sale);

```

```

CoreSale sale = new CoreSale();
sale.amount = 1.00m;
sale.miFareBlocksToRead = new byte[] { 1, 2 };
sale.SetMiFareClassicAuthGlobalKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF"); // replace key
sale.AddMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 0, 1 }); // replace key
sale.AddMiFareClassicAuthSectorKeyConfig(CoreMiFareClassicAuthConfig.CoreMiFareClassicKeyMode.KEY_A, "FFFFFFFFFFFF", new short[] { 2, 3 }); // replace key
sale.loyaltyMode = CoreLoyaltyMode.LOYALTY_AND_PAYMENT;
Terminal.Instance.ProcessSale(saleDevice);

```

```

{
    "type": "REQ_PROCESS_SALE",
    "data": {
        "amount": 1.5,
        "loyaltyMode": "LOYALTY_ONLY",
        "miFareBlocksToRead": [ 1, 2 ],
        "miFareClassicAuthConfig": {
            "globalKeyMode": "KEY_A",
            "globalKeyValue": "FFFFFFFFFFFF",
            "sectorKeyConfigs": [
                {
                    "keyMode": "KEY_A",
                    "keyValue": "FFFFFFFFFFFF",
                    "sectors": [ 0 , 1 ]
                },
                {
                    "keyMode": "KEY_A",
                    "keyValue": "FFFFFFFFFFFF",
                    "sectors": [ 2, 3 ]
                }
            ]
        }
    }
}

```

### Reading MIFARE Ultralight Cards

`MIFARE Ultralight` cards differ from the Classic one. Compared to the Classic which has a block size of 16 bytes, Ultralight uses pages which are 4 bytes each. When reading Ultralight cards, 16 bytes of data are returned from the specified start block (page number). For example, passing block 1 would read pages 1 to 4.

Additionally, the final 4 pages of Ultralight cards are for the authentication key and are not readable. If ever the 16 bytes would include bytes from the final 4 pages, it would just read the remaining bytes starting from page 0.

> **Note**
> **WARNING**: Data overlap when reading consecutive blocks is expected.

### Response data

When a loyalty card is read the callback `onLoyaltyCardDataRetrieved` will be called with the loyalty card information in the `CoreLoyaltyCardData` object. If using web sockets, a message with type `RES_ON_LOYALTY_CARD_DATA_RETRIEVED` will be sent.

Required fields:

**Apple VAS:**

```

{
    "type": "APPLE_VAS",
    "data": "<SAMPLE_HEX_VALUE>"
}

```

**Google Smart TAP:**

```

{
    "type": "GOOGLE_SMARTTAP",
    "data": "<SAMPLE_HEX_VALUE>"
}

```

The Smart Tap data is an NDEF record which you could parse on this [Parser](https://www.ndefparser.net/).

**MIFARE:**

```

{
    "type": "MIFARE_ULTRALIGHT",
    "data": "{
        \"errorCode\": \"E0\",
        \"cardType\": \"04\",
        \"uid\": \"0455E299102880\",
        \"blockData\": {
            \"3\": \"00000000020000100006011011FF0000\",
            \"4\": \"020000100006011011FF000000000000\",
            \"5\": \"0006011011FF00000000000000000000\",
            \"6\": \"11FF0000000000000000000000000000\"
        }
    }"
}

```
