---
consumed_apis:
- gitlab-oauth2
description: Unified capability for GitLab OAuth 2.0 authentication flows and user identity. Enables developers and platform administrators to manage OAuth application authorization, token lifecycle, and authenticated user profile retrieval.
layout: capability
name: GitLab Authentication And Identity
operations:
- description: Initiate the OAuth 2.0 authorization code flow.
  method: GET
  name: authorize-oauth
  path: /v1/authorizations
- description: Initiate the device authorization grant flow.
  method: POST
  name: authorize-device
  path: /v1/device-authorizations
- description: Exchange an authorization code, device code, or refresh token for an access token.
  method: POST
  name: exchange-token
  path: /v1/tokens
- description: Revoke an OAuth access or refresh token.
  method: POST
  name: revoke-token
  path: /v1/token-revocations
- description: Get information about the current access token.
  method: GET
  name: get-token-info
  path: /v1/token-info
- description: Get profile information about the authenticated user.
  method: GET
  name: get-user-info
  path: /v1/user-info
personas: []
provider_name: GitLab
provider_slug: gitlab
search_terms:
- authentication
- get profile information about the authenticated user.
- get information about the current oauth access token including scopes and expiration.
- token revocation.
- revoke an existing oauth access or refresh token.
- initiate the oauth 2.0 authorization code flow.
- exchange token
- software development
- revoke token
- authorize oauth
- identity
- initiate the device authorization grant flow.
- token introspection and validation.
- source control
- get user info
- device authorization grant flow for input-constrained devices.
- oauth 2.0 authorization code flow initiation.
- tokens
- exchange an authorization code, device code, or refresh token for an access token.
- authenticated user profile information.
- code
- oauth token exchange and creation.
- revoke an oauth access or refresh token.
- oauth
- get profile information about the currently authenticated user.
- authorize device
- initiate the oauth 2.0 authorization code flow with optional pkce support.
- platform
- initiate the device authorization grant flow for input-constrained devices.
- get token info
- get information about the current access token.
- gitlab
slug: authentication-and-identity
tags:
- Gitlab
- Authentication
- OAuth
- Identity
- Tokens
tools:
- description: Initiate the OAuth 2.0 authorization code flow with optional PKCE support.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: authorize-oauth
- description: Initiate the device authorization grant flow for input-constrained devices.
  hints:
    idempotent: false
    openWorld: true
    readOnly: false
  name: authorize-device
- description: Exchange an authorization code, device code, or refresh token for an access token.
  hints:
    idempotent: false
    openWorld: true
    readOnly: false
  name: exchange-token
- description: Revoke an existing OAuth access or refresh token.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: revoke-token
- description: Get information about the current OAuth access token including scopes and expiration.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-token-info
- description: Get profile information about the currently authenticated user.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-user-info
---
