---
description: Resource capacity settings. Fleet capacity is measured in Amazon EC2 instances. Pending and terminating counts are non-zero when the fleet capacity is adjusting to a scaling event or if access to resources is temporarily affected.
layout: schema
name: EC2InstanceCounts
properties_list:
- description: ''
  name: DESIRED
  type: object
- description: ''
  name: MINIMUM
  type: object
- description: ''
  name: MAXIMUM
  type: object
- description: ''
  name: PENDING
  type: object
- description: ''
  name: ACTIVE
  type: object
- description: ''
  name: IDLE
  type: object
- description: ''
  name: TERMINATING
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-ec2-instance-counts-schema.json
slug: gamelift-ec2-instance-counts
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: EC2InstanceCounts
---
