---
api_count: 0
apis: []
common:
- title: ''
  type: Portal
  url: https://apievangelist.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-03-26'
description: An index and topic collection covering API aggregation, marketplaces, directories, unified APIs, and catalog platforms. API aggregation brings together multiple APIs under a single interface, simplifying integration, reducing maintenance overhead, and enabling consistent authentication and data normalization across disparate services. This collection includes API marketplaces like RapidAPI, unified API platforms like Merge and Apideck, API directories like APIs.guru and APIs.io, web scraping aggregators, and open-source catalog tools like Backstage.
features:
- description: API aggregation platforms expose multiple underlying APIs through a single, standardized interface, reducing the integration burden for developers.
  name: Unified API Interface
- description: API directories and marketplaces like RapidAPI, APIs.guru, and APIs.io help developers discover, evaluate, and subscribe to APIs from multiple providers.
  name: API Marketplaces and Discovery
- description: Unified API platforms like Merge and Apideck normalize data schemas across disparate HR, CRM, and accounting systems into a consistent model.
  name: Data Normalization
- description: Aggregation layers handle OAuth, API keys, and other authentication flows across multiple providers, presenting a single auth interface to the consumer.
  name: Authentication Abstraction
- description: Internal API catalog tools like Backstage and Stoplight enable organizations to document, discover, and govern APIs across the enterprise.
  name: API Catalogs and Internal Discovery
- description: Platforms like Bright Data, Apify, and ScrapingBee aggregate web data and expose it through structured APIs, removing the need for custom scraper maintenance.
  name: Web Scraping as API
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: The largest API marketplace with 40,000+ APIs available to developers through a unified subscription and API key model.
  name: RapidAPI
- description: Unified API for HR, payroll, accounting, CRM, and ATS integrations across 100+ providers.
  name: Merge
- description: Unified API platform for CRM, file storage, accounting, and e-commerce integrations.
  name: Apideck
- description: API aggregation platform enabling AI agents to use 100+ apps as structured tools.
  name: Composio
- description: Open-source developer portal and API catalog platform from Spotify for internal service discovery.
  name: Backstage
- description: Open-source directory of machine-readable API specifications (OpenAPI) maintained by the community.
  name: APIs.guru
- description: Financial data aggregation platform connecting apps to bank accounts and financial institutions.
  name: Plaid
- description: Open-source unified API for OAuth integrations across 200+ apps.
  name: Nango
jsonld:
- class_count: 5
  name: Aggregation Context
  property_count: 12
  slug: aggregation-context
layout: provider
modified: '2026-04-19'
name: Aggregation
skills: []
slug: aggregation
solutions: []
tags:
- API Aggregation
- API Directory
- API Marketplace
url: https://raw.githubusercontent.com/api-evangelist/aggregation/refs/heads/main/apis.yml
use_cases:
- description: Unified API platforms like Merge and Apideck enable applications to sync with dozens of HR systems (BambooHR, Workday, ADP) through a single normalized API.
  name: Unified HR and CRM Integration
- description: API providers publish their APIs to marketplaces like RapidAPI to reach new developer audiences and monetize access through tiered subscription plans.
  name: API Marketplace Distribution
- description: Organizations use API catalogs like Backstage or Stoplight to document, version, and govern internal APIs across product teams.
  name: Internal API Governance
- description: Platforms like Plaid and Codat aggregate financial account data from banks and accounting systems into normalized APIs for fintech applications.
  name: Financial Data Aggregation
- description: Aggregation platforms like Composio expose hundreds of third-party APIs as unified tool sets that AI agents can discover and invoke.
  name: AI Agent Tool Federation
---
