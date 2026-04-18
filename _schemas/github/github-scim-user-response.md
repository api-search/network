---
description: user-response from GitHub API
layout: schema
name: user-response
properties_list:
- description: The URIs that are used to indicate the namespaces of the SCIM schemas.
  name: schemas
  type: array
- description: A unique identifier for the resource as defined by the provisioning client.
  name: externalId
  type: string
- description: Whether the user active in the IdP.
  name: active
  type: boolean
- description: The username for the user.
  name: userName
  type: string
- description: ''
  name: name
  type: object
- description: A human-readable name for the user.
  name: displayName
  type: string
- description: ''
  name: emails
  type: object
- description: ''
  name: roles
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-scim-user-response-schema.json
slug: github-scim-user-response
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: user-response
---
