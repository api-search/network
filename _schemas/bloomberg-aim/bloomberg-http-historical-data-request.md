---
description: ''
layout: schema
name: HistoricalDataRequest
properties_list:
- description: List of security identifiers
  name: securities
  type: array
- description: List of Bloomberg field mnemonics
  name: fields
  type: array
- description: Start date in YYYYMMDD format
  name: startDate
  type: string
- description: End date in YYYYMMDD format
  name: endDate
  type: string
- description: ''
  name: periodicitySelection
  type: string
- description: ''
  name: periodicityAdjustment
  type: string
- description: Three-letter currency code for cross-currency conversion
  name: currency
  type: string
- description: ''
  name: overrides
  type: array
- description: ''
  name: nonTradingDayFillOption
  type: string
- description: ''
  name: nonTradingDayFillMethod
  type: string
- description: ''
  name: adjustmentNormal
  type: boolean
- description: ''
  name: adjustmentAbnormal
  type: boolean
- description: ''
  name: adjustmentSplit
  type: boolean
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-historical-data-request-schema.json
slug: bloomberg-http-historical-data-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: HistoricalDataRequest
---
