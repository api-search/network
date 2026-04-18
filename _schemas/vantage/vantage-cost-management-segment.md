---
description: ''
layout: schema
name: Segment
properties_list:
- description: The unique token identifier for the Segment.
  name: token
  type: string
- description: The title of the Segment.
  name: title
  type: string
- description: The VQL filter expression for the Segment.
  name: filter
  type: string
- description: The priority order of the Segment.
  name: priority
  type: integer
- description: The token of the Workspace this Segment belongs to.
  name: workspace_token
  type: string
- description: The date and time the Segment was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-segment-schema.json
slug: vantage-cost-management-segment
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Segment
---
