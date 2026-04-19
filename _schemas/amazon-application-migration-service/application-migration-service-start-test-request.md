---
description: Request to start a test migration job
layout: schema
name: StartTestRequest
properties_list:
- description: Source server IDs to test
  name: sourceServerIDs
  type: array
- description: Tags for the test job
  name: tags
  type: object
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-start-test-request-schema.json
slug: application-migration-service-start-test-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: StartTestRequest
---
