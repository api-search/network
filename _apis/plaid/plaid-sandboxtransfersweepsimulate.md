---
aid: plaid:plaid-sandboxtransfersweepsimulate
name: Plaid Simulate creating a sweep
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all transfers with a sweep status of `swept` will become `swept_settled`, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.

---
