---
description: A batch of log records with optional shared attributes
layout: schema
name: LogDataObject
properties_list:
- description: Shared attributes applied to all log records in this batch
  name: common
  type: object
- description: Array of individual log records
  name: logs
  type: array
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/new-relic-log-log-data-object-schema.json
slug: new-relic-log-log-data-object
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
title: LogDataObject
---
