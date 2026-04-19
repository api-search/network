---
api_count: 17
apis:
- description: Unified API endpoint to access data, intelligence, and insights from Microsoft 365, Windows, and Enterprise Mobility + Security.
  name: Microsoft Graph API
  slug: ''
- description: Access to Outlook email, including reading, sending, and managing messages.
  name: Outlook Mail API
  slug: ''
- description: Access to Outlook calendar events, scheduling, and meeting management.
  name: Outlook Calendar API
  slug: ''
- description: Access to Outlook personal contacts for managing contact information, creating contact folders, and organizing people data.
  name: Outlook Contacts API
  slug: ''
- description: Access to OneDrive file storage, sharing, and collaboration features.
  name: OneDrive API
  slug: ''
- description: Access to SharePoint sites, lists, and document libraries.
  name: SharePoint API
  slug: ''
- description: Access to Microsoft Teams channels, messages, and collaboration features.
  name: Microsoft Teams API
  slug: ''
- description: Manage Office 365 users, profiles, and organizational information.
  name: Office 365 Users API
  slug: ''
- description: Access to Microsoft Planner tasks, plans, and project management features.
  name: Planner API
  slug: ''
- description: Access to OneNote notebooks, sections, and pages for creating and managing notes and structured content.
  name: OneNote API
  slug: ''
- description: Read and modify Excel workbooks stored in OneDrive and SharePoint, including managing worksheets, tables, charts, ranges, and sessions.
  name: Excel Workbooks and Charts API
  slug: ''
- description: Manage tasks and task lists across To Do clients, Outlook, and Teams for personal task management and day planning.
  name: Microsoft To Do API
  slug: ''
- description: Manage customer bookings, appointment scheduling, business services, and staff information for enterprise and small business owners.
  name: Microsoft Bookings API
  slug: ''
- description: Manage Microsoft 365 groups, group membership, conversations, and group-related resources for collaboration.
  name: Office 365 Groups API
  slug: ''
- description: Connect security products, services, and partners to streamline security operations and improve threat protection, detection, and response.
  name: Microsoft Graph Security API
  slug: ''
- description: Create and join online meetings, manage call records, and enable cloud communications capabilities for applications.
  name: Microsoft Graph Communications API
  slug: ''
- description: Platform for building solutions that extend Office applications including Excel, Outlook, Word, PowerPoint, and OneNote using web technologies and the Office JavaScript API.
  name: Office Add-ins Platform
  slug: ''
capabilities:
- description: Unified productivity workflow combining mail, calendar, user management, and group collaboration for enterprise users and IT administrators.
  name: Microsoft Office 365 Productivity and Collaboration
  slug: productivity-and-collaboration
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-365
- title: ''
  type: StatusPage
  url: https://status.office365.com/
- title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/graph/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: Graph Explorer
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- title: ''
  type: SDK
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- title: What's New
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/graph/whats-new-overview
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- title: ''
  type: TermsOfService
  url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- title: Webhooks
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks
- title: ''
  type: Quickstart
  url: https://developer.microsoft.com/en-us/graph/quick-start
- title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
- title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/graph/compliance-concept-overview
- title: ''
  type: SpectralRules
  url: rules/microsoft-office-365-spectral-rules.yml
- title: Microsoft Graph API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/graph-api.yaml
- title: Productivity and Collaboration Workflow
  type: NaftikoCapability
  url: capabilities/productivity-and-collaboration.yaml
created: '2024-01-15'
description: A collection of APIs provided by Microsoft Office 365 for productivity, collaboration, and enterprise services.
features:
- description: Access Microsoft 365 data through a single REST endpoint at graph.microsoft.com covering mail, calendar, files, users, and groups.
  name: Unified API Endpoint
- description: Subscribe to change notifications via webhooks to receive real-time updates when data changes across Microsoft 365 services.
  name: Real-Time Notifications
- description: Combine multiple API requests into a single HTTP call to reduce network overhead and improve performance.
  name: Batch Requests
- description: Track incremental changes to resources efficiently using delta links without polling entire datasets.
  name: Delta Queries
- description: Read, send, reply, forward, and organize email messages with full attachment and folder support.
  name: Rich Mail Management
- description: Create events, manage calendars, check free/busy availability, and handle meeting responses programmatically.
  name: Calendar and Scheduling
- description: Access OneDrive and SharePoint files with upload, download, sharing, and real-time collaboration capabilities.
  name: File Storage and Sharing
- description: Manage Microsoft Teams channels, messages, tabs, and apps for team communication and collaboration.
  name: Team Collaboration
- description: Create, update, and manage users, groups, and organizational directory resources.
  name: User and Group Management
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365.png
integrations:
- description: Integrate with Azure AD for user authentication, authorization, and directory management.
  name: Azure Active Directory
- description: Build bots, tabs, and messaging extensions that integrate with Microsoft Teams collaboration platform.
  name: Microsoft Teams
- description: Connect Microsoft Graph data to Power Automate flows for no-code/low-code automation.
  name: Power Automate
- description: Feed Microsoft 365 data into Power BI dashboards for business intelligence and reporting.
  name: Power BI
- description: Access SharePoint sites, lists, and document libraries for enterprise content management.
  name: SharePoint
- description: Integrate with Outlook mail, calendar, and contacts for personal and shared mailbox management.
  name: Outlook
jsonld:
- class_count: 0
  name: Microsoft Graph Context
  property_count: 0
  slug: microsoft-graph-context
- class_count: 0
  name: Microsoft Office 365 Context
  property_count: 10
  slug: microsoft-office-365-context
layout: provider
modified: '2026-04-18'
name: Microsoft Office 365
rules:
- name: Microsoft Office 365 API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: microsoft-office-365-spectral-rules
skills: []
slug: microsoft-office-365
solutions: []
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
url: https://www.microsoft.com/en-us/microsoft-365
use_cases:
- description: Build applications that integrate email, calendar, and file management into unified productivity workflows.
  name: Enterprise Productivity Integration
- description: Generate automated reports by pulling data from mail, calendar, and user profiles across the organization.
  name: Automated Reporting
- description: Manage user provisioning, group membership, and directory synchronization for enterprise identity workflows.
  name: Identity and Access Management
- description: Automate team notifications, channel management, and messaging workflows across Microsoft Teams.
  name: Team Communication Automation
- description: Enable multi-user document editing, sharing, and version tracking through OneDrive and SharePoint APIs.
  name: Document Collaboration
---
