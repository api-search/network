---
description: Diablo III career profile
layout: schema
name: D3CareerProfile
properties_list:
- description: Player BattleTag
  name: battletag
  type: string
- description: Paragon level
  name: paragonLevel
  type: integer
- description: Hardcore paragon level
  name: paragonLevelHardcore
  type: integer
- description: Guild name
  name: guildName
  type: string
- description: List of heroes
  name: heroes
  type: array
- description: ID of last hero played
  name: lastHeroPlayed
  type: integer
- description: Kill statistics
  name: kills
  type: object
- description: Time played by class
  name: timePlayed
  type: object
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-d3-career-profile-schema.json
slug: activision-blizzard-d3-career-profile
tags: []
title: D3CareerProfile
---
