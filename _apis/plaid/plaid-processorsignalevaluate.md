---
aid: plaid:plaid-processorsignalevaluate
name: Plaid Evaluate a planned ACH transaction
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Use `/processor/signal/evaluate` to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.  In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the u...

---
