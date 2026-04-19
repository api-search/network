---
api_count: 4
apis:
- description: The ADP Workers API enables access to employee and worker data including personal information, job assignments, pay grades, and employment status. REST APIs support worker lifecycle management for HCM
  name: ADP Workers API
  slug: adp-workers-api
- description: The ADP Payroll API provides programmatic access to payroll processing, payroll output data, and compensation management. REST APIs support payroll runs, payroll output retrieval (including CSV-format
  name: ADP Payroll API
  slug: adp-payroll-api
- description: The ADP Embedded Payroll API enables ISVs and platforms to embed ADP payroll capabilities directly into their applications. REST APIs support payroll processing, tax compliance, and workforce manageme
  name: ADP Embedded Payroll API
  slug: adp-embedded-payroll-api
- description: The ADP Benefits Administration API provides access to employee benefits enrollment, eligibility, and plan data. APIs support benefits carrier connectivity, open enrollment workflows, and benefits dat
  name: ADP Benefits Administration API
  slug: adp-benefits-api
common:
- title: ''
  type: Portal
  url: https://developers.adp.com/
- title: ''
  type: Documentation
  url: https://developers.adp.com/
- title: ''
  type: GettingStarted
  url: https://developers.adp.com/getting-started/client-integration-overview
- title: ''
  type: Authentication
  url: https://developers.adp.com/getting-started/client-integration-overview
- title: ADP Workers OpenAPI
  type: OpenAPI
  url: openapi/adp-workers-openapi.yml
- title: ADP Payroll OpenAPI
  type: OpenAPI
  url: openapi/adp-payroll-openapi.yml
- title: ADP Worker JSON Schema
  type: JSONSchema
  url: json-schema/adp-worker-schema.json
- title: ADP JSON-LD Context
  type: JSONLD
  url: json-ld/adp-context.jsonld
created: '2026-03-18'
description: ADP (Automatic Data Processing) is a global provider of cloud-based human capital management solutions including payroll, benefits, talent, time, tax, and HR services for businesses of all sizes.
features:
- description: Manage the complete worker lifecycle including hiring, onboarding, job changes, and termination through REST APIs.
  name: Worker Lifecycle Management
- description: Programmatic access to payroll runs, payroll output data, and compensation analysis across ADP platforms.
  name: Payroll Processing
- description: Embed ADP payroll capabilities directly into ISV and partner applications with white-label support.
  name: Embedded Payroll
- description: Manage employee benefits enrollment, eligibility, and plan data with carrier connectivity support.
  name: Benefits Administration
- description: Access department structures, organizational hierarchies, and work assignment data.
  name: Organizational Data
- description: Retrieve payroll and workforce data in CSV-formatted bulk exports for analytics and reporting.
  name: Bulk Data Export
image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
integrations:
- description: Full integration with ADP Workforce Now for mid-market HR, payroll, talent, and benefits management.
  name: ADP Workforce Now
- description: Enterprise-grade HCM integration for large organizations with complex payroll and HR requirements.
  name: ADP Vantage HCM
- description: Payroll and HR integration for small businesses using the ADP RUN platform.
  name: ADP RUN Powered by ADP
jsonld:
- class_count: 0
  name: Adp Context
  property_count: 5
  slug: adp-context
- class_count: 0
  name: Adp Payroll Context
  property_count: 0
  slug: adp-payroll-context
- class_count: 0
  name: Adp Workers Context
  property_count: 0
  slug: adp-workers-context
layout: provider
modified: '2026-04-18'
name: ADP
rules:
- name: ADP API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: adp-spectral-rules
skills: []
slug: adp
solutions: []
tags:
- Benefits
- HCM
- HR
- Payroll
- Workforce
url: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/apis.yml
use_cases:
- description: Synchronize worker data between ADP and third-party HRIS, ERP, and workforce management systems.
  name: HCM Integration
- description: Automate payroll instruction submission and output retrieval for streamlined payroll processing workflows.
  name: Payroll Automation
- description: Extract headcount, compensation, and departmental data for workforce planning and business intelligence.
  name: Workforce Analytics
- description: Integrate ADP payroll processing directly into partner software applications for small business customers.
  name: ISV Embedded Payroll
---
