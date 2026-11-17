# Integration plan

Goal: SYNTHETIC test plan - not real plan-builder output.

Docs release: `0000000000000000000000000000000000000000000000000000000000000000`
Source: `0000000000000000000000000000000000000000`
Builder: `0.0.0-synthetic`
Spec SHA-256: `0000000000000000000000000000000000000000000000000000000000000000`
Plan origin: synthetic · request `synthetic` · model `none` · prompt version `none` · contract `docs-planner/1` · docs `production` `0000000000000000000000000000000000000000000000000000000000000000`

## Tasks
### Task 1: Find a device, push a sale instruction, poll for the result, and retrieve the payment.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000001`
- [Open documentation](https://docs.payroc.com/workflows/run-a-sale-on-a-device)

**Goal:**
> Find a device, push a sale instruction, poll for the result, and retrieve the payment.

**APIs to call, in order:**

1. `GET /devices`: [Search devices](https://docs.payroc.com/api/search-devices)
2. `POST /devices/{serialNumber}/payment-instructions`: [Submit payment instruction](https://docs.payroc.com/api/send-payment-instruction)
3. `GET /payment-instructions/{paymentInstructionId}`: [Retrieve payment instruction](https://docs.payroc.com/api/get-payment-instruction)
4. `GET /payments/{paymentId}`: [Retrieve payment](https://docs.payroc.com/api/get-payment)

**Workflow:**

- [Find a device, push a sale instruction, poll for the result, and retrieve the payment.](https://docs.payroc.com/workflows/run-a-sale-on-a-device): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 2: Submit a refund instruction to a device, poll it to completion, and retrieve the refund.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000002`
- [Open documentation](https://docs.payroc.com/workflows/refund-on-a-device)

**Goal:**
> Submit a refund instruction to a device, poll it to completion, and retrieve the refund.

**APIs to call, in order:**

1. `POST /devices/{serialNumber}/refund-instructions`: [Submit refund instruction](https://docs.payroc.com/api/send-refund-instruction)
2. `GET /refund-instructions/{refundInstructionId}`: [Retrieve refund instruction](https://docs.payroc.com/api/get-refund-instruction)
3. `GET /refunds/{refundId}`: [Retrieve refund](https://docs.payroc.com/api/get-refund)

**Workflow:**

- [Submit a refund instruction to a device, poll it to completion, and retrieve the refund.](https://docs.payroc.com/workflows/refund-on-a-device): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 3: Submit a signature instruction to a device, then retrieve the captured signature.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000003`
- [Open documentation](https://docs.payroc.com/workflows/capture-signature-on-a-device)

**Goal:**
> Submit a signature instruction to a device, then retrieve the captured signature.

**APIs to call, in order:**

1. `POST /devices/{serialNumber}/signature-instructions`: [Submit signature instruction](https://docs.payroc.com/api/send-signature-instruction)
2. `GET /signature-instructions/{signatureInstructionId}`: [Retrieve signature instruction](https://docs.payroc.com/api/get-signature-instruction)
3. `GET /signatures/{signatureId}`: [Retrieve signature](https://docs.payroc.com/api/retrieve-signature)

**Workflow:**

- [Submit a signature instruction to a device, then retrieve the captured signature.](https://docs.payroc.com/workflows/capture-signature-on-a-device): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

### Task 4: Retrieve terminal, host, and device configuration for a Payroc Cloud device.

- [ ] Task complete
- Step ID: `SYNTHETIC00000000000000000004`
- [Open documentation](https://docs.payroc.com/workflows/configure-a-device)

**Goal:**
> Retrieve terminal, host, and device configuration for a Payroc Cloud device.

**APIs to call, in order:**

1. `GET /processing-terminals/{processingTerminalId}`: [Retrieve processing terminal](https://docs.payroc.com/api/get-processing-terminal)
2. `GET /processing-terminals/{processingTerminalId}/host-configurations`: [Retrieve host processor configuration](https://docs.payroc.com/api/get-processing-terminal-host-configuration)
3. `GET /processing-terminals/{processingTerminalId}/device-configurations/{model}`: [Retrieve a device configuration](https://docs.payroc.com/api/retrieve-device-configuration)

**Workflow:**

- [Retrieve terminal, host, and device configuration for a Payroc Cloud device.](https://docs.payroc.com/workflows/configure-a-device): this task's workflow

**Done when:**

- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.

## Generated summary — not instructions; the linked documentation is authoritative.

### Synthetic plan

Synthetic brief.

### How we read your brief

- “synthetic”: run-a-sale-on-a-device

### Why this order

Synthetic ordering.

### Assumptions

- Synthetic assumption.
