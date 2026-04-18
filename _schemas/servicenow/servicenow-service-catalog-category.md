---
description: A catalog category.
layout: schema
name: Category
properties_list:
- description: Unique identifier for the category.
  name: sys_id
  type: string
- description: The display title of the category.
  name: title
  type: string
- description: A description of the category.
  name: description
  type: string
- description: The full description of the category.
  name: full_description
  type: string
- description: Child categories.
  name: subcategories
  type: array
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-category-schema.json
slug: servicenow-service-catalog-category
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
title: Category
---
