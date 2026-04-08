---
aid: plaid:plaid-identitymatch
name: Plaid Retrieve identity match score
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.  Fields within the `balances` object will always be null when retrieved by `/identity/match`. Instead, use the free `/accounts/get` endpoint to request balance cached data, or `/accounts/balance/get` for real-time data.  This request may take some time to complete if Identity was not specified as a...

---
