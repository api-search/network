---
description: A financial security or instrument tracked within Bloomberg AIM, representing an equity, fixed income, derivative, or other tradeable asset.
layout: schema
name: Security
properties_list:
- description: Bloomberg ticker symbol (e.g., 'IBM US Equity')
  name: ticker
  type: string
- description: Full name of the security
  name: name
  type: string
- description: Financial Instrument Global Identifier (FIGI)
  name: figi
  type: string
- description: Composite FIGI for the security
  name: compositeFigi
  type: string
- description: International Securities Identification Number
  name: isin
  type: string
- description: Committee on Uniform Securities Identification Procedures number
  name: cusip
  type: string
- description: Stock Exchange Daily Official List number
  name: sedol
  type: string
- description: Bloomberg unique security identifier
  name: bloombergUniqueId
  type: string
- description: Asset class classification
  name: assetClass
  type: string
- description: Specific security type within the asset class
  name: securityType
  type: string
- description: Primary exchange where the security is listed
  name: exchange
  type: string
- description: Country of domicile (ISO 3166-1 alpha-2)
  name: country
  type: string
- description: Trading currency (ISO 4217)
  name: currency
  type: string
- description: Industry sector classification
  name: sector
  type: string
- description: Industry group within the sector
  name: industryGroup
  type: string
- description: Market capitalization in the trading currency
  name: marketCap
  type: number
- description: Last traded price
  name: lastPrice
  type: number
- description: Current bid price
  name: bidPrice
  type: number
- description: Current ask price
  name: askPrice
  type: number
- description: Trading volume for the current session
  name: volume
  type: integer
- description: Minimum trading lot size
  name: lotSize
  type: integer
- description: Coupon rate for fixed income securities (as a percentage)
  name: couponRate
  type: number
- description: Maturity date for fixed income and derivative securities
  name: maturityDate
  type: string
- description: Issue date of the security
  name: issueDate
  type: string
- description: Strike price for options
  name: strikePrice
  type: number
- description: Expiration date for options and futures
  name: expirationDate
  type: string
- description: Option type
  name: optionType
  type: string
- description: Ticker of the underlying security for derivatives
  name: underlyingTicker
  type: string
- description: Whether the security is actively trading
  name: active
  type: boolean
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/security.json
slug: security
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: Security
---
