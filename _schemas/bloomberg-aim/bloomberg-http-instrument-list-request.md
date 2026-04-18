---
description: ''
layout: schema
name: InstrumentListRequest
properties_list:
- description: Search string for instrument lookup
  name: query
  type: string
- description: Maximum number of results to return
  name: maxResults
  type: integer
- description: Filter by Bloomberg yellow key
  name: yellowKeyFilter
  type: string
- description: Two-letter language code
  name: languageOverride
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-instrument-list-request-schema.json
slug: bloomberg-http-instrument-list-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: InstrumentListRequest
---
