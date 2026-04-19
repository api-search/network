---
description: Status information for an asynchronous batch request.
layout: schema
name: BatchStatus
properties_list:
- description: The batch request identifier.
  name: id
  type: string
- description: Time when the batch request started (Eastern Time Zone).
  name: startTime
  type: string
- description: Time when the batch request ended. Null if still processing.
  name: endTime
  type: '[''string'', ''null'']'
- description: Current batch processing status.
  name: status
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-batch-status-schema.json
slug: factset-fundamentals-batch-status
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: BatchStatus
---
