---
description: Request body for creating a core network.
layout: schema
name: CreateCoreNetworkRequest
properties_list:
- description: The ID of the global network that a core network will be a part of.
  name: GlobalNetworkId
  type: string
- description: The description of a core network.
  name: Description
  type: string
- description: Key-value tags for the core network.
  name: Tags
  type: array
provider_name: Amazon Cloud WAN
provider_slug: amazon-cloud-wan
schema_file: json-schema/cloud-wan-create-core-network-request-schema.json
slug: cloud-wan-create-core-network-request
tags:
- AWS
- Cloud WAN
- Networking
- Wide Area Network
- SD-WAN
title: CreateCoreNetworkRequest
---
