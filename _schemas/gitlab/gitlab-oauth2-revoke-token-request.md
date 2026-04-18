---
description: RevokeTokenRequest from GitLab API
layout: schema
name: RevokeTokenRequest
properties_list:
- description: The application ID registered in GitLab.
  name: client_id
  type: string
- description: The application secret.
  name: client_secret
  type: string
- description: The access token or refresh token to revoke.
  name: token
  type: string
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-oauth2-revoke-token-request-schema.json
slug: gitlab-oauth2-revoke-token-request
tags:
- Code
- Platform
- Software Development
- Source Control
title: RevokeTokenRequest
---
