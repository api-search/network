---
description: Summary of a WoW character
layout: schema
name: WoWCharacterSummary
properties_list:
- description: Character reference with href
  name: character
  type: object
- description: Protected character reference
  name: protected_character
  type: object
- description: Character name
  name: name
  type: string
- description: Character ID
  name: id
  type: integer
- description: ''
  name: realm
  type: object
- description: Playable class reference
  name: playable_class
  type: object
- description: Playable race reference
  name: playable_race
  type: object
- description: Character gender
  name: gender
  type: object
- description: Character faction (Alliance or Horde)
  name: faction
  type: object
- description: Character level
  name: level
  type: integer
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-wo-w-character-summary-schema.json
slug: activision-blizzard-wo-w-character-summary
tags: []
title: WoWCharacterSummary
---
