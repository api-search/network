---
description: Request to create a migration wave
layout: schema
name: CreateWaveRequest
properties_list:
- description: Wave name
  name: name
  type: string
- description: Wave description
  name: description
  type: string
- description: Tags for the wave
  name: tags
  type: object
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-create-wave-request-schema.json
slug: application-migration-service-create-wave-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: CreateWaveRequest
---
