---
description: API_Entities_BulkImports model
layout: schema
name: API_Entities_BulkImports
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: bulk_import_id
  type: integer
- description: ''
  name: status
  type: string
- description: ''
  name: entity_type
  type: string
- description: ''
  name: source_full_path
  type: string
- description: ''
  name: destination_full_path
  type: string
- description: ''
  name: destination_name
  type: string
- description: ''
  name: destination_slug
  type: string
- description: ''
  name: destination_namespace
  type: string
- description: ''
  name: parent_id
  type: integer
- description: ''
  name: namespace_id
  type: integer
- description: ''
  name: project_id
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: failures
  type: array
- description: ''
  name: migrate_projects
  type: boolean
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-api-v4-bulk-imports-api_entities_bulk-imports-schema.json
slug: gitlab-api-v4-bulk-imports-api_entities_bulk-imports
tags:
- Code
- Platform
- Software Development
- Source Control
title: API_Entities_BulkImports
---
