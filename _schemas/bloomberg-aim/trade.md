---
description: A trade execution record within Bloomberg AIM/EMSX, representing a route sent to a broker and its associated fills. Maps to the EMSX route concept with embedded fill data.
layout: schema
name: Trade
properties_list:
- description: Parent order sequence number in EMSX
  name: sequenceNumber
  type: integer
- description: Unique route identifier within the parent order
  name: routeId
  type: integer
- description: Bloomberg ticker of the traded security
  name: ticker
  type: string
- description: Trade direction
  name: side
  type: string
- description: Quantity routed to the broker
  name: amount
  type: integer
- description: Quantity filled on this route
  name: filledAmount
  type: integer
- description: Volume-weighted average fill price for this route
  name: averagePrice
  type: number
- description: Broker code the route was sent to
  name: broker
  type: string
- description: Order type for this route
  name: orderType
  type: string
- description: Limit price sent with the route
  name: limitPrice
  type: number
- description: Stop price sent with the route
  name: stopPrice
  type: number
- description: Time in force for this route
  name: timeInForce
  type: string
- description: Broker execution strategy name
  name: strategy
  type: string
- description: Strategy-specific parameters sent to the broker
  name: strategyParameters
  type: object
- description: Free-text execution instructions for the broker
  name: executionInstructions
  type: string
- description: Current route status
  name: status
  type: string
- description: Trading account used for this route
  name: account
  type: string
- description: Exchange where execution occurred
  name: exchange
  type: string
- description: Commission charged for this route execution
  name: commission
  type: number
- description: How commission is calculated
  name: commissionType
  type: string
- description: Net monetary amount of the trade (quantity x avgPrice +/- commission)
  name: netAmount
  type: number
- description: Expected or actual settlement date
  name: settlementDate
  type: string
- description: Individual fill records for this route
  name: fills
  type: array
- description: Date the route was created
  name: createdDate
  type: string
- description: Time the route was created (HH:MM:SS)
  name: createdTime
  type: string
- description: Date of the most recent fill
  name: lastFillDate
  type: string
- description: Time of the most recent fill (HH:MM:SS)
  name: lastFillTime
  type: string
- description: Timestamp of the last route update
  name: lastUpdated
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/trade.json
slug: trade
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Trade
---
