---
description: A job cost code for categorizing construction costs.
layout: schema
name: CostCode
properties_list:
- description: Cost code identifier.
  name: id
  type: string
- description: Associated project identifier.
  name: project_id
  type: string
- description: Cost code value.
  name: code
  type: string
- description: Cost code description.
  name: description
  type: string
- description: Cost type classification.
  name: cost_type
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-cost-code-schema.json
slug: unified-api-cost-code
tags:
- Accounting
- Construction
- Integration
title: CostCode
---
