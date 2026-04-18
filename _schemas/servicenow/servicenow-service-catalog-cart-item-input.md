---
description: Input for adding a catalog item to the cart or ordering directly.
layout: schema
name: CartItemInput
properties_list:
- description: The quantity of items to order.
  name: sysparm_quantity
  type: integer
- description: Name-value pairs for the catalog item variables. Keys are variable names and values are the user-provided entries.
  name: variables
  type: object
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-cart-item-input-schema.json
slug: servicenow-service-catalog-cart-item-input
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
title: CartItemInput
---
