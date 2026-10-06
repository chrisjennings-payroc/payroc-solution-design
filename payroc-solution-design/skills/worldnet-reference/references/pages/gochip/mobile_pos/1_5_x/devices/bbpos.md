<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:mobile_pos:1_5_x:devices:bbpos | synced: 2026-10-05 -->

# BBPos [Back to Devices](doku.php?id=gochip:mobile_pos:devices)

BBPos devices offer a range of options for mPOS processing. The Wisepad 2, Chipper C2X (and BT variant) both support NFC. All devices support EMV and swipe. The Wisepad 2, Chipper BT and Chipper C2X BT support Bluetooth and the Chipper supports audio jack.

## Supported devices

|  | iOS | Android |
|---|---|---|
| Wisepad 2 | ✔ | ✔ |
| Chipper | ✔ | ✔ |
| Chipper BT | ✔ | ✔ |
| Chipper C2X | ✔ | ✔ |
| Chipper C2X BT | ✔ | ✔ |

### Installation instructions

#### SDK

##### Android

1. Add the BBPOS plugin libraries as dependencies to your project.
1. Please add additional permissions AndroidManifest.xml.

```
<uses-permission android:name="android.permission.BLUETOOTH"/>
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
<uses-permission android:name=“android.permission.ACCESS_COARSE_LOCATION”/>
```

List item

*Note: Depending on device, you may be able to remove some of these permissions (i.e. Chipper doesn’t need BT). However, BBPos recommend all of these*

##### iOS

1.

Add the BBPOS plugin libraries as dependencies to your project.
1.

Link the `Libc++.tbd` framework to your Xcode project.
1.

Add `External accessory communication` and `Uses Bluetooth LE accessories` to the `Background Modes` capabilities of the project.
1.

Add these frameworks to `Build Phases / Link Binary With Libraries` section of your project.

> **Note**
> For approved PCI PTS device that supports Apple MFi, the Project Info/Info.plist file must include the supported external accessory protocols key UISupportedExternalAccessoryProtocols with value "com.bbpos.bt.wisepad":

```
ExternalAccessory.framework
CoreBluetooth.framework
AudioToolbox.framework
CoreAudio.framework
MediaPlayer.framework
AVFoundation.framework
```
