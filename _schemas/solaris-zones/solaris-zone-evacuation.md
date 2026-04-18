---
description: Represents a multi-zone evacuation operation in Oracle Solaris, including overall status, per-zone migration results, and progress tracking for evacuating zones from one host to another. Available since RAD zonemgr API version 1.4.
layout: schema
name: Oracle Solaris Zone Evacuation
properties_list:
- description: Overall evacuation status
  name: status
  type: string
- description: Whether this is a return evacuation (zones being moved back to original host)
  name: returning
  type: boolean
- description: Per-zone migration results keyed by zone name
  name: migrationResults
  type: object
- description: ''
  name: progress
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-evacuation-schema.json
slug: solaris-zone-evacuation
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
title: Oracle Solaris Zone Evacuation
---
