---
description: A single log entry for the Azure Log Analytics Ingestion API. The schema must match the stream declaration in the data collection rule.
layout: schema
name: LogEntry
properties_list:
- description: The timestamp of the log entry.
  name: TimeGenerated
  type: string
- description: The computer or source generating the log.
  name: Computer
  type: string
- description: Additional context or message for the log entry.
  name: AdditionalContext
  type: string
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
schema_file: json-schema/ingestion-api-log-entry-schema.json
slug: ingestion-api-log-entry
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
title: LogEntry
---
