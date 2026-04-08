---
aid: spiffe:spiffe-gettrustbundle
name: SPIFFE Get trust bundle
tags:
- Bundle
humanURL: 
properties: []
description: >-
  Returns the current trust bundle for this SPIFFE trust domain as a JWKS (JSON Web Key Set) document. The trust bundle contains the root CA certificates that are used to validate X.509-SVIDs and JWT-SVIDs issued by this trust domain. Foreign SPIFFE implementations poll this endpoint to stay synchronized with trust bundle updates, enabling cross-domain workload authentication. The response is a standard JWKS document where each key entry represents a root CA certificate encoded as an X.509 cert...

---
