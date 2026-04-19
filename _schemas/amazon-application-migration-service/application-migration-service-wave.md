---
description: A migration wave grouping applications
layout: schema
name: Wave
properties_list:
- description: Wave ID
  name: waveID
  type: string
- description: ARN of the wave
  name: arn
  type: string
- description: Wave name
  name: name
  type: string
- description: Wave description
  name: description
  type: string
- description: Whether the wave is archived
  name: isArchived
  type: boolean
- description: waveAggregatedStatus
  name: waveAggregatedStatus
  type: string
- description: Creation date/time
  name: creationDateTime
  type: string
- description: Last modification date/time
  name: lastModifiedDateTime
  type: string
- description: Tags on the wave
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-wave-schema.json
slug: application-migration-service-wave
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: Wave
---
