---
description: A catalog item summary.
layout: schema
name: CatalogItem
properties_list:
- description: Unique identifier for the catalog item.
  name: sys_id
  type: string
- description: The display name of the item.
  name: name
  type: string
- description: A brief description of the item.
  name: short_description
  type: string
- description: The category sys_id.
  name: category
  type: string
- description: The displayed price of the item.
  name: price
  type: string
- description: URL to the item picture.
  name: picture
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-catalog-item-schema.json
slug: servicenow-service-catalog-catalog-item
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: CatalogItem
---
