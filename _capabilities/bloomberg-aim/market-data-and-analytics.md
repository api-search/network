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
- get historical data
- list field lists
- get reference data
- get reference data for securities via http api
- order management
- list distributions
- create data request
- security universe management
- data distributions
- financial analytics
- get historical end-of-day data
- create a security universe for data requests
- get historical data for securities
- search for securities and instruments
- search available bloomberg data fields
- financial data
- create a bloomberg data request
- search fields
- bloomberg
- data catalog browsing
- get intraday bar data
- get data catalog details
- field list management
- list security universes
- search instruments
- list catalogs
- create universe
- market data
- list available bloomberg data catalogs
- get catalog
- get reference data for securities
- list completed data distributions
- get intraday bars
- list available data catalogs
- portfolio management
- list field lists for data requests
- trading
- reference data access
- list universes
- reference data
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
