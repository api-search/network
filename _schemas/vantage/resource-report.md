---
description: A Resource Report that provides detailed views of individual cloud resources and their associated costs.
layout: schema
name: Vantage Resource Report
properties_list:
- description: The unique token identifier for the Resource Report.
  name: token
  type: string
- description: The title of the Resource Report.
  name: title
  type: string
- description: The VQL filter applied to the Resource Report.
  name: filter
  type: string
- description: The token of the Workspace this report belongs to.
  name: workspace_token
  type: string
- description: The date and time the Resource Report was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/resource-report.json
slug: resource-report
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Resource Report
---
