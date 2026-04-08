---
aid: plaid:plaid-transactionsrefresh
name: Plaid Refresh transaction data
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/transactions/refresh` is an optional endpoint that initiates an on-demand extraction to fetch the newest transactions for an Item. The on-demand extraction takes place in addition to the periodic extractions that automatically occur one or more times per day for any Transactions-enabled Item. The Item must already have Transactions added as a product in order to call `/transactions/refresh`.  If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a ...

---
