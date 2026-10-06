<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:1_5_x:devices:idtech | synced: 2026-10-05 -->

# IDTech [Back to Devices](doku.php?id=gochip:pos:devices)

Our IDTech plugin supports a number of IDTech devices for attended (Augusta, Minismart, VP3300, VP8300) or unattended operation (VP5300, VP6300, VP3300, VP8300).

### Supported devices

        VP8300 ✔ ✔ ✔

|  | Windows | Linux | Android |
|---|---|---|---|
| VP3300 | ✔ | ✔ | ✔ |
| VP5300 | ✔ | ✔ | ✔ |
| VP6300 | ✔ | ✔ | ✔ |
| Augusta | ✔ | ✔ | ✔ |
| Minismart II | ✔ | ✔ | ✔ |

## Installation Instructions

Below you can find the different platforms where you can integrate the SDK. Please proceed to the platform you have chosen to integrate with.

> **Note**
> Before proceeding, please download all necessary files for your device. You can find all the necessary files in the Downloads section.

#### Video tutorial showing how to set up IDTech device step by step

### Linux

#### Prerequisites

- glibc 2.16+
- x86_64 / ARM architectures
- libcurl

#### Installation steps:

1. Extract libraries and symbolic links from `IDTECH/` folder.
1. Create file `/etc/ld.so.conf.d/idtech.conf` - This file should contain the path to the extracted libs directory in Step 1.
1. From the command line run `sudo ldconfig`.
1. Additionally, if using a NEO2 (family of devices which includes the VP6300 and VP5300) device, please copy the `NEO2_devices.xml` from `libs/IDTECH/` folder into your project root directory. Permissions must be set for the USB device. This can be achieved by creating a new file in /etc/udev/rules.d named usb.rules - It must have the following contents: `SUBSYSTEM=="usb", MODE="0666"`. *If you don’t want to add permissions for all devices you could add the IDTech vendor ID*
1. Add the Worldnet IDTech plugin libraries as dependencies to your project.

***NOTE:** When running in Java, you must also set the VM option: `-Xss100m`*

Done! With your environment properly configured you are now ready to perform your first sales transaction. Check out the [Coding 101](doku.php?id=gochip:pos:coding_101) section for more information.

### Windows

#### Prerequisites

- Windows 7/8/10
- If using Java: 32 bit with version 8 or above is required.
- [Visual C++ Redistributable Packages for Visual Studio 2013 is required](https://www.microsoft.com/en-ie/download/details.aspx?id=40784)

#### Installation steps:

1.

Extract libraries from `win-native-32/` and copy all dll files to the application folder.

1.

Depending on the language, run the app as follows:

##### Java

You’ll need the following VM options:

  - Set the java library path `-Djna.library.path=“path to application”`
  - Set the stack size `-Xss50m`

##### Visual Studio C

In solution explorer:

  - Right click the project file and click `Add Existing Item`. Find all other dll files and click Add. Select each dll file under properties select under `Copy to Output Directory` to `Copy Always`.
1.

Add the Worldnet IDTech plugin libraries as dependencies to your project.

Done! With your environment properly configured you are now ready to perform your first sales transaction. Check out the [Coding 101](doku.php?id=gochip:pos:coding_101) section for more information.

### Android

#### Installation steps:

1. Extract libraries from libs folder and copy them into your project.
1. IDTech devices require USB access which can be enabled by following the steps below:

  - Create a new file under `res/xml` folder called `device_filter.xml` and add the following:

```
[](#cb1-1)<?xml version="1.0" encoding="utf-8"?>
[](#cb1-2)<resources>
[](#cb1-3)    <!-- 0ACD / 3530 - IDTech VP3300 -->
[](#cb1-4)    <usb-device vendor-id="2765" product-id="13616"/>
[](#cb1-3)    <!-- 0ACD / 3530 - IDTech VP8300 -->
[](#cb1-4)    <usb-device vendor-id="2765" product-id="13616"/>
[](#cb1-5)    <!-- OACD / 4440 - IDTech VP6300 -->
[](#cb1-6)    <usb-device vendor-id="2765" product-id="17472"/>
[](#cb1-7)</resources>
```

  - Add the following contents into `AndroidManifest.xml` file

```
[](#cb2-1)<intent-filter>
[](#cb2-2)    <action android:name="android.hardware.usb.action.USB_DEVICE_ATTACHED"/>
[](#cb2-3)</intent-filter>
[](#cb2-4)<meta-data android:name="android.hardware.usb.action.USB_DEVICE_ATTACHED" android:resource="@xml/device_filter" />
```

1. Add the Worldnet IDTech plugin libraries as dependencies to your project.

Done! With your environment properly configured you are now ready to perform your first sales transaction. Check out the [Coding 101](doku.php?id=gochip:pos:coding_101) section for more information.

## Need further assistance?

Please check our [Device Configuration](doku.php?id=gochip:support:device_configuration) section in the Support menu.
