---
description: ''
layout: schema
name: MaterialTransaction
properties_list:
- description: WIP entity identifier
  name: wipEntityId
  type: integer
- description: Organization identifier
  name: organizationId
  type: integer
- description: Operation sequence number
  name: operationSeqNum
  type: integer
- description: Inventory item identifier
  name: inventoryItemId
  type: integer
- description: Transaction quantity (positive=issue, negative=return)
  name: transactionQuantity
  type: number
- description: Transaction unit of measure
  name: transactionUom
  type: string
- description: Transaction type
  name: transactionType
  type: string
- description: Source/destination subinventory
  name: subinventoryCode
  type: string
- description: Locator identifier
  name: locatorId
  type: integer
- description: Transaction date
  name: transactionDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-material-transaction-schema.json
slug: manufacturing-material-transaction
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: MaterialTransaction
---
