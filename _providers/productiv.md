---
api_count: 1
apis:
- description: The Productiv Developer APIs support integrating custom applications into the Productiv platform, allowing external developers to define and publish new connected applications. Includes APIs for pushi
  name: Productiv Developer API
  slug: developer-api
capabilities:
- description: Unified workflow for managing SaaS applications, tracking usage and spend, provisioning users, and auditing platform activity using the Productiv Developer API.
  name: Productiv SaaS Management
  slug: saas-management
common:
- title: ''
  type: Documentation
  url: https://docs.app.productiv.com/
- title: ''
  type: DeveloperPortal
  url: https://productiv.com/
- title: ''
  type: Authentication
  url: https://docs.app.productiv.com/developer-api/authorization.html
- title: ''
  type: Rules
  url: rules/productiv-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/productiv-vocabulary.yaml
- title: ''
  type: Capabilities
  url: capabilities/shared/developer-api.yaml
- title: ''
  type: Capabilities
  url: capabilities/saas-management.yaml
created: '2025-07-11'
description: The SaaS Management Platform that delivers the industrys most comprehensive view of your SaaS portfolio with deep usage analytics, spend data, and feature-level insights to power the technology decisions that support your business.
features:
- name: SaaS Portfolio Management
- name: Usage Analytics
- name: Spend Data Tracking
- name: Provisioning Workflows
- name: Audit Events
- name: Org Chart Integration
- name: Custom Application Connectors
- name: Batch File Upload
- name: Data Export
- name: OAuth2 Authentication
image: /assets/icons/productiv.png
integrations:
- name: Okta
- name: Azure Active Directory
- name: Salesforce
- name: ServiceNow
- name: Workday
- name: Slack
jsonld:
- class_count: 49
  name: Productiv Context
  property_count: 5
  slug: productiv-context
- class_count: 0
  name: Productiv Developer Context
  property_count: 0
  slug: productiv-developer-context
layout: provider
modified: '2026-04-18'
name: Productiv
rules:
- name: Productiv API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: productiv-spectral-rules
skills: []
slug: productiv
solutions: []
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
url: https://raw.githubusercontent.com/api-evangelist/productiv/refs/heads/main/apis.yml
use_cases:
- name: Track SaaS Application Usage
- name: Optimize Software Spend
- name: Automate User Provisioning
- name: Audit Platform Activity
- name: Integrate Custom Applications
- name: Export App Portfolio Data
---
