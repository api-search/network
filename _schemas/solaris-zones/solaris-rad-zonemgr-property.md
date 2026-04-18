---
description: A zone resource property with support for simple, list, and complex values
layout: schema
name: Property
properties_list:
- description: Property name
  name: name
  type: string
- description: Simple property value
  name: value
  type: string
- description: Property value type
  name: type
  type: string
- description: List of values for list-type properties
  name: listValue
  type: array
- description: Complex structured values
  name: complexValue
  type: array
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-property-schema.json
slug: solaris-rad-zonemgr-property
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
title: Property
---
