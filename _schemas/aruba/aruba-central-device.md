---
description: Represents a device in the Aruba Central inventory including access points, switches, gateways, and SD-WAN appliances.
layout: schema
name: Device
properties_list:
- description: Unique serial number of the device.
  name: serial
  type: string
- description: MAC address of the device.
  name: macaddr
  type: string
- description: Type classification of the device.
  name: device_type
  type: string
- description: Hardware model name.
  name: model
  type: string
- description: Current firmware version running on the device.
  name: firmware_version
  type: string
- description: Current operational status.
  name: status
  type: string
- description: Name of the configuration group the device belongs to.
  name: group_name
  type: string
- description: Name of the site the device is assigned to.
  name: site
  type: string
- description: IP address of the device.
  name: ip_address
  type: string
- description: Labels assigned to the device.
  name: labels
  type: array
- description: Aruba part number for the device hardware.
  name: aruba_part_no
  type: string
- description: Customer ID associated with the device.
  name: customer_id
  type: string
- description: Customer name associated with the device.
  name: customer_name
  type: string
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-device-schema.json
slug: aruba-central-device
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Device
---
