---
aid: visa:visa-put-vcms-v1-consents-consentid-constraints-remainingnumberuses
name: Update Remaining Consent Uses
tags:
- Visa Consent Management API
humanURL: 
properties: []
description: >-
  API for Visa partners (Consent Requestors) to update the remaining number of uses for a multi-use consent. Notes: + This API is idempotent. + For an active consent, this value may be set to less than or equal to the current value, and only if maxNumberUses is set as non-zero on the consent. Any violation of the above conditions will result in a 409 error with <code>invalidConsentModification</code> reason. If set to zero, the status of the consent changes to CONSUMED and is no longer active.

---
