---
api_count: 1
apis:
- description: The AWS Supply Chain API provides programmatic access to create and manage supply chain instances, data lakes, data integrations, and bills of materials for supply chain visibility and risk management
  name: AWS Supply Chain API
  slug: aws-supply-chain-api
capabilities: []
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/supply-chain/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/aws-supply-chain/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/industries/supply-chain/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/scn/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-supply-chain-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-supply-chain-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-supply-chain.yaml
created: '2026-03-16'
description: AWS Supply Chain is a cloud-based application that works with your existing enterprise resource planning (ERP) and supply chain management systems to help you manage supply chain risks. It provides ML-powered insights and recommended actions to help mitigate supply chain disruptions.
features:
- description: Machine learning models provide risk visibility and recommended actions for supply chain disruptions.
  name: ML-Powered Insights
- description: Connects with existing ERP and supply chain management systems via data integration flows.
  name: ERP Integration
- description: Centralized data lake for supply chain data with namespace and dataset management.
  name: Data Lake
- description: Import bill of materials data from S3 for inventory and component tracking.
  name: Bill of Materials Import
- description: Event-driven data ingestion for real-time supply chain data updates.
  name: Data Integration Events
- description: Create and manage multiple supply chain instances for different business units.
  name: Multi-instance
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Connect SAP ERP data to AWS Supply Chain via data integration flows.
  name: SAP ERP
- description: Integrate Oracle ERP supply chain data for unified visibility.
  name: Oracle ERP
- description: Import and export supply chain data via S3 for batch processing.
  name: Amazon S3
- description: Send supply chain events to EventBridge for downstream processing.
  name: Amazon EventBridge
- description: Integrate IoT sensor data for real-time supply chain monitoring.
  name: AWS IoT
jsonld:
- class_count: 8
  name: Amazon Supply Chain Context
  property_count: 23
  slug: amazon-supply-chain-context
layout: provider
modified: '2026-04-19'
name: Amazon Supply Chain
rules:
- name: Amazon Supply Chain API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 5
  slug: amazon-supply-chain-spectral-rules
skills: []
slug: amazon-supply-chain
solutions: []
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/apis.yml
use_cases:
- description: Identify and mitigate supply chain disruptions with ML-powered risk insights.
  name: Supply Chain Risk Management
- description: Unified view of inventory across suppliers, warehouses, and distribution centers.
  name: Inventory Visibility
- description: Integrate ERP data with AWS Supply Chain for unified supply chain visibility.
  name: ERP Data Integration
- description: Use ML models to forecast demand and optimize inventory levels.
  name: Demand Forecasting
---
