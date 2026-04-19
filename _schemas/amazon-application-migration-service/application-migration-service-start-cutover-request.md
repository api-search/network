---
description: Request to start a cutover migration job
layout: schema
name: StartCutoverRequest
properties_list:
- description: Source server IDs to cut over
  name: sourceServerIDs
  type: array
- description: Tags for the cutover job
  name: tags
  type: object
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-start-cutover-request-schema.json
slug: application-migration-service-start-cutover-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: StartCutoverRequest
---
