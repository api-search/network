---
api_count: 4
apis:
- description: Provides programmatic access to Bloomberg's comprehensive financial, pricing, reference, regulatory, and alternative data covering over 50 million securities and 56,000 fields via the Hypermedia API (
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: Server API delivers real-time market data, historical data, premium reference data, and calculation tools from the Bloomberg Terminal into front-office applications.
  name: Bloomberg Server API (SAPI)
  slug: bloomberg-server-api
- description: The Execution Management System API allows developers to manage and automate trading for equities, futures, and options.
  name: Bloomberg EMSX API
  slug: bloomberg-emsx-api
- description: Makes the Bloomberg Open API available via HTTP and WebSockets, allowing clients to access reference and historical request-response data as well as subscribe to live streaming market data.
  name: Bloomberg HTTP API
  slug: bloomberg-http-api
capabilities:
- description: Workflow for accessing Bloomberg market data combining the Data License HAPI for bulk data with the HTTP API for real-time reference and historical data, used by quantitative analysts and portfolio ma
  name: Bloomberg Market Data and Analytics
  slug: market-data-and-analytics
- description: Workflow for automated trading combining EMSX order/route management with HTTP API market data for traders and algorithmic trading teams.
  name: Bloomberg Trading and Execution
  slug: trading-and-execution
common:
- title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- title: ''
  type: Documentation
  url: https://bloomberg.github.io/blpapi-docs/
- title: ''
  type: GettingStarted
  url: https://data.bloomberglp.com/professional/sites/10/2017/03/BLPAPI-Core-Developer-Guide.pdf
- title: ''
  type: Console
  url: https://console.bloomberg.com/
- title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/
- title: ''
  type: Blog
  url: https://www.bloomberg.com/company/stories/category/tech-at-bloomberg/
- title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- title: ''
  type: SDK
  url: https://github.com/bloomberg/blpapi-node
- title: ''
  type: SDK
  url: https://github.com/bloomberg/blpapi-python
- title: ''
  type: SDK
  url: https://github.com/bloomberg/blpapi-java
created: '2024-01-15'
description: Bloomberg's Asset and Investment Manager (AIM) is a comprehensive buy-side solution offering global, multi-asset capabilities for portfolio management, trading, compliance, and operations. Bloomberg provides a suite of developer APIs including BLPAPI, Server API, and the Hypermedia API for programmatic access to market data, analytics, and enterprise services.
features:
- Access to 50M+ Securities and 56K+ Data Fields
- Real-Time and Historical Market Data
- Hypermedia-Driven REST API (HAPI)
- Execution Management for Equities, Futures, and Options
- WebSocket Streaming for Live Market Data
- Instrument and Field Search
- Scheduled Data Delivery via Triggers
image: /assets/icons/bloomberg-aim.png
integrations:
- Bloomberg Terminal
- Excel via Bloomberg Add-In
- Python (blpapi-python)
- Java (blpapi-java)
- Node.js (blpapi-node)
- .NET (blpapi-dotnet)
- Order Management Systems
jsonld:
- class_count: 0
  name: Bloomberg Data License Context
  property_count: 0
  slug: bloomberg-data-license-context
- class_count: 0
  name: Bloomberg Emsx Context
  property_count: 0
  slug: bloomberg-emsx-context
- class_count: 0
  name: Bloomberg Http Context
  property_count: 0
  slug: bloomberg-http-context
- class_count: 0
  name: context Context
  property_count: 6
  slug: context
layout: provider
modified: '2026-04-18'
name: Bloomberg AIM
rules:
- name: Bloomberg AIM API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: bloomberg-aim-spectral-rules
skills: []
slug: bloomberg-aim
solutions: []
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-aim/refs/heads/main/apis.yml
use_cases:
- Automated Portfolio Data Retrieval
- Algorithmic Trading Order Management
- Regulatory Compliance Data Extraction
- Real-Time Market Data Integration
- Historical Data Analysis and Backtesting
- Multi-Asset Trade Execution Automation
---
