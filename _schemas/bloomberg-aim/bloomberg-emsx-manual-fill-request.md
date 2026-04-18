---
description: ''
layout: schema
name: ManualFillRequest
properties_list:
- description: Order sequence number
  name: EMSX_SEQUENCE
  type: integer
- description: Route ID
  name: EMSX_ROUTE_ID
  type: integer
- description: Fill quantity
  name: EMSX_FILL_AMOUNT
  type: integer
- description: Fill price
  name: EMSX_FILL_PRICE
  type: number
- description: Fill date (YYYYMMDD)
  name: EMSX_FILL_DATE
  type: string
- description: Fill time (HHMMSS)
  name: EMSX_FILL_TIME
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-manual-fill-request-schema.json
slug: bloomberg-emsx-manual-fill-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: ManualFillRequest
---
