---
description: Represents an Aruba wireless access point with monitoring data including radio information, client counts, and operational status.
layout: schema
name: AccessPoint
properties_list:
- description: Serial number of the access point.
  name: serial
  type: string
- description: Configured name of the access point.
  name: name
  type: string
- description: MAC address of the access point.
  name: macaddr
  type: string
- description: Hardware model.
  name: model
  type: string
- description: Current operational status.
  name: status
  type: string
- description: IP address of the access point.
  name: ip_address
  type: string
- description: Current firmware version.
  name: firmware_version
  type: string
- description: Configuration group assignment.
  name: group_name
  type: string
- description: Site assignment.
  name: site
  type: string
- description: Labels assigned to the access point.
  name: labels
  type: array
- description: Swarm/cluster identifier for the AP.
  name: swarm_id
  type: string
- description: Name of the Swarm/cluster.
  name: swarm_name
  type: string
- description: Cluster identifier.
  name: cluster_id
  type: string
- description: Deployment mode of the access point.
  name: ap_deployment_mode
  type: string
- description: Mesh role of the access point.
  name: mesh_role
  type: string
- description: Number of clients currently connected.
  name: client_count
  type: integer
- description: Uptime in seconds since last reboot.
  name: uptime
  type: integer
- description: Current CPU utilization percentage.
  name: cpu_utilization
  type: integer
- description: Total memory in bytes.
  name: mem_total
  type: integer
- description: Free memory in bytes.
  name: mem_free
  type: integer
- description: Radio interface information.
  name: radios
  type: array
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-access-point-schema.json
slug: aruba-central-access-point
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: AccessPoint
---
