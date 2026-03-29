---
aid: hashicorp:hashicorp-postsysrevokeforceprefix
name: Revokes all secrets or tokens generated under a given prefix immediately
tags:
- system
humanURL: 
properties: []
description: >-
  Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

---
