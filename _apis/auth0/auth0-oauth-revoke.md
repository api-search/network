---
aid: auth0:auth0-oauth-revoke
name: Revoke Refresh Token
tags:
- Revoke Refresh Token
humanURL: 
properties: []
description: >-
  Use this endpoint to invalidate a Refresh Token if it has been compromised. The behaviour of this endpoint depends on the state of the Refresh Token Revocation Deletes Grant toggle. If this toggle is enabled, then each revocation request invalidates not only the specific token, but all other tokens based on the same authorization grant. This means that all Refresh Tokens that have been issued for the same user, application, and audience will be revoked. If this toggle is disabled, then only t...

---
