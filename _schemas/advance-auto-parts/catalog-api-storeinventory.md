---
description: Inventory at a specific store.
layout: schema
name: StoreInventory
properties_list:
- description: Store identifier.
  name: storeId
  type: string
- description: Store name.
  name: storeName
  type: string
- description: Available quantity.
  name: quantity
  type: integer
- description: Whether in stock.
  name: available
  type: boolean
provider_name: Advance Auto Parts
provider_slug: advance-auto-parts
schema_file: json-schema/catalog-api-storeinventory-schema.json
slug: catalog-api-storeinventory
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
title: StoreInventory
---
