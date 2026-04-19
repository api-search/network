---
description: Contains information about a routing profile.
layout: schema
name: RoutingProfile
properties_list:
- description: The identifier of the Amazon Connect instance.
  name: InstanceId
  type: string
- description: The name of the routing profile.
  name: Name
  type: string
- description: The Amazon Resource Name (ARN) of the routing profile.
  name: RoutingProfileArn
  type: string
- description: The identifier of the routing profile.
  name: RoutingProfileId
  type: string
- description: The description of the routing profile.
  name: Description
  type: string
- description: ''
  name: MediaConcurrencies
  type: array
- description: The identifier of the default outbound queue for this routing profile.
  name: DefaultOutboundQueueId
  type: string
- description: ''
  name: Tags
  type: object
- description: The number of associated queues in routing profile.
  name: NumberOfAssociatedQueues
  type: integer
- description: The number of associated users in routing profile.
  name: NumberOfAssociatedUsers
  type: integer
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/routing-profile-schema.json
slug: routing-profile
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: RoutingProfile
---
