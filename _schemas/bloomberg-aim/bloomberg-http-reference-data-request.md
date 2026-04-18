---
description: ''
layout: schema
name: ReferenceDataRequest
properties_list:
- description: List of security identifiers
  name: securities
  type: array
- description: List of Bloomberg field mnemonics
  name: fields
  type: array
- description: ''
  name: overrides
  type: array
- description: ''
  name: returnFormattedValue
  type: boolean
- description: ''
  name: useUTCTime
  type: boolean
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-reference-data-request-schema.json
slug: bloomberg-http-reference-data-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: ReferenceDataRequest
---
