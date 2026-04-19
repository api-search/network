---
description: A trading order in the Aladdin system
layout: schema
name: Order
properties_list:
- description: Unique order identifier
  name: orderId
  type: string
- description: Portfolio identifier
  name: portfolioId
  type: string
- description: Security identifier
  name: securityId
  type: string
- description: Order side
  name: side
  type: string
- description: Order quantity in shares or units
  name: quantity
  type: number
- description: Quantity filled
  name: filledQuantity
  type: number
- description: Average execution price
  name: averagePrice
  type: number
- description: Order status
  name: status
  type: string
- description: Order type
  name: orderType
  type: string
- description: Order creation timestamp
  name: createdAt
  type: string
- description: Order fill timestamp
  name: filledAt
  type: string
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-trading-order-schema.json
slug: aladdin-studio-trading-order
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: Order
---
