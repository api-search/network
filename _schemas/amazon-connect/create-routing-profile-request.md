---
description: CreateRoutingProfileRequest schema from Amazon Connect Service API
layout: schema
name: CreateRoutingProfileRequest
properties_list:
- description: The name of the routing profile. Must not be more than 127 characters.
  name: Name
  type: string
- description: Description of the routing profile.
  name: Description
  type: string
- description: The default outbound queue for the routing profile.
  name: DefaultOutboundQueueId
  type: string
- description: ''
  name: QueueConfigs
  type: array
- description: ''
  name: MediaConcurrencies
  type: array
- description: ''
  name: Tags
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/create-routing-profile-request-schema.json
slug: create-routing-profile-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: CreateRoutingProfileRequest
---
