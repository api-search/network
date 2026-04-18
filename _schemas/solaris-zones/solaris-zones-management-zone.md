---
description: ''
layout: schema
name: Zone
properties_list:
- description: Zone name
  name: name
  type: string
- description: Zone brand type (e.g., solaris, solaris-kz, solaris10)
  name: brand
  type: string
- description: Numeric zone ID (only when running or ready)
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
schema_file: json-schema/solaris-zones-management-zone-schema.json
slug: solaris-zones-management-zone
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
title: Zone
---
