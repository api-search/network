---
aid: plaid:plaid-incomeverificationcreate
name: Plaid (Deprecated) Create an income verification instance
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished process...

---
