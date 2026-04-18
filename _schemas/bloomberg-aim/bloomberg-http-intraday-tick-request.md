---
description: ''
layout: schema
name: IntradayTickRequest
properties_list:
- description: Single security identifier
  name: security
  type: string
- description: ''
  name: eventTypes
  type: array
- description: Start of the time range
  name: startDateTime
  type: string
- description: End of the time range
  name: endDateTime
  type: string
- description: ''
  name: includeConditionCodes
  type: boolean
- description: ''
  name: includeExchangeCodes
  type: boolean
- description: ''
  name: includeBrokerCodes
  type: boolean
- description: ''
  name: includeRPSCodes
  type: boolean
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-intraday-tick-request-schema.json
slug: bloomberg-http-intraday-tick-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: IntradayTickRequest
---
