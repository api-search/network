---
aid: plaid:plaid-identityrefresh
name: Plaid Refresh identity data
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/identity/refresh` is an optional endpoint for users of the Identity product. It initiates an on-demand extraction to fetch the most up to date Identity information from the Financial Institution. This on-demand extraction takes place in addition to the periodic extractions that automatically occur for any Identity-enabled Item. If changes to Identity are discovered after calling `/identity/refresh`, Plaid will fire a webhook [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/identity/#d...

---
