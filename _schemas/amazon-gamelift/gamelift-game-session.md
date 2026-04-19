---
description: <p>Properties describing a game session.</p> <p>A game session in ACTIVE status can host players. When a game session ends, its status is set to <code>TERMINATED</code>. </p> <p>Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.</p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>
layout: schema
name: GameSession
properties_list:
- description: ''
  name: GameSessionId
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: FleetId
  type: object
- description: ''
  name: FleetArn
  type: object
- description: ''
  name: CreationTime
  type: object
- description: ''
  name: TerminationTime
  type: object
- description: ''
  name: CurrentPlayerSessionCount
  type: object
- description: ''
  name: MaximumPlayerSessionCount
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: StatusReason
  type: object
- description: ''
  name: GameProperties
  type: object
- description: ''
  name: IpAddress
  type: object
- description: ''
  name: DnsName
  type: object
- description: ''
  name: Port
  type: object
- description: ''
  name: PlayerSessionCreationPolicy
  type: object
- description: ''
  name: CreatorId
  type: object
- description: ''
  name: GameSessionData
  type: object
- description: ''
  name: MatchmakerData
  type: object
- description: ''
  name: Location
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-game-session-schema.json
slug: gamelift-game-session
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: GameSession
---
