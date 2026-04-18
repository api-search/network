---
description: TokenResponse from GitLab API
layout: schema
name: TokenResponse
properties_list:
- description: The OAuth 2.0 access token.
  name: access_token
  type: string
- description: The type of token. Always Bearer.
  name: token_type
  type: string
- description: Token lifetime in seconds. Typically 7200 (2 hours).
  name: expires_in
  type: integer
- description: The refresh token for obtaining new access tokens.
  name: refresh_token
  type: string
- description: Space-separated list of granted scopes.
  name: scope
  type: string
- description: Unix timestamp of when the token was created.
  name: created_at
  type: integer
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-oauth2-token-response-schema.json
slug: gitlab-oauth2-token-response
tags:
- Code
- Platform
- Software Development
- Source Control
title: TokenResponse
---
