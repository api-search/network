---
description: A node in the ONTAP cluster
layout: schema
name: ClusterNode
properties_list:
- description: Node UUID
  name: uuid
  type: string
- description: Node name
  name: name
  type: string
- description: Hardware model of the node
  name: model
  type: string
- description: System serial number
  name: serial_number
  type: string
- description: Node uptime in seconds
  name: uptime
  type: integer
- description: ONTAP version running on the node
  name: version
  type: object
- description: Node controller information
  name: controller
  type: object
- description: Current operational state of the node
  name: state
  type: string
provider_name: NetApp
provider_slug: netapp
schema_file: json-schema/netapp-ontap-cluster-node-schema.json
slug: netapp-ontap-cluster-node
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
title: ClusterNode
---
