---
aid: plaid:plaid-processortransactionsrefresh
name: Plaid Refresh transaction data
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/processor/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for a processor token. This on-demand extraction takes place in addition to the periodic extractions that automatically occur one or more times per day for any Transactions-enabled processor token. If changes to transactions are discovered after calling `/processor/transactions/refresh`, Plaid will fire a webhook: for `/transact...

---
