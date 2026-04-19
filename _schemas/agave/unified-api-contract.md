---
description: A prime contract for a construction project.
layout: schema
name: Contract
properties_list:
- description: Contract identifier.
  name: id
  type: string
- description: Associated project identifier.
  name: project_id
  type: string
- description: Contract name.
  name: name
  type: string
- description: Contract number.
  name: number
  type: string
- description: Contract status.
  name: status
  type: string
- description: Original contract value in USD.
  name: original_value
  type: number
- description: Revised contract value including change orders.
  name: revised_value
  type: number
- description: Date the contract was executed.
  name: executed_date
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-contract-schema.json
slug: unified-api-contract
tags:
- Accounting
- Construction
- Integration
title: Contract
---
