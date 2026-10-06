# Integration plan

Goal: SYNTHETIC test plan - not real plan-builder output.

Docs release: `0000000000000000000000000000000000000000000000000000000000000000`
Source: `0000000000000000000000000000000000000000`
Builder: `0.0.0-synthetic`
Spec SHA-256: `0000000000000000000000000000000000000000000000000000000000000000`
Plan origin: synthetic · request `synthetic` · model `none` · prompt version `none` · contract `docs-planner/1` · docs `production` `0000000000000000000000000000000000000000000000000000000000000000`

## Tasks
### Task 1: Validate an Apple Pay merchant session, then run a sale with the wallet token.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000001`
- [Open documentation](https://docs.payroc.com/workflows/accept-apple-pay)

**Goal:**
> Validate an Apple Pay merchant session, then run a sale with the wallet token.

**APIs to call, in order:**

1. Manual step `step1`: PREREQUISITE, done once: the merchant's domain is registered for Apple Pay in the Self-Care Portal, which issues the `appleDomainId` input used by `startApplePaySession`. There is no API operation for this; it is an external-system step supplying an input.
2. `POST /processing-terminals/{processingTerminalId}/apple-pay-sessions`: [Start Apple Pay session](https://docs.payroc.com/api/apple-pay-sessions)
3. Manual step `step3`: The browser hands the `startSessionResponse` to the Apple Pay JS API (web flow) at the validation URL supplied by the `appleValidationUrl` input; the cardholder authorizes the charge in Apple Pay on their device, and Apple releases the encrypted payment data used by `runApplePaySale`. In the in-app 
4. `POST /payments`: [Create payment](https://docs.payroc.com/api/payment)

**Workflow:**

- [Validate an Apple Pay merchant session, then run a sale with the wallet token.](https://docs.payroc.com/workflows/accept-apple-pay): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 2: Run a sale using an encrypted Google Pay token.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000002`
- [Open documentation](https://docs.payroc.com/workflows/accept-google-pay)

**Goal:**
> Run a sale using an encrypted Google Pay token.

**APIs to call, in order:**

1. Manual step `step1`: The customer authorizes the payment through Google Pay, and the client (web page or mobile app) obtains the customer's encrypted payment details from the Google Pay API and converts them to hexadecimal - there is no dedicated Payroc session or tokenization call for Google Pay. The web and in-app var
2. `POST /payments`: [Create payment](https://docs.payroc.com/api/payment)

**Workflow:**

- [Run a sale using an encrypted Google Pay token.](https://docs.payroc.com/workflows/accept-google-pay): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 3: Run a card sale.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000003`
- [Open documentation](https://docs.payroc.com/workflows/run-a-card-sale)

**Goal:**
> Run a card sale.

**APIs to call, in order:**

1. `POST /payments`: [Create payment](https://docs.payroc.com/api/payment)

**Workflow:**

- [Run a card sale.](https://docs.payroc.com/workflows/run-a-card-sale): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

## Generated summary — not instructions; the linked documentation is authoritative.

### Synthetic plan

Synthetic brief.

### How we read your brief

- “synthetic”: accept-apple-pay

### Why this order

Synthetic ordering.

### Assumptions

- Synthetic assumption.
