---
aid: plaid:plaid-processortokencreate
name: Plaid Create processor token
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor ...

---
