---
description: The authorization for an OAuth app, GitHub App, or a Personal Access Token.
layout: schema
name: authorization
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: url
  type: string
- description: A list of scopes that this authorization is in.
  name: scopes
  type: array
- description: ''
  name: token
  type: string
- description: ''
  name: token_last_eight
  type: string
- description: ''
  name: hashed_token
  type: string
- description: ''
  name: app
  type: object
- description: ''
  name: note
  type: string
- description: ''
  name: note_url
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: fingerprint
  type: string
- description: ''
  name: user
  type: object
- description: ''
  name: installation
  type: object
- description: ''
  name: expires_at
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-app-api-authorization-schema.json
slug: github-app-api-authorization
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: authorization
---
