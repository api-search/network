---
aid: vtex:vtex-createpayment
name: VTex Create payment
tags:
- Payment Flow
humanURL: 
properties: []
description: >-
  Creates a new payment and initiates the payment flow.  > ℹ️ This request is made from VTEX to the payment provider.  Payment providers must:  - Execute authorization on payments made through credit/debit card or any synchronized payments;  - Return the required information to the customer on payments made through bank-issued invoice, redirect, or any async payments.   >ℹ️ This endpoint has to meet the principle of [idempotence](https://en.wikipedia.org/wiki/Idempotence). When callin...

---
