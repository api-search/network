---
description: Replication configuration for an individual disk
layout: schema
name: ReplicationConfigurationReplicatedDisk
properties_list:
- description: Device name
  name: deviceName
  type: string
- description: Whether this is the boot disk
  name: isBootDisk
  type: boolean
- description: EBS volume type for staging
  name: stagingDiskType
  type: string
- description: IOPS for the staging disk
  name: iops
  type: integer
- description: Throughput for the staging disk in MB/s
  name: throughput
  type: integer
- description: Optimized staging disk type recommendation
  name: optimizedStagingDiskType
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-replication-configuration-replicated-disk-schema.json
slug: application-migration-service-replication-configuration-replicated-disk
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: ReplicationConfigurationReplicatedDisk
---
