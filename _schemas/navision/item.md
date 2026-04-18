---
description: Represents an inventory item entity in Dynamics 365 Business Central. Items are the goods or services that the company buys, sells, or holds in inventory. Each item record contains pricing, categorization, unit of measure, tax, and posting group information.
layout: schema
name: Item
properties_list:
- description: ETag for optimistic concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier (GUID) of the item record
  name: id
  type: string
- description: The item number, a unique business identifier assigned automatically or manually
  name: number
  type: string
- description: The primary display name or description of the item
  name: displayName
  type: string
- description: A secondary display name or additional description for the item
  name: displayName2
  type: string
- description: 'The type of item: Inventory (physical goods tracked in stock), Service (labor or services), or Non-Inventory (physical goods not tracked in stock)'
  name: type
  type: string
- description: The unique identifier of the item category
  name: itemCategoryId
  type: string
- description: The code of the item category used for grouping and reporting
  name: itemCategoryCode
  type: string
- description: Indicates whether the item is blocked from being used in transactions
  name: blocked
  type: boolean
- description: The Global Trade Item Number (barcode) for the item
  name: gtin
  type: string
- description: The current quantity in inventory (read-only, computed from item ledger entries)
  name: inventory
  type: number
- description: The default selling unit price of the item
  name: unitPrice
  type: number
- description: Indicates whether the unit price includes tax
  name: priceIncludesTax
  type: boolean
- description: The unit cost of the item used for inventory valuation
  name: unitCost
  type: number
- description: The unique identifier of the tax group for the item
  name: taxGroupId
  type: string
- description: The tax group code that determines how the item is taxed
  name: taxGroupCode
  type: string
- description: The unique identifier of the base unit of measure
  name: baseUnitOfMeasureId
  type: string
- description: The base unit of measure code (e.g., PCS, KG, EA)
  name: baseUnitOfMeasureCode
  type: string
- description: The unique identifier of the general product posting group
  name: generalProductPostingGroupId
  type: string
- description: The general product posting group code used for G/L account mapping
  name: generalProductPostingGroupCode
  type: string
- description: The unique identifier of the inventory posting group
  name: inventoryPostingGroupId
  type: string
- description: The inventory posting group code used for inventory valuation posting
  name: inventoryPostingGroupCode
  type: string
- description: The date and time the item record was last modified (read-only)
  name: lastModifiedDateTime
  type: string
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/item.json
slug: item
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: Item
---
