---
description: Result of a zone evacuation operation
layout: schema
name: EvacuationResult
properties_list:
- description: Overall evacuation status
  name: status
  type: string
- description: Whether zones are being returned from a previous evacuation
  name: returning
  type: boolean
- description: Per-zone migration results keyed by zone name
  name: migrationResults
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-evacuation-result-schema.json
slug: solaris-rad-zonemgr-evacuation-result
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
title: EvacuationResult
---
