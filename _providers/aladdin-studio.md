---
api_count: 4
apis:
- description: The Aladdin Graph API provides RESTful access to portfolio data, securities, positions, risk analytics, and other Aladdin platform capabilities. Powers the AladdinSDK Python client with OAuth and Basi
  name: Aladdin Graph API
  slug: graph-api
- description: The Aladdin Data Cloud API provides access to Snowflake-based analytics data warehousing with OAuth and JWT authentication. Enables large-scale portfolio analytics and data science workflows using Sno
  name: Aladdin Data Cloud API
  slug: data-cloud-api
- description: The Aladdin Trading API enables order management and trading workflow integration. Available as the asdk_plugin_trading Python package built on the AladdinSDK framework.
  name: Aladdin Trading API
  slug: trading-api
- description: The Aladdin Investment Research API provides access to research data, analyst insights, and quantitative analytics built on Aladdin's data infrastructure. Available as the asdk_plugin_investment_resea
  name: Aladdin Investment Research API
  slug: investment-research-api
capabilities:
- description: Workflow capability combining the Aladdin Graph API and Data Cloud API for institutional portfolio analytics. Provides portfolio managers, risk analysts, and quantitative researchers with unified acce
  name: Aladdin Studio Portfolio Analytics
  slug: portfolio-analytics
common:
- title: ''
  type: Portal
  url: https://www.blackrock.com/aladdin/products/apis
- title: ''
  type: Documentation
  url: https://www.blackrock.com/aladdin/products/aladdin-studio
- title: ''
  type: GitHubOrganization
  url: https://github.com/blackrock
- title: Python SDK (AladdinSDK)
  type: SDK
  url: https://github.com/blackrock/aladdinsdk
- title: Python SDK (PyPI)
  type: SDK
  url: https://pypi.org/project/aladdinsdk/
- title: Plugin Builder
  type: SDK
  url: https://github.com/blackrock/aladdinsdk-plugin-builder
- title: ''
  type: SpectralRules
  url: rules/aladdin-studio-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/aladdin-studio-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/aladdin-studio-context.jsonld
- title: Aladdin Graph API Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/graph-api.yaml
- title: Aladdin Data Cloud API Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/data-cloud-api.yaml
- title: Portfolio Analytics Workflow
  type: NaftikoCapability
  url: capabilities/portfolio-analytics.yaml
created: '2024-03-05'
description: Aladdin Studio is BlackRock's developer platform enabling institutional investors, asset managers, and wealth managers to build custom solutions on top of the Aladdin investment operating system. APIs provide access to portfolio data, risk analytics, trading, investment research, and the Aladdin Data Cloud, supporting approximately $25 trillion in assets managed on the platform.
features:
- description: Retrieve comprehensive portfolio data including positions, holdings, securities, and performance metrics across asset classes.
  name: Portfolio Data Access
- description: Access Aladdin's institutional-grade risk analytics including factor exposures, VaR, scenario analysis, and stress testing across public and private markets.
  name: Risk Analytics
- description: Snowflake-based data warehousing providing access to large-scale portfolio analytics with OAuth and JWT authentication supporting both Snowflake connectors and Snowpark.
  name: Aladdin Data Cloud
- description: Order management and trading workflow APIs enabling integration with Aladdin's trading platform for order creation, tracking, and execution.
  name: Trading Integration
- description: APIs for accessing investment research data, analyst insights, and quantitative analytics built on Aladdin's data infrastructure.
  name: Investment Research Access
- description: Support for long-running operation (LRO) patterns with configurable polling, enabling asynchronous processing of computationally intensive analytics requests.
  name: Long-Running Operations
- description: Batch API support with sequential and parallel execution capabilities for processing large volumes of portfolio data operations efficiently.
  name: Batch Processing
- description: Flexible authentication supporting Basic Auth with API tokens, OAuth client credentials flow, OAuth refresh token flow, and Snowflake JWT for Data Cloud access.
  name: Multi-Auth Support
- description: Extensible SDK plugin architecture enabling domain-specific packages (trading, investment research) built on top of the core AladdinSDK.
  name: Plugin Architecture
- description: Downloadable Python Jupyter Notebooks and code samples in multiple languages for rapid solution development and prototyping.
  name: Jupyter Notebook Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native Aladdin Data Cloud integration with Snowflake for large-scale analytics, supporting both standard connectors and Snowpark for Python-based data science workflows.
  name: Snowflake
- description: Aladdin available on AWS infrastructure (general availability expected second half of 2026) complementing existing Azure deployment.
  name: Amazon Web Services
- description: Primary cloud infrastructure for Aladdin platform, supporting enterprise deployments across institutional clients.
  name: Microsoft Azure
- description: Private markets data integrated into Aladdin ecosystem following BlackRock's acquisition for alternatives and private market analytics.
  name: Preqin
- description: First-class Python support via AladdinSDK on PyPI, with Jupyter Notebook examples and plugin architecture for domain extensions.
  name: Python Ecosystem
- description: ESG risk data integrated into Aladdin portfolio management for reputational and environmental risk analysis.
  name: RepRisk
jsonld:
- class_count: 18
  name: Aladdin Studio Context
  property_count: 72
  slug: aladdin-studio-context
layout: provider
modified: '2026-04-19'
name: Aladdin Studio
rules:
- name: Aladdin Studio API Rules
  rule_count: 36
  severity_counts:
    error: 16
    hint: 0
    info: 3
    warn: 17
  slug: aladdin-studio-spectral-rules
skills: []
slug: aladdin-studio
solutions: []
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
url: https://raw.githubusercontent.com/api-evangelist/aladdin-studio/refs/heads/main/apis.yml
use_cases:
- description: Build bespoke portfolio analysis tools using Aladdin's risk and performance data to generate custom insights for investment teams.
  name: Custom Portfolio Analytics
- description: Automate generation of risk reports, factor exposure summaries, and stress test results using Aladdin's risk analytics APIs.
  name: Automated Risk Reporting
- description: Integrate Aladdin trading data into proprietary order management systems and automate trading workflow processes.
  name: Trading Workflow Automation
- description: Connect internal research platforms to Aladdin's investment research data for unified analyst workflow tooling.
  name: Investment Research Integration
- description: Access Aladdin Data Cloud from Snowflake-based data science environments for quantitative model development and backtesting.
  name: Data Science and Quantitative Research
- description: Build automated client reporting solutions pulling portfolio performance, risk, and holdings data from Aladdin APIs.
  name: Client Reporting Automation
- description: Analyze portfolios across public equities, fixed income, alternatives, and private markets using Aladdin's unified data platform.
  name: Multi-Asset Class Analytics
---
