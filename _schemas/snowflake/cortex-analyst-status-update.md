---
description: ''
layout: schema
name: StatusUpdate
properties_list:
- description: The latest status for processing the request
  name: status
  type: string
- description: A human readable description on the current request processing status
  name: status_message
  type: string
- description: Unique request ID.
  name: request_id
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-analyst-status-update-schema.json
slug: cortex-analyst-status-update
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: StatusUpdate
---
