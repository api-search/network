---
description: A zone configuration resource such as anet, fs, capped-cpu, etc.
layout: schema
name: Resource
properties_list:
- description: Resource type identifier
  name: type
  type: string
- description: List of properties for this resource
  name: properties
  type: array
- description: Parent resource reference for nested resources
  name: parent
  type: string
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-resource-schema.json
slug: solaris-rad-zonemgr-resource
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
