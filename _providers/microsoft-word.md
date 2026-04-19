---
api_count: 4
apis:
- description: 'REST API for interacting with Word documents in Microsoft 365 and OneDrive via the Microsoft Graph unified endpoint. Provides operations for file management, content access, sharing, permissions, and '
  name: Microsoft Graph Word API
  slug: ''
- description: JavaScript API for building Word add-ins and automating Word tasks. Provides strongly-typed objects for document manipulation, content controls, tables, formatting, comments, collaboration, and shapes
  name: Office JavaScript API for Word
  slug: ''
- description: Server-side document conversion and automation service for SharePoint. Supports batch conversion of Word documents to PDF, XPS, and other formats without user interaction.
  name: Word Automation Services (SharePoint)
  slug: ''
- description: .NET library for programmatically creating and manipulating Word documents using the ECMA-376 Open XML standard. Provides strongly-typed classes for document structure, styles, tables, images, and con
  name: Open XML SDK for Word
  slug: ''
capabilities:
- description: Unified workflow for Word document creation, editing, collaboration, conversion, and lifecycle management. Combines Microsoft Graph for cloud storage and sharing, JavaScript API for content manipulati
  name: Microsoft Word Document Management
  slug: document-management
common:
- title: ''
  type: Portal
  url: https://developer.microsoft.com/
- title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- title: ''
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- title: ''
  type: SignUp
  url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/get-started
- title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- title: ''
  type: Support
  url: https://developer.microsoft.com/graph/support
- title: ''
  type: StatusPage
  url: https://status.office.com/
- title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/microsoft-graph
- title: ''
  type: X
  url: https://twitter.com/MSGraphDev
- title: ''
  type: YouTube
  url: https://www.youtube.com/@Microsoft365Developer
- title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/browse/?products=ms-graph
- title: ''
  type: SpectralRules
  url: rules/microsoft-word-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-word-vocabulary.yaml
- title: Document Management
  type: NaftikoCapability
  url: capabilities/document-management.yaml
created: '2024'
description: APIs for Microsoft Word document creation, manipulation, and automation across Microsoft 365 cloud services, Office Add-ins, SharePoint, and Open XML document processing.
features:
- description: Programmatically create Word documents from templates or scratch using REST APIs or JavaScript.
  name: Document Creation
- description: Convert Word documents to PDF, HTML, and other formats using server-side automation services.
  name: Document Conversion
- description: Insert, edit, and format text, paragraphs, tables, images, and content controls in Word documents.
  name: Content Manipulation
- description: Track changes, manage comments, co-authoring sessions, and revision history through APIs.
  name: Collaboration
- description: Mail merge, document assembly, and template-based document generation for enterprise workflows.
  name: Template Processing
- description: Access and manipulate Word documents stored in OneDrive, SharePoint, and Microsoft 365 cloud services.
  name: Cloud Storage Integration
- description: Build custom Word add-ins with JavaScript APIs for task panes, content insertion, and document automation.
  name: Add-In Extensibility
- description: Low-level manipulation of Word document structure using the ECMA-376 Open XML standard.
  name: Open XML Processing
image: /assets/icons/microsoft-word.png
integrations:
- description: Store, manage, and collaborate on Word documents through SharePoint document libraries and workflows.
  name: Microsoft SharePoint
- description: Access and sync Word documents via OneDrive cloud storage through Microsoft Graph APIs.
  name: Microsoft OneDrive
- description: Collaborate on Word documents directly within Teams channels and chat conversations.
  name: Microsoft Teams
- description: Automate Word document workflows including creation, conversion, and approval routing with Power Automate flows.
  name: Microsoft Power Automate
- description: AI-powered document creation, editing, and summarization through Copilot agents with add-in actions.
  name: Microsoft Copilot
- description: OAuth 2.0 authentication and authorization for secure API access through Microsoft Identity Platform.
  name: Azure Active Directory
jsonld:
- class_count: 11
  name: Microsoft Word Graph Api Context
  property_count: 16
  slug: microsoft-word-graph-api-context
- class_count: 10
  name: Microsoft Word Javascript Api Context
  property_count: 27
  slug: microsoft-word-javascript-api-context
- class_count: 4
  name: Microsoft Word Open Xml Sdk Context
  property_count: 23
  slug: microsoft-word-open-xml-sdk-context
layout: provider
modified: '2026-04-18'
name: Microsoft Word
rules:
- name: Microsoft Word API Rules
  rule_count: 39
  severity_counts:
    error: 18
    hint: 0
    info: 4
    warn: 17
  slug: microsoft-word-spectral-rules
skills: []
slug: microsoft-word
solutions: []
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/apis.yml
use_cases:
- description: Generate standardized reports from data sources using templates and API-driven document creation.
  name: Automated Report Generation
- description: Assemble legal documents by merging clauses, terms, and client data into Word templates.
  name: Contract and Legal Document Assembly
- description: Automate review cycles with tracked changes, comments, and approval workflows via APIs.
  name: Document Review Workflows
- description: Process large volumes of Word documents for format conversion, content extraction, or metadata updates.
  name: Bulk Document Processing
- description: Build task pane add-ins that connect Word to CRM, ERP, or other business systems for data insertion.
  name: Custom Business Add-Ins
- description: Ensure regulatory compliance by automating document formatting, metadata tagging, and archiving.
  name: Compliance Document Management
---
