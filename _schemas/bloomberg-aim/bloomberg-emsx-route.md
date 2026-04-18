---
description: ''
layout: schema
name: Route
properties_list:
- description: Parent order sequence number
  name: EMSX_SEQUENCE
  type: integer
- description: Unique route identifier
  name: EMSX_ROUTE_ID
  type: integer
- description: Broker code
  name: EMSX_BROKER
  type: string
- description: Routed quantity
  name: EMSX_AMOUNT
  type: integer
- description: Filled quantity on this route
  name: EMSX_FILLED
  type: integer
- description: ''
  name: EMSX_STATUS
  type: string
- description: ''
  name: EMSX_ORDER_TYPE
  type: string
- description: ''
  name: EMSX_LIMIT_PRICE
  type: number
- description: Average fill price for this route
  name: EMSX_AVG_PRICE
  type: number
- description: ''
  name: EMSX_STRATEGY
  type: string
- description: ''
  name: EMSX_EXEC_INSTRUCTIONS
  type: string
- description: ''
  name: EMSX_LAST_FILL_DATE
  type: string
- description: ''
  name: EMSX_LAST_FILL_TIME
  type: string
- description: ''
  name: EMSX_ROUTE_CREATE_DATE
  type: string
- description: ''
  name: EMSX_ROUTE_CREATE_TIME
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-route-schema.json
slug: bloomberg-emsx-route
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Route
---
