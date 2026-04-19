---
description: Replication status for an individual disk
layout: schema
name: DataReplicationInfoReplicatedDisk
properties_list:
- description: Device name of the disk
  name: deviceName
  type: string
- description: Total storage in bytes
  name: totalStorageBytes
  type: integer
- description: Amount of storage replicated in bytes
  name: replicatedStorageBytes
  type: integer
- description: Amount rescanned in bytes
  name: rescannedStorageBytes
  type: integer
- description: Amount backlogged in bytes
  name: backloggedStorageBytes
  type: integer
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-data-replication-info-replicated-disk-schema.json
slug: application-migration-service-data-replication-info-replicated-disk
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: DataReplicationInfoReplicatedDisk
---
