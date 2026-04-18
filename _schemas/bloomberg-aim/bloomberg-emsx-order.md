---
description: ''
layout: schema
name: Order
properties_list:
- description: Unique order sequence number
  name: EMSX_SEQUENCE
  type: integer
- description: Security identifier
  name: EMSX_TICKER
  type: string
- description: ''
  name: EMSX_SIDE
  type: string
- description: Total order quantity
  name: EMSX_AMOUNT
  type: integer
- description: Quantity filled so far
  name: EMSX_FILLED
  type: integer
- description: Quantity currently working (routed but not filled)
  name: EMSX_WORKING
  type: integer
- description: ''
  name: EMSX_ORDER_TYPE
  type: string
- description: ''
  name: EMSX_LIMIT_PRICE
  type: number
- description: ''
  name: EMSX_STOP_PRICE
  type: number
- description: ''
  name: EMSX_TIF
  type: string
- description: Current order status
  name: EMSX_STATUS
  type: string
- description: Average fill price
  name: EMSX_AVG_PRICE
  type: number
- description: ''
  name: EMSX_ACCOUNT
  type: string
- description: ''
  name: EMSX_TRADER
  type: string
- description: ''
  name: EMSX_NOTES
  type: string
- description: ''
  name: EMSX_BASKET_NAME
  type: string
- description: Order creation date (YYYYMMDD)
  name: EMSX_DATE
  type: string
- description: Last update timestamp
  name: EMSX_TIME_STAMP
  type: string
- description: ''
  name: EMSX_PORTFOLIO
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-order-schema.json
slug: bloomberg-emsx-order
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Order
---
