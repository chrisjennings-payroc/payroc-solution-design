<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:pos:devices:ingenico | synced: 2026-10-05 -->

# Ingenico[Back to Devices](doku.php?id=gochip:pos:devices)

Our Ingenico plugin supports multiple Ingenico devices running on the **RBA, UPP, and Axium** platforms. We support 2 main devices for 2 different configurations; attended (LANE 3000,5000,7000) and unattended (SELF 2000,3000,4000,5000,7000/8000). If you have another UPP device please contact %CompanyContact for assistance in setting up.

### Supported devices

|  | Windows | Linux | Android |
|---|---|---|---|
| Axium DX4000 | ✘ | ✘ | ✔ |
| Axium DX8000 | ✘ | ✘ | ✔ |
| Axium EX8000 | ✘ | ✘ | ✔ |
| Axium RX7000 | ✘ | ✘ | ✔ |
| IPP320/350 | ✔ | ✔ | ✔ |
| IUC285 | ✔ | ✔ | ✔ |
| Lane3000 | ✔ | ✔ | ✔ |
| Lane5000 | ✔ | ✔ | ✔ |
| Lane7000 | ✔ | ✔ | ✔ |
| Self 2000 | ✔ | ✔ | ✔ |
| Self 3000 | ✔ | ✔ | ✔ |
| Self 4000 | ✔ | ✔ | ✔ |
| Self 5000 | ✔ | ✔ | ✔ |
| Self 7000/8000 | ✔ | ✔ | ✔ |

Check the [Troubleshooting section](https://developers.worldnetpayments.com/doku.php?id=gochip:support:troubleshooting#21) to view what RBA/UPP/Axium version is supported on Ingenico devices

## Installation Instructions

### SDK

Below you can find the different platforms where you can integrate the SDK. Please proceed to the platform you have chosen to integrate with.

> **Note**
> Before proceeding, please download all necessary files for your device. You can find all the necessary files in the Downloads section.

#### Linux

1. Download sample app as well as ingenico plugin from [here](doku.php?id=gochip:downloads:sdk)
1. Unzip both zip files
1. Open up SwingSample folder located in Sample app in some IDE
1. Open MainForm.java and run it
1. Edit configuration on MainForm.java
1. Depending on architecture unzip the 32 or 64 bit RBA native libs that are bundled.
1. Point your environment to the library files:

  - For Java: Set the `-Djava.library.path=<native libs folder>`
1. Set the permissions for the user to have access to usb TTY devices where <user> is the user that will be running your payment application. **N.B.** you need to re login to take effect!

```
[](#cb1-1)        sudo usermod -a -G uucp <user>
[](#cb1-2)        sudo usermod -a -G dialout <user>
[](#cb1-3)        sudo usermod -a -G lock <user>
[](#cb1-4)        sudo usermod -a -G tty <user>
```

-

**Note:** If you see the error `libudev.so.0: cannot open shared object file: No such file or directory`

Please link the existing libudev.so.1 to the requested libudev.so.0: `sudo ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-gnu/libudev.so.0`

Done! With your ENVIRONMENT properly configured you are now ready to perform your first sales transaction. Check out the [Coding 101](doku.php?id=gochip:pos:coding_101) section for more information.

#### Windows

1. Depending on architecture unzip the 32 or 64 bit RBA native libs that are bundled.
1. Copy the dlls from Resources folder to C:\Windows\SysWow64`
1. Install **‘Microsoft Visual C++ Redistributable Package (x86)’** or alternatively copy the included windows dll files to `C:\Windows\Syswow64`.

Done! With your ENVIRONMENT properly configured you are now ready to perform your first sales transaction. Check out the [Coding 101](doku.php?id=gochip:pos:coding_101) section for more information.

### Android

#### RBA/UPP Platforms

1. Extract libraries from “jniLibs” folder and copy them into your app/src/main/jniLibs directory.
1. Ingenico device requires USB access, to do this :

  1.

Create a new file under res/xml folder called device_filter.xml

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- INGENICO-->
    <usb-device vendor-id="1947"/>
    <usb-device vendor-id="2816"/>
    <usb-device vendor-id="4096"/>
</resources>
```

  1.

Add the following contents into AndroidManifest.xml file

```
[](#cb2-1)<intent-filter>
[](#cb2-2)    <action android:name="android.hardware.usb.action.USB_DEVICE_ATTACHED" />
[](#cb2-3)</intent-filter>
[](#cb2-4)<meta-data android:name="android.hardware.usb.action.USB_DEVICE_ATTACHED" android:resource="@xml/device_filter" />
```

Done! With your ENVIRONMENT properly configured you are now ready to perform your first sales transaction. Check out the [Coding 101](doku.php?id=gochip:pos:coding_101) section for more information.

#### Axium Platform

Axium platform is different as the application, with the GoChip integration, will run on the device itself.

Please refer to the **Axium Debug Unit Installing Firmware and Configuration Files.pdf file** from [here](https://payrocllc-my.sharepoint.com/:f:/g/personal/jorge_interno_payroc_com/EkFVaImSH19Kq-rirT09rwMBDlrC-k2pCzCrLlo1J-JvWQ?e=HEeGg0) on how to configure an Axium debug unit.

## Need further assistance?

Please check our [Device Configuration](doku.php?id=gochip:support:device_configuration) section in the Support menu.
