---
description: Current data replication state and statistics for a source server
layout: schema
name: DataReplicationInfo
properties_list:
- description: Replication lag duration
  name: lagDuration
  type: string
- description: Date/time of the last snapshot
  name: lastSnapshotDateTime
  type: string
- description: List of replicated disks
  name: replicatedDisks
  type: array
- description: Current replication state
  name: dataReplicationState
  type: string
- description: dataReplicationInitiation
  name: dataReplicationInitiation
  type: string
- description: dataReplicationError
  name: dataReplicationError
  type: string
- description: Availability zone used for staging
  name: stagingAvailabilityZone
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-data-replication-info-schema.json
slug: application-migration-service-data-replication-info
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: DataReplicationInfo
---
