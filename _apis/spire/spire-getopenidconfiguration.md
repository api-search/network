---
aid: spire:spire-getopenidconfiguration
name: SPIRE Get OpenID Connect discovery document
tags:
- Discovery
humanURL: 
properties: []
description: >-
  Returns the OpenID Connect discovery document describing the OIDC provider's configuration. The document includes the issuer URL, JWKS URI, supported response types, subject types, and supported signing algorithms. This endpoint is used by OIDC-compatible systems to auto-configure themselves to validate JWT-SVIDs issued by SPIRE. The path prefix can be customized via the server_path_prefix option.

---
