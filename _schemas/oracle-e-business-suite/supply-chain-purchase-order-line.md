---
description: ''
layout: schema
name: PurchaseOrderLine
properties_list:
- description: Purchase order line identifier
  name: poLineId
  type: integer
- description: Line number
  name: lineNum
  type: integer
- description: Line type
  name: lineType
  type: string
- description: Inventory item identifier
  name: itemId
  type: integer
- description: Item description
  name: itemDescription
  type: string
- description: Item category identifier
  name: categoryId
  type: integer
- description: Ordered quantity
  name: quantity
  type: number
- description: Unit of measure
  name: unitMeasLookupCode
  type: string
- description: Unit price
  name: unitPrice
  type: number
- description: Line amount
  name: amount
  type: number
- description: Need-by date
  name: needByDate
  type: string
- description: Promised date
  name: promisedDate
  type: string
- description: Line close status
  name: closedCode
  type: string
- description: ''
  name: shipments
  type: array
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-purchase-order-line-schema.json
slug: supply-chain-purchase-order-line
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: PurchaseOrderLine
---
