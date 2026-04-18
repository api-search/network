---
description: group-response from GitHub API
layout: schema
name: group-response
properties_list:
- description: The URIs that are used to indicate the namespaces of the SCIM schemas.
  name: schemas
  type: array
- description: A unique identifier for the resource as defined by the provisioning client.
  name: externalId
  type: string
- description: A human-readable name for a security group.
  name: displayName
  type: string
- description: The group members.
  name: members
  type: array
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-scim-group-response-schema.json
slug: github-scim-group-response
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: group-response
---
