---
description: Represents a complete Solaris zone configuration including global properties, resource assignments, and networking for non-global zones managed through zonecfg(8) and the RAD zonemgr module.
layout: schema
name: Oracle Solaris Zone Configuration
properties_list:
- description: Unique name identifying the zone on the system
  name: name
  type: string
- description: Universally unique identifier assigned to the zone
  name: uuid
  type: string
- description: Zone brand determining the runtime environment and kernel behavior
  name: brand
  type: string
- description: File system path for the zone root directory
  name: zonepath
  type: string
- description: Whether the zone should automatically boot when the global zone boots
  name: autoboot
  type: boolean
- description: Action to take when the global zone is shut down
  name: autoshutdown
  type: string
- description: Boot arguments passed to the zone at boot time
  name: bootargs
  type: string
- description: File MAC policy profile for mandatory access control
  name: file-mac-profile
  type: string
- description: Emulated host identifier for the zone
  name: hostid
  type: string
- description: IP stack type for the zone
  name: ip-type
  type: string
- description: Comma-separated list of privileges for the zone
  name: limitpriv
  type: string
- description: Default scheduling class for processes in the zone
  name: scheduling-class
  type: string
- description: Maximum number of lightweight processes allowed in the zone
  name: max-lwps
  type: integer
- description: Maximum number of processes allowed in the zone
  name: max-processes
  type: integer
- description: Maximum shared memory allowed for the zone
  name: max-shm-memory
  type: string
- description: Maximum number of shared memory identifiers
  name: max-shm-ids
  type: integer
- description: Maximum number of message queue identifiers
  name: max-msg-ids
  type: integer
- description: Maximum number of semaphore identifiers
  name: max-sem-ids
  type: integer
- description: Current runtime state of the zone (read-only, not a configuration property)
  name: state
  type: string
- description: Kernel-assigned zone ID when the zone is running (read-only)
  name: id
  type: integer
- description: Automatic network interface resources providing network connectivity
  name: anet
  type: array
- description: ''
  name: capped-cpu
  type: object
- description: ''
  name: capped-memory
  type: object
- description: ''
  name: dedicated-cpu
  type: object
- description: ''
  name: virtual-cpu
  type: object
- description: Device resources made available to the zone
  name: device
  type: array
- description: File system mount resources
  name: fs
  type: array
- description: Network interface resources for shared-IP zones
  name: net
  type: array
- description: ZFS dataset resources delegated to the zone
  name: dataset
  type: array
- description: Resource control entries for the zone
  name: rctl
  type: array
- description: Generic attribute key-value pairs
  name: attr
  type: array
- description: Administrative access entries for zone delegation
  name: admin
  type: array
- description: ''
  name: rootzpool
  type: object
- description: Additional ZFS pools available to the zone
  name: zpool
  type: array
- description: SMF service dependencies required before zone boot
  name: smf-dependency
  type: array
- description: ''
  name: verified-boot
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-configuration-schema.json
slug: solaris-zone-configuration
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
title: Oracle Solaris Zone Configuration
---
