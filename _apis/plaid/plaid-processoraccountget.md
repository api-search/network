---
aid: plaid:plaid-processoraccountget
name: Plaid Retrieve the account associated with a processor token
tags:
- Plaid
humanURL: 
properties: []
description: >-
  This endpoint returns the account associated with a given processor token.  This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, the account balance returned may not be up-to-date; for realtime balance information, use `/processor/balance/get` instead. Note that some information is nullable.

---
