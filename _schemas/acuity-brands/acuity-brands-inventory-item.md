---
description: Inventory availability record for a product
layout: schema
name: InventoryItem
properties_list:
- description: Acuity Brands product number
  name: productNumber
  type: string
- description: Product description
  name: description
  type: string
- description: Brand name
  name: brand
  type: string
- description: Total available quantity across all warehouses
  name: totalQuantity
  type: integer
- description: Per-warehouse availability
  name: warehouses
  type: array
- description: Last inventory update time
  name: updatedAt
  type: string
provider_name: acuity-brands
provider_slug: acuity-brands
schema_file: json-schema/acuity-brands-inventory-item-schema.json
slug: acuity-brands-inventory-item
tags: []
title: InventoryItem
---
