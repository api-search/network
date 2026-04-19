---
description: ''
layout: schema
name: BatchStatus
properties_list:
- description: the id of batch request.
  name: id
  type: string
- description: Time when the batch request is started. This is in Eastern Time Zone. The date-time format is expressed as [YYYY-MM-DD]T[HH:MM:SSS], following ISO 8601.
  name: startTime
  type: string
- description: Time when the batch request is ended. This is in Eastern Time Zone. The date-time format is expressed as [YYYY-MM-DD]T[HH:MM:SSS], following ISO 8601.
  name: endTime
  type: string
- description: ''
  name: status
  type: string
- description: Error message.
  name: error
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-batch-status-schema.json
slug: factset-formula-batch-status
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: BatchStatus
---
