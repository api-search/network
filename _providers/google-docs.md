---
api_count: 1
apis:
- description: The Google Docs API lets you create and modify documents.
  name: Google Docs API
  slug: ''
capabilities:
- description: Unified workflow for creating, reading, and editing Google Docs documents including content manipulation, formatting, and template automation. Used by developers automating document workflows.
  name: Google Docs Document Management
  slug: document-management
common:
- title: ''
  type: Portal
  url: https://developers.google.com/docs
- title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/guides/enable-apis
- title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/
- title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- title: ''
  type: SpectralRules
  url: rules/google-docs-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/google-docs-vocabulary.yaml
- title: Docs API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/docs-api.yaml
- title: Document Management Workflow
  type: NaftikoCapability
  url: capabilities/document-management.yaml
created: '2024-01-01'
description: API for creating, reading, and editing Google Docs documents.
features:
- description: Programmatically create new Google Docs documents with titles and initial content.
  name: Document Creation
- description: Insert, replace, and delete text, images, tables, and other content elements using batch updates.
  name: Content Manipulation
- description: Apply text styles, paragraph styles, named styles, headers, footers, and document-level styling.
  name: Rich Formatting
- description: Create, modify, merge, and unmerge table cells with fine-grained style control.
  name: Table Management
- description: Work with suggestions, comments, and revision history in shared documents.
  name: Collaborative Editing
- description: Use named ranges and text replacement to merge data into document templates at scale.
  name: Template Automation
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Store and organize documents in Google Drive with sharing and permission controls.
  name: Google Drive
- description: Embed linked charts from Google Sheets that update automatically in documents.
  name: Google Sheets
- description: Extend document functionality with custom menus, sidebars, and automation scripts.
  name: Google Apps Script
- description: Build add-ons that enhance the Docs editing experience with custom UI panels.
  name: Google Workspace Add-ons
- description: Connect Google Docs to thousands of apps for automated document workflows.
  name: Zapier
jsonld:
- class_count: 0
  name: Google Docs Context
  property_count: 36
  slug: google-docs-context
- class_count: 0
  name: Google Docs V1 Context
  property_count: 0
  slug: google-docs-v1-context
layout: provider
modified: '2026-04-18'
name: Google Docs
rules:
- name: Google Docs API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-docs-spectral-rules
skills: []
slug: google-docs
solutions: []
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
url: https://raw.githubusercontent.com/api-evangelist/google-docs/refs/heads/main/apis.yml
use_cases:
- description: Generate reports, invoices, contracts, and other documents from templates with dynamic data insertion.
  name: Document Generation
- description: Perform bulk document personalization by replacing placeholders with recipient-specific data.
  name: Mail Merge
- description: Import and convert content from other formats into Google Docs for collaboration.
  name: Content Migration
- description: Automate document creation and updates as part of business workflows triggered by events.
  name: Workflow Automation
- description: Generate standardized compliance reports and audit documentation from structured data.
  name: Compliance Documentation
---
