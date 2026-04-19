---
description: A migration application grouping source servers
layout: schema
name: Application
properties_list:
- description: Application ID
  name: applicationID
  type: string
- description: ARN of the application
  name: arn
  type: string
- description: Application name
  name: name
  type: string
- description: Application description
  name: description
  type: string
- description: Whether the application is archived
  name: isArchived
  type: boolean
- description: applicationAggregatedStatus
  name: applicationAggregatedStatus
  type: string
- description: Creation date/time
  name: creationDateTime
  type: string
- description: Last modification date/time
  name: lastModifiedDateTime
  type: string
- description: Tags on the application
  name: tags
  type: object
- description: Wave ID this application belongs to
  name: waveID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-application-schema.json
slug: application-migration-service-application
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: Application
---
