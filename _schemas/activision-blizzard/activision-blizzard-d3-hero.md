---
description: A Diablo III hero
layout: schema
name: D3Hero
properties_list:
- description: Hero ID
  name: id
  type: integer
- description: Hero name
  name: name
  type: string
- description: Hero class
  name: class
  type: string
- description: Hero gender (0=male, 1=female)
  name: gender
  type: integer
- description: Hero level
  name: level
  type: integer
- description: Paragon level
  name: paragonLevel
  type: integer
- description: Whether this is a hardcore hero
  name: hardcore
  type: boolean
- description: Whether this is a seasonal hero
  name: seasonal
  type: boolean
- description: Whether this hero is dead
  name: dead
  type: boolean
- description: Kill statistics
  name: kills
  type: object
- description: Hero skills and runes
  name: skills
  type: object
- description: Equipped items
  name: items
  type: object
- description: Character stats
  name: stats
  type: object
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-d3-hero-schema.json
slug: activision-blizzard-d3-hero
tags: []
title: D3Hero
---
