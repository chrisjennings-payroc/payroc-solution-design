# Card-present device operations on Worldnet — what the snapshot says (derived)

> Feeds Solution Design section **8.6b Card-present operational requirements & open questions**.
> **Confirmed by Payroc (internal, not in the public Worldnet docs; 2026-10-05):** Worldnet and Payroc are the same
> gateway with different APIs, so **key injection is the same for both**; **neither supports PCI DSS-validated P2PE**;
> the **primary key structure is TDES DUKPT**; and **device KSNs are shared with the Payroc Sales Engineer on the
> project**. Where the public Worldnet pages below say otherwise (for example sending KSNs to a Worldnet contact),
> follow the Payroc statement.
> Everything below is traceable to the snapshot (paths relative to `references/`). Anything not listed is
> **not documented in snapshot** — treat it as an open question, not an answer. No key values are reproduced:
> the PAX page publishes test key material; **do not copy it**.

## Documented

| Topic | What the snapshot says | Source |
|---|---|---|
| **PIN key vs data key (PAX)** | PAX devices must be configured with **DUKPT** keys to decrypt EBT/EMV transactions. Two separate slots must be injected: **Slot 1 — online PIN encryption**, **Slot 2 — data encryption** (the page lists published test keys for testing — not reproduced here). | `pages/gochip/pos/devices/pax.md` |
| **KSN registration** | When a device ships with Worldnet **test/live keys**, the device's **KSN must be added to Worldnet's HSM** for decryption. A "KSN error" is the symptom. The wiki says to supply the **first 10 digits of the EMV and TRACK KSNs** to the Worldnet contact; **for Payroc projects the KSNs go to the project's Payroc SE** (confirmed by Payroc). | `pages/gochip/support/troubleshooting.md` (FAQ "What is a KSN Error?") |
| **Ingenico setup** | Configuration files are loaded with Ingenico's **LLT tool (5.x, supplied by Ingenico)** with the device in LLT mode: clean the terminal, load the firmware package (`.OGZ` RBA/UPP) and config files (EMV contact/contactless XML, prompts, tips file). Firmware can also be loaded programmatically (`loadFirmware` in the SDK / Websockets request). Different SELF devices need different firmware paths. | `pages/gochip/support/device_configuration.md` |
| **On-device key injection menu (Ingenico)** | After loading firmware, if the device shows a **key injection** option, the documented step is to choose **"NO Key Injection"** and delete the KIA/RKI entry; a `KIACFG.txt` file disables key injection (iUC285 only). The page does not explain where keys come from instead. | `pages/gochip/support/device_configuration.md` |
| **Firmware variants** | Firmware package names include a DUKPT variant for some devices (for example SELF series live packages). Device download list: `pages/gochip/downloads/devices.md`. | `pages/gochip/support/device_configuration.md` |
| **Device families and platforms** | IDTech, Ingenico, PAX (app runs on the device), BBPOS (mPOS). Model tables in `sdks.md`. | `references/sdks.md` |
| **EBT / PIN** | EBT on PAX needs an EBT PIN key slot; EBT on FiServ and TSYS processors. | `pages/gochip/pos/devices/pax/ebt.md`, `references/sdks.md` |

## Payroc side (from the Payroc skills, for contrast)

- **Payroc Cloud:** physical device configuration, pairing and binding a real serial number are **out of scope**
  of the Payroc Cloud API/skill; the API starts once a device `serialNumber` exists (`GET /devices`). A Cloud
  simulator issues mock serial numbers for testing (`integrate-payroc-cloud`).
- **Terminal orders:** placing an order is API-driven; fulfilment and shipping are operational (SD template 8.6;
  `order-a-terminal`).

## Not documented in snapshot (open questions → SD 8.6b)

- Who owns the base derivation keys / key hierarchy (Payroc, processor, ISV, device vendor), and whether PIN and data
  keys use separate hierarchies for each device model. (Key structure is TDES DUKPT — confirmed; P2PE is not
  supported — confirmed.)
- **Remote key injection (RKI) vs direct injection** per device model; who injects, where, turnaround; re-injection
  after RMA/swap; key rotation, expiry and destruction. (Same process for Worldnet and Payroc — confirmed.)
- How keys for IDTech, Ingenico and BBPOS devices are provided and registered (only PAX slots and the generic KSN
  step are documented).
- How test and production key sets are separated and what evidence certification needs.
- PCI PIN scope (given no validated P2PE), PTS versions and end-of-life, EMV L2/L3 certification process.
- Hardware procurement, staging and shipping; who maps device serial/KSN to the merchant terminal.
- Terminal-estate / TMS management (apps, parameters, OS/firmware updates, per-merchant groups).
- Support responsibilities and SLAs for device issues.

## Snapshot caveat
The snapshot contains unresolved wiki macros such as `%CompanyContact` (the public wiki does not name the contact
for integration issues). For KSNs on Payroc projects the recipient is the project's Payroc SE; for other
integration issues confirm the right contact rather than assuming one.
