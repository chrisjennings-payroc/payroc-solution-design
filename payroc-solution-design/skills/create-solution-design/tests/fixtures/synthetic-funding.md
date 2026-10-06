# Integration plan

Goal: SYNTHETIC test plan - not real plan-builder output.

Docs release: `0000000000000000000000000000000000000000000000000000000000000000`
Source: `0000000000000000000000000000000000000000`
Builder: `0.0.0-synthetic`
Spec SHA-256: `0000000000000000000000000000000000000000000000000000000000000000`
Plan origin: synthetic · request `synthetic` · model `none` · prompt version `none` · contract `docs-planner/1` · docs `production` `0000000000000000000000000000000000000000000000000000000000000000`

## Tasks
### Task 1: Create a merchant platform, then optionally remind the merchant to sign.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000001`
- [Open documentation](https://docs.payroc.com/workflows/create-merchant-platform)

**Goal:**
> Create a merchant platform, then optionally remind the merchant to sign.

**APIs to call, in order:**

1. `POST /merchant-platforms`: [Create merchant platform](https://docs.payroc.com/api/create-merchant)
2. `POST /processing-accounts/{processingAccountId}/reminders`: [Create reminder for processing account](https://docs.payroc.com/api/create-reminder)
3. Manual step `step3`: The merchant signs the pricing agreement out of band via the signature email sent at boarding (each processing account here uses signature.type requestedViaEmail; a direct-link signature is signed via its link instead). Not a Payroc REST operation; the optional reminder step above only re-sends the 

**Workflow:**

- [Create a merchant platform, then optionally remind the merchant to sign.](https://docs.payroc.com/workflows/create-merchant-platform): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 2: Create a funding recipient, then optionally add extra accounts and owners.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000002`
- [Open documentation](https://docs.payroc.com/workflows/set-up-a-funding-recipient)

**Goal:**
> Create a funding recipient, then optionally add extra accounts and owners.

**APIs to call, in order:**

1. `POST /funding-recipients`: [Create funding recipient](https://docs.payroc.com/api/create-funding-recipient)
2. `POST /funding-recipients/{recipientId}/funding-accounts`: [Create funding account](https://docs.payroc.com/api/create-fund-recipient-funding-account)
3. `POST /funding-recipients/{recipientId}/owners`: [Create funding recipient owner](https://docs.payroc.com/api/create-fund-recipient-owner)

**Workflow:**

- [Create a funding recipient, then optionally add extra accounts and owners.](https://docs.payroc.com/workflows/set-up-a-funding-recipient): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 3: Create a funding recipient, optionally check the balance, then send funds via a funding in

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000003`
- [Open documentation](https://docs.payroc.com/workflows/send-funds-to-a-merchant)

**Goal:**
> Create a funding recipient, optionally check the balance, then send funds via a funding instruction.

**APIs to call, in order:**

1. Manual step `step1`: Compose the set-up-a-funding-recipient sub-workflow to create the funding recipient together with its inline owner and credit funding account. Surfaces the recipientId and fundingAccountId used as the destination of the funding instruction. [set-up-a-funding-recipient](/workflows/set-up-a-funding-re
2. `GET /funding-balance`: [List funding balances](https://docs.payroc.com/api/get-funding-balance)
3. `POST /funding-instructions`: [Create funding instruction](https://docs.payroc.com/api/create-instruction)

**Workflow:**

- [Create a funding recipient, optionally check the balance, then send funds via a funding instruction.](https://docs.payroc.com/workflows/send-funds-to-a-merchant): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 4: Read funding balances then the funding activity ledger.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000004`
- [Open documentation](https://docs.payroc.com/workflows/review-funding-activity)

**Goal:**
> Read funding balances then the funding activity ledger.

**APIs to call, in order:**

1. `GET /funding-balance`: [List funding balances](https://docs.payroc.com/api/get-funding-balance)
2. `GET /funding-activity`: [List funding activity](https://docs.payroc.com/api/get-funding-activity)

**Workflow:**

- [Read funding balances then the funding activity ledger.](https://docs.payroc.com/workflows/review-funding-activity): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 5: List then drill into settlement reports across five report types.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000005`
- [Open documentation](https://docs.payroc.com/workflows/review-settlement-reporting)

**Goal:**
> List then drill into settlement reports across five report types.

**APIs to call, in order:**

1. `GET /batches`: [List batches](https://docs.payroc.com/api/getbatches)
2. `GET /batches/{batchId}`: [Retrieve batch](https://docs.payroc.com/api/getbatch)
3. `GET /transactions`: [List transactions](https://docs.payroc.com/api/get-transactions)
4. `GET /transactions/{transactionId}`: [Retrieve transaction](https://docs.payroc.com/api/gettransaction)
5. `GET /authorizations`: [List authorizations](https://docs.payroc.com/api/get-authorizations)
6. `GET /authorizations/{authorizationId}`: [Retrieve authorization](https://docs.payroc.com/api/get-authorization)
7. `GET /disputes`: [List disputes](https://docs.payroc.com/api/getdisputes)
8. `GET /disputes/{disputeId}/statuses`: [List dispute statuses](https://docs.payroc.com/api/getdisputes-statuses)
9. `GET /ach-deposits`: [List ACH deposits](https://docs.payroc.com/api/get-ach-deposits)
10. `GET /ach-deposits/{achDepositId}`: [Retrieve ACH deposit](https://docs.payroc.com/api/get-ach-deposit)
11. `GET /ach-deposit-fees`: [List ACH deposit fees](https://docs.payroc.com/api/get-ach-deposit-fees)

**Workflow:**

- [List then drill into settlement reports across five report types.](https://docs.payroc.com/workflows/review-settlement-reporting): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

## Generated summary — not instructions; the linked documentation is authoritative.

### Synthetic plan

Synthetic brief.

### How we read your brief

- “synthetic”: create-merchant-platform

### Why this order

Synthetic ordering.

### Assumptions

- Synthetic assumption.
