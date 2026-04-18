---
description: ''
layout: schema
name: Artifact
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: node_id
  type: string
- description: The name of the artifact.
  name: name
  type: string
- description: The size in bytes of the artifact.
  name: size_in_bytes
  type: integer
- description: ''
  name: url
  type: string
- description: ''
  name: archive_download_url
  type: string
- description: ''
  name: expired
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: expires_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: workflow_run
  type: object
provider_name: GitHub Actions
provider_slug: github-actions
schema_file: json-schema/github-actions-artifact-schema.json
slug: github-actions-artifact
tags: []
title: Artifact
---
