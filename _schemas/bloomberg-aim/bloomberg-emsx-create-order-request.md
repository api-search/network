---
description: ''
layout: schema
name: CreateOrderRequest
properties_list:
- description: Bloomberg security identifier
  name: EMSX_TICKER
  type: string
- description: Order quantity (number of shares/contracts)
  name: EMSX_AMOUNT
  type: integer
- description: Order type
  name: EMSX_ORDER_TYPE
  type: string
- description: Buy or sell
  name: EMSX_SIDE
  type: string
- description: Time in force
  name: EMSX_TIF
  type: string
- description: Limit price (required for LMT and STP LMT orders)
  name: EMSX_LIMIT_PRICE
  type: number
- description: Stop price (required for STP and STP LMT orders)
  name: EMSX_STOP_PRICE
  type: number
- description: Trading account identifier
  name: EMSX_ACCOUNT
  type: string
- description: Free-text notes attached to the order
  name: EMSX_NOTES
  type: string
- description: Handling instruction
  name: EMSX_HAND_INSTRUCTION
  type: string
- description: Name of the basket this order belongs to
  name: EMSX_BASKET_NAME
  type: string
- description: Contract for difference flag
  name: EMSX_CFD_FLAG
  type: string
- description: ''
  name: EMSX_CUSTOM_NOTE1
  type: string
- description: ''
  name: EMSX_CUSTOM_NOTE2
  type: string
- description: ''
  name: EMSX_CUSTOM_NOTE3
  type: string
- description: ''
  name: EMSX_CUSTOM_NOTE4
  type: string
- description: ''
  name: EMSX_CUSTOM_NOTE5
  type: string
- description: Good-till-date in YYYYMMDD format
  name: EMSX_GTD_DATE
  type: string
- description: Investor identifier for allocation
  name: EMSX_INVESTOR_ID
  type: string
- description: Locate broker for short sells
  name: EMSX_LOCATE_BROKER
  type: string
- description: Locate ID for short sells
  name: EMSX_LOCATE_ID
  type: string
- description: Portfolio name for the order
  name: EMSX_PORTFOLIO
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-emsx-create-order-request-schema.json
slug: bloomberg-emsx-create-order-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: CreateOrderRequest
---
