---
description: A set of instructions for launching server processes on each instance in a fleet. Server processes run either an executable in a custom game build or a Realtime Servers script. Server process configurations are part of a fleet's runtime configuration.
layout: schema
name: ServerProcess
properties_list:
- description: ''
  name: LaunchPath
  type: object
- description: ''
  name: Parameters
  type: object
- description: ''
  name: ConcurrentExecutions
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-server-process-schema.json
slug: gamelift-server-process
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: ServerProcess
---
