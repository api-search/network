---
description: A budget line item for a construction project.
layout: schema
name: Budget
properties_list:
- description: Agave budget line item identifier.
  name: id
  type: string
- description: Associated project identifier.
  name: project_id
  type: string
- description: Associated cost code identifier.
  name: cost_code_id
  type: string
- description: Budget line item description.
  name: description
  type: string
- description: Original budgeted amount in USD.
  name: original_amount
  type: number
- description: Revised budget amount including changes.
  name: revised_amount
  type: number
- description: Actual cost incurred to date.
  name: actual_cost
  type: number
- description: Total projected cost at completion.
  name: projected_cost
  type: number
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-budget-schema.json
slug: unified-api-budget
tags:
- Accounting
- Construction
- Integration
title: Budget
---
