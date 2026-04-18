---
description: ''
layout: schema
name: StatisticMetadata
properties_list:
- description: Statistics identifier
  name: ssid
  type: string
- description: Human-readable description
  name: description
  type: string
- description: Data type
  name: type
  type: string
- description: Unit of measurement (e.g., bytes, percent, count)
  name: unit
  type: string
- description: Collection interval in seconds
  name: interval
  type: integer
- description: Whether historical data is retained
  name: persistent
  type: boolean
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-statsstore-statistic-metadata-schema.json
slug: solaris-statsstore-statistic-metadata
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
title: StatisticMetadata
---
