---
description: ''
layout: schema
name: Resource
properties_list:
- description: 'Resource type name. Common types include: net, anet, device, fs, dataset, rctl, attr, dedicated-cpu, capped-memory, capped-cpu, admin, security-flags'
  name: type
  type: string
- description: Resource properties
  name: properties
  type: array
- description: Parent resource reference
  name: parent
  type: string
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-configuration-resource-schema.json
slug: solaris-zone-configuration-resource
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
title: Resource
---
