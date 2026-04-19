---
description: A construction project record from the linked source system.
layout: schema
name: Project
properties_list:
- description: Agave unified project identifier.
  name: id
  type: string
- description: Project identifier in the source system.
  name: source_id
  type: string
- description: Project name.
  name: name
  type: string
- description: Project number or code.
  name: number
  type: string
- description: Project status.
  name: status
  type: string
- description: Project address.
  name: address
  type: string
- description: Project start date.
  name: start_date
  type: string
- description: Estimated project completion date.
  name: estimated_completion_date
  type: string
- description: Total approved project budget in USD.
  name: total_budget
  type: number
- description: Timestamp when the record was created.
  name: created_at
  type: string
- description: Timestamp when the record was last updated.
  name: updated_at
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-project-schema.json
slug: unified-api-project
tags:
- Accounting
- Construction
- Integration
title: Project
---
