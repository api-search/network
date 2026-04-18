---
description: Service group schema from Veritas InfoScale REST API
layout: schema
name: ServiceGroup
properties_list:
- description: Service group name
  name: name
  type: string
- description: Current service group state
  name: state
  type: string
- description: List of systems where this group can run
  name: systemList
  type: array
- description: System where the group is currently online
  name: currentSystem
  type: string
- description: Whether the group starts automatically
  name: autoStart
  type: boolean
- description: Whether the group can run on multiple systems
  name: parallel
  type: boolean
- description: Number of resources in this group
  name: resourceCount
  type: integer
- description: Type classification of the service group
  name: groupType
  type: string
- description: Whether this is a critical service group
  name: critical
  type: boolean
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
schema_file: json-schema/rest-api-service-group-schema.json
slug: rest-api-service-group
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
title: ServiceGroup
---
