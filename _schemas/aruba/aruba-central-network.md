---
description: A wireless SSID or wired network managed by Central.
layout: schema
name: Network
properties_list:
- description: Extended Service Set Identifier (network name).
  name: essid
  type: string
- description: Network type.
  name: type
  type: string
- description: Number of connected clients.
  name: client_count
  type: integer
- description: Configuration group the network belongs to.
  name: group_name
  type: string
- description: Site assignment.
  name: site
  type: string
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-network-schema.json
slug: aruba-central-network
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Network
---
