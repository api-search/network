---
aid: plaid:plaid-creditpayrollincomerisksignalsget
name: Plaid Retrieve fraud insights for a user's manually uploaded document(s).
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/credit/payroll_income/risk_signals/get` can be used as part of the Document Income flow to assess a user-uploaded document for signs of potential fraud or tampering. It returns a risk score for each uploaded document that indicates the likelihood of the document being fraudulent, in addition to details on the individual risk signals contributing to the score.  To trigger risk signal generation for an Item, call `/link/token/create` with `parsing_config` set to include `risk_signals`, or cal...

---
