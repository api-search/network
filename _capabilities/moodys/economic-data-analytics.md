---
consumed_apis:
- data-buffet
description: Unified economic data analytics capability combining time series retrieval, basket management, order processing, and data search. Used by economists, risk analysts, and data scientists.
layout: capability
name: Moody's Economic Data Analytics
operations:
- description: Retrieve a time series
  method: GET
  name: get-series
  path: /v1/series
personas: []
provider_name: Moody's
provider_slug: moodys
search_terms:
- delete a basket
- list orders
- retrieve a time series
- list vintages for a series
- list baskets
- get multi series
- get order
- download completed order output
- get basket
- search series
- update a basket
- create a new data order
- list vintages
- list all data baskets
- list available data frequencies
- time series data
- list supported output file types
- insurance
- list all orders
- download order
- list frequencies
- climate risk
- get order status and details
- check data buffet api health
- credit risk
- retrieve a single time series by mnemonic
- economic data
- search for available series
- compliance
- risk
- forecasting
- check health
- analytics
- update basket
- get series
- moody's
- create basket
- retrieve multiple time series
- delete basket
- kyc
- screening
- entity verification
- create a new data basket
- list file types
- create order
- financial analytics
- get basket details
slug: economic-data-analytics
tags:
- Moody's
- Economic Data
- Analytics
- Forecasting
tools:
- description: Retrieve a single time series by mnemonic
  hints:
    readOnly: true
  name: get-series
- description: Retrieve multiple time series
  hints:
    readOnly: true
  name: get-multi-series
- description: Search for available series
  hints:
    openWorld: true
    readOnly: true
  name: search-series
- description: List all data baskets
  hints:
    readOnly: true
  name: list-baskets
- description: Create a new data basket
  hints: {}
  name: create-basket
- description: Get basket details
  hints:
    readOnly: true
  name: get-basket
- description: Update a basket
  hints: {}
  name: update-basket
- description: Delete a basket
  hints:
    destructive: true
  name: delete-basket
- description: List all orders
  hints:
    readOnly: true
  name: list-orders
- description: Create a new data order
  hints: {}
  name: create-order
- description: Get order status and details
  hints:
    readOnly: true
  name: get-order
- description: Download completed order output
  hints:
    readOnly: true
  name: download-order
- description: List available data frequencies
  hints:
    readOnly: true
  name: list-frequencies
- description: List vintages for a series
  hints:
    readOnly: true
  name: list-vintages
- description: List supported output file types
  hints:
    readOnly: true
  name: list-file-types
- description: Check Data Buffet API health
  hints:
    readOnly: true
  name: check-health
---
