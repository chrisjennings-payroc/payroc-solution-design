<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:device_configuration | synced: 2026-10-05 -->

# Device Configuration

Check your device and proceed to the sections below to configure your device.

# Ingenico Devices

To update any configuration files on the `INGENICO` devices, the LLT tool (5.x) is used (supplied by INGENICO). If you do not have this tool please contact INGENICO.

1. To update the files on the `INGENICO` devices, the device must be in LLT mode.

  - To put the INGENICO iUC285 device in LLT mode, hold the circular button on the back of the device until the light is red. The screen will display "LLT".
  - For the INGENICO iPP320 & INGENICO iPP350 - restart the device and HOLD F3 until the device displays LLT.
  - For the Ingenico Tetra Lane - restart the device and HOLD # until the device displays LLT
  - For SELF devices, restart the device and hold the button on the back of the device until the light is red. The device will boot into LLT mode and the screen will display "LLT". All steps below will be the same for all supported INGENICO devices:
1. Open the LLT tool, select the target terminal (your device will be listed), and connect the device by double clicking on the device icon
1.
1. Clean the terminal by following this [guide](https://developers.worldnetpayments.com/lib/exe/fetch.php?media=tetra_clear_terminal_llt.pdf).
1. Once the terminal is cleaned, connect the device again and in the LLT tool navigate to DEVICE_NAME/LLT_DEVICE_NAME (for IPP, IUC devices navigate to the extracted directory)
1. Right-click on DEVICE_NAME_NOTKI.M## file and click download
1. Wait until the status says 100%
1. Once loaded, double click on the device icon to disconnect (the device will take a few minutes to process this update)
1. If the device displays a key injection option, select NO Key Injection and Delete KIA
1. Once the device displays “This lane closed”, put the device into LLT mode again and load all configuration files from the configuration files directory: EMVCLESS.XML, EMVCONTACT.XML, tips.K3Z, and CB5BTTDES5.PGZ

> **Note**
> If the `INGENICO iPP320, INGENICO iPP350` or Lane device displays KEY INJECTION menu after loading .OGZ file please select "NO KEY INJECTION". Delete RKI ? "YES". *All the files inside the package can be loaded all at once except .OGZ RBA file which is required to be loaded separately. Once the OGZ file (the RBA package) is loaded the device needs to be restarted. Once restarted place the `INGENICO` device into LLT mode again and the rest of the files can be loaded all at once.

Package contents of `Worldnet` are as follows;

- .OGZ file - Contains full RBA/UPP package.
- EMVCONTACT.XML - EMV configuration file.
- EMVCLESS.XML - contactless configuration file.
- tips.K3Z - required by the SDK to display prompts on the device.
- KIACFG.txt - used to disable key injection (applicable only to iUC285).
- PROMPT.XML - contains all required strings
For loading configuration files programatically please use the following instructions:

- Update to the latest [SDK](https://developers.worldnetpayments.com/gochip:downloads:sdk) or [Websocket](https://developers.worldnetpayments.com/gochip:downloads:websockets) version
- Download the firmware package for your [device](https://developers.worldnetpayments.com/gochip:downloads:devices)
- Connect the device (please make sure onDeviceConnected callback is called before loading any files)
- Once the device is connected, load the .OGZ(UPP firmware) file located in the firmware package under DEVICE_NAME/OGZ/XXX.OGZ directory
- The .OGZ package should be loaded using terminal.loadFirmware method if using the SDK. For websockets please use the following request [message](https://developers.worldnetpayments.com/apis/websockets/#request_loadFirmware)
- Example:

```
Terminal.Instance.LoadFirmware("Y:\\UPP V8.81.04\\LIVE\\Self5000-dukpt-live\\Self5000\\OGZ\\UTKI95P088104.OGZ");
```

> **Note**
> Please note that the SELF3000 and SELF4000 devices require a different approach for loading the firmware. Instead of providing the .OGZ file path, use the absolute path to:
> - Multi_OGZ_upgrade_SELF3000_UPP8.81.12 directory for the SELF3000 devices.
> - Multi_OGZ_upgrade_SELF4000_UPP8.81.12 directory for the SELF4000 devices.
> - Example:
>
> ```
> Terminal.Instance.LoadFirmware("Y:\\UPP V8.81.12\\LIVE\\Self3000-dukpt-live\\Multi_OGZ_upgrade_SELF3000_UPP8.81.12");
> ```
>
> Additionally, the starting UPP version must be:
> - 7.83.35 for the SELF3000
> - 7.81.01 for the SELF4000 During the firmware upgrade process the device will reboot multiple times.

- The device will process the file and reboots, it might take 30+ min for the UPP to be upgraded succesfully
- If the upgrade process was succesfull you will receive FILE_LOADED_SUCCESSFULLY message, otherwise an error will be returned. (ERROR_OCCURRED_DURING_LOADING or NOT_ALL_REQUIRED_FIRMWARE_FILES_FOUND)
- Once the device is back up, connect to the device and use terminal.loadConfiguration method if using the SDK. For websockets please use the following request [message](https://developers.worldnetpayments.com/apis/websockets/#request_loadConfiguration) and load the rest of the configuration files located under "Configuration files" directory
- Example:

```
Terminal.Instance.LoadConfiguration("Y:\\UPP V8.81.04\\LIVE\\Self5000-dukpt-live\\Configuration files");
```

- The device will reboot.
- Once the device reboots, connect to the device and verify the UPP version by checking the device info table.

# IDTech Devices

Config instructions

The Device MUST have the correct test key injected. Please contact [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection) if you are unsure of which key is required. If an alternate firmware is required please contact [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection).

If you are running an old firmware on any of the following `IDTech TEST Devices` and would like to update the firmware on the device yourself, please download the latest `TEST FIRMWARE` that we support [here ](doku.php?id=gochip:downloads:devices). Please follow the instructions listed below your device. If you are using the `AUGUSTA` or `MINISMART`, the test Firmware for these devices can be updated by installing the dot NET SDK Demo application. Please download the latest version of this tool from IDTech [here](https://atlassian.idtechproducts.com/confluence/display/KB/Universal+Library+for+Visual+Studio+-+Home).

1. Open the IDTech dot NET SDK Demo Tool.

  - using this tool you can check what firmware is loaded onto your device.
  - open the dot NET SDK Demo with device connected - expand device section - firmware version - execute command.
  - to obtain the extended firmware version on the AUGUSTA or MINISMART - expand device section - send data command 7831 and ensure the wrap NGA checkbox is checked.
1. To update the firmware.

  - expand device section - click on "Update Device Firmware".
  - navigate to the correct file downloaded from above for your device and click OK.
  - "Firmware Update Successful" - your device has been updated.
If you are using the `VP3300` or `VP8300`, the test Firmware for these devices can be updated by installing the NEO application supplied in the folder you have downloaded for your device [here](doku.php?id=gochip:downloads:devices). Please follow these steps:

1. Install NEO download application supplied in the folder.

  - make sure your device is connected via USB.
  - please ignore the NO COM PORT warning and select OK (this will show when connecting via USB).
1. Select LOAD.

  - please select the correct firmware file for your device contained in the same folder.
  - window will display "100% Done and Rebooting".
  - Update Successful - your device has been updated.
If you are using the `VP5300` or `VP6300`, the test Firmware for these devices can be updated using the bootloader tool supplied in the folder you have downloaded [here](doku.php?id=gochip:downloads:devices). Please follow these steps:

1. Open the Bootloader tool supplied in the folder for your device.

  - Please check the Select All CheckBox.
  - Select Update.
  - Select Continue.
1. Wait for all files to fully update. Status will show Completed.

  - Update Successful - your device has been updated.
