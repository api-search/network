---
description: Data associated with a job log event
layout: schema
name: JobLogEventData
properties_list:
- description: Source server ID
  name: sourceServerID
  type: string
- description: Conversion server ID
  name: conversionServerID
  type: string
- description: Target EC2 instance ID
  name: targetInstanceID
  type: string
- description: Raw error message if applicable
  name: rawError
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-job-log-event-data-schema.json
slug: application-migration-service-job-log-event-data
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: JobLogEventData
---
