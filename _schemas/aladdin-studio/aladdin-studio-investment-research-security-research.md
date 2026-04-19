---
description: Investment research data for a security
layout: schema
name: SecurityResearch
properties_list:
- description: Security identifier
  name: securityId
  type: string
- description: Ticker symbol
  name: ticker
  type: string
- description: Analyst consensus rating
  name: rating
  type: string
- description: Consensus price target
  name: priceTarget
  type: number
- description: Number of analysts covering the security
  name: analystCount
  type: integer
- description: Date of consensus calculation
  name: consensusDate
  type: string
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-investment-research-security-research-schema.json
slug: aladdin-studio-investment-research-security-research
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: SecurityResearch
---
