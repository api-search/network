---
description: A sales opportunity or deal from a connected CRM system.
layout: schema
name: Opportunity
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: remote_id
  type: string
- description: Opportunity name.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Deal value in cents.
  name: amount
  type: integer
- description: ''
  name: owner
  type: string
- description: ''
  name: account
  type: string
- description: ''
  name: stage
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: close_date
  type: string
- description: ''
  name: last_activity_at
  type: string
- description: ''
  name: remote_was_deleted
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: modified_at
  type: string
provider_name: Merge
provider_slug: merge
schema_file: json-schema/crm-api-opportunity-schema.json
slug: crm-api-opportunity
tags:
- Integrations
- Platform
- Unified API
title: Opportunity
---
