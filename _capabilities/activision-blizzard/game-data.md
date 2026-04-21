---
consumed_apis:
- battle-net
description: Unified game data workflow for accessing World of Warcraft characters, realms, guilds, items, Hearthstone cards, Diablo III profiles, and StarCraft II ladder data. Used by game developers, community app builders, and gaming analytics teams.
layout: capability
name: Activision Blizzard Game Data
operations:
- description: Get a WoW character profile
  method: GET
  name: get-wow-character
  path: /v1/wow/characters/{realmSlug}/{characterName}
- description: Get WoW realm list
  method: GET
  name: get-wow-realms
  path: /v1/wow/realms
- description: Search Hearthstone cards
  method: GET
  name: search-hearthstone-cards
  path: /v1/hearthstone/cards
- description: Get Diablo III career profile
  method: GET
  name: get-diablo-profile
  path: /v1/diablo/profiles/{battletag}
personas: []
provider_name: activision-blizzard
provider_slug: activision-blizzard
search_terms:
- get a specific hearthstone card by id or slug
- Community Developer
- search hearthstone cards by class, set, mana cost, or other criteria
- world of warcraft character data
- battle.net
- diablo
- get a wow character profile
- world of warcraft realms
- world of warcraft
- get the achievements completed by a world of warcraft character
- get diablo iii career profile
- builds community tools, addons, and apps using battle.net game data
- get wow realm list
- Game Analyst
- search hearthstone cards
- get wow realms
- get wow character achievements
- diablo iii profiles
- get the list of world of warcraft realms
- gaming
- get wow character
- static and dynamic game data apis for community development
- get diablo career profile
- analyzes game statistics, leaderboards, and player performance data
- hearthstone card data
- get a world of warcraft character profile including level, class, race, guild, and achievement points
- access wow characters/realms, hearthstone cards, diablo iii profiles, and starcraft ii ladder data
- creates fan websites, discord bots, and companion apps using game data
- get diablo profile
- starcraft
- get a diablo iii career profile for a battletag account
- hearthstone
- video game data and player profiles across blizzard franchises
- get hearthstone card
- activision blizzard
- Fan App Builder
slug: game-data
tags:
- Activision Blizzard
- Battle.net
- Gaming
- World of Warcraft
- Hearthstone
- Diablo
- StarCraft
tools:
- description: Get a World of Warcraft character profile including level, class, race, guild, and achievement points
  hints:
    openWorld: true
    readOnly: true
  name: get-wow-character
- description: Get the achievements completed by a World of Warcraft character
  hints:
    openWorld: true
    readOnly: true
  name: get-wow-character-achievements
- description: Get the list of World of Warcraft realms
  hints:
    openWorld: true
    readOnly: true
  name: get-wow-realms
- description: Search Hearthstone cards by class, set, mana cost, or other criteria
  hints:
    openWorld: true
    readOnly: true
  name: search-hearthstone-cards
- description: Get a specific Hearthstone card by ID or slug
  hints:
    openWorld: false
    readOnly: true
  name: get-hearthstone-card
- description: Get a Diablo III career profile for a BattleTag account
  hints:
    openWorld: true
    readOnly: true
  name: get-diablo-career-profile
---
