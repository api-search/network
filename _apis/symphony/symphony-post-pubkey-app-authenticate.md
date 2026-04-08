---
aid: symphony:symphony-post-pubkey-app-authenticate
name: Symphony Authenticate an App with public key
tags:
- Authenticate
humanURL: 
properties: []
description: >-
  Based on an authentication request token signed by the application's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid app, malformed authentication token, app's public key not imported in the pod, invalid token signature etc.).

---
