---
description: An item in the shopping cart.
layout: schema
name: CartItem
properties_list:
- description: Unique identifier for the cart item.
  name: cart_item_id
  type: string
- description: The sys_id of the catalog item.
  name: catalog_item_id
  type: string
- description: The quantity ordered.
  name: quantity
  type: integer
- description: The subtotal for this cart item.
  name: subtotal
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-cart-item-schema.json
slug: servicenow-service-catalog-cart-item
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
title: CartItem
---
