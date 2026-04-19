---
description: Request to create a migration application
layout: schema
name: CreateApplicationRequest
properties_list:
- description: Application name
  name: name
  type: string
- description: Application description
  name: description
  type: string
- description: Tags for the application
  name: tags
  type: object
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-create-application-request-schema.json
slug: application-migration-service-create-application-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: CreateApplicationRequest
---
