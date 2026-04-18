---
description: Full details of a catalog item including its variables.
layout: schema
name: CatalogItemDetail
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
- description: The full description of the item.
  name: description
  type: string
- description: The category sys_id.
  name: category
  type: string
- description: The displayed price.
  name: price
  type: string
- description: URL to the item picture.
  name: picture
  type: string
- description: Whether a file attachment is required to order the item.
  name: mandatory_attachment
  type: boolean
- description: The method used to fulfill the request.
  name: request_method
  type: string
- description: The list of variables (form fields) that must be filled in when ordering the item.
  name: variables
  type: array
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-catalog-item-detail-schema.json
slug: servicenow-service-catalog-catalog-item-detail
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
title: CatalogItemDetail
---
