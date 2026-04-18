---
description: ''
layout: schema
name: OnhandQuantity
properties_list:
- description: Inventory item identifier
  name: inventoryItemId
  type: integer
- description: Organization identifier
  name: organizationId
  type: integer
- description: Subinventory code
  name: subinventoryCode
  type: string
- description: Locator identifier
  name: locatorId
  type: integer
- description: Lot number
  name: lotNumber
  type: string
- description: Serial number
  name: serialNumber
  type: string
- description: On-hand quantity
  name: transactionQuantity
  type: number
- description: Unit of measure code
  name: transactionUomCode
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-onhand-quantity-schema.json
slug: supply-chain-onhand-quantity
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: OnhandQuantity
---
