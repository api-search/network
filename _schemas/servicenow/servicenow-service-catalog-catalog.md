---
description: A ServiceNow service catalog.
layout: schema
name: Catalog
properties_list:
- description: Unique identifier for the catalog.
  name: sys_id
  type: string
- description: The display title of the catalog.
  name: title
  type: string
- description: A description of the catalog.
  name: description
  type: string
- description: Whether the catalog has categories.
  name: has_categories
  type: boolean
- description: Whether the catalog has items.
  name: has_items
  type: boolean
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-catalog-schema.json
slug: servicenow-service-catalog-catalog
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
title: Catalog
---
