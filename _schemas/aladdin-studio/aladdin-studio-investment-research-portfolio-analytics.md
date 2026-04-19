---
description: Investment analytics and performance metrics for a portfolio
layout: schema
name: PortfolioAnalytics
properties_list:
- description: Portfolio identifier
  name: portfolioId
  type: string
- description: Analytics period start date
  name: fromDate
  type: string
- description: Analytics period end date
  name: toDate
  type: string
- description: Total portfolio return for the period
  name: totalReturn
  type: number
- description: Excess return vs benchmark
  name: excessReturn
  type: number
- description: Information ratio for the period
  name: informationRatio
  type: number
- description: Sharpe ratio for the period
  name: sharpeRatio
  type: number
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-investment-research-portfolio-analytics-schema.json
slug: aladdin-studio-investment-research-portfolio-analytics
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: PortfolioAnalytics
---
