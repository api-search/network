---
description: Paginated list of budget line items.
layout: schema
name: BudgetList
properties_list:
- description: Array of budget records.
  name: data
  type: array
- description: Cursor for the next page.
  name: next_cursor
  type: string
- description: Number of records returned.
  name: count
  type: integer
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-budget-list-schema.json
slug: unified-api-budget-list
tags:
- Accounting
- Construction
- Integration
title: BudgetList
---
