---
aid: auth0:auth0-mfa-associate
name: Associates or adds a new authenticator for multi-factor authentication (MFA).
tags:
- MFA
humanURL: 
properties: []
description: >-
  If the user has active authenticators, an Access Token with the enroll scope and the audience set to https://{yourDomain}/mfa/ is required to use this endpoint. If the user has no active authenticators, you can use the mfa_token from the mfa_required error in place of an Access Token for this request. After an authenticator is added, it must be verified. To verify the authenticator, use the response values from the /mfa/associate request in place of the values returned from the /mfa/challenge...

---
