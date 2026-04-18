---
description: A trading order within Bloomberg AIM/EMSX, representing an instruction to buy or sell a financial instrument with specified parameters.
layout: schema
name: Order
properties_list:
- description: Unique EMSX order sequence number assigned by the system
  name: sequenceNumber
  type: integer
- description: Bloomberg security identifier for the order
  name: ticker
  type: string
- description: Order side indicating direction of the trade
  name: side
  type: string
- description: Total order quantity (shares or contracts)
  name: amount
  type: integer
- description: Type of order determining execution behavior
  name: orderType
  type: string
- description: Limit price for LMT and STP LMT orders
  name: limitPrice
  type: number
- description: Stop trigger price for STP and STP LMT orders
  name: stopPrice
  type: number
- description: Duration the order remains active
  name: timeInForce
  type: string
- description: Expiry date for Good-Till-Date orders
  name: gtdDate
  type: string
- description: Current order status
  name: status
  type: string
- description: Cumulative quantity filled across all routes
  name: filledAmount
  type: integer
- description: Quantity currently working (routed but not yet filled)
  name: workingAmount
  type: integer
- description: Volume-weighted average fill price
  name: averagePrice
  type: number
- description: Trading account identifier
  name: account
  type: string
- description: Portfolio name associated with the order
  name: portfolio
  type: string
- description: Trader responsible for the order
  name: trader
  type: string
- description: UUID of the assigned trader
  name: traderUuid
  type: string
- description: Name of the basket this order belongs to
  name: basketName
  type: string
- description: Handling instruction for the order
  name: handInstruction
  type: string
- description: Investor identifier for allocation purposes
  name: investorId
  type: string
- description: Free-text notes attached to the order
  name: notes
  type: string
- description: Custom note field 1
  name: customNote1
  type: string
- description: Custom note field 2
  name: customNote2
  type: string
- description: Custom note field 3
  name: customNote3
  type: string
- description: Custom note field 4
  name: customNote4
  type: string
- description: Custom note field 5
  name: customNote5
  type: string
- description: Whether this is a contract for difference order
  name: cfdFlag
  type: boolean
- description: Locate broker for short sell orders
  name: locateBroker
  type: string
- description: Locate ID for short sell orders
  name: locateId
  type: string
- description: Date the order was created
  name: createdDate
  type: string
- description: Timestamp of last order update
  name: lastUpdated
  type: string
- description: Routes associated with this order
  name: routes
  type: array
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/order.json
slug: order
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Order
---
