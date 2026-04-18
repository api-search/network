---
description: Represents a configurable resource within an Oracle Solaris Zone, such as a network interface, device, filesystem, resource control, or CPU/memory allocation. Resources are managed through the zonecfg interface exposed via the RAD zonemgr module.
layout: schema
name: Oracle Solaris Zone Resource
properties_list:
- description: Resource type identifier determining the kind of resource
  name: type
  type: string
- description: Array of property name-value pairs for the resource
  name: properties
  type: array
- description: Reference to a parent resource, if applicable
  name: parent
  type:
  - string
  - 'null'
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-resource-schema.json
slug: solaris-zone-resource
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
title: Oracle Solaris Zone Resource
---
