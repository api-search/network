---
description: Shared attributes applied to all log records in this batch
layout: schema
name: CommonBlock
properties_list:
- description: Default Unix timestamp in milliseconds for all logs in the batch
  name: timestamp
  type: integer
- description: Key-value attributes applied to all logs in this batch
  name: attributes
  type: object
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/log-api-common-block-schema.json
slug: log-api-common-block
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
title: CommonBlock
---
