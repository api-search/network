---
aid: zendesk:zendesk-updateuseridentity
name: Zendesk Put  Api V2 Users User_id Identities User_identity_id
tags:
- User Identities
humanURL: 
properties: []
description: >-
  This endpoint allows you to:  * Set the specified identity as verified (by setting `verified` to "true" or `verification_method` to "low") * Unverify a verified identity (by setting `verified` to "false" or `verification_method` to "none") * Update the `value` property of the specified identity  You can't change an identity's `primary` attribute with this endpoint. You must use the [Make Identity Primary](#make-identity-primary) endpoint instead.  #### Allowed For  * Agents

---
