---
description: Detailed information about a specific Solaris zone
layout: schema
name: ZoneDetail
properties_list:
- description: Zone name
  name: name
  type: string
- description: Zone numeric ID assigned by the kernel when the zone is running
  name: id
  type: integer
- description: Universally unique identifier for the zone
  name: uuid
  type: string
- description: Current zone state
  name: state
  type: string
- description: Zone brand determining the runtime environment
  name: brand
  type: string
- description: Auxiliary state information for the zone
  name: auxstate
  type: array
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-zone-detail-schema.json
slug: solaris-rad-zonemgr-zone-detail
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
title: ZoneDetail
---
