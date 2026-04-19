---
description: A Hearthstone card
layout: schema
name: HearthstoneCard
properties_list:
- description: Card ID
  name: id
  type: integer
- description: Whether the card is collectible (1=yes)
  name: collectible
  type: integer
- description: Card slug
  name: slug
  type: string
- description: Class ID
  name: classId
  type: integer
- description: Multi-class IDs
  name: multiClassIds
  type: array
- description: Card type ID
  name: cardTypeId
  type: integer
- description: Card set ID
  name: cardSetId
  type: integer
- description: Rarity ID
  name: rarityId
  type: integer
- description: Artist name
  name: artistName
  type: string
- description: Card health
  name: health
  type: integer
- description: Card attack
  name: attack
  type: integer
- description: Mana cost
  name: manaCost
  type: integer
- description: Card name
  name: name
  type: string
- description: Card text
  name: text
  type: string
- description: Card image URL
  name: image
  type: string
- description: Gold card image URL
  name: imageGold
  type: string
- description: Card flavor text
  name: flavorText
  type: string
- description: Cropped card image URL
  name: cropImage
  type: string
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-hearthstone-card-schema.json
slug: activision-blizzard-hearthstone-card
tags: []
title: HearthstoneCard
---
