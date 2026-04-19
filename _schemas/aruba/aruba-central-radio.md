---
description: Radio interface on an access point.
layout: schema
name: Radio
properties_list:
- description: Radio index (0 or 1).
  name: index
  type: integer
- description: MAC address of the radio interface.
  name: macaddr
  type: string
- description: Operating frequency band in GHz.
  name: band
  type: number
- description: Operating channel number.
  name: channel
  type: string
- description: Transmit power in dBm.
  name: power
  type: integer
- description: Effective transmit power in dBm.
  name: tx_power
  type: integer
- description: Channel utilization percentage.
  name: utilization
  type: integer
- description: Noise floor in dBm.
  name: noise_floor
  type: integer
- description: Radio operational status.
  name: status
  type: string
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-radio-schema.json
slug: aruba-central-radio
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Radio
---
