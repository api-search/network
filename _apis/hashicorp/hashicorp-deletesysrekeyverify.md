---
aid: hashicorp:hashicorp-deletesysrekeyverify
name: Cancel any in-progress rekey verification operation.
tags:
- system
humanURL: 
properties: []
description: >-
  This clears any progress made and resets the nonce. Unlike a `DELETE` against `sys/rekey/init`, this only resets the current verification operation, not the entire rekey atttempt.

---
