---
description: A point-in-time snapshot of an Amazon FSx for OpenZFS volume.
layout: schema
name: Snapshot
properties_list:
- description: Unique ID of the snapshot.
  name: SnapshotId
  type: string
- description: Name of the snapshot.
  name: Name
  type: string
- description: ID of the volume this snapshot was taken from.
  name: VolumeId
  type: string
- description: ''
  name: CreationTime
  type: string
- description: ''
  name: Lifecycle
  type: string
- description: ''
  name: ResourceARN
  type: string
- description: ''
  name: Tags
  type: array
- description: ''
  name: AdministrativeActions
  type: array
provider_name: Amazon FSx
provider_slug: amazon-fsx
schema_file: json-schema/amazon-fsx-snapshot-schema.json
slug: amazon-fsx-snapshot
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
title: Snapshot
---
