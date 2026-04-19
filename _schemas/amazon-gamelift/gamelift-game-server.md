---
description: <p> <b>This data type is used with the Amazon GameLift FleetIQ and game server groups.</b> </p> <p>Properties describing a game server that is running on an instance in a game server group. </p> <p>A game server is created by a successful call to <code>RegisterGameServer</code> and deleted by calling <code>DeregisterGameServer</code>. A game server is claimed to host a game session by calling <code>ClaimGameServer</code>. </p>
layout: schema
name: GameServer
properties_list:
- description: ''
  name: GameServerGroupName
  type: object
- description: ''
  name: GameServerGroupArn
  type: object
- description: ''
  name: GameServerId
  type: object
- description: ''
  name: InstanceId
  type: object
- description: ''
  name: ConnectionInfo
  type: object
- description: ''
  name: GameServerData
  type: object
- description: ''
  name: ClaimStatus
  type: object
- description: ''
  name: UtilizationStatus
  type: object
- description: ''
  name: RegistrationTime
  type: object
- description: ''
  name: LastClaimTime
  type: object
- description: ''
  name: LastHealthCheckTime
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-game-server-schema.json
slug: gamelift-game-server
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: GameServer
---
