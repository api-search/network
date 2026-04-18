---
description: ''
layout: schema
name: InventoryItem
properties_list:
- description: Inventory item identifier
  name: inventoryItemId
  type: integer
- description: Item number
  name: segment1
  type: string
- description: Item description
  name: description
  type: string
- description: Extended item description
  name: longDescription
  type: string
- description: Primary unit of measure
  name: primaryUomCode
  type: string
- description: Item type
  name: itemType
  type: string
- description: Item status code
  name: inventoryItemStatusCode
  type: string
- description: Inventory organization identifier
  name: organizationId
  type: integer
- description: Weight unit of measure
  name: weightUomCode
  type: string
- description: Unit weight
  name: unitWeight
  type: number
- description: Volume unit of measure
  name: volumeUomCode
  type: string
- description: Unit volume
  name: unitVolume
  type: number
- description: Item list price
  name: listPrice
  type: number
- description: ''
  name: purchasingEnabledFlag
  type: string
- description: ''
  name: customerOrderEnabledFlag
  type: string
- description: ''
  name: internalOrderEnabledFlag
  type: string
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-inventory-item-schema.json
slug: supply-chain-inventory-item
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: InventoryItem
---
