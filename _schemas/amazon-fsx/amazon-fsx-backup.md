---
description: An automatic or user-initiated backup of an Amazon FSx file system.
layout: schema
name: Backup
properties_list:
- description: Unique ID of the backup.
  name: BackupId
  type: string
- description: Current lifecycle state.
  name: Lifecycle
  type: string
- description: Type of backup.
  name: Type
  type: string
- description: ''
  name: CreationTime
  type: string
- description: The file system that was backed up.
  name: FileSystem
  type: object
- description: ''
  name: KmsKeyId
  type: string
- description: ''
  name: ResourceARN
  type: string
- description: ''
  name: Tags
  type: array
- description: ''
  name: OwnerId
  type: string
- description: ''
  name: SourceBackupId
  type: string
provider_name: Amazon FSx
provider_slug: amazon-fsx
schema_file: json-schema/amazon-fsx-backup-schema.json
slug: amazon-fsx-backup
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
title: Backup
---
