# Worldnet SDKs, POS / mPOS, plugins and legacy XML (derived)

> Sources: `pages/gochip/**` (gochip = Worldnet card-present SDK + Websockets), `pages/plugins/**`,
> `pages/selfcare/developer/**`, `pages/selfcare/sample_codes/**`. Paths relative to `references/`.
> **Credentials in snapshot samples are not reproduced here** - use `<API_KEY>`, `<INTEGRATION_ID>`.

## 1. gochip overview

Worldnet's card-present stack (`pages/gochip/introduction.md`): "We recommend using our **Websockets** solution as
the best way to integrate"; otherwise the **GoChip SDK** is available in several languages. Two solution lines:

| Line | Environments (wiki wording) | Devices | Entry page |
|---|---|---|---|
| **POS** | restaurants, taxi, standard retail, gas stations, unattended kiosks | IDTech, Ingenico, PAX | `pages/gochip/pos/coding_101.md` |
| **mPOS** | tradesmen, drivers, handheld taxi, conventions, self-employed; Android + iOS | BBPOS | `pages/gochip/mobile_pos/coding_101.md` |

Architecture (`pages/gochip/pos/basic_solutions.md`): POS application -> Websockets/SDK (platform + device plugins +
gateway connector) -> payment device; the gateway connector talks to the Worldnet gateway (REST). PAX devices
differ: the application with the GoChip integration **runs on the device itself** (`pages/gochip/pos/devices/pax.md`).

### Integration options
| Option | How | Notes |
|---|---|---|
| **Websockets** | Download zip, run `ws-setup`, start `start.bat` / `start.sh`; talk JSON messages (`REQ_*` / `RES_*`) from any language | Java 17+ required for the Java WebSockets service (`pages/gochip/support/troubleshooting.md`). Core flow: `REQ_INIT_WITH_CONFIGURATION` (terminalId) -> `REQ_INIT_DEVICE` (device, connectionType, inputMethod) -> `REQ_PROCESS_SALE` (amount) -> `RES_ON_SALE_RESPONSE` (includes `uniqueRef`) (`pages/gochip/pos/coding_101.md`) |
| **SDK** | Native libraries; listeners/callbacks (`CoreAPIListener`, `onSaleResponse`, `onSignatureRequired`...) | Java (>= 8), Android (SDK needs Java 17; min Android 5), iOS (min 9.1), Ubuntu (min 16.04), .NET C# (min 4.5.1) (`troubleshooting.md` FAQ) |
| **Modes** | `CoreMode.TEST` / live; `payconfig.xml` holds gateway URLs + `apiKey` + `integrationId` | `pages/gochip/support/authentication.md` |

## 2. Supported devices (tables in snapshot)

| Family | Models (from snapshot) | Platforms | Page |
|---|---|---|---|
| IDTech | VP3350, VP3300, VP8300, VP5300, VP6300, VP6800, Augusta, Minismart II, Kiosk V | Windows, Linux, Android | `pages/gochip/pos/devices/idtech.md` |
| Ingenico | Axium DX4000/DX8000/EX8000/RX7000 (Android only), iPP320/350, iUC285, Lane 3000/5000/7000, Self 2000-8000 | Windows/Linux/Android (Axium Android only) | `pages/gochip/pos/devices/ingenico.md` |
| PAX | A80, A920, A920 PRO, A920 MAX, E700, E800, E500, IM30, IM25, A77, A35 | Android (app on device) | `pages/gochip/pos/devices/pax.md` |
| BBPOS (mPOS) | Wisepad 2, Wisepad 3 / 3S, Chipper, Chipper BT, C2X, C2X BT, C3X BT | iOS + Android | `pages/gochip/mobile_pos/devices/bbpos.md` |

Device configuration (LLT tool for Ingenico, DUKPT key slots for PAX, KSN registration) is in
`pages/gochip/support/device_configuration.md` and the device pages; **published test keys appear in the snapshot
- do not copy them**. Device firmware/RBA/UPP/Axium versions: `pages/gochip/support/troubleshooting.md`. Device
download package list: `pages/gochip/downloads/devices.md`.

## 3. Modes and advanced flows (Websockets/SDK)

| Flow | Summary | Page |
|---|---|---|
| Basic sale / refund / reversal | Reversal updates original amount; refund is a new transaction. In SDK 1.6.x `onRefundResponse` returns `CoreSaleResponse` if a reversal was done instead of a refund. OrderID alone is not unique - keep `dateTime` + `orderId` to reverse/refund when `UniqueRef` is missing | `pages/gochip/pos/reversal_refunds.md`, `pages/gochip/support/update_guide_1_6_x.md` |
| **Authorization** (pre-auth / tip adjust) | Auth low amount, then `UpdateTransaction` with `uniqueRef` for the higher final amount | `pages/gochip/pos/advanced_solutions/authorization.md` |
| **Polling mode** | Device listens for a card with no sale command (unattended: car wash, laundromat, parking); **requires Quick Chip** | `.../polling_mode.md` |
| **Delayed auth mode** | Card read first (Quick Chip with default amount), final amount set before going online | `.../delayed_auth_mode.md` |
| **Offline mode** | Sales stored when offline (manual switch or HEALTH CHECKER), offline expiry checks, later submit to gateway; Websockets 3.0.2 notes "encrypted payload usable directly with our API while using offline mode" | `.../offline_mode.md`, `pages/gochip/downloads/websockets.md` |
| **Secure tokens (formerly secure card)** | Registration/auto-tokenisation returns `securecardmerchantref`; wiki says Websockets "does not currently support processing transactions using" the token - use with the XML gateway (REST not mentioned there) | `.../secure_card.md` |
| **Loyalty cards** | Three loyalty features, IDTech VP3300 only | `.../loyalty_card.md` |
| **EBT** | PAX sample requests (EBT cash / food stamp); EBT on FiServ and TSYS processors; needs EBT PIN key slot | `pages/gochip/pos/devices/pax/ebt.md`, `pages/selfcare/integration_docs/introduction.md` |
| **Reward Pay (surcharging)** | SDK 1.6.53: flows by `allowBypass` x `discloseFee`; Axium (Android; FDRC, TSYS), BBPOS Chipper 3X (TSYS), PAX (FDRC, TSYS); terminal `Allow surcharges`, `Surcharge (%)` | `pages/gochip/support/what_is_new/sdk_1_6_53.md` |
| **Frictionless payment** | Identify returning customers during polling/delayed-auth via token history; fully supported only on IDTech; needs Merchant Portfolio with token uniqueness + auto sharing | `pages/gochip/support/what_is_new/websocket_3_0_28_and_sdk_1_6_28.md` |
| Signature collection | `SignatureCollection.AUTOMATIC` (callback) or `MANUAL` (paper) | `troubleshooting.md` |
| Transaction search | `getTransactions` (cursor via `UniqueRef`/`next`), `getTransaction`; **18 months** history | `update_guide_1_6_x.md` |

Selecting a flow: the wiki's questionnaire (attended vs unattended, amount known before card, connectivity)
is in `pages/gochip/pos/advanced_solutions.md`.

## 4. Authentication for SDK / Websockets

- Since 1.6.x: **API key** (random 128-char string) replaces Terminal ID + secret; plus optional **Integration ID** for ISV
  accounts (`pages/gochip/support/update_guide_1_6_x.md`, `authentication.md`).
- Set via `payconfig.xml` (`apiKey`, `integrationId`, `gatewayLiveUrl`, `gatewayTestUrl`, `gatewayDevUrl`) or in code
  (`setApiKey`, `setIntegrationId`) or Websockets messages `REQ_SET_API_KEY` / `REQ_SET_INTEGRATION_ID` (`data.key`).
- Keys come from Worldnet support or an existing account; ISV integrations may use one key for many merchants.
- 1.5.x and earlier used terminal ID + secret (`pages/gochip/1_5_x/introduction.md`, `pages/gochip/pos/1_5_x/*`).
Details: `auth-and-signatures.md`.

## 5. Errors and troubleshooting
See `errors-and-response-codes.md` (SDK error families, `A/D/C/R` codes, cancellation statuses in Websocket 3.0.28/SDK 1.6.28).

## 6. Versions / what's new

| Item | Note | Source |
|---|---|---|
| SDK 1.5.x -> 1.6.x | API key auth, native date/time types, reversals return `CoreSaleResponse`, transaction search rewrite, OpenAPI-based dependencies | `pages/gochip/support/update_guide_1_6_x.md` (identical `update_guide_1_6_0.md`) |
| Websocket 3.0.28 / SDK 1.6.28 | **Breaking**: "Secure Card" renamed to "Secure Token" (message types and fields), new transaction-cancellation flow, communication-error handling; new frictionless payment, host request timeout, IDTech card-removal timeouts, MiniSmart II APDU | `pages/gochip/support/what_is_new/websocket_3_0_28_and_sdk_1_6_28.md` |
| SDK 1.6.53 | Reward Pay (surcharging) flow | `pages/gochip/support/what_is_new/sdk_1_6_53.md` |
| Download pages | Sparse/legacy (e.g. release 1.5.2 of Aug 2019; Websockets 3_0_2 of May 2021); no current binaries linked in snapshot | `pages/gochip/downloads*.md` |
Docs for 1.5.x are mirrored under `pages/gochip/**/1_5_x/`. Some gochip pages are empty/placeholder
(`api_documentation/sdk.md`, `api_documentation/websockets.md`, `solutions.md`, `support.md`) - ignore them.

## 7. E-commerce plugins (alternative path)

| Plugin | Notes | Source |
|---|---|---|
| WooCommerce | Listed with WordPress.org link only (no install page in snapshot) | `pages/plugins/introduction.md` |
| Magento 2 | Plugin zip; configure primary currency, terminal ID, shared secret; AVS/CVV from Selfcare; refund via Credit Memo (full refund -> void); custom fields; multi-currency; Apple Pay certificate steps | `pages/plugins/magento.md` |
| OpenCart | Marketplace link; "contact support to enable" | `pages/selfcare/developer/plugins/opencart.md` |
| Shopify | Worldnet Payments app; terminal number + Shopify password (from support); test mode toggle | `pages/plugins/shopify.md` |
Credentials differ by plugin (Magento: terminal ID + shared secret; Shopify: terminal number + support-issued password). Version inconsistencies exist (Magento v1.2.0 in `plugins/magento.md` vs `magento2x-V1.6.zip` link in `selfcare/developer/plugins.md`) - confirm the supported version with support.

## 8. XML API and sample code (legacy / alternative)

- XML gateway = "feature modelled" XML calls for payments (pre-auth, completion, refund, unreferenced refund, status update), Pay Link,
  eInvoice, account verification, secure tokens, subscriptions, 3DS, terminal info. The index is in
  `pages/selfcare/developer/api_specification.md`, **but the per-feature XML spec pages are not in the snapshot** -> "not documented in snapshot".
- Recommended for "elaborate integrations and very large sites"; merchant carries heavier PCI scope
  (`pages/selfcare/developer/understanding_the_integration.md`). Hash: MD5 historically, SHA-512 current (see `auth-and-signatures.md`).
- Sample code (`pages/selfcare/sample_codes/`): PHP hosted payments / secure tokens / subscriptions / payment+token storage / Amazon-solution variants,
  PHP XML payments / secure tokens / subscriptions / 3DS payments, .NET hosted + XML (payments, secure tokens, subscriptions), Java XML (`java.xml.md`).
  Index: `pages/selfcare/sample_codes/introduction.md`. Samples set `$secret`, `$terminalId` in a settings file - use placeholders only.
- Change history of the XML/HPP API (v2.x - 5.2, last entry 2018): `pages/selfcare/api_specification/change_log.md`.
- For new builds prefer REST (`rest-api.md`) or HPP (`hosted-pages.md`); position XML as legacy unless the partner already uses it.

## Not documented in snapshot (open questions)
- Current SDK/Websockets download locations and a complete release history after 1.6.53.
- Whether Websockets/SDK token flows work against the REST API (wiki points to XML).
- Certification status per device/acquirer/region; EMV L3 process.
- Supported card-present features on the Merchant REST API device instructions vs gochip (the REST spec has device instruction endpoints; relationship to gochip is not explained).
