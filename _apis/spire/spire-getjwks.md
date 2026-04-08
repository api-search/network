---
aid: spire:spire-getjwks
name: SPIRE Get JSON Web Key Set
tags:
- Keys
humanURL: 
properties: []
description: >-
  Returns the JSON Web Key Set (JWKS) containing the public keys used to verify JWT-SVIDs issued by SPIRE. The keys are derived from the SPIRE trust bundle and are automatically rotated as SPIRE rotates its signing keys. Consumers must re-fetch this endpoint periodically to stay current with key rotations. Supported signing algorithms include RS256, ES256, and ES384.

---
