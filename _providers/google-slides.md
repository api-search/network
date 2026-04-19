---
api_count: 1
apis:
- description: Create and edit presentations programmatically.
  name: Google Slides API
  slug: ''
capabilities:
- description: Unified presentation management workflow for creating, reading, editing, and generating thumbnails of Google Slides presentations for content creators and automation engineers.
  name: Google Slides Presentation Management
  slug: presentation-management
common:
- title: ''
  type: Portal
  url: https://console.cloud.google.com/
- title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- title: ''
  type: GettingStarted
  url: https://developers.google.com/slides/api/quickstart/python
- title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- title: Developer Products
  type: Documentation
  url: https://developers.google.com/workspace/products
- title: Credentials
  type: Documentation
  url: https://developers.google.com/workspace/guides/create-credentials
- title: Enable APIs
  type: Documentation
  url: https://developers.google.com/workspace/guides/enable-apis
- title: OAuth Consent Screen
  type: Documentation
  url: https://developers.google.com/workspace/guides/configure-oauth-consent
- title: OAuth Scopes
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2/scopes
- title: Issue Tracker
  type: Support
  url: https://issuetracker.google.com/bookmark-groups/78025
- title: Workspace Release Notes
  type: ReleaseNotes
  url: https://developers.google.com/workspace/release-notes
- title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/application-development/introducing-google-slides-api
- title: ''
  type: SpectralRules
  url: rules/google-slides-spectral-rules.yml
- title: Google Slides API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/slides-api.yaml
- title: Presentation Management Workflow
  type: NaftikoCapability
  url: capabilities/presentation-management.yaml
created: '2024-01-01'
description: An API for creating, reading, and editing Google Slides presentations.
features:
- description: Create blank or pre-configured presentations programmatically with custom titles and layouts.
  name: Presentation Creation
- description: Apply multiple changes to a presentation in a single atomic request for efficient editing.
  name: Batch Updates
- description: Add, reorder, duplicate, and delete slides within presentations.
  name: Slide Management
- description: Insert and format text, shapes, images, videos, tables, and charts on slides.
  name: Text and Shape Editing
- description: Generate thumbnail images of individual slides for previews and exports.
  name: Page Thumbnails
- description: Use existing presentations as templates and populate them with dynamic content.
  name: Template Support
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Embed live charts and data from Google Sheets into presentations for dynamic data visualization.
  name: Google Sheets
- description: Store, organize, and share presentations through Google Drive with collaboration permissions.
  name: Google Drive
- description: Part of the Google Workspace suite with seamless integration across Docs, Sheets, and other apps.
  name: Google Workspace
- description: Automate Slides workflows using Apps Script for custom macros and triggers.
  name: Google Apps Script
- description: Deploy Slides API integrations on Google Cloud Platform infrastructure.
  name: Google Cloud
jsonld:
- class_count: 0
  name: Google Slides Context
  property_count: 0
  slug: google-slides-context
layout: provider
modified: '2026-04-18'
name: Google Slides
rules:
- name: Google Slides API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-slides-spectral-rules
skills: []
slug: google-slides
solutions: []
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
url: https://developers.google.com/slides
use_cases:
- description: Generate presentation reports from data sources, populating charts, tables, and text automatically.
  name: Automated Report Generation
- description: Create branded presentations from templates, filling in customer-specific data for sales or marketing decks.
  name: Dynamic Presentation Templates
- description: Build educational slide decks programmatically from lesson plans, quizzes, or course materials.
  name: Educational Content Creation
- description: Automatically compile meeting agendas, status updates, and metrics into presentation format.
  name: Meeting Preparation
---
