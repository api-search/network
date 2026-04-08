---
aid: plaid:plaid-identityverificationcreate
name: Plaid Create a new Identity Verification
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided. If you don't know whether the associated user already has an active Identity Verification, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. ...

---
