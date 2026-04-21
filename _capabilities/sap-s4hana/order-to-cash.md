---
consumed_apis:
- sales-order
description: Unified order-to-cash capability combining sales order management with items, partners, pricing, schedule lines, and text records. Used by sales operations and order management teams.
layout: capability
name: SAP S/4HANA Order-to-Cash
operations:
- description: List sales orders
  method: GET
  name: list-sales-orders
  path: /v1/sales-orders
- description: Create a sales order
  method: POST
  name: create-sales-order
  path: /v1/sales-orders
personas: []
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
search_terms:
- erp
- manufacturing
- get sales order
- finance
- create sales order item
- delete a sales order
- sales
- order-to-cash
- retrieve items for a sales order
- cloud
- logistics
- list sales order pricing
- create a new sales order
- business applications
- procurement
- sap
- update a sales order header
- retrieve partners for a sales order
- update sales order
- human resources
- create sales order
- sales order management
- retrieve a single sales order by key
- create a new sales order item
- inventory
- retrieve header pricing elements
- retrieve a list of sales orders
- retrieve text records for a sales order
- create a sales order
- list sales orders
- enterprise resource planning
- plant maintenance
- list sales order partners
- s/4hana
- delete sales order
- list sales order texts
- list sales order items
slug: order-to-cash
tags:
- SAP
- S/4HANA
- Sales
- Order-to-Cash
tools:
- description: Retrieve a list of sales orders
  hints:
    openWorld: true
    readOnly: true
  name: list-sales-orders
- description: Retrieve a single sales order by key
  hints:
    readOnly: true
  name: get-sales-order
- description: Create a new sales order
  hints: {}
  name: create-sales-order
- description: Update a sales order header
  hints: {}
  name: update-sales-order
- description: Delete a sales order
  hints:
    destructive: true
  name: delete-sales-order
- description: Retrieve items for a sales order
  hints:
    readOnly: true
  name: list-sales-order-items
- description: Create a new sales order item
  hints: {}
  name: create-sales-order-item
- description: Retrieve partners for a sales order
  hints:
    readOnly: true
  name: list-sales-order-partners
- description: Retrieve header pricing elements
  hints:
    readOnly: true
  name: list-sales-order-pricing
- description: Retrieve text records for a sales order
  hints:
    readOnly: true
  name: list-sales-order-texts
---
