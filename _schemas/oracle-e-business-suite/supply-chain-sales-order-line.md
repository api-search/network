---
description: ''
layout: schema
name: SalesOrderLine
properties_list:
- description: Line identifier
  name: lineId
  type: integer
- description: Line number
  name: lineNumber
  type: integer
- description: Ordered item number
  name: orderedItem
  type: string
- description: Inventory item identifier
  name: inventoryItemId
  type: integer
- description: Ordered quantity
  name: orderedQuantity
  type: number
- description: Unit of measure
  name: orderQuantityUom
  type: string
- description: Unit selling price
  name: unitSellingPrice
  type: number
- description: Unit list price
  name: unitListPrice
  type: number
- description: ''
  name: lineAmount
  type: number
- description: Scheduled ship date
  name: scheduleShipDate
  type: string
- description: Actual ship date
  name: actualShipDate
  type: string
- description: Line flow status
  name: flowStatusCode
  type: string
- description: ''
  name: shippedQuantity
  type: number
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-sales-order-line-schema.json
slug: supply-chain-sales-order-line
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: SalesOrderLine
---
