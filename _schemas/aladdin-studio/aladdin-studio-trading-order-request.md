---
description: Request body for creating a new trading order
layout: schema
name: OrderRequest
properties_list:
- description: Portfolio identifier
  name: portfolioId
  type: string
- description: Security identifier
  name: securityId
  type: string
- description: Order side
  name: side
  type: string
- description: Order quantity
  name: quantity
  type: number
- description: Order type
  name: orderType
  type: string
- description: Limit price (required for limit orders)
  name: limitPrice
  type: number
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-trading-order-request-schema.json
slug: aladdin-studio-trading-order-request
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: OrderRequest
---
