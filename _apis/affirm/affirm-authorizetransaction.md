---
aid: affirm:affirm-authorizetransaction
name: Authorize a transaction
tags:
- Transactions
humanURL: 
properties: []
description: >-
  Authorizes a new transaction using a checkout token obtained after a customer completes the Affirm checkout flow. The checkout token is a one-time-use token that must be exchanged server-side within the authorization window. A successful authorization places a hold on the customer's Affirm credit and returns a transaction object with status "authorized". The transaction must subsequently be captured to initiate transfer of funds to the merchant.

---
