---
description: TokenInfo from GitLab API
layout: schema
name: TokenInfo
properties_list:
- description: The ID of the user who authorized the token.
  name: resource_owner_id
  type: integer
- description: Information about the OAuth application.
  name: application
  type: object
- description: List of scopes the token has been granted.
  name: scope
  type: array
- description: Remaining lifetime of the token in seconds.
  name: expires_in_seconds
  type: integer
- description: Unix timestamp of when the token was created.
  name: created_at
  type: number
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-oauth2-token-info-schema.json
slug: gitlab-oauth2-token-info
tags:
- Code
- Platform
- Software Development
- Source Control
title: TokenInfo
---
