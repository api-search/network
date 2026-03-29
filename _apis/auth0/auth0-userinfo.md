---
aid: auth0:auth0-userinfo
name: Returns a user's profile
tags:
- User Profile
humanURL: 
properties: []
description: >-
  Given the Auth0 Access Token obtained during login, this endpoint returns a user's profile. This endpoint will work only if openid was granted as a scope for the Access Token. The user profile information included in the response depends on the scopes requested. For example, a scope of just openid may return less information than a a scope of openid profile email.

---
