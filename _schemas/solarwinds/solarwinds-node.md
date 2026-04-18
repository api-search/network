---
description: Schema for a monitored node (network device, server, or virtual machine) in the SolarWinds Orion Platform.
layout: schema
name: SolarWinds Monitored Node
properties_list:
- description: Unique identifier for the node in Orion
  name: NodeID
  type: integer
- description: Display name of the node
  name: Caption
  type: string
- description: Primary IP address of the node
  name: IPAddress
  type: string
- description: GUID representation of the IP address
  name: IPAddressGUID
  type: string
- description: Current monitoring status of the node
  name: Status
  type: integer
- description: Human-readable status description
  name: StatusDescription
  type: string
- description: Type of machine or device
  name: MachineType
  type: string
- description: Hardware or software vendor
  name: Vendor
  type: string
- description: Node sub-type classification
  name: ObjectSubType
  type: string
- description: SNMP sysName value
  name: SysName
  type: string
- description: SNMP sysObjectID value
  name: SysObjectID
  type: string
- description: Physical location of the node
  name: Location
  type: string
- description: Contact person for the node
  name: Contact
  type: string
- description: SNMP community string
  name: Community
  type: string
- description: SNMP version used for polling
  name: SNMPVersion
  type: integer
- description: Polling engine responsible for this node
  name: EngineID
  type: integer
- description: Current CPU utilization percentage
  name: CPULoad
  type: number
- description: Current memory utilization percentage
  name: PercentMemoryUsed
  type: number
- description: Last ICMP response time in milliseconds
  name: ResponseTime
  type: integer
- description: Packet loss percentage
  name: PercentLoss
  type: number
- description: Last boot timestamp
  name: LastBoot
  type: string
- description: Last synchronization timestamp
  name: LastSync
  type: string
- description: SWIS URI for this node entity
  name: Uri
  type: string
- description: Custom properties defined for this node
  name: CustomProperties
  type: object
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-node-schema.json
slug: solarwinds-node
tags:
- Application Monitoring
- Database Monitoring
- Infrastructure
- IP Address Management
- IT Management
- ITSM
- Log Management
- Network Monitoring
- Observability
title: SolarWinds Monitored Node
---
