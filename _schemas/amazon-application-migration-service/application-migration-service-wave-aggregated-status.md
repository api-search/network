---
description: Aggregated status of all applications in a wave
layout: schema
name: WaveAggregatedStatus
properties_list:
- description: Date/time of last status update
  name: lastUpdateDateTime
  type: string
- description: Overall health status
  name: healthStatus
  type: string
- description: Overall progress status
  name: progressStatus
  type: string
- description: Total number of applications in the wave
  name: totalApplications
  type: integer
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-wave-aggregated-status-schema.json
slug: application-migration-service-wave-aggregated-status
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: WaveAggregatedStatus
---
