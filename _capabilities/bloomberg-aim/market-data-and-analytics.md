---
consumed_apis:
- data-license
- http-api
description: Workflow for accessing Bloomberg market data combining the Data License HAPI for bulk data with the HTTP API for real-time reference and historical data, used by quantitative analysts and portfolio managers.
layout: capability
name: Bloomberg Market Data and Analytics
operations:
- description: List available data catalogs
  method: GET
  name: list-catalogs
  path: /v1/catalogs
- description: List security universes
  method: GET
  name: list-universes
  path: /v1/universes
- description: List field lists
  method: GET
  name: list-field-lists
  path: /v1/field-lists
- description: Get reference data for securities
  method: POST
  name: get-reference-data
  path: /v1/reference-data
- description: Get historical end-of-day data
  method: POST
  name: get-historical-data
  path: /v1/historical-data
- description: List completed data distributions
  method: GET
  name: list-distributions
  path: /v1/distributions
personas: []
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
search_terms:
- historical data access
- list available data catalogs
- financial analytics
- reference data access
- get intraday bar data
- portfolio management
- data distributions
- list security universes
- create universe
- financial data
- list completed data distributions
- get historical end-of-day data
- get reference data
- create a bloomberg data request
- order management
- market data
- security universe management
- list field lists
- get reference data for securities
- reference data
- bloomberg
- get data catalog details
- trading
- list universes
- create a security universe for data requests
- search instruments
- data catalog browsing
- get intraday bars
- create data request
- list distributions
- search available bloomberg data fields
- search for securities and instruments
- get historical data
- get reference data for securities via http api
- list available bloomberg data catalogs
- get historical data for securities
- list field lists for data requests
- list catalogs
- search fields
- field list management
- get catalog
slug: market-data-and-analytics
tags:
- Bloomberg
- Market Data
- Financial Analytics
- Reference Data
tools:
- description: List available Bloomberg data catalogs
  hints:
    readOnly: true
  name: list-catalogs
- description: Get data catalog details
  hints:
    readOnly: true
  name: get-catalog
- description: List security universes
  hints:
    readOnly: true
  name: list-universes
- description: Create a security universe for data requests
  hints:
    readOnly: false
  name: create-universe
- description: List field lists for data requests
  hints:
    readOnly: true
  name: list-field-lists
- description: Create a Bloomberg data request
  hints:
    readOnly: false
  name: create-data-request
- description: List completed data distributions
  hints:
    readOnly: true
  name: list-distributions
- description: Get reference data for securities via HTTP API
  hints:
    readOnly: true
  name: get-reference-data
- description: Get historical data for securities
  hints:
    readOnly: true
  name: get-historical-data
- description: Get intraday bar data
  hints:
    readOnly: true
  name: get-intraday-bars
- description: Search available Bloomberg data fields
  hints:
    readOnly: true
  name: search-fields
- description: Search for securities and instruments
  hints:
    readOnly: true
  name: search-instruments
---
