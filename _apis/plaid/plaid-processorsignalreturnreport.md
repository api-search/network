---
aid: plaid:plaid-processorsignalreturnreport
name: Plaid Report a return for an ACH transaction
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.  If you are using the [Plaid Transfer product](https://www.plaid.com/docs/transfer) to create transfers, it is not necessary to use this endpoint, as Plaid already knows whether the transfer was returned.

---
