---
description: ''
layout: schema
name: Folder
properties_list:
- description: The unique token identifier for the Folder.
  name: token
  type: string
- description: The title of the Folder.
  name: title
  type: string
- description: The token of the parent Folder, if nested.
  name: parent_folder_token
  type: string
- description: The token of the Workspace this Folder belongs to.
  name: workspace_token
  type: string
- description: The date and time the Folder was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-folder-schema.json
slug: vantage-cost-management-folder
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Folder
---
