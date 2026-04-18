---
description: The result of a log search query.
layout: schema
name: LogRecordSearchResult
properties_list:
- description: The cursor for the next page of results. Null if all results have been returned.
  name: nextSliceKey
  type: string
- description: The list of log records matching the search query on this page.
  name: results
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-log-monitoring-v2-log-record-search-result-schema.json
slug: dynatrace-log-monitoring-v2-log-record-search-result
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
title: LogRecordSearchResult
---
