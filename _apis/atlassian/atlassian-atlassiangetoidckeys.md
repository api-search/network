---
aid: atlassian:atlassian-atlassiangetoidckeys
name: Get Keys For Oidc In Pipelines
tags:
- Get
- Keys
- Openid Connect
- Pipelines
humanURL: 
properties: []
description: >-
  This API endpoint retrieves the JSON Web Key Set (JWKS) containing the public keys used for OpenID Connect (OIDC) authentication in Bitbucket Pipelines for a specific workspace. It accepts a GET request to the path /workspaces/{workspace}/pipelines-config/identity/oidc/keys.json, where {workspace} is replaced with the workspace ID or slug. The endpoint returns a keys.json file that contains cryptographic keys used to verify JWT tokens issued by Bitbucket Pipelines' OIDC provider, enabling sec...

---
