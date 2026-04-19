---
description: Describes a core network.
layout: schema
name: CoreNetwork
properties_list:
- description: The ID of a core network.
  name: CoreNetworkId
  type: string
- description: The ARN of a core network.
  name: CoreNetworkArn
  type: string
- description: The ID of the global network where a core network is a part of.
  name: GlobalNetworkId
  type: string
- description: The description of a core network.
  name: Description
  type: string
- description: The current state of a core network.
  name: State
  type: string
- description: The timestamp when a core network was created.
  name: CreatedAt
  type: string
provider_name: Amazon Cloud WAN
provider_slug: amazon-cloud-wan
schema_file: json-schema/cloud-wan-core-network-schema.json
slug: cloud-wan-core-network
tags:
- AWS
- Cloud WAN
- Networking
- Wide Area Network
- SD-WAN
title: CoreNetwork
---
