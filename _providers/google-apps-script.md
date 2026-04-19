---
api_count: 1
apis:
- description: The Apps Script API manages Google Apps Script projects, deployments, versions, and processes. It supports creating script projects, updating content, managing deployments, monitoring execution proces
  name: Google Apps Script API
  slug: google-apps-script
capabilities:
- description: Workflow capability for managing Google Apps Script projects, deployments, versions, and script execution. Enables developers and IT admins to automate Google Workspace workflows, manage script lifecy
  name: Google Workspace Automation
  slug: workspace-automation
common:
- title: ''
  type: GettingStarted
  url: https://developers.google.com/apps-script/api/concepts
- title: ''
  type: Pricing
  url: https://developers.google.com/apps-script/guides/services/quotas
- title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
- title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- title: ''
  type: SDK
  url: https://developers.google.com/apps-script/api/quickstart/nodejs
- title: ''
  type: CLI
  url: https://developers.google.com/apps-script/guides/clasp
- title: ''
  type: Documentation
  url: https://developers.google.com/apps-script/reference
- title: ''
  type: Support
  url: https://developers.google.com/apps-script/support
- title: ''
  type: Blog
  url: https://developers.google.com/apps-script/updates
- title: ''
  type: Rules
  url: rules/google-apps-script-spectral-rules.yml
- title: ''
  type: Capabilities
  url: capabilities/shared/apps-script.yaml
- title: ''
  type: Capabilities
  url: capabilities/workspace-automation.yaml
created: '2026-03-13'
description: The Apps Script API provides programmatic access to manage Google Apps Script projects, deployments, and executions. It enables creating and updating script projects, managing project versions and deployments, monitoring script processes, and remotely executing Apps Script functions. The API is essential for automating Apps Script project management and integrating script execution into external applications.
features:
- Create and manage Apps Script projects programmatically
- Deploy script projects as web apps, add-ons, and API executables
- Remotely execute Apps Script functions from external applications
- Monitor script execution processes and metrics
- Version management with immutable snapshots of script code
image: /assets/icons/google-apps-script.png
integrations:
- Google Workspace apps including Sheets, Docs, Slides, Gmail, and Calendar
- Google Cloud Platform services for extended functionality
- External REST APIs via Apps Script UrlFetchApp service
- Google Drive for document and file management automation
- clasp CLI for local development and version control workflows
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 5
  slug: json-ld
- class_count: 0
  name: Openapi Context
  property_count: 0
  slug: openapi-context
layout: provider
modified: '2026-04-18'
name: Google Apps Script
rules:
- name: Google Apps Script API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-apps-script-spectral-rules
skills: []
slug: google-apps-script
solutions: []
tags:
- Apps Script
- Automation
- Deployments
- Google
- Google Workspace
- Scripting
url: https://raw.githubusercontent.com/api-evangelist/google-apps-script/refs/heads/main/apis.yml
use_cases:
- Automating Google Workspace workflows across Sheets, Docs, and Gmail
- Building custom add-ons and integrations for Google Workspace
- Managing script deployments across development and production environments
- Monitoring script execution health and performance metrics
- Integrating Apps Script automation into CI/CD pipelines
---
