---
description: Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
layout: schema
name: Player
properties_list:
- description: ''
  name: PlayerId
  type: object
- description: ''
  name: PlayerAttributes
  type: object
- description: ''
  name: Team
  type: object
- description: ''
  name: LatencyInMs
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-player-schema.json
slug: gamelift-player
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: Player
---
