---
description: A single log record
layout: schema
name: LogRecord
properties_list:
- description: Unix epoch timestamp in milliseconds when the log event occurred
  name: timestamp
  type: integer
- description: The log message text
  name: message
  type: string
- description: Log severity level
  name: level
  type: string
- description: Log format type for automatic parsing (e.g., nginx, apache, syslog)
  name: logtype
  type: string
- description: Additional key-value attributes for this log record
  name: attributes
  type: object
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/log-api-log-record-schema.json
slug: log-api-log-record
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
title: LogRecord
---
