---
description: ''
layout: schema
name: Fill
properties_list:
- description: Parent order sequence number
  name: EMSX_SEQUENCE
  type: integer
- description: Route that was filled
  name: EMSX_ROUTE_ID
  type: integer
- description: Unique fill identifier
  name: EMSX_FILL_ID
  type: integer
- description: ''
  name: EMSX_TICKER
  type: string
- description: ''
  name: EMSX_SIDE
  type: string
- description: Quantity filled
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
- description: ''
  name: EMSX_BROKER
  type: string
- description: Exchange where the fill occurred
  name: EMSX_EXCHANGE
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-fill-schema.json
slug: bloomberg-emsx-fill
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Fill
---
