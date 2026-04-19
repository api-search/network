---
description: <p> <b>This data type is used with the Amazon GameLift FleetIQ and game server groups.</b> </p> <p>Configuration settings for intelligent automatic scaling that uses target tracking. These settings are used to add an Auto Scaling policy when creating the corresponding Auto Scaling group. After the Auto Scaling group is created, all updates to Auto Scaling policies, including changing this policy and adding or removing other policies, is done directly on the Auto Scaling group. </p>
layout: schema
name: GameServerGroupAutoScalingPolicy
properties_list:
- description: ''
  name: EstimatedInstanceWarmup
  type: object
- description: ''
  name: TargetTrackingConfiguration
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-game-server-group-auto-scaling-policy-schema.json
slug: gamelift-game-server-group-auto-scaling-policy
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: GameServerGroupAutoScalingPolicy
---
