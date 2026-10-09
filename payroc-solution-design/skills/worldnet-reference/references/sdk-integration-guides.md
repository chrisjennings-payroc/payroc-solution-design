# GoChip native SDK integration guides — derived summary (internal)

> **Source:** Payroc-issued GoChip SDK integration guides, SDK **1.6.89** (iOS BBPOS Chipper 3X; Android BBPOS, PAX, Ingenico,
> IDTech). The PAX guide is dated July 2026. These guides are marked *Confidential — Not for Public Distribution* and are
> **not part of the public Worldnet wiki snapshot**; this file is a **derived, non-sensitive summary** written 2026-10-09.
> **Do not copy the guides, key identifiers/components, sample private keys or any credentials into this repo or an SD.**
> Feeds Solution Design **8.2f** (platforms, device matrix, build deliverables, logging, certification checklist) and **8.6b**.
> The public-wiki view of the same stack is `sdks.md`; where the two differ, this file reflects the newer Payroc guides.

## Platforms

| Platform | Baseline (guides) | Devices | Source |
|---|---|---|---|
| Android | SDK 1.6.89; minSdk 22, compileSdk 34, targetSdk 33; Java 17 source/target; core-library desugaring; JARs in `app/libs`; native `.so` per ABI where the device needs them | BBPOS, PAX, Ingenico, IDTech | Android guides |
| iOS | SDK 1.6.89; Xcode 14+, iOS 12+; Objective-C static libraries, single `Core.h`, Swift bridging header, `-ObjC`, Bitcode off | **BBPOS Chipper 3X only** (confirmed by Payroc: no other device on iOS) | iOS guide |
| Windows (.NET C#) | Not reviewed. Wiki: .NET C# min 4.5.1 | IDTech, Ingenico only (confirmed by Payroc) | `sdks.md` only |
| Java | Not reviewed. Wiki: Java >= 8 | IDTech, Ingenico only (confirmed by Payroc) | `sdks.md` only |
| Ubuntu/Linux | Not reviewed. Wiki: Ubuntu min 16.04. Supported SDK target (confirmed by Payroc) | IDTech, Ingenico only | `sdks.md` only |

Windows, Java and Ubuntu/Linux build, driver and per-device details are **out of scope of this summary** — leave them as unresolved
fields in an SD; never invent them. Core concepts (credentials, logging, modes, certification checklist) are the same across platforms
(confirmed by Payroc).

## Device matrix (Android unless stated)

| Family | Models (guides) | Connection | Prerequisites before the SDK works | Test-plan notes |
|---|---|---|---|---|
| BBPOS Chipper 3X | BT, USB, Audio, Serial models (Android); BLE and audio jack (iOS) | Bluetooth LE / USB / audio jack / serial | `android.permission.BBPOS`; native libraries in every target ABI; Bluetooth + location permissions (Android 12+); iOS Bluetooth entitlement/usage strings; audio mode needs microphone permission | Surcharge enabled => manual signature collection or the sale can fail |
| PAX | A80, A920 / Pro / Max, A77, IM25, A35, IM30 (AIDL); E700, E800, E500 (USB via TermLink); any IP model (TCP, port 9100) | AIDL / USB / TCP | PAXstore account + device registration; TermLink installed (version depends on model); DUKPT key slots for online PIN, data and EBT PIN injected by Payroc; configuration ZIP via `loadConfiguration` (IM30 has its own ZIP); PAX manifest permissions | App runs on the device, distributed via PAXstore (confirmed). EBT needs the EBT PIN slot. Polling not on all models |
| Ingenico | Lane 3000/5000/7000, iPP320/350, iUC285, Self 2000–8000, Axium DX4000/DX8000/EX8000/RX7000 | USB-CDC only | RBA SDK + native libraries in every ABI; USB device filter with all three vendor IDs; both USB attach intent filters; firmware and EMV configuration on the terminal | SELF series unattended (terminal category, self-check time). `loadFirmware`/`loadConfiguration`/`loadAsset`/`loadRKI` exist in the SDK; **`loadRKI` is for dev/test units run by the developer; production units are keyed by an approved KIF** (confirmed) |
| IDTech | VP3350, VP3300 (BT + USB); VP5300, VP6300, VP6800, VP8300, Augusta, MiniSmart II, Kiosk V (USB) | Bluetooth LE / USB | USB device filter; NEO2 devices file for VP5300/VP6300; Bluetooth + location permissions (Android 12+) | Polling (VP3350/VP3300); loyalty reads (Google Smart Tap, Apple VAS, MIFARE; the partner holds those keys; the guide lists VP3300/VP6300/VP8300, the wiki says VP3300 only); VP6300/VP6800 approved-offline display flag |

## Confirmed by Payroc (not from the guides)

- **Production key injection:** PAX = remote key injection (RKI); Ingenico, IDTech and BBPOS = a Payroc-approved KIF.
- **SDK certification** sign-off and EMV L2/L3/brand certification evidence are owned by **Payroc**.
- **iOS** supports BBPOS only. Linux/Ubuntu is a supported SDK target.
- No SDK upgrade/support policy is stated in the SD (deliberately excluded).

## Mandatory logging (all guides)

| Item | Requirement |
|---|---|
| Levels | TEST/DEV: full; LIVE: info (SDK rejects full in LIVE with a message); "none" is not allowed in production; "error only" is not sufficient for support |
| Capture | Register the SDK log listener at start-up; persist on device; rotation via `payconfig.xml` (max lines, file size, file count) |
| Remote upload | Partner-hosted HTTPS endpoint (TLS 1.2+, authenticated) plus at least one remote trigger (silent push, polling, staff-only menu) |
| Retention / protection | 7–30 day rolling window; encrypt at rest; consent where required (GDPR/CCPA); remove debug viewers from production |
| Content | Never log PAN, CVV, track data or cardholder PII (including application-level additions) — PCI DSS |
| Support impact | Payroc support needs the logs; no logs => limited support SLA |

## Credentials and provisioning

- Terminal ID + API key (+ Integration ID for ISV accounts) per terminal, issued by Payroc; separate TEST and LIVE (gateway URLs selected by the SDK mode).
- `payconfig.xml` can hold the key; the guides warn not to embed credentials in a distributed client — decide where they live.
- A device not registered/keyed to the Terminal ID fails decryption (`DECRYPTION_FAILED_DEVICE_NOT_REGISTERED`).
- Initialise once; **wait for the settings callback** before connecting a device or processing a sale.

## Pre-production checklist themes (basis for the SD certification checklist)

LIVE mode; production Terminal ID/key; info-level logging; no hard-coded or test credentials; log capture + upload + remote trigger
verified; no PAN/CVV/track in logs; both SDK-error and device-error handlers plus the communication-error handler; reconnect across
background/foreground; permissions/manifest/entitlements for each connection type; native libraries in every ABI; every connection mode and
input method the deployment uses tested (chip, tap, swipe, keyed); surcharge (manual signature on BBPOS), polling, EBT, loyalty tested where enabled;
device-specific items (PAXstore/TermLink/keys/config ZIP; Ingenico firmware/config and vendor IDs; IDTech NEO2 file and vendor ID).

## Not documented here (open)

Windows/Java/Ubuntu build and per-device details; current SDK download locations; who creates PAXstore accounts, installs TermLink and supplies the PAX
configuration ZIP; who registers a device to a Terminal ID and what happens when a device moves; how test key sets are provided for non-Ingenico devices.
