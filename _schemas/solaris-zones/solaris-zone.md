---
description: Represents an Oracle Solaris Zone instance managed through the RAD zonemgr module, including its identity, brand type, lifecycle state, and auxiliary state information.
layout: schema
name: Oracle Solaris Zone
properties_list:
- description: Unique zone name used as the primary identifier
  name: name
  type: string
- description: Zone brand type determining the virtualization model
  name: brand
  type: string
- description: Numeric zone ID assigned when the zone is running or ready. The global zone is always ID 0.
  name: id
  type: integer
- description: Universally unique identifier for the zone
  name: uuid
  type:
  - string
  - 'null'
- description: Current lifecycle state of the zone
  name: state
  type: string
- description: Dynamic auxiliary state flags providing additional status information
  name: auxstate
  type: array
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-schema.json
slug: solaris-zone
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
title: Oracle Solaris Zone
---
