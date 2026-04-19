---
description: Full World of Warcraft character profile
layout: schema
name: WoWCharacter
properties_list:
- description: Character ID
  name: id
  type: integer
- description: Character name
  name: name
  type: string
- description: Character gender
  name: gender
  type: object
- description: Character faction
  name: faction
  type: object
- description: Character race
  name: race
  type: object
- description: Character class
  name: character_class
  type: object
- description: Active specialization
  name: active_spec
  type: object
- description: ''
  name: realm
  type: object
- description: ''
  name: guild
  type: object
- description: Character level
  name: level
  type: integer
- description: Character experience points
  name: experience
  type: integer
- description: Total achievement points
  name: achievement_points
  type: integer
- description: Unix timestamp of last login
  name: last_login_timestamp
  type: integer
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-wo-w-character-schema.json
slug: activision-blizzard-wo-w-character
tags: []
title: WoWCharacter
---
