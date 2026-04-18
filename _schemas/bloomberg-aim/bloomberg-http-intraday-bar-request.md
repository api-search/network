---
description: ''
layout: schema
name: IntradayBarRequest
properties_list:
- description: Single security identifier
  name: security
  type: string
- description: ''
  name: eventType
  type: string
- description: ''
  name: startDateTime
  type: string
- description: ''
  name: endDateTime
  type: string
- description: Bar interval in minutes
  name: interval
  type: integer
- description: ''
  name: gapFillInitialBar
  type: boolean
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-intraday-bar-request-schema.json
slug: bloomberg-http-intraday-bar-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: IntradayBarRequest
---
