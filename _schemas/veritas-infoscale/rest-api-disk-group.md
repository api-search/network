---
description: Disk group schema from Veritas InfoScale REST API
layout: schema
name: DiskGroup
properties_list:
- description: Disk group name
  name: name
  type: string
- description: Disk group state
  name: state
  type: string
- description: Total disk group size
  name: totalSize
  type: string
- description: Free space in disk group
  name: freeSize
  type: string
- description: Number of disks in the group
  name: diskCount
  type: integer
- description: Number of volumes in the group
  name: volumeCount
  type: integer
- description: Default layout type
  name: layout
  type: string
- description: Disk group version
  name: version
  type: string
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
schema_file: json-schema/rest-api-disk-group-schema.json
slug: rest-api-disk-group
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
title: DiskGroup
---
