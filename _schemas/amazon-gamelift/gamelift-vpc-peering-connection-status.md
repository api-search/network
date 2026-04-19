---
description: Represents status information for a VPC peering connection. Status codes and messages are provided from EC2 (see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcPeeringConnectionStateReason.html">VpcPeeringConnectionStateReason</a>). Connection status information is also communicated as a fleet event.
layout: schema
name: VpcPeeringConnectionStatus
properties_list:
- description: ''
  name: Code
  type: object
- description: ''
  name: Message
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-vpc-peering-connection-status-schema.json
slug: gamelift-vpc-peering-connection-status
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: VpcPeeringConnectionStatus
---
