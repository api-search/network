---
description: Risk analytics for a portfolio computed by Aladdin's risk engine
layout: schema
name: PortfolioRisk
properties_list:
- description: Portfolio identifier
  name: portfolioId
  type: string
- description: Risk calculation date
  name: asOfDate
  type: string
- description: Annualized tracking error vs benchmark
  name: trackingError
  type: number
- description: 95% Value at Risk (1-day)
  name: var95
  type: number
- description: Portfolio beta vs benchmark
  name: beta
  type: number
- description: Annualized portfolio volatility
  name: volatility
  type: number
- description: Factor exposure breakdown
  name: factorExposures
  type: array
- description: Risk model used for calculation
  name: riskModel
  type: string
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-graph-portfolio-risk-schema.json
slug: aladdin-studio-graph-portfolio-risk
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: PortfolioRisk
---
