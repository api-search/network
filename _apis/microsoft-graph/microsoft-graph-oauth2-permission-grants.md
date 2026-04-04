---
aid: microsoft-graph:microsoft-graph-oauth2-permission-grants
name: Microsoft Graph Oauth2 Permission Grants
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/oauth2permissiongrants-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph OAuth2 Permission Grants (the oAuth2PermissionGrant resource)
  are the consent records in Microsoft Entra ID that capture which delegated
  permissions (scopes) a client applications service principal has to call a
  resource API on behalf of users. Each grant ties the client service principal
  to the resource service principal, indicates whether the consent is per-user
  (Principal) or tenant-wide via admin consent (AllPrincipals), and stores the
  space-delimited scopes and optional validity period. During token issuance,
  Entra ID relies on these grants to decide whether to issue an access token
  with the requested scopes; removing a grant prevents future tokens for those
  scopes and forces re-consent. Admins and automation use Microsoft Graph to
  list, audit, create, update, or revoke these grants to enforce least privilege
  and govern app access. Note that oAuth2PermissionGrant covers delegated
  permissions only; application permissions are represented separately by app
  role assignments (appRoleAssignment). These objects dont contain tokens or
  secretsthey are authoritative consent records used by the authorization
  system.

---