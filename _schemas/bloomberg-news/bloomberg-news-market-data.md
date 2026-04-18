---
description: Schema for Bloomberg market data representing real-time and reference data for financial securities as delivered through the BLPAPI //blp/mktdata (subscription) and //blp/refdata (request/response) services. Covers equities, fixed income, commodities, currencies, and indices.
layout: schema
name: Bloomberg Market Data
properties_list:
- description: ''
  name: security
  type: object
- description: ISO 8601 timestamp of the market data snapshot
  name: timestamp
  type: string
- description: ''
  name: pricing
  type: object
- description: ''
  name: volume
  type: object
- description: ''
  name: referenceData
  type: object
- description: Array of historical data points from the //blp/refdata HistoricalDataRequest service
  name: historicalData
  type: array
- description: Intraday bar data from the BLPAPI IntradayBarRequest service with OHLCV aggregation per interval
  name: intradayBar
  type: array
- description: Field-level errors for unavailable or invalid requested fields as returned by the BLPAPI response
  name: fieldExceptions
  type: array
- description: ''
  name: securityError
  type: object
provider_name: Bloomberg News
provider_slug: bloomberg-news
schema_file: json-schema/bloomberg-news-market-data-schema.json
slug: bloomberg-news-market-data
tags:
- Analytics
- Business Intelligence
- Financial Services
- Market Data
- News
title: Bloomberg Market Data
---
