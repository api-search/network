---
description: A World of Warcraft guild
layout: schema
name: WoWGuild
properties_list:
- description: Guild ID
  name: id
  type: integer
- description: Guild name
  name: name
  type: string
- description: Guild faction
  name: faction
  type: object
- description: ''
  name: realm
  type: object
- description: Number of guild members
  name: member_count
  type: integer
- description: Guild achievement points
  name: achievement_points
  type: integer
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-wo-w-guild-schema.json
slug: activision-blizzard-wo-w-guild
tags: []
title: WoWGuild
---
