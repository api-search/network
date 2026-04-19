---
description: Sets a latency cap for individual players when placing a game session. With a latency policy in force, a game session cannot be placed in a fleet location where a player reports latency higher than the cap. Latency policies are used only with placement request that provide player latency information. Player latency policies can be stacked to gradually relax latency requirements over time.
layout: schema
name: PlayerLatencyPolicy
properties_list:
- description: ''
  name: MaximumIndividualPlayerLatencyMilliseconds
  type: object
- description: ''
  name: PolicyDurationSeconds
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-player-latency-policy-schema.json
slug: gamelift-player-latency-policy
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: PlayerLatencyPolicy
---
