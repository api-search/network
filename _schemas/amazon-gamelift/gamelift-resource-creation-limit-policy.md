---
description: <p>A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.</p> <p>The policy is evaluated when a player tries to create a new game session. On receiving a <code>CreateGameSession</code> request, Amazon GameLift checks that the player (identified by <code>CreatorId</code>) has created fewer than game session limit in the specified time period.</p>
layout: schema
name: ResourceCreationLimitPolicy
properties_list:
- description: ''
  name: NewGameSessionsPerCreator
  type: object
- description: ''
  name: PolicyPeriodInMinutes
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-resource-creation-limit-policy-schema.json
slug: gamelift-resource-creation-limit-policy
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: ResourceCreationLimitPolicy
---
