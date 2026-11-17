<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:devices:pax | synced: 2026-10-05 -->

# PAX [Back to Devices](doku.php?id=gochip:pos:devices)

PAX devices are different from our other offering as the application, with the GoChip integration, will run on the device itself.

### Supported devices

          PAX A920 MAX ✔           PAX IM25 ✔

|  | Android |
|---|---|
| PAX A80 | ✔ |
| PAX A920 | ✔ |
| PAX A920 PRO | ✔ |
| PAX E700 | ✔ |
| PAX E800 | ✔ |
| PAX E500 | ✔ |
| PAX IM30 | ✔ |
| PAX A77 | ✔ |
| PAX A35 | ✔ |

### Configuring PAX devices

- To be able to support decrypting EBT/EMV transactions, PAX devices need to be correctly configured with DUKPT encryption keys.
- The following slots are required to be injected (for testing use the following keys):

#### Slot 1 - used for Online PIN encryption

    - Component 1: 0123456789ABCDEFFEDCBA9876543210 , KCV:08D7B4 (Standard ANSI Test key)
    - Component 2: 00000000000000000000000000000000
    - KSI: F876543210

#### Slot 2 - used for DATA encryption

    - Component 1: 0123456789ABCDEFFEDCBA9876543210 , KCV: 08D7B4 (Standard ANSI Test key)
    - Component 2: 00000000000000000000000000000000
    - KSI: F876543211

#### Slot 3 - used for EBT pin encryption

    - Component 1: 0123456789ABCDEFFEDCBA9876543210 , KCV: 08D7B4 (Standard ANSI Test key)
    - Component 2: 00000000000000000000000000000000
    - KSI: F876543212
- PAX devices will also need to be activated and registered in PAXstore.
- Once registered, TermLink (tested using version:V1.05.09_20250124) is required to be installed which is responsible for communicating with device modules (magstripe, EMV and contactless).
- With the PAX A80, there's the ability to use an external PED - the PAX SP30. **If using the SP30 as the external PED:**

  - SP30 must have appropriate reader app(base V.1.50), and same key configuration as the A80
- For E700 devices, Q20L needs to have the following Termlink version installed: V1.01.00
- For E500 devices, Q20L needs to have the following Termlink version installed: V1.01.02
- For E800 devices, Q20L needs to have the following Termlink version installed: V1.01.02

### Installation Instructions

#### SDK

> **Note**
> Before proceeding, please download all necessary files for your device. You can find all the necessary files in the Downloads section.

  1. Please use the following link which describes how to install the [SDK](https://docs.gochipnow.com/doku.php?id=gochip:mobile_pos:coding_101)
  1. Follow this link to set up your [API key](https://developers.worldnetpayments.com/doku.php?id=gochip:support:authentication)
  1. Using the package provided, and once SDK is installed, install the PAX libraries by dropping them in your project.
  1. Initialize the SDK by calling ` AndroidTerminal.getInstance().initWithConfiguration(this, "TERMINAL_ID"); `
  1. Once onSettingsRetrieved is called, initialize the device using the following code ` AndroidTerminal.getInstance().initDevice(DeviceEnum.PAX, DeviceConnectionType.AIDL, null, null); `
  1. For E700, E800 and E500 device please use `DeviceConnectionType.USB AndroidTerminal.getInstance().initDevice(DeviceEnum.PAX, DeviceConnectionType.USB, null, null);`
  1. onDeviceConnected will be returned if the device has been successfully initialized.
  1. At this point you can start processing EBT transactions.

### EMV

**Configuring PAX device with EMV configuration**

> **Note**
> Please ensure your API key is set up correctly.

  1. Download the following configuration [file](https://developers.worldnetpayments.com/lib/exe/fetch.php?media=paxconfig.zip). For IM30/IM25 use this [configuration file](https://developers.worldnetpayments.com/lib/exe/fetch.php?media=paxconfig-unattended.zip).
  1. Copy the configuration file to PAX sdcard
  1. Import sample application to Android Studio, build it and install it on the device
  1. Navigate to side menu “App Settings” and enter your terminal ID and tap on Save button
  1. Once the SDK gets initialized, tap on pinpad icon in top right corner and select PAX from the list
  1. Once the device get connected, navigate to App Settings and tap on Load Configuration button
  1. Tap on Confirm and select paxConfig.zip from the list
  1. Once loaded, tap on Save button
  1. To test the transaction, enter amount, tap on SALE button and select either EMV or EBT transaction EMV transactions
  1.

To start EMV transaction

```

CoreSale coreSale = new CoreSale(BigDecimal.valueOf(12.00));
coreSale.setTransactionInputMethod(CoreTransactionInputMetho
d.SWIPE_OR_INSERT_OR_TAP_OR_KEYED);
AndroidTerminal.getInstance().processSale(coreSale);

```

  1. If the card requires a PIN, the onRequestPin callback will be triggered the same as for EBT.
  1. If the card requires signature, onSignatureRequired will be triggered with CoreSignature object to be populated with x and y coordinates of the signature. Our sample app contains the sample code for drawing signature using canvas. Below is the sample code.
  1. The transaction gets processed and the transaction response will be returned in onSaleResponse callback method.

### EBT

Click this [link](doku.php?id=gochip:pos:devices:pax:ebt) to go to ebt section.
