---
description: A migration or conversion job
layout: schema
name: Job
properties_list:
- description: Job ID
  name: jobID
  type: string
- description: ARN of the job
  name: arn
  type: string
- description: Job type
  name: type
  type: string
- description: Who initiated the job
  name: initiatedBy
  type: string
- description: Date/time job was created
  name: creationDateTime
  type: string
- description: Date/time job ended
  name: endDateTime
  type: string
- description: Job status
  name: status
  type: string
- description: Servers participating in the job
  name: participatingServers
  type: array
- description: Tags on the job
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-job-schema.json
slug: application-migration-service-job
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: Job
---
