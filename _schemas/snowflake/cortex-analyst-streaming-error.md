---
description: ''
layout: schema
name: StreamingError
properties_list:
- description: A description of the error
  name: message
  type: string
- description: The Snowflake error code categorizing the error
  name: code
  type: string
- description: Unique request ID
  name: request_id
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-analyst-streaming-error-schema.json
slug: cortex-analyst-streaming-error
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: StreamingError
---
