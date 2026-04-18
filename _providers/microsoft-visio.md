---
api_count: 2
apis:
- description: REST API for accessing and interacting with Visio files stored in SharePoint Online and OneDrive for Business through Microsoft Graph. Supports reading pages, shapes, shape data, comments, and hyperli
  name: Microsoft Graph Visio API
  slug: ''
- description: JavaScript API for building add-ins and extending Visio functionality in the browser with access to documents, pages, shapes, and comments.
  name: Visio JavaScript API
  slug: ''
capabilities:
- description: 'Workflow capability for analyzing Visio diagrams including reading pages, shapes, data items, comments, and hyperlinks. Used by business analysts and IT architects to programmatically inspect diagram '
  name: Microsoft Visio Diagram Analysis
  slug: diagram-analysis
common:
- title: ''
  type: Support
  url: https://support.microsoft.com/visio
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/visio-blog/bg-p/VisioBlog
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- title: ''
  type: StatusPage
  url: https://status.microsoft365.com/
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options
- title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- title: ''
  type: SpectralRules
  url: rules/microsoft-visio-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/diagram-analysis.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-visio-vocabulary.yaml
created: '2024'
description: APIs and resources for Microsoft Visio, a diagramming and vector graphics application that helps visualize data-connected business process flows. Provides programmatic access to diagrams, pages, shapes, data items, comments, and hyperlinks through Microsoft Graph and JavaScript APIs.
features:
- description: Render Visio diagrams in the browser via JavaScript API.
  name: Diagram Rendering
- description: Read data items attached to diagram shapes.
  name: Shape Data Access
- description: Navigate and list pages within Visio documents.
  name: Page Navigation
- description: Read and manage comments on shapes.
  name: Comment Support
- description: Access hyperlinks associated with diagram shapes.
  name: Hyperlink Management
image: https://learn.microsoft.com/en-us/graph/images/visio-logo.png
integrations:
- description: Access Visio files stored in SharePoint document libraries.
  name: SharePoint
- description: Work with Visio diagrams in OneDrive for Business.
  name: OneDrive
- description: Trigger workflows based on Visio diagram changes.
  name: Power Automate
jsonld:
- class_count: 7
  name: Microsoft Visio Graph Api Context
  property_count: 13
  slug: microsoft-visio-graph-api-context
layout: provider
modified: '2026-04-18'
name: Microsoft Visio
rules:
- name: Microsoft Visio API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 4
  slug: microsoft-visio-spectral-rules
skills: []
slug: microsoft-visio
solutions: []
tags:
- Business Process
- Diagramming
- Flowcharts
- Microsoft 365
- Visualization
url: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/apis.yml
use_cases:
- description: Programmatically analyze network diagrams for infrastructure review.
  name: Network Topology Analysis
- description: Extract and analyze business process flow data from diagrams.
  name: Business Process Review
- description: Inspect diagram shapes and data for compliance validation.
  name: Compliance Auditing
---
