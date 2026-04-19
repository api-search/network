---
description: Schema for a device managed by HPE Aruba Networking Central, covering access points, switches, gateways, and SD-WAN appliances in the device inventory.
layout: schema
name: Aruba Central Device
properties_list:
- description: Unique serial number identifying the device in the Aruba Central inventory.
  name: serial
  type: string
- description: MAC address of the device in colon-separated hexadecimal format.
  name: macaddr
  type: string
- description: Classification of the device type within the Aruba Central platform.
  name: device_type
  type: string
- description: Hardware model name or number of the device.
  name: model
  type: string
- description: Current firmware version running on the device.
  name: firmware_version
  type: string
- description: Current operational status of the device.
  name: status
  type: string
- description: IPv4 address assigned to the device.
  name: ip_address
  type: string
- description: User-configured name or hostname of the device.
  name: name
  type: string
- description: Name of the Aruba Central configuration group the device belongs to.
  name: group_name
  type: string
- description: Name of the physical site the device is assigned to.
  name: site
  type: string
- description: Labels assigned to the device for custom categorization and filtering.
  name: labels
  type: array
- description: Aruba hardware part number for the device.
  name: aruba_part_no
  type: string
- description: Aruba Central customer ID that owns the device.
  name: customer_id
  type: string
- description: Name of the customer organization that owns the device.
  name: customer_name
  type: string
- description: Deployment mode for access point devices. IAP indicates Instant AP mode, AOS10 indicates the AOS 10 architecture.
  name: ap_deployment_mode
  type: string
- description: Identifier of the Swarm or AP cluster the device belongs to (access points only).
  name: swarm_id
  type: string
- description: Name of the Swarm or AP cluster.
  name: swarm_name
  type: string
- description: Cluster identifier for the device.
  name: cluster_id
  type: string
- description: Mesh networking role of the access point.
  name: mesh_role
  type: string
- description: Number of clients currently connected to the device.
  name: client_count
  type: integer
- description: Time since last reboot in seconds.
  name: uptime
  type: integer
- description: Current CPU utilization as a percentage.
  name: cpu_utilization
  type: integer
- description: Total device memory in bytes.
  name: mem_total
  type: integer
- description: Available free memory in bytes.
  name: mem_free
  type: integer
- description: Radio interfaces on the device (access points only).
  name: radios
  type: array
- description: Physical uplink connection details.
  name: uplink
  type: object
- description: ISO 8601 timestamp of the last configuration change on the device.
  name: last_modified
  type: string
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-device-schema.json
slug: aruba-device
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Aruba Central Device
---
