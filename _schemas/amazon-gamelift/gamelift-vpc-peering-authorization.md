---
description: <p>Represents an authorization for a VPC peering connection between the VPC for an Amazon GameLift fleet and another VPC on an account you have access to. This authorization must exist and be valid for the peering connection to be established. Authorizations are valid for 24 hours after they are issued.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>
layout: schema
name: VpcPeeringAuthorization
properties_list:
- description: ''
  name: GameLiftAwsAccountId
  type: object
- description: ''
  name: PeerVpcAwsAccountId
  type: object
- description: ''
  name: PeerVpcId
  type: object
- description: ''
  name: CreationTime
  type: object
- description: ''
  name: ExpirationTime
  type: object
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
schema_file: json-schema/gamelift-vpc-peering-authorization-schema.json
slug: gamelift-vpc-peering-authorization
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
title: VpcPeeringAuthorization
---
