---
description: GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
layout: schema
name: integration
properties_list:
- description: Unique identifier of the GitHub app
  name: id
  type: integer
- description: The slug name of the GitHub app
  name: slug
  type: string
- description: ''
  name: node_id
  type: string
- description: ''
  name: owner
  type: object
- description: The name of the GitHub app
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: external_url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: The set of permissions for the GitHub app
  name: permissions
  type: object
- description: The list of events for the GitHub app
  name: events
  type: array
- description: The number of installations associated with the GitHub app
  name: installations_count
  type: integer
- description: ''
  name: client_id
  type: string
- description: ''
  name: client_secret
  type: string
- description: ''
  name: webhook_secret
  type: string
- description: ''
  name: pem
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-app-api-integration-schema.json
slug: github-app-api-integration
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: integration
---
