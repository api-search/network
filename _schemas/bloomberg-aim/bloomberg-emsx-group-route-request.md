---
description: ''
layout: schema
name: GroupRouteRequest
properties_list:
- description: List of order sequence numbers to route as a group
  name: EMSX_SEQUENCE
  type: array
- description: Percentage of each order to route (0-100)
  name: EMSX_AMOUNT_PERCENT
  type: number
- description: ''
  name: EMSX_BROKER
  type: string
- description: ''
  name: EMSX_ORDER_TYPE
  type: string
- description: ''
  name: EMSX_LIMIT_PRICE
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
schema_file: json-schema/bloomberg-emsx-group-route-request-schema.json
slug: bloomberg-emsx-group-route-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: GroupRouteRequest
---
