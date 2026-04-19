---
description: ''
layout: schema
name: Distribution
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: FactSet identifier that uniquely identifies the Event.
  name: eventId
  type: string
- description: Corporate Actions Event type code.
  name: eventTypeCode
  type: string
- description: Corporate Actions Event type description.
  name: eventTypeDesc
  type: string
- description: Date Event was announced in YYYY-MM-DD format.
  name: announcementDate
  type: string
- description: Date of Record for distribution in YYYY-MM-DD format.
  name: recordDate
  type: string
- description: Date of Payment for distribution in YYYY-MM-DD format.
  name: payDate
  type: string
- description: Effective Date or Ex-Date of distribution in YYYY-MM-DD format.
  name: effectiveDate
  type: string
- description: Factor for adjusting price and shares. A 2-for-1 split returns .50, the number you would multiply the stock price by to adjust for the split.
  name: adjFactor
  type: number
- description: Combined adjustment factor for all distribution events on that day.
  name: adjFactorCombined
  type: number
- description: Default Amount - Trading Currency, Split Adjusted
  name: amtDefTradingAdj
  type: number
- description: Default Amount - Trading Currency, Unadjusted
  name: amtDefTradingUnadj
  type: number
- description: 'Currency ISO code. For more details, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: Distribution percentage of the event (i.e. 10%). Typical for stock distributions.
  name: distPct
  type: number
- description: Component of distribution ratio - Number of shares held.
  name: distOldTerm
  type: number
- description: Component of distribution ratio - Number of shares received.
  name: distNewTerm
  type: number
- description: Description
  name: rightsIssuePrice
  type: number
- description: Description
  name: rightsIssueCurrency
  type: string
- description: Textual description identifying the event.
  name: shortDesc
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-global-prices-distribution-schema.json
slug: factset-global-prices-distribution
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Distribution
---
