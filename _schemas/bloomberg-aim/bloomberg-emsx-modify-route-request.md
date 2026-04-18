---
description: ''
layout: schema
name: ModifyRouteRequest
properties_list:
- description: Order sequence number
  name: EMSX_SEQUENCE
  type: integer
- description: Route ID to modify
  name: EMSX_ROUTE_ID
  type: integer
- description: ''
  name: EMSX_AMOUNT
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
- description: ''
  name: EMSX_STRATEGY
  type: string
- description: ''
  name: EMSX_STRATEGY_PARAMS
  type: object
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-modify-route-request-schema.json
slug: bloomberg-emsx-modify-route-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: ModifyRouteRequest
---
