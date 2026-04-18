---
description: Read-only snapshot of the executing zone information
layout: schema
name: ZoneInfo
properties_list:
- description: Name of the executing zone
  name: name
  type: string
- description: Numeric zone ID
  name: id
  type: integer
- description: Zone UUID
  name: uuid
  type: string
- description: Zone brand type
  name: brand
  type: string
- description: Whether this is the global zone
  name: isGlobal
  type: boolean
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-zone-info-schema.json
slug: solaris-rad-zonemgr-zone-info
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
title: ZoneInfo
---
