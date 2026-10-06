<!-- source: https://developers.worldnetpayments.com/doku.php?id=gochip:mobile_pos:1_5_x:devices:datecs | synced: 2026-10-05 -->

# Datecs [Back to Devices](doku.php?id=gochip:mobile_pos:devices)

We support the Datecs Bluepad 50. This mPOS device supports Chip and PIN, NFC and swipe transactions. Currently only supported on the Android platform.

#### []Supported devices

- Bluepad 50

#### []Installation instructions

##### []Android

1. Add the Bluepad plugin libraries as dependencies to your project.
1. Please add the following permissions to `AndroidManifest.xml` file.

```
<uses-permission android:name="android.permission.BLUETOOTH"/>
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>

```
