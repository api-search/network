---
aid: plaid:plaid-processorsignaldecisionreport
name: Plaid Report whether you initiated an ACH transaction
tags:
- Plaid
humanURL: 
properties: []
description: >-
  After calling `/processor/signal/evaluate`, call `/processor/signal/decision/report` to report whether the transaction was initiated.  If you are using the [Plaid Transfer product](https://www.plaid.com/docs/transfer) to create transfers, it is not necessary to use this endpoint, as Plaid already knows whether the transfer was initiated.

---
