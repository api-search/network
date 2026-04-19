---
api_count: 6
apis:
- description: The Airwallex Payment Acceptance API enables businesses to accept online payments globally. Supports credit and debit cards, local payment methods, and 3D Secure. Available as hosted checkout or embed
  name: Airwallex Payment Acceptance API
  slug: payment-acceptance
- description: The Airwallex Global Accounts API enables businesses to create and manage multi-currency accounts. Supports account creation, balance management, account statements, and receiving funds in multiple cu
  name: Airwallex Global Accounts API
  slug: global-accounts
- description: The Airwallex Payouts API enables businesses to send cross-border payments to suppliers, contractors, and employees globally. Supports bank transfers to 150+ countries, bulk payouts, and beneficiary m
  name: Airwallex Payouts API
  slug: payouts
- description: The Airwallex FX API provides access to real-time foreign exchange rates and currency conversion. Supports spot conversions, rate quotes, and conversion history for 60+ currencies.
  name: Airwallex FX API
  slug: fx
- description: The Airwallex Issuing API enables businesses to create and manage virtual and physical corporate cards for employee spending. Supports card issuance, spend controls, transaction management, and expens
  name: Airwallex Issuing API
  slug: issuing
- description: The Airwallex Platform API enables businesses to embed financial services into their products. Supports merchant onboarding, sub-account management, platform payments, and split payouts for marketplac
  name: Airwallex Platform API
  slug: platform
capabilities:
- description: ''
  name: Payments Management
  slug: payments-management
common:
- title: ''
  type: Portal
  url: https://www.airwallex.com
- title: ''
  type: GettingStarted
  url: https://www.airwallex.com/docs/api
- title: ''
  type: Documentation
  url: https://www.airwallex.com/docs/api#/Introduction
- title: ''
  type: Authentication
  url: https://www.airwallex.com/docs/api#/Payment_Acceptance/Authentication
- title: ''
  type: Pricing
  url: https://www.airwallex.com/pricing
- title: ''
  type: TermsOfService
  url: https://www.airwallex.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://www.airwallex.com/privacy
- title: ''
  type: Blog
  url: https://www.airwallex.com/blog
- title: ''
  type: GitHubOrganization
  url: https://github.com/airwallex
- title: Airwallex CLI
  type: CLI
  url: https://github.com/airwallex/airwallex-cli
- title: Magento Plugin
  type: SDK
  url: https://github.com/airwallex/paymentacceptance-plugin-magento
- title: Salesforce Commerce Cloud
  type: SDK
  url: https://github.com/airwallex/airwallex-salesforce-commerce-cloud-cartridge
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/rules/airwallex-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/capabilities/payments-management.yaml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/vocabulary/airwallex-vocabulary.yaml
created: '2025-02-17'
description: Airwallex is a financial technology company that specializes in providing global payment solutions for businesses. Their platform enables companies to accept payments, manage multi-currency accounts, convert currencies at competitive rates, send cross-border payments, issue corporate cards, and embed financial services into their own products. Airwallex serves businesses in over 150 countries with APIs for payment acceptance, FX, accounts, transfers, and embedded finance.
features:
- description: Accept payments in 180+ currencies via cards and local payment methods.
  name: Global Payment Acceptance
- description: Hold, manage, and convert funds in 60+ currencies.
  name: Multi-Currency Accounts
- description: Send payments to 150+ countries with competitive FX rates.
  name: Cross-Border Payouts
- description: Real-time currency conversion at competitive exchange rates.
  name: FX Conversion
- description: Issue virtual and physical Visa cards for employee spending.
  name: Corporate Card Issuing
- description: Embed Airwallex financial services into your own platform.
  name: Embedded Finance
- description: iOS, Android, React Native, and Flutter SDKs for in-app payments.
  name: Mobile SDKs
- description: Real-time event notifications for payment status changes.
  name: Webhooks
- description: Built-in fraud detection and risk scoring via the Airwallex Risk SDK.
  name: Risk Management
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Airwallex payment plugin for Magento/Adobe Commerce stores.
  name: Magento
- description: Airwallex payment cartridge for Salesforce Commerce Cloud.
  name: Salesforce Commerce Cloud
- description: Payment gateway plugin for WooCommerce stores.
  name: WooCommerce
- description: Sync Airwallex transactions with Xero accounting software.
  name: Xero
- description: Accounting integration for Airwallex transactions.
  name: QuickBooks
- description: ERP integration for Airwallex payment data.
  name: NetSuite
jsonld:
- class_count: 6
  name: Airwallex Context
  property_count: 19
  slug: airwallex-context
layout: provider
modified: '2026-04-19'
name: Airwallex
rules:
- name: Airwallex API Rules
  rule_count: 29
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 14
  slug: airwallex-spectral-rules
skills: []
slug: airwallex
solutions: []
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/apis.yml
use_cases:
- description: Accept global payments on e-commerce stores and marketplaces.
  name: E-Commerce Checkout
- description: Pay international suppliers and contractors efficiently.
  name: Cross-Border B2B Payments
- description: Issue cards and track employee spending globally.
  name: Employee Expense Management
- description: Manage treasury operations across multiple currencies.
  name: Multi-Currency Treasury
- description: Collect and distribute payments to marketplace sellers.
  name: Marketplace Split Payments
- description: Embed payment processing into SaaS platforms.
  name: SaaS Platform Monetization
- description: Pay remote workers and freelancers in their local currencies.
  name: Freelancer Payouts
---
