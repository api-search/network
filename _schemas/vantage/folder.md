---
description: A Folder for organizing Cost Reports within a Workspace, supporting nested folder hierarchies.
layout: schema
name: Vantage Folder
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
schema_file: json-schema/folder.json
slug: folder
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Folder
---
