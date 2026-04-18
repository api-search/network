---
description: Authentication token for a GitHub App installed on a user or org.
layout: schema
name: installation-token
properties_list:
- description: ''
  name: token
  type: string
- description: ''
  name: expires_at
  type: string
- description: ''
  name: permissions
  type: object
- description: ''
  name: repository_selection
  type: string
- description: ''
  name: repositories
  type: array
- description: ''
  name: single_file
  type: string
- description: ''
  name: has_multiple_single_files
  type: boolean
- description: ''
  name: single_file_paths
  type: array
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-installation-installation-token-schema.json
slug: github-installation-installation-token
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: installation-token
---
