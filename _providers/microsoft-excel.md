---
api_count: 3
apis:
- description: REST API for accessing and manipulating Excel workbooks stored in OneDrive for Business, SharePoint sites, or Group drives through Microsoft Graph. Supports worksheet, table, chart, range, named item,
  name: Microsoft Graph Excel API
  slug: ''
- description: Office Add-ins API for building custom functionality within Excel using JavaScript and TypeScript.
  name: Excel JavaScript API
  slug: ''
- description: TypeScript-based automation for Excel on the web, enabling Power Automate integration for business process automation.
  name: Office Scripts API
  slug: ''
capabilities:
- description: Workflow capability for automating Excel spreadsheet operations including worksheet management, data manipulation, table operations, and chart generation via Microsoft Graph.
  name: Microsoft Excel Spreadsheet Automation
  slug: spreadsheet-automation
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-365
- title: ''
  type: Support
  url: https://support.microsoft.com/excel
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/excel
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/excel-blog/bg-p/ExcelBlog
- title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- title: ''
  type: SpectralRules
  url: rules/microsoft-excel-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/spreadsheet-automation.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-excel-vocabulary.yaml
created: '2024'
description: APIs for automating, integrating, and extending Microsoft Excel functionality including workbook management, data manipulation, charting, and formula execution through Microsoft Graph REST APIs.
features:
- description: Persistent and non-persistent sessions for efficient API operations.
  name: Workbook Sessions
- description: Read, write, and format individual cells or ranges of cells.
  name: Cell Range Operations
- description: Create, update, sort, and filter structured tables.
  name: Table Management
- description: Create and manage charts with customizable source data.
  name: Chart Generation
- description: Invoke Excel functions programmatically via the API.
  name: Workbook Functions
- description: Define and manage named ranges for reusable cell references.
  name: Named Ranges
image: https://learn.microsoft.com/en-us/graph/images/excel-logo.png
integrations:
- description: Automate Excel workflows using Power Automate connectors.
  name: Microsoft Power Automate
- description: Access and modify Excel files stored in SharePoint sites.
  name: SharePoint
- description: Work with Excel workbooks stored in OneDrive for Business.
  name: OneDrive
- description: Share and collaborate on Excel workbooks within Teams.
  name: Microsoft Teams
jsonld:
- class_count: 9
  name: Microsoft Excel Graph Api Context
  property_count: 20
  slug: microsoft-excel-graph-api-context
layout: provider
modified: '2026-04-18'
name: Microsoft Excel
rules:
- name: Microsoft Excel API Rules
  rule_count: 24
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 6
  slug: microsoft-excel-spectral-rules
skills: []
slug: microsoft-excel
solutions: []
tags:
- Automation
- Data Analysis
- Microsoft
- Microsoft 365
- Office
- Spreadsheets
url: https://raw.githubusercontent.com/api-evangelist/microsoft-excel/refs/heads/main/apis.yml
use_cases:
- description: Generate and update Excel reports from external data sources.
  name: Automated Reporting
- description: Programmatically insert and update data in spreadsheets.
  name: Data Entry Automation
- description: Use Excel functions API for financial calculations.
  name: Financial Modeling
- description: Create charts and visualizations from data.
  name: Dashboard Generation
---
