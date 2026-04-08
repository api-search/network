---
aid: plaid:plaid-processortransactionssync
name: Plaid Get incremental transaction updates on a processor token
tags:
- Plaid
humanURL: 
properties: []
description: >-
  This endpoint replaces `/processor/transactions/get` and its associated webhooks for most common use-cases.  The `/processor/transactions/sync` endpoint allows developers to subscribe to all transactions associated with a processor token and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/processor/transactions/sync` provides the same functionality as `/processor/transactions/get` and can be used instead of `/processor/transac...

---
