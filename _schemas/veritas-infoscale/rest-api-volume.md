---
description: Volume schema from Veritas InfoScale REST API
layout: schema
name: Volume
properties_list:
- description: Volume name
  name: name
  type: string
- description: Parent disk group
  name: diskGroup
  type: string
- description: Volume state
  name: state
  type: string
- description: Volume size
  name: size
  type: string
- description: Volume layout type
  name: layout
  type: string
- description: Number of plexes
  name: plexCount
  type: integer
- description: Read policy for the volume
  name: readPolicy
  type: string
- description: Volume usage type
  name: usageType
  type: string
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
schema_file: json-schema/rest-api-volume-schema.json
slug: rest-api-volume
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
title: Volume
---
