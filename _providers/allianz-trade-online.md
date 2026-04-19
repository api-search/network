---
api_count: 4
apis:
- description: 'Report payment overdues, request extension periods, and manage debt rescheduling for trade credit insurance policies. Supports three overdue category types: OVD (report default), EXP (extension period'
  name: Allianz Trade Payment Overdues API
  slug: payment-overdues-api
- description: Retrieve the creditworthiness grade of clients after a cover request. Supports bulk operations for grading multiple companies simultaneously, enabling automated credit risk assessment within ERP syste
  name: Allianz Trade Company Grade API
  slug: company-grade-api
- description: Access and manage all insurance claims declared to Allianz Trade from within your ERP system. Retrieve claim status, submit new claims, and track claim progression for trade credit insurance policies.
  name: Allianz Trade Claims API
  slug: claims-api
- description: Manage your trade credit insurance policy portfolio. Retrieve policy details, create joint insured policies, and manage policy configurations directly from your ERP or credit management system.
  name: Allianz Trade Policy API
  slug: policy-api
capabilities:
- description: ''
  name: Trade Credit Management
  slug: trade-credit-management
common:
- title: ''
  type: Website
  url: https://www.allianz-trade.com/
- title: ''
  type: Portal
  url: https://developers.allianz-trade.com/
- title: ''
  type: GettingStarted
  url: https://developers.allianz-trade.com/docs/getting-started
- title: ''
  type: Documentation
  url: https://developers.allianz-trade.com/docs/api-design-guidelines
- title: ''
  type: ChangeLog
  url: https://developers.allianz-trade.com/whatsnew
- title: ''
  type: Support
  url: mailto:api@allianz-trade.com
- title: ''
  type: SpectralRules
  url: rules/allianz-trade-online-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/allianz-trade-online-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/trade-credit-management.yaml
created: '2024-01-01'
description: 'Allianz Trade APIs enable businesses to automate trade credit insurance management including cover requests, credit limit monitoring, payment overdue reporting, claims management, and company credit grading. Built on secure REST architecture with OAuth2, the APIs support three business lines: Trade Credit Insurance, E-Commerce B2B, and Surety/Guarantee.'
features:
- description: Automate credit limit and cover information importing from Allianz Trade into ERP systems for real-time credit risk management.
  name: Credit Limit Management
- description: Retrieve creditworthiness grades for clients and prospects with bulk operations supporting large portfolio risk assessments.
  name: Company Credit Grading
- description: Report payment defaults, request extension periods, and manage debt rescheduling through standardized overdue category codes.
  name: Payment Overdue Reporting
- description: Integrate claims declaration and tracking directly into ERP systems for streamlined insurance claim management.
  name: Claims Management
- description: Manage trade credit insurance policy portfolios including joint insured policies and policy configuration from enterprise systems.
  name: Policy Portfolio Management
- description: Real-time credit evaluation on a per-transaction basis for B2B e-commerce platforms enabling buy-now-pay-later type scenarios.
  name: E-Commerce B2B Credit
- description: Secure OAuth2 authentication for all API endpoints with client credentials flow for machine-to-machine ERP integrations.
  name: OAuth2 Security
- description: Webhook-based notifications for technical events (job completion) and functional events (business decisions) with HTTPS and IP whitelisting.
  name: Webhook Notifications
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: ERP integration with SAP for automated trade credit management, policy data synchronization, and claims processing.
  name: SAP
- description: Oracle ERP integration for credit limit monitoring and automated policy data synchronization.
  name: Oracle
- description: OpenAPI collections downloadable from the developer portal for Postman, Insomnia, and HTTPie testing.
  name: Postman
- description: CRM integration for combining Allianz Trade risk data with customer relationship management workflows.
  name: Salesforce
jsonld:
- class_count: 0
  name: Allianz Trade Claims Context
  property_count: 22
  slug: allianz-trade-claims-context
- class_count: 0
  name: Allianz Trade Company Grade Context
  property_count: 21
  slug: allianz-trade-company-grade-context
- class_count: 0
  name: Allianz Trade Payment Overdues Context
  property_count: 19
  slug: allianz-trade-payment-overdues-context
- class_count: 0
  name: Allianz Trade Policy Context
  property_count: 23
  slug: allianz-trade-policy-context
layout: provider
modified: '2026-04-19'
name: Allianz Trade
rules:
- name: Allianz Trade API Rules
  rule_count: 22
  severity_counts:
    error: 5
    hint: 0
    info: 3
    warn: 14
  slug: allianz-trade-online-spectral-rules
skills: []
slug: allianz-trade-online
solutions: []
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/apis.yml
use_cases:
- description: Integrate Allianz Trade APIs into SAP, Oracle, or other ERP systems to automate credit risk management and policy administration.
  name: ERP Credit Management Integration
- description: Build custom credit management dashboards pulling live credit grades, cover status, and claim data from Allianz Trade APIs.
  name: Automated Credit Risk Dashboard
- description: Enable real-time per-transaction credit underwriting for B2B online marketplaces and trade platforms using the E-Commerce APIs.
  name: B2B E-Commerce Credit Evaluation
- description: Automate payment overdue reporting to Allianz Trade when customers miss payment deadlines, triggering insurance coverage workflows.
  name: Payment Monitoring and Overdue Automation
---
