---
description: ''
layout: schema
name: EvacuationResult
properties_list:
- description: Overall evacuation status
  name: status
  type: string
- description: Whether this is a return evacuation
  name: returning
  type: boolean
- description: Per-zone migration results keyed by zone name
  name: migrationResults
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zones-management-evacuation-result-schema.json
slug: solaris-zones-management-evacuation-result
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
