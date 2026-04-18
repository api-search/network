---
description: Cluster system node schema from Veritas InfoScale REST API
layout: schema
name: System
properties_list:
- description: System hostname
  name: name
  type: string
- description: System state in the cluster
  name: state
  type: string
- description: Whether the system is frozen
  name: frozen
  type: boolean
- description: Current CPU usage percentage
  name: cpuUsage
  type: number
- description: Current memory usage percentage
  name: memoryUsage
  type: number
- description: Number of service groups on this system
  name: serviceGroupCount
  type: integer
- description: Operating system platform
  name: platform
  type: string
- description: Hardware architecture
  name: architecture
  type: string
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
schema_file: json-schema/rest-api-system-schema.json
slug: rest-api-system
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
title: System
---
