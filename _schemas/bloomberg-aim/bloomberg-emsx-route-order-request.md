---
description: ''
layout: schema
name: RouteOrderRequest
properties_list:
- description: Order sequence number to route
  name: EMSX_SEQUENCE
  type: integer
- description: Quantity to route
  name: EMSX_AMOUNT
  type: integer
- description: Broker code
  name: EMSX_BROKER
  type: string
- description: ''
  name: EMSX_ORDER_TYPE
  type: string
- description: ''
  name: EMSX_TIF
  type: string
- description: ''
  name: EMSX_LIMIT_PRICE
  type: number
- description: ''
  name: EMSX_STOP_PRICE
  type: number
- description: Broker strategy name
  name: EMSX_STRATEGY
  type: string
- description: ''
  name: EMSX_STRATEGY_PARAMS
  type: object
- description: ''
  name: EMSX_EXEC_INSTRUCTIONS
  type: string
- description: ''
  name: EMSX_ACCOUNT
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-route-order-request-schema.json
slug: bloomberg-emsx-route-order-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: RouteOrderRequest
---
