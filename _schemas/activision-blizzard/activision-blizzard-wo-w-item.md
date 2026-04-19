---
description: A World of Warcraft item
layout: schema
name: WoWItem
properties_list:
- description: Item ID
  name: id
  type: integer
- description: Item name
  name: name
  type: string
- description: Item quality (Common, Rare, Epic, etc.)
  name: quality
  type: object
- description: Item level
  name: level
  type: integer
- description: Item class
  name: item_class
  type: object
- description: Item subclass
  name: item_subclass
  type: object
- description: Inventory type
  name: inventory_type
  type: object
- description: Purchase price in copper
  name: purchase_price
  type: integer
- description: Sell price in copper
  name: sell_price
  type: integer
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-wo-w-item-schema.json
slug: activision-blizzard-wo-w-item
tags: []
title: WoWItem
---
