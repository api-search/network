---
description: Represents runtime state information for a Solaris zone as reported by zoneadm(8) and the RAD zonemgr module, including lifecycle state, resource utilization, and migration status.
layout: schema
name: Oracle Solaris Zone State
properties_list:
- description: Unique name identifying the zone on the system
  name: name
  type: string
- description: Kernel-assigned numeric zone ID, present only when the zone is running or ready
  name: id
  type: integer
- description: Universally unique identifier for the zone
  name: uuid
  type: string
- description: Current lifecycle state of the zone
  name: state
  type: string
- description: Zone brand type determining the runtime environment
  name: brand
  type: string
- description: Auxiliary state flags providing additional zone status information
  name: auxstate
  type: array
- description: Whether this is the global (host) zone
  name: isGlobal
  type: boolean
- description: File system path for the zone root
  name: zonepath
  type: string
- description: ''
  name: stateChange
  type: object
- description: ''
  name: migrationState
  type: object
- description: ''
  name: evacuationState
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-state-schema.json
slug: solaris-zone-state
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
title: Oracle Solaris Zone State
---
