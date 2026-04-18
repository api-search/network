---
description: The result of a log export operation, containing a page of records.
layout: schema
name: LogExportResult
properties_list:
- description: Cursor for the next page of export results.
  name: nextSliceKey
  type: string
- description: The list of exported log records on this page.
  name: results
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/log-monitoring-api-v2-log-export-result-schema.json
slug: log-monitoring-api-v2-log-export-result
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
title: LogExportResult
---
