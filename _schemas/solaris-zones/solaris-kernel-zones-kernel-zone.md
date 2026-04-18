---
description: ''
layout: schema
name: KernelZone
properties_list:
- description: Kernel zone name
  name: name
  type: string
- description: Zone brand (solaris-kz for kernel zones)
  name: brand
  type: string
- description: Numeric zone ID
  name: id
  type: integer
- description: Zone UUID
  name: uuid
  type: string
- description: Current zone state
  name: state
  type: string
- description: Auxiliary zone states
  name: auxstate
  type: array
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-kernel-zones-kernel-zone-schema.json
slug: solaris-kernel-zones-kernel-zone
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
title: KernelZone
---
