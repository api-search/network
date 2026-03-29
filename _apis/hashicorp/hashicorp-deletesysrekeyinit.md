---
aid: hashicorp:hashicorp-deletesysrekeyinit
name: Cancels any in-progress rekey.
tags:
- system
humanURL: 
properties: []
description: >-
  This clears the rekey settings as well as any progress made. This must be called to change the parameters of the rekey. Note: verification is still a part of a rekey. If rekeying is canceled during the verification flow, the current unseal keys remain valid.

---
