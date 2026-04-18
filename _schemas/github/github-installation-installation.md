---
description: Installation
layout: schema
name: installation
properties_list:
- description: The ID of the installation.
  name: id
  type: integer
- description: ''
  name: account
  type: object
- description: Describe whether all repositories have been selected or there's a selection involved
  name: repository_selection
  type: string
- description: ''
  name: access_tokens_url
  type: string
- description: ''
  name: repositories_url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: app_id
  type: integer
- description: The ID of the user or organization this token is being scoped to.
  name: target_id
  type: integer
- description: ''
  name: target_type
  type: string
- description: ''
  name: permissions
  type: object
- description: ''
  name: events
  type: array
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: single_file_name
  type: string
- description: ''
  name: has_multiple_single_files
  type: boolean
- description: ''
  name: single_file_paths
  type: array
- description: ''
  name: app_slug
  type: string
- description: ''
  name: suspended_by
  type: object
- description: ''
  name: suspended_at
  type: string
- description: ''
  name: contact_email
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-installation-installation-schema.json
slug: github-installation-installation
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: installation
---
