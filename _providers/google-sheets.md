---
api_count: 2
apis:
- description: The Google Sheets API lets you read, write, and format Google Sheets data.
  name: Google Sheets API v4
  slug: ''
- description: The built-in Google Apps Script Spreadsheet Service allows creation, access, and modification of Google Sheets files directly from Apps Script with performance bundling and numerous classes for format
  name: Google Apps Script Spreadsheet Service
  slug: ''
capabilities:
- description: Workflow for managing spreadsheet data including creating spreadsheets, reading and writing cell values, batch operations, and metadata management. Used by data analysts, developers, and automation en
  name: Google Sheets Spreadsheet Data Management
  slug: spreadsheet-data-management
common:
- title: ''
  type: Portal
  url: https://developers.google.com/workspace/sheets/api
- title: ''
  type: Documentation
  url: https://developers.google.com/workspace/sheets/api/reference/rest
- title: ''
  type: Blog
  url: https://workspace.google.com/blog/developers-practitioners
- title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- title: ''
  type: Support
  url: https://developers.google.com/sheets/api/support
- title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: SignUp
  url: https://console.cloud.google.com/
- title: ''
  type: Login
  url: https://console.cloud.google.com/
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-sheets-api
- title: ''
  type: YouTube
  url: https://developers.google.com/workspace/sheets/api/videos
- title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/sheets/api/guides/concepts
- title: ''
  type: Authentication
  url: https://developers.google.com/sheets/api/guides/authorizing
- title: ''
  type: SDK
  url: https://developers.google.com/workspace/sheets/api/guides/libraries
- title: ''
  type: ReleaseNotes
  url: https://developers.google.com/workspace/sheets/release-notes
- title: ''
  type: Pricing
  url: https://developers.google.com/workspace/sheets/api/limits
- title: ''
  type: RateLimits
  url: https://developers.google.com/workspace/sheets/api/limits
- title: ''
  type: SpectralRules
  url: rules/google-sheets-spectral-rules.yml
- title: Google Sheets API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/google-sheets.yaml
- title: Spreadsheet Data Management Workflow
  type: NaftikoCapability
  url: capabilities/spreadsheet-data-management.yaml
created: '2024-01-01'
description: API for reading, writing, and formatting data in Google Sheets.
features:
- description: Create, read, update, and delete spreadsheets programmatically with full control over properties and metadata.
  name: Spreadsheet Management
- description: Read and write individual cell values, ranges, and batch operations across multiple ranges.
  name: Cell Value Operations
- description: Apply rich formatting to cells including fonts, colors, borders, alignment, and number formats.
  name: Formatting
- description: Add, remove, copy, and configure individual sheets within a spreadsheet.
  name: Sheet Management
- description: Attach custom metadata to spreadsheets, sheets, rows, and columns for application-specific data.
  name: Developer Metadata
- description: Set validation rules on cells to enforce data quality and consistency.
  name: Data Validation
- description: Apply conditional formatting rules based on cell values and formulas.
  name: Conditional Formatting
- description: Create and manage embedded charts within spreadsheets.
  name: Charts and Graphs
- description: Define and manage named ranges for easier formula references.
  name: Named Ranges
- description: Execute multiple read and write operations in a single API call for efficiency.
  name: Batch Operations
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Deep integration with Google Docs, Slides, Forms, and other Workspace applications.
  name: Google Workspace
- description: Extend Sheets functionality with custom functions, menus, and automation scripts.
  name: Google Apps Script
- description: Connect to BigQuery, Cloud Functions, and other GCP services for advanced data processing.
  name: Google Cloud Platform
- description: Connect Google Sheets to thousands of apps through Zapier automation workflows.
  name: Zapier
- description: Send notifications and updates to Slack channels based on spreadsheet changes.
  name: Slack
jsonld:
- class_count: 0
  name: Google Sheets Context
  property_count: 0
  slug: google-sheets-context
layout: provider
modified: '2026-04-18'
name: Google Sheets
rules:
- name: Google Sheets API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-sheets-spectral-rules
skills: []
slug: google-sheets
solutions: []
tags:
- Google Workspace
- Productivity
- Spreadsheets
url: https://developers.google.com/sheets/api
use_cases:
- description: Collect data from various sources and generate automated reports in Google Sheets.
  name: Data Collection and Reporting
- description: Use Google Sheets as a lightweight database for web applications and prototypes.
  name: Database Backend
- description: Automate data entry, processing, and distribution workflows using the API.
  name: Workflow Automation
- description: Synchronize data between Google Sheets and other business applications.
  name: Data Integration
- description: Build interactive dashboards and visualizations from spreadsheet data.
  name: Dashboard Creation
---
