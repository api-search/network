---
description: A position representing holdings of a specific security within a Bloomberg AIM portfolio, including quantity, valuation, and analytics.
layout: schema
name: Position
properties_list:
- description: Unique position identifier
  name: positionId
  type: string
- description: Identifier of the portfolio holding this position
  name: portfolioId
  type: string
- description: Bloomberg ticker of the security held
  name: ticker
  type: string
- description: Full name of the security
  name: securityName
  type: string
- description: FIGI identifier of the security
  name: figi
  type: string
- description: ISIN of the security
  name: isin
  type: string
- description: Asset class of the held security
  name: assetClass
  type: string
- description: Number of shares, contracts, or units held (negative for short positions)
  name: quantity
  type: number
- description: Long or short position
  name: side
  type: string
- description: Total cost basis of the position in local currency
  name: costBasis
  type: number
- description: Average cost per unit
  name: averageCost
  type: number
- description: Current market price per unit
  name: marketPrice
  type: number
- description: Current market value of the position (quantity x market price)
  name: marketValue
  type: number
- description: Market value converted to portfolio base currency
  name: marketValueBase
  type: number
- description: Local trading currency of the security (ISO 4217)
  name: localCurrency
  type: string
- description: Exchange rate from local currency to portfolio base currency
  name: fxRate
  type: number
- description: Position weight as percentage of total portfolio market value
  name: weight
  type: number
- description: Unrealized profit or loss on the position
  name: unrealizedPnL
  type: number
- description: Realized profit or loss from closed portions
  name: realizedPnL
  type: number
- description: Unrealized P&L as a percentage of cost basis
  name: unrealizedPnLPercent
  type: number
- description: Profit or loss for the current trading day
  name: dailyPnL
  type: number
- description: Accrued interest for fixed income positions
  name: accruedInterest
  type: number
- description: Current yield for fixed income positions
  name: yield
  type: number
- description: Modified duration for fixed income positions
  name: duration
  type: number
- description: Convexity for fixed income positions
  name: convexity
  type: number
- description: Credit rating for fixed income positions
  name: creditRating
  type: string
- description: Beta of the security relative to the benchmark
  name: beta
  type: number
- description: Industry sector of the security
  name: sector
  type: string
- description: Country of the security (ISO 3166-1 alpha-2)
  name: country
  type: string
- description: Date the position was initiated or last traded
  name: tradeDate
  type: string
- description: Settlement date for the most recent trade
  name: settleDate
  type: string
- description: Timestamp of the last position update
  name: lastUpdated
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/position.json
slug: position
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Position
---
