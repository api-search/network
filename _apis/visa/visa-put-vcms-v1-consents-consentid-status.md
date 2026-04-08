---
aid: visa:visa-put-vcms-v1-consents-consentid-status
name: Update Consent Status
tags:
- Visa Consent Management API
humanURL: 
properties: []
description: >-
  API for Visa partners (Consent Requestors) to update consent status. Notes: Status may be set in accordance with the following state transitions, with invalid transitions resulting in a 409 error with <code>invalidConsentStateTransition</code> reason.   + ACTIVE -> PAUSED   + PAUSED -> ACTIVE   + ACTIVE -> CONSUMED

---
