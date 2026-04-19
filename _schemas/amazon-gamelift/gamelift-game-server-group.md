---
description: <p> <b>This data type is used with the Amazon GameLift FleetIQ and game server groups.</b> </p> <p>Properties that describe a game server group resource. A game server group manages certain properties related to a corresponding Amazon EC2 Auto Scaling group. </p> <p>A game server group is created by a successful call to <code>CreateGameServerGroup</code> and deleted by calling <code>DeleteGameServerGroup</code>. Game server group activity can be temporarily suspended and resumed by calling <code>SuspendGameServerGroup</code> and <code>ResumeGameServerGroup</code>, respectively. </p>
layout: schema
name: GameServerGroup
properties_list:
- description: ''
  name: GameServerGroupName
  type: object
- description: ''
  name: GameServerGroupArn
  type: object
- description: ''
  name: RoleArn
  type: object
- description: ''
  name: InstanceDefinitions
  type: object
- description: ''
  name: BalancingStrategy
  type: object
- description: ''
  name: GameServerProtectionPolicy
  type: object
- description: ''
  name: AutoScalingGroupArn
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: StatusReason
  type: object
- description: ''
  name: SuspendedActions
  type: object
- description: ''
  name: CreationTime
  type: object
- description: ''
  name: LastUpdatedTime
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-game-server-group-schema.json
slug: gamelift-game-server-group
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: GameServerGroup
---
