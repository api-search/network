---
aid: vtex:vtex-4doauthorization
name: VTex 4. Authorize new transaction
tags:
- Transaction Process
humanURL: 
properties: []
description: >-
  The fourth and last step to create a new transaction. It will authorized the new transaction creation according to the data previously informed in the latests requests.  This step is the trigger to process each of payments that were received in step 2.  Each payment will be sent to acquirer. If all payments are authorized, the transaction will be authorized. If one of the payments is denied, all payments in transaction will be cancelled.  ## Permissions  Any user or [application key](...

---
