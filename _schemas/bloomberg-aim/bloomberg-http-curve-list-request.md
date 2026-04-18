---
description: ''
layout: schema
name: CurveListRequest
properties_list:
- description: Search string for curve lookup
  name: query
  type: string
- description: ''
  name: maxResults
  type: integer
- description: Two-letter country code filter
  name: countryCode
  type: string
- description: Three-letter currency code filter
  name: currencyCode
  type: string
- description: Curve type filter
  name: type
  type: string
- description: ''
  name: subtype
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-curve-list-request-schema.json
slug: bloomberg-http-curve-list-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: CurveListRequest
---
