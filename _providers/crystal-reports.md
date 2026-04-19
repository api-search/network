---
api_count: 3
apis:
- description: RESTful API for managing and generating Crystal Reports programmatically.
  name: Crystal Reports REST API
  slug: rest-api
- description: Software Development Kit for embedding Crystal Reports into applications.
  name: Crystal Reports SDK
  slug: sdk
- description: API for Crystal Reports Server administration and report management.
  name: Crystal Reports Server REST API
  slug: server-rest-api
capabilities:
- description: Unified workflow for managing Crystal Reports including authentication, repository browsing, report viewing, data access, and export. Used by report developers, BI analysts, and application developers
  name: Crystal Reports Report Management
  slug: report-management
common:
- title: ''
  type: Portal
  url: https://api.sap.com
- title: ''
  type: Blog
  url: https://blogs.sap.com/tags/73554900100800000134/
- title: ''
  type: Community
  url: https://community.sap.com/topics/crystal-reports
- title: ''
  type: Support
  url: https://support.sap.com/crystal-reports
- title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
created: '2024-01-01'
description: APIs and resources for Crystal Reports, a business intelligence application for designing and generating reports from various data sources.
features:
- description: Generate formatted reports from relational databases, spreadsheets, and XML data sources.
  name: Report Generation
- description: Embed report viewers in web and desktop applications for interactive report consumption.
  name: Report Viewing
- description: Schedule automated report generation and delivery via email or file system.
  name: Report Scheduling
- description: Pass dynamic parameters to filter and customize report content at runtime.
  name: Parameter Prompts
- description: Export reports to PDF, Excel, Word, CSV, XML, and other formats programmatically.
  name: Export Formats
- description: Embed linked sub-reports within parent reports for drill-down capabilities.
  name: Sub-Reports
- description: Generate pivot-table style cross-tabulation reports from data.
  name: Cross-Tab Reports
- description: Create charts and graphs within reports for data visualization.
  name: Charting
- description: Connect to SQL Server, Oracle, SAP HANA, ODBC, JDBC, and other data sources.
  name: Data Source Connectivity
- description: Manage report server instances, folders, users, and security via REST API.
  name: Report Server Management
image: /assets/icons/crystal-reports.png
integrations: []
jsonld:
- class_count: 22
  name: Crystal Reports Context
  property_count: 54
  slug: crystal-reports-context
layout: provider
modified: '2026-04-17'
name: Crystal Reports
rules:
- name: Crystal Reports API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: crystal-reports-spectral-rules
skills: []
slug: crystal-reports
solutions:
- description: Desktop report designer for creating and editing report templates.
  name: SAP Crystal Reports
- description: Server platform for scheduling, managing, and distributing reports.
  name: SAP Crystal Reports Server
- description: Enterprise BI platform with Crystal Reports integration.
  name: SAP BusinessObjects BI
tags:
- Business Intelligence
- Crystal Reports
- Data Analytics
- Enterprise Software
- Reporting
- SAP
url: https://raw.githubusercontent.com/api-evangelist/crystal-reports/refs/heads/main/apis.yml
use_cases:
- description: Generate financial statements, balance sheets, and P&L reports from ERP data.
  name: Financial Reporting
- description: Create operational reports for manufacturing, logistics, and supply chain.
  name: Operational Dashboards
- description: Generate regulatory compliance reports for auditing and governance.
  name: Compliance Reports
- description: Produce formatted invoices and statements from billing data.
  name: Customer Invoicing
- description: Generate employee reports, headcount analytics, and compensation summaries.
  name: HR Analytics
- description: Embed Crystal Reports viewer into custom applications for end-user reporting.
  name: Embedded Reporting
---
