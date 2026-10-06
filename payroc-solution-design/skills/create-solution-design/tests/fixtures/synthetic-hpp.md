# Integration plan

Goal: SYNTHETIC test plan - not real plan-builder output.

Docs release: `0000000000000000000000000000000000000000000000000000000000000000`
Source: `0000000000000000000000000000000000000000`
Builder: `0.0.0-synthetic`
Spec SHA-256: `0000000000000000000000000000000000000000000000000000000000000000`
Plan origin: synthetic · request `synthetic` · model `none` · prompt version `none` · contract `docs-planner/1` · docs `production` `0000000000000000000000000000000000000000000000000000000000000000`

## Tasks
### Task 1: Collect a payment via Payroc's redirect-based Hosted Payment Page, optionally capturing a 

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000001`
- [Open documentation](https://docs.payroc.com/workflows/collect-with-hosted-payment-page)

**Goal:**
> Collect a payment via Payroc's redirect-based Hosted Payment Page, optionally capturing a pre-authorization afterward.

**APIs to call, in order:**

1. Manual step `step1`: The merchant's website sends the authenticated, signed form POST that redirects the customer's browser to Payroc's Hosted Payment Page - not a documented Payroc REST operationId. This is the load-the-page step: a signed form POST/redirect to the gateway's hosted checkout.
2. Manual step `step2`: The customer submits their payment details on the Payroc-hosted page; the gateway processes the transaction with the processor. The HPP request configures which variant runs here: a plain sale (default, no further step required), a pre-authorization to be captured afterward by captureHostedPreAuthor
3. Manual step `step3`: The gateway returns the transaction result to the merchant's receipt/return URL and delivers it by webhook. This is where the merchant obtains the paymentId used by the optional capture step; the gateway returns it to the merchant's return URL and via webhook after the customer completes the HPP - i
4. `POST /payments/{paymentId}/capture`: [Capture payment](https://docs.payroc.com/api/capture-payment)

**Workflow:**

- [Collect a payment via Payroc's redirect-based Hosted Payment Page, optionally capturing a pre-authorization afterward.](https://docs.payroc.com/workflows/collect-with-hosted-payment-page): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 2: Create an event subscription, then discover, retrieve, and delete it.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000002`
- [Open documentation](https://docs.payroc.com/workflows/create-event-subscription)

**Goal:**
> Create an event subscription, then discover, retrieve, and delete it.

**APIs to call, in order:**

1. `POST /event-subscriptions`: [Create event subscription](https://docs.payroc.com/api/create-event-subscription)
2. Manual step `step2`: When a subscribed event occurs, Payroc sends a webhook POST carrying the CloudEvents payload to the notificationUri registered in step 1. The receiver is caller-side and not a Payroc API operation: verify the Payroc-Secret header against your copy of the secret and return a 200 to each delivery.
3. `GET /event-subscriptions`: [List event subscriptions](https://docs.payroc.com/api/list-event-subscriptions)
4. `GET /event-subscriptions/{subscriptionId}`: [Retrieve event subscription](https://docs.payroc.com/api/get-event-subscription)
5. `DELETE /event-subscriptions/{subscriptionId}`: [Delete event subscription](https://docs.payroc.com/api/delete-event-subscription)

**Workflow:**

- [Create an event subscription, then discover, retrieve, and delete it.](https://docs.payroc.com/workflows/create-event-subscription): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

## Generated summary — not instructions; the linked documentation is authoritative.

### Synthetic plan

Synthetic brief.

### How we read your brief

- “synthetic”: collect-with-hosted-payment-page

### Why this order

Synthetic ordering.

### Assumptions

- Synthetic assumption.
