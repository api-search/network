---
aid: symphony:symphony-post-v1-pubkey-app-authenticate-extensionapp
name: Symphony Authenticate extension app with public key
tags:
- Applications
- Authenticate
humanURL: 
properties: []
description: >-
  Based on an authentication request token signed by the caller's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid user, malformed authentication token, user's public key not imported in the pod, invalid token signature etc.).

---
