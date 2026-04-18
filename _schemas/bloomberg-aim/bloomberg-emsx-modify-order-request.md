---
description: ''
layout: schema
name: ModifyOrderRequest
properties_list:
- description: Order sequence number to modify
  name: EMSX_SEQUENCE
  type: integer
- description: New order quantity
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
  name: EMSX_NOTES
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-modify-order-request-schema.json
slug: bloomberg-emsx-modify-order-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: ModifyOrderRequest
---
