---
consumed_apis:
- emsx
- http-api
description: Workflow for automated trading combining EMSX order/route management with HTTP API market data for traders and algorithmic trading teams.
layout: capability
name: Bloomberg Trading and Execution
operations:
- description: Create a trading order
  method: POST
  name: create-order
  path: /v1/orders
- description: Get orders from blotter
  method: POST
  name: get-orders
  path: /v1/orders
- description: Route an order to a broker
  method: POST
  name: route-order
  path: /v1/routes
- description: Get routes from blotter
  method: POST
  name: get-routes
  path: /v1/routes
- description: Get order fills
  method: POST
  name: get-fills
  path: /v1/fills
- description: Get security reference data
  method: POST
  name: get-reference-data
  path: /v1/market-data
personas: []
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
search_terms:
- route order
- create a new trading order
- get orders
- market data for trading decisions
- execution management
- get fills
- modify an existing order
- create order
- get routes
- get available broker strategies
- get security reference data for trading
- create a trading order
- fill tracking
- get orders from the emsx blotter
- get intraday ticks
- route an order to a broker
- bloomberg
- cancel/delete an order
- get broker strategies
- delete order
- modify order
- trading
- get routes from blotter
- get intraday tick data for a security
- get emsx teams
- get orders from blotter
- get security reference data
- route management
- order management
- get teams
- market data
- financial data
- get order and route fills
- get routes from the emsx blotter
- portfolio management
- get order fills
- get reference data
slug: trading-and-execution
tags:
- Bloomberg
- Trading
- Execution Management
- Order Management
tools:
- description: Create a new trading order
  hints:
    readOnly: false
  name: create-order
- description: Modify an existing order
  hints:
    readOnly: false
  name: modify-order
- description: Cancel/delete an order
  hints:
    destructive: true
    readOnly: false
  name: delete-order
- description: Get orders from the EMSX blotter
  hints:
    readOnly: true
  name: get-orders
- description: Route an order to a broker
  hints:
    readOnly: false
  name: route-order
- description: Get routes from the EMSX blotter
  hints:
    readOnly: true
  name: get-routes
- description: Get order and route fills
  hints:
    readOnly: true
  name: get-fills
- description: Get available broker strategies
  hints:
    readOnly: true
  name: get-broker-strategies
- description: Get EMSX teams
  hints:
    readOnly: true
  name: get-teams
- description: Get security reference data for trading
  hints:
    readOnly: true
  name: get-reference-data
- description: Get intraday tick data for a security
  hints:
    readOnly: true
  name: get-intraday-ticks
---
