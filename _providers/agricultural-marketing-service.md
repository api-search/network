---
api_count: 3
apis:
- description: The Market Analysis Reporting System (MARS) API provides programmatic access to USDA AMS agricultural market news data. The API allows users to automatically pull raw market news data including commod
  name: USDA AMS MARS API (MyMarketNews)
  slug: ''
- description: The Livestock Mandatory Price Reporting System (LMPRS) API provides programmatic access to federally mandated livestock price report data. The API requires no authentication for public access and retu
  name: USDA AMS LMPRS API (Livestock Mandatory Price Reporting)
  slug: ''
- description: The USDA Local Food Directories API provides data sharing access to directory information for farmers markets, food hubs, on-farm markets, community supported agriculture (CSA) operations, and food co
  name: USDA Local Food Directories API
  slug: ''
common:
- title: ''
  type: Website
  url: https://www.ams.usda.gov/
- title: ''
  type: Portal
  url: https://www.ams.usda.gov/resources/apis-open-data
- title: ''
  type: GitHubOrganization
  url: https://github.com/usda
- title: ''
  type: TermsOfService
  url: https://www.usda.gov/policies-and-links
- title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
- title: ''
  type: SpectralRules
  url: rules/agricultural-marketing-service-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/agricultural-marketing-service-vocabulary.yaml
created: '2024-11-21'
description: 'The Agricultural Marketing Service (AMS), an agency of the United States Department of Agriculture (USDA), oversees programs in five commodity areas: cotton and tobacco, dairy, fruits and vegetables, livestock and seeds, and poultry. AMS provides testing, standardization, grading, and market news services. AMS operates several public APIs for agricultural market data including the Market Analysis Reporting System (MARS) API for real-time commodity market news and the Livestock Mandatory Price Reporting System (LMPRS) API for livestock price data.'
features:
- description: The MARS and LMPRS APIs are publicly accessible without authentication; registered users can obtain API keys for higher rate limits.
  name: No Authentication Required
- description: All API responses are returned in JSON format including errors and paginated results.
  name: JSON Data Format
- description: MARS API provides up-to-date commodity price and volume data as reports are released by AMS market reporters.
  name: Real-Time Market News
- description: Access up to 180 days of historical market data per request with up to 100,000 records returned per call.
  name: Historical Data Access
- description: Market data covers livestock, dairy, fruits, vegetables, grains, cotton, tobacco, poultry, and other agricultural commodities.
  name: Commodity Coverage
- description: LMPRS API provides federally mandated livestock price data under the Livestock Mandatory Reporting Act.
  name: Mandatory Price Reporting
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: USDA AMS provides guides for integrating MARS API data directly into Microsoft Excel for market analysis.
  name: Microsoft Excel
- description: AMS APIs are accessible through the federal api.data.gov gateway for consistent API key management.
  name: api.data.gov
jsonld:
- class_count: 9
  name: Agricultural Marketing Service Mars Api Context
  property_count: 25
  slug: agricultural-marketing-service-mars-api-context
layout: provider
modified: '2026-04-19'
name: Agricultural Marketing Service
rules:
- name: Agricultural Marketing Service API Rules
  rule_count: 23
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 13
  slug: agricultural-marketing-service-spectral-rules
skills: []
slug: agricultural-marketing-service
solutions: []
tags:
- Agriculture
- Federal Government
- Market News
- Livestock
- Dairy
- Fruits And Vegetables
- Cotton
- Tobacco
url: https://raw.githubusercontent.com/api-evangelist/agricultural-marketing-service/refs/heads/main/apis.yml
use_cases:
- description: Track commodity prices across livestock, dairy, fruits, and vegetables to support trading, purchasing, and production decisions.
  name: Agricultural Price Monitoring
- description: Pull historical and current market news data for academic research, economic analysis, and policy work.
  name: Market Analysis and Research
- description: Integrate USDA market news data into supply chain management and procurement systems for real-time pricing.
  name: Supply Chain Integration
- description: Use the Local Food Directories API to locate and integrate data about farmers markets, CSAs, and food hubs.
  name: Local Food System Mapping
- description: Build automated price monitoring systems using the MARS API to trigger alerts when prices cross defined thresholds.
  name: Commodity Price Alerts
---
