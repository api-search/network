---
description: Replication initiation steps and their status
layout: schema
name: DataReplicationInitiation
properties_list:
- description: Date/time replication initiation started
  name: startDateTime
  type: string
- description: Date/time of next retry attempt
  name: nextAttemptDateTime
  type: string
- description: Initiation steps
  name: steps
  type: array
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-data-replication-initiation-schema.json
slug: application-migration-service-data-replication-initiation
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: DataReplicationInitiation
---
