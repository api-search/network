---
aid: plaid:plaid-paymentprofilecreate
name: Plaid Create payment profile
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Use `/payment_profile/create` endpoint to create a new payment profile. To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field. You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.

---
