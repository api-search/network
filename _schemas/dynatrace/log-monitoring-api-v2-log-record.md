---
description: A log record retrieved from the Dynatrace Grail data lakehouse. Contains the original log content plus enriched metadata added by Dynatrace during ingestion and processing.
layout: schema
name: LogRecord
properties_list:
- description: The timestamp of the log record in ISO 8601 format.
  name: timestamp
  type: string
- description: The log message content.
  name: content
  type: string
- description: The severity level of the log record.
  name: severity
  type: string
- description: The source identifier of the log record.
  name: log.source
  type: string
- description: The associated host entity ID.
  name: dt.entity.host
  type: string
- description: Additional fields present in the log record beyond the standard set. Content varies based on what was ingested and how OpenPipeline processed the record.
  name: additionalFields
  type: object
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/log-monitoring-api-v2-log-record-schema.json
slug: log-monitoring-api-v2-log-record
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: LogRecord
---
