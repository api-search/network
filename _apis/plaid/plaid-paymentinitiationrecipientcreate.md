---
aid: plaid:plaid-paymentinitiationrecipientcreate
name: Plaid Create payment recipient
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.  It is recommended to use `bacs` in the UK and `iban` in EU.  The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same ...

---
