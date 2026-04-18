---
description: ''
layout: schema
name: KernelZoneResource
properties_list:
- description: Resource type. Kernel zone specific types include dedicated-cpu and capped-memory for virtual hardware allocation.
  name: type
  type: string
- description: Resource property values
  name: properties
  type: array
- description: Parent resource reference
  name: parent
  type: string
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-kernel-zones-kernel-zone-resource-schema.json
slug: solaris-kernel-zones-kernel-zone-resource
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
title: KernelZoneResource
---
