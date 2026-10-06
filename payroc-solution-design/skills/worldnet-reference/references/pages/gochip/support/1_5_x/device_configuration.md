<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:support:1_5_x:device_configuration | synced: 2026-10-05 -->

# Device Configuration

Check your device and proceed to the sections below to configure your device.

# Ingenico Devices

To update any configuration files on the `INGENICO` devices, the LLT tool (5.5.0) is used (supplied by INGENICO). If you do not have this tool please contact INGENICO.

1. To update the files on the `INGENICO` devices, the device must be in LLT mode.

  - To put the `INGENICO iUC285` device in LLT mode, hold the circular button on the back of the device until the light is red. The screen will display "LLT".
  - For the `INGENICO iPP320 & INGENICO iPP350 `- restart the device and HOLD F3 until the device displays LLT. All steps below will be the same for all supported `INGENICO` devices (`iUC285` / `iPP320` / `iPP350`):
1. Select the target terminal (your device will be listed).
1. Select "Transfer Contents".
1. Navigate to the unzipped folder in local browser.
1. Select the necessary files needed for your device, right-click and select download. If loading the OGZ file is required (the RBA package) please load this first and on it's own. - If Download cannot be selected, you will need to double-click the device icon in Plugged terminals window to connect the device - a COMX window will appear.
1. Once loaded (progress at 100%), double-click on the device icon in the Plugged Terminals section - the device will restart and process the files. Please note it may restart a few times in this process if a number of files has been selected.
1. Once completed (the screen will return to default screen), and your device will be ready to use.

> **Note**
> If the `INGENICO iPP320 & INGENICO iPP350` device displays KEY INJECTION menu after loading .OGZ file please select “NO KEY INJECTION”. Delete RKI ? “YES”. *All the files inside the package can be loaded all at once except .OGZ RBA file which is required to be loaded separately. Once the OGZ file (the RBA package) is loaded the device needs to be restarted. Once restarted place the `INGENICO` device into LLT mode again and the rest of the files can be loaded all at once.

Package contents of `Worldnet` are as follows;

- .OGZ file - Contains full RBA 2352 package.
- EMVCONTACT.XML - EMV configuration file.
- EMVCLESS.XML - contactless configuration file.
- MANAGER.PAR - enables contactless operation in the supported device.
- tips.K3Z - required by the SDK to display prompts on the device.
- KIACFG.txt - used to disable key injection (applicable only to iUC285).
- PROMPT.XML - contains all required strings

# IDTech Devices

Config instructions

The Device MUST have the correct test key injected. Please contact [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection) if you are unsure of which key is required. The supported firmware for your device is located [here](doku.php?id=gochip:downloads:devices), please ensure this is the firmware version used. If an alternate firmware is required please contact [[email protected]](https://developers.worldnetpayments.com/cdn-cgi/l/email-protection).

If you are running an old firmware on any of the following `IDTech TEST Devices` and would like to update the firmware on the device yourself, please download the latest `TEST FIRMWARE` that we support [here ](doku.php?id=gochip:downloads:devices). Please follow the instructions listed below your device. If you are using the `AUGUSTA` or `MINISMART`, the test Firmware for these devices can be updated by installing the uDemo application. Please download the latest version of this tool from IDTech [here](doku.php?id=gochip:downloads:sdk).

1. Open the IDTech uDemo Tool.

  - using this tool you can check what firmware is loaded onto your device.
  - open the uDemo with device connected - expand device section - firmware version - execute command.
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
