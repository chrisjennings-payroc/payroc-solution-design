# Worldnet sandbox, test data and go-live (derived)

> Sources: `pages/selfcare/integration_docs/introduction.md` ("Testing Guide"), `pages/selfcare/integration_docs/sandbox_testing.md`,
> `pages/selfcare/developer/f_a_q.md`, `pages/selfcare/developer/understanding_the_integration.md`, `pages/gochip/support/troubleshooting.md`,
> `merchant-api/openapi_worldnet.yaml`. Paths relative to `references/`.
>
> **SECRETS WARNING:** `sandbox_testing.md` publishes shared sandbox API keys, terminal secrets and Shopify passwords, and several pages contain sample
> secrets and device test keys. This summary intentionally **omits all of them**. Tell partners to obtain credentials from the sandbox sign-up / Worldnet
> support; never paste them into a Solution Design.

## 1. Sandbox access

| Item | Detail | Source |
|---|---|---|
| Sign-up | "Sign up for a sandbox account" at `https://developers.worldnetpayments.com/signup` (also `/selfcare/signup` in some pages) | `hosted_pages/introduction.md`, `3d_secure.md` |
| Sandbox host | `https://testpayments.worldnettps.com/merchant/` (REST base, HPP pages, MPI, bulk, account-updater reply) | spec `servers`, HPP pages |
| Dev host (SDK config) | `https://devpayments.worldnettps.com/merchant` | `pages/gochip/support/troubleshooting.md` |
| What the shared sandbox is | "shared testing account", **one account per currency**, "very basic functionality and no access to the back-end Merchant Selfcare" | `sandbox_testing.md` |
| Published shared accounts | Sandbox **EU** (ID 4479): EUR and GBP terminals, processor Elavon. Sandbox **US** (ID 4480): USD terminal, processor FDRC. Each has a merchant API key (REST only), terminal secret and Shopify password - **values omitted here** | `sandbox_testing.md` |
| What you can test on shared sandbox | Basic sales and refunds with any of the three integration methods, incl. DCC | `sandbox_testing.md` |
| Needs a **full test account** | Pre-auths, completions, secure tokens ("SecureCard"), subscriptions, unreferenced refunds, other currencies/features, **HPP page customization** - request by email to Worldnet support (address obfuscated in snapshot) | `sandbox_testing.md` |
| Full test account contents | Login to Virtual Terminal + Selfcare, test Terminal ID | `troubleshooting.md` (gochip FAQ) |
| REST keys | Merchant-level keys self-service in Selfcare (Settings -> API Keys); ISV integration keys by support | spec "Generating an API Key" |
| Gateway variants | The wiki also mentions a "CashFlows Gateway" sandbox page - **not in snapshot** | `developer/integration_docs.md` |

Note the apparent conflict: the spec tells developers to log into Selfcare on the sandbox with credentials from a welcome email, while the shared sandbox has no
Selfcare. Resolve by requesting a full test account.

## 2. Published test cards (public test numbers; `integration_docs/introduction.md`)

| Scheme | Test number | CVV required |
|---|---|---|
| American Express | 3400000000000000 | Y |
| Debit MasterCard | 5100270000000007 | Y |
| Diners | 3600000000000008 | N |
| Discover | 6011000000000004 | Y |
| JCB | 3528000000000007 | Y |
| Maestro | 5000330000000000 | Y |
| MasterCard | 5001650000000000 | Y |
| Switch | 6301144000000009 | N |
| Visa Credit | 4539858876047062 | Y |
| Visa Debit | 4000060000000006 | Y |
| Visa Electron | 4001020000000009 | N |

Any future expiry; CVV 3 digits (4 for Amex). **EBT** test cards exist (Food Stamp / Cash Only / Inactive) with a published test PIN - EBT supported only on FiServ and TSYS processors;
see the page for numbers. Live and expired cards must not be used in test (PCI).

## 3. Simulating responses

| Mechanism | Rule | Source |
|---|---|---|
| Cent values (host simulator) | `.01` Declined, `.02` Referral, `.03` CVV failure (decline), anything else Authorised (e.g. 5.01 declines) | `integration_docs/introduction.md` |
| SDK on First Data terminals | < $100.00 approved; $45.67 = no host response (time-out reversal test); > $100.00 returns a response code from the last three digits | `gochip/support/troubleshooting.md` |
| SDK on TSYS Sierra terminals | same cent-value table; Amex $10.00 triggers timeout | `gochip/support/troubleshooting.md` |
| Card-present testing | Needs a device with **TEST firmware and TEST keys injected**; LIVE-key devices will not work on the test system; KSN registration by Worldnet | `gochip/support/troubleshooting.md` |

## 4. Sandbox testing rules (Testing Guide)

- Test only on sandbox/test accounts; never use live cards in test (PCI DSS scope/audit; Worldnet not accountable).
- Configure the test environment like live (web server, session timeout, DB, firewall, latest plugins/SDKs).
- Strongly consider **Background Validation** for HPP.
- **Always**: handle host unavailable, bad parameters, validate response hash, handle all response types, receipt-page refresh must not re-run transaction, PCI, all required currencies.
- **HPP**: customer abandons, receipt URL misconfigured, customer takes >60 minutes, simultaneous transactions, validation succeeds for all.
- **REST**: API key valid, tokens refreshed before expiry, digits-only card/CVV, 400 for bad JSON, 422 for business-rule failures.
- **Shopping carts**: digits-only card fields, order status updates, customer emails (no duplicates), session time-outs, large values (1,000 / 1,000,000).

## 5. Go-live / validation checklist items documented

1. Complete the **Testing Guide**; Worldnet must receive confirmation before it will activate the live account ("policy", `developer/f_a_q.md`). Worldnet does not test on merchants' behalf.
2. **Merchant Validation Document**: perform the relevant transaction types and supply **at least TWO successful transactions per transaction type** you will use; return completed forms to the integration team, who then confirm validation (`understanding_the_integration.md`).
3. Large merchants: specialised test scripts available on request (`introduction.md` "Advanced solutions").
4. Switch URLs from `testpayments` to live: "contact our support team for the correct URLs" (bulk page) and "The live URL will be provided once merchant testing is completed" (account updater). Live REST host: see `rest-api.md` (not stated in spec).
5. Re-enter terminal secret, Receipt/Validation/MPI/Token URLs and feature flags (3DS, Apple/Google Pay domains, DCC) on the **live** terminal; Selfcare settings are per terminal (`terminal.md`).
6. Plugins: change Account Type Test -> Live and update Terminal ID/Shared Secret (`plugins/magento.md`); Shopify "Enable test mode" toggle (`plugins/shopify.md`).
7. Card-present: live devices with live keys; KSN registered; firmware validated version (`gochip/support/troubleshooting.md`).

## 6. Suggested UAT plan skeleton for a Solution Design
- Request full test account + terminals per currency/processor; confirm processor/acquirer (feature availability varies: Apple/Google Pay and eDCC = Elavon; Level 2/3 = FDRC/TSYS; EBT = FiServ/TSYS).
- Execute positive/negative cases from section 4 plus decline simulations from section 3; capture two successes per transaction type for validation.
- Record go-live URL/secret/hash cut-over steps and owner (partner vs Worldnet support).

## Not documented in snapshot
- UAT SLAs, turnaround for full test accounts or go-live activation.
- Production hosts for HPP/MPI/bulk and the REST API (only sandbox in spec).
- Sandbox test data for ACH/PAD/bank transfer, subscriptions and 3DS challenge flows (card/account numbers, outcomes).
- Whether Worldnet UAT is reachable with Payroc UAT credentials (confirm with Product).
