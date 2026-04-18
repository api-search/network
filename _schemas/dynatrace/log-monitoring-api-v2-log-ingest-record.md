---
description: A single log record to ingest into the Dynatrace Grail data lakehouse. The content field is required. Additional fields provide context for routing, filtering, and entity association.
layout: schema
name: LogIngestRecord
properties_list:
- description: The main log message or text. Required. This is the primary searchable content of the log record.
  name: content
  type: string
- description: The severity level of the log record. Standard syslog severity levels are supported.
  name: severity
  type: string
- description: The timestamp of the log record. Accepts ISO 8601 format (e.g., 2024-01-15T10:30:00.000Z) or Unix timestamp in milliseconds. If not specified, the ingestion time is used.
  name: timestamp
  type: string
- description: A string identifier for the source of the log record, such as an application name, component, or log file path.
  name: log.source
  type: string
- description: The Dynatrace host entity ID to associate this log record with, e.g., HOST-1234567890ABCDEF. This enables correlation between logs and monitored infrastructure.
  name: dt.entity.host
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/log-monitoring-api-v2-log-ingest-record-schema.json
slug: log-monitoring-api-v2-log-ingest-record
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
title: LogIngestRecord
---
