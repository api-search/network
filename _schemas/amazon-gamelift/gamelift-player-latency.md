---
description: Regional latency information for a player, used when requesting a new game session. This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a player's latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.
layout: schema
name: PlayerLatency
properties_list:
- description: ''
  name: PlayerId
  type: object
- description: ''
  name: RegionIdentifier
  type: object
- description: ''
  name: LatencyInMilliseconds
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-player-latency-schema.json
slug: gamelift-player-latency
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: PlayerLatency
---
