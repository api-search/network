---
description: An investment portfolio managed within Bloomberg AIM, containing positions across multiple securities with associated analytics and compliance attributes.
layout: schema
name: Portfolio
properties_list:
- description: Unique portfolio identifier within the AIM system
  name: portfolioId
  type: string
- description: Human-readable portfolio name
  name: name
  type: string
- description: Description of the portfolio strategy or purpose
  name: description
  type: string
- description: Classification of the portfolio
  name: portfolioType
  type: string
- description: Base reporting currency (ISO 4217)
  name: currency
  type: string
- description: Bloomberg ticker of the benchmark index
  name: benchmarkTicker
  type: string
- description: Portfolio manager responsible for investment decisions
  name: manager
  type: string
- description: Unique identifier for the portfolio manager
  name: managerId
  type: string
- description: Custodian institution for the portfolio's assets
  name: custodian
  type: string
- description: Account identifier at the custodian
  name: custodianAccountId
  type: string
- description: Date the portfolio was created
  name: inceptionDate
  type: string
- description: Current portfolio status
  name: status
  type: string
- description: Total market value of all positions in base currency
  name: totalMarketValue
  type: number
- description: Total cost basis of all positions in base currency
  name: totalCostBasis
  type: number
- description: Available cash balance in the portfolio
  name: cashBalance
  type: number
- description: Unrealized profit and loss across all open positions
  name: unrealizedPnL
  type: number
- description: Realized profit and loss from closed positions
  name: realizedPnL
  type: number
- description: Total return as a percentage since inception
  name: totalReturn
  type: number
- description: Year-to-date return as a percentage
  name: ytdReturn
  type: number
- description: Month-to-date return as a percentage
  name: mtdReturn
  type: number
- description: Current positions held in the portfolio
  name: positions
  type: array
- description: Asset allocation breakdown as percentage weights
  name: assetAllocation
  type: object
- description: Portfolio-level risk metrics
  name: riskMetrics
  type: object
- description: Portfolio compliance status
  name: complianceStatus
  type: string
- description: Custom tags for portfolio classification
  name: tags
  type: array
- description: Timestamp of the last portfolio update
  name: lastUpdated
  type: string
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/portfolio.json
slug: portfolio
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Portfolio
---
