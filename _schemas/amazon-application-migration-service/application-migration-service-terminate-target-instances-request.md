---
description: Request to terminate test or cutover instances
layout: schema
name: TerminateTargetInstancesRequest
properties_list:
- description: Source server IDs whose instances to terminate
  name: sourceServerIDs
  type: array
- description: Tags for the termination job
  name: tags
  type: object
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-terminate-target-instances-request-schema.json
slug: application-migration-service-terminate-target-instances-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: TerminateTargetInstancesRequest
---
