---
consumed_apis:
- factset-ofdb
- factset-sdf
- factset-cfd
- factset-xdf-model
- factset-xdf-entire
- factset-xdf-symbol
- factset-dst
- factset-prog
- factset-prb
description: Unified workflow for data management including custom databases, standard datafeeds, exchange datafeeds, content feeds, and programmatic environments. Used by data engineers.
layout: capability
name: FactSet Data Management
operations:
- description: List databases.
  method: GET
  name: list-databases
  path: /v1/databases
- description: List datafeeds.
  method: GET
  name: list-datafeeds
  path: /v1/datafeeds
personas: []
provider_name: Factset
provider_slug: factset
search_terms:
- standard datafeed.
- get exchange datafeed model.
- data management
- get direct streaming data.
- get exchange datafeed snapshot.
- etl
- get streaming
- list datafeeds
- list datafeeds.
- get programmatic environment.
- datafeed
- get content feeds
- financial data
- get content feeds dictionary.
- investment analytics
- get standard datafeed.
- market data
- research
- get xdf snapshot
- get xdf model
- factset
- list ofdb
- get standard datafeed
- get prog env
- list databases
- ofdb database management.
- portfolio analytics
- list databases.
- financial
- list ofdb databases.
slug: data-management
tags:
- FactSet
- Data Management
- Datafeed
- ETL
tools:
- description: List OFDB databases.
  hints:
    readOnly: true
  name: list-ofdb
- description: Get standard datafeed.
  hints:
    readOnly: true
  name: get-standard-datafeed
- description: Get content feeds dictionary.
  hints:
    readOnly: true
  name: get-content-feeds
- description: Get exchange datafeed model.
  hints:
    readOnly: true
  name: get-xdf-model
- description: Get exchange datafeed snapshot.
  hints:
    readOnly: true
  name: get-xdf-snapshot
- description: Get direct streaming data.
  hints:
    readOnly: true
  name: get-streaming
- description: Get programmatic environment.
  hints:
    readOnly: true
  name: get-prog-env
---
