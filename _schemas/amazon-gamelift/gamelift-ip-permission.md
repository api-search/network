---
description: A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an instance in a fleet. New game sessions are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges. Fleets with custom game builds must have permissions explicitly set. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.
layout: schema
name: IpPermission
properties_list:
- description: ''
  name: FromPort
  type: object
- description: ''
  name: ToPort
  type: object
- description: ''
  name: IpRange
  type: object
- description: ''
  name: Protocol
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-ip-permission-schema.json
slug: gamelift-ip-permission
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: IpPermission
---
