# Integration plan

Goal: SYNTHETIC test plan - not real plan-builder output.

Docs release: `0000000000000000000000000000000000000000000000000000000000000000`
Source: `0000000000000000000000000000000000000000`
Builder: `0.0.0-synthetic`
Spec SHA-256: `0000000000000000000000000000000000000000000000000000000000000000`
Plan origin: synthetic · request `synthetic` · model `none` · prompt version `none` · contract `docs-planner/1` · docs `production` `0000000000000000000000000000000000000000000000000000000000000000`

## Tasks
### Task 1: Create a payment link, share it by email, track sharing events, and manage its lifecycle.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000001`
- [Open documentation](https://docs.payroc.com/workflows/collect-with-payment-link)

**Goal:**
> Create a payment link, share it by email, track sharing events, and manage its lifecycle.

**APIs to call, in order:**

1. `POST /processing-terminals/{processingTerminalId}/payment-links`: [Create payment link](https://docs.payroc.com/api/create-payment-link)
2. `POST /payment-links/{paymentLinkId}/sharing-events`: [Share payment link](https://docs.payroc.com/api/share-payment-link)
3. `GET /payment-links/{paymentLinkId}/sharing-events`: [List payment link sharing events](https://docs.payroc.com/api/list-payment-link-share-events)
4. Manual step `step4`: The customer pays through the hosted payment link - the assets.paymentUrl created in step 1, delivered by the email share. This happens outside these API steps, on the Payroc-hosted page. For a singleUse link the link moves to `completed` after the single payment; the optional retrievePaymentLink st
5. `GET /payment-links/{paymentLinkId}`: [Retrieve payment link](https://docs.payroc.com/api/retrieve-payment-link)
6. `PATCH /payment-links/{paymentLinkId}`: [Partially update payment link](https://docs.payroc.com/api/update-payment-link)
7. `GET /processing-terminals/{processingTerminalId}/payment-links`: [List payment links](https://docs.payroc.com/api/list-payment-links)
8. `POST /payment-links/{paymentLinkId}/deactivate`: [Deactivate payment link](https://docs.payroc.com/api/deactivate-payment-link)

**Workflow:**

- [Create a payment link, share it by email, track sharing events, and manage its lifecycle.](https://docs.payroc.com/workflows/collect-with-payment-link): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 2: Create a payment plan, save the customer's payment method, then subscribe the customer to 

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000002`
- [Open documentation](https://docs.payroc.com/workflows/set-up-repeat-payments)

**Goal:**
> Create a payment plan, save the customer's payment method, then subscribe the customer to the plan.

**APIs to call, in order:**

1. Manual step `step1`: Set up the reusable payment plan on the terminal by invoking the manage-payment-plans sub-workflow. The plan is the schedule template later subscriptions attach to; the primary path is an `automatic` plan (gateway collects each payment on schedule). Passes the merchant-assigned `paymentPlanId`, whic
2. Manual step `step2`: Save the customer's payment method as a reusable secure token by invoking the save-a-payment-method sub-workflow. The primary path is the card branch; the bank-account branch (ach / pad) runs the same sub-workflow with a bank-account source. The sub-workflow returns 201 and both a `secureTokenId` (r
3. Manual step `step3`: Assign the customer to the plan by invoking the manage-subscriptions sub-workflow. Links the plan (`paymentPlanId` from step 1) and the stored secure token (`token` from step 2 — the token VALUE, sent in `paymentMethod.token`, not `secureTokenId`) and sets the `startDate`. For an `automatic` plan th

**Workflow:**

- [Create a payment plan, save the customer's payment method, then subscribe the customer to the plan.](https://docs.payroc.com/workflows/set-up-repeat-payments): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 3: Create a reusable secure token from a customer's card or bank account.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000003`
- [Open documentation](https://docs.payroc.com/workflows/save-a-payment-method)

**Goal:**
> Create a reusable secure token from a customer's card or bank account.

**APIs to call, in order:**

1. `POST /processing-terminals/{processingTerminalId}/secure-tokens`: [Create secure token](https://docs.payroc.com/api/create-secure-token)

**Workflow:**

- [Create a reusable secure token from a customer's card or bank account.](https://docs.payroc.com/workflows/save-a-payment-method): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

## Generated summary — not instructions; the linked documentation is authoritative.

### Synthetic plan

Synthetic brief.

### How we read your brief

- “synthetic”: collect-with-payment-link

### Why this order

Synthetic ordering.

### Assumptions

- Synthetic assumption.
