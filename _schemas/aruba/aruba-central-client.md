---
description: A client device connected to the network.
layout: schema
name: Client
properties_list:
- description: MAC address of the client.
  name: macaddr
  type: string
- description: Hostname or display name of the client.
  name: name
  type: string
- description: IP address assigned to the client.
  name: ip_address
  type: string
- description: Operating system type detected.
  name: os_type
  type: string
- description: Connection type.
  name: connection
  type: string
- description: SSID or network name the client is connected to.
  name: network
  type: string
- description: Radio band of the wireless connection.
  name: band
  type: number
- description: Channel number of the wireless connection.
  name: channel
  type: string
- description: Signal strength in dBm.
  name: signal_strength
  type: integer
- description: Signal-to-noise ratio in dB.
  name: signal_db
  type: integer
- description: Connection speed in Mbps.
  name: speed
  type: integer
- description: Serial number of the device the client is connected to.
  name: associated_device
  type: string
- description: Group name of the associated device.
  name: group_name
  type: string
- description: Site name of the associated device.
  name: site
  type: string
- description: Data usage statistics.
  name: usage
  type: object
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-client-schema.json
slug: aruba-central-client
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Client
---
