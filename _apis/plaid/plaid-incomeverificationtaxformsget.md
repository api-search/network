---
aid: plaid:plaid-incomeverificationtaxformsget
name: Plaid (Deprecated) Retrieve information from the tax documents used for income verification
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.  This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

---
