---
description: Request to update a migration application
layout: schema
name: UpdateApplicationRequest
properties_list:
- description: Application ID to update
  name: applicationID
  type: string
- description: New application name
  name: name
  type: string
- description: New application description
  name: description
  type: string
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-update-application-request-schema.json
slug: application-migration-service-update-application-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: UpdateApplicationRequest
---
