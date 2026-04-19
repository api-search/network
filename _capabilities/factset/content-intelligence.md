---
consumed_apis:
- factset-callstreet
- factset-streetaccount
- factset-filings
- factset-signals
- factset-nlp
- factset-search
- factset-conv
description: Unified workflow for content retrieval and intelligence including news, filings, earnings calls, NLP, signals, and conversational search. Used by content consumers and data scientists.
layout: capability
name: FactSet Content and Intelligence
operations:
- description: Get news articles.
  method: GET
  name: get-news
  path: /v1/news
- description: Get regulatory filings.
  method: GET
  name: get-filings
  path: /v1/filings
- description: Get signals.
  method: GET
  name: get-signals
  path: /v1/signals
- description: Search for answers.
  method: GET
  name: search
  path: /v1/search
personas: []
provider_name: Factset
provider_slug: factset
search_terms:
- streetaccount news.
- search
- signals
- research
- run nlp
- get global regulatory filings.
- get streetaccount news.
- get earnings call transcripts.
- conversational ai query.
- search answers
- get regulatory filings.
- factset
- material event signals.
- get signals
- financial data
- investment analytics
- get news articles.
- global filings.
- get news
- get signals.
- natural language search.
- conversational query
- market data
- portfolio analytics
- news
- get material event signals.
- content
- search for answers.
- run nlp analysis on text.
- financial
- get callstreet events
- get filings
- nlp
slug: content-intelligence
tags:
- FactSet
- Content
- NLP
- News
- Signals
tools:
- description: Get earnings call transcripts.
  hints:
    readOnly: true
  name: get-callstreet-events
- description: Get StreetAccount news.
  hints:
    readOnly: true
  name: get-news
- description: Get global regulatory filings.
  hints:
    readOnly: true
  name: get-filings
- description: Get material event signals.
  hints:
    readOnly: true
  name: get-signals
- description: Run NLP analysis on text.
  hints:
    readOnly: true
  name: run-nlp
- description: Natural language search.
  hints:
    readOnly: true
  name: search-answers
- description: Conversational AI query.
  hints:
    readOnly: true
  name: conversational-query
---
