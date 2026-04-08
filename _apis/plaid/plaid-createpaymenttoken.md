---
aid: plaid:plaid-createpaymenttoken
name: Plaid Create payment token
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.  The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a pa...

---
