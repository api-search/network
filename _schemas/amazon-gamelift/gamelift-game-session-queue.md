---
description: Configuration for a game session placement mechanism that processes requests for new game sessions. A queue can be used on its own or as part of a matchmaking solution.
layout: schema
name: GameSessionQueue
properties_list:
- description: ''
  name: Name
  type: object
- description: ''
  name: GameSessionQueueArn
  type: object
- description: ''
  name: TimeoutInSeconds
  type: object
- description: ''
  name: PlayerLatencyPolicies
  type: object
- description: ''
  name: Destinations
  type: object
- description: ''
  name: FilterConfiguration
  type: object
- description: ''
  name: PriorityConfiguration
  type: object
- description: ''
  name: CustomEventData
  type: object
- description: ''
  name: NotificationTarget
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-game-session-queue-schema.json
slug: gamelift-game-session-queue
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: GameSessionQueue
---
