---
api_count: 5
apis:
- description: Provides real-time and historical market data, including stock prices, indices, commodities, and currencies.
  name: Bloomberg Market Data API
  slug: bloomberg-market-data-api
- description: Delivers real-time market data, historical data, reference data, and calculation engine capabilities from the Bloomberg Terminal for server applications.
  name: Bloomberg Server API (SAPI)
  slug: bloomberg-server-api
- description: Provides programmatic access to Bloomberg Data License content including reference, pricing, regulatory, ESG, corporate actions, fundamentals, and alternative data.
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: Enables programmatic management and automation of equities, futures, and options trading through the Bloomberg Execution Management System.
  name: Bloomberg EMSX API
  slug: bloomberg-emsx-api
- description: The Bloomberg Open API (BLPAPI) Core — the foundational service-oriented, socket-based API used by the Desktop API, Server API (SAPI), B-PIPE, and Bloomberg Platform products. Provides Request/Respons
  name: Bloomberg BLPAPI Core
  slug: bloomberg-blpapi-core
capabilities:
- description: Unified workflow for accessing Bloomberg reference data, historical data, intraday analytics, and field discovery. Used by quantitative analysts and portfolio managers.
  name: Bloomberg Market Data
  slug: market-data
common:
- title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
- title: ''
  type: SDK
  url: https://bloomberg.github.io/blpapi-docs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- title: ''
  type: GettingStarted
  url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
- title: ''
  type: Login
  url: https://console.bloomberg.com/
- title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy
- title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- title: ''
  type: SpectralRules
  url: rules/bloomberg-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/bloomberg-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/market-data.yaml
created: '2024-01-20'
description: Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News. Bloomberg provides a suite of developer APIs including BLPAPI, Server API, and the Hypermedia API for programmatic access to market data, analytics, and enterprise services.
features:
- description: Stream live market data for equities, fixed income, commodities, and currencies via subscription.
  name: Real-Time Market Data
- description: Access end-of-day historical time series with periodicity, currency, and corporate-action adjustments.
  name: Historical Data
- description: Retrieve raw tick-by-tick trade and quote data for granular intraday analysis.
  name: Intraday Tick Data
- description: Query current reference, descriptive, fundamental, and pricing field values for securities.
  name: Reference Data
- description: Search and discover Bloomberg field mnemonics and metadata via the API Data Dictionary.
  name: Field Discovery
- description: Access BLPAPI through C, C++, Java, .NET, Python, Perl, and COM Excel SDKs.
  name: Multi-Language SDK
image: /assets/icons/bloomberg.png
integrations:
- description: Extend Bloomberg Terminal capabilities through the Desktop API integration.
  name: Bloomberg Terminal
- description: Access BLPAPI data directly from Excel spreadsheets using the COM Excel SDK.
  name: Excel
- description: Build data analytics and machine learning pipelines with the Python BLPAPI SDK.
  name: Python
- description: Distribute Bloomberg data across enterprise infrastructure using the B-PIPE product.
  name: B-PIPE
jsonld:
- class_count: 0
  name: Bloomberg Context
  property_count: 17
  slug: bloomberg-context
- class_count: 0
  name: Blpapi Core Context
  property_count: 0
  slug: blpapi-core-context
layout: provider
modified: '2026-04-18'
name: Bloomberg
rules:
- name: Bloomberg API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: bloomberg-spectral-rules
skills: []
slug: bloomberg
solutions: []
tags:
- Analytics
- Business Intelligence
- Data License
- Enterprise
- Execution Management
- Financial Services
- Market Data
- News
- Quantitative Analysis
- Trading
- Transaction Cost Analysis
url: https://raw.githubusercontent.com/api-evangelist/bloomberg/refs/heads/main/apis.yml
use_cases:
- description: Build quantitative models using historical and real-time market data for alpha generation.
  name: Quantitative Research
- description: Monitor portfolio risk exposure using real-time pricing and reference data feeds.
  name: Risk Management
- description: Feed market data into trading algorithms via EMSX for automated order execution.
  name: Algorithmic Trading
- description: Access regulatory and compliance data through Data License for reporting requirements.
  name: Regulatory Reporting
---
