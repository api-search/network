---
description: TokenRequest from GitLab API
layout: schema
name: TokenRequest
properties_list:
- description: The grant type for the token request.
  name: grant_type
  type: string
- description: The application ID registered in GitLab.
  name: client_id
  type: string
- description: The application secret. Required for confidential clients using authorization_code or refresh_token grant types.
  name: client_secret
  type: string
- description: The authorization code received from the authorize endpoint.
  name: code
  type: string
- description: The redirect URI used in the original authorization request.
  name: redirect_uri
  type: string
- description: The PKCE code verifier corresponding to the code_challenge.
  name: code_verifier
  type: string
- description: The refresh token to exchange for a new access token.
  name: refresh_token
  type: string
- description: The device code from the device authorization response.
  name: device_code
  type: string
- description: Resource owner username. Only for password grant type.
  name: username
  type: string
- description: Resource owner password. Only for password grant type.
  name: password
  type: string
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-oauth2-token-request-schema.json
slug: gitlab-oauth2-token-request
tags:
- Code
- Platform
- Software Development
- Source Control
title: TokenRequest
---
