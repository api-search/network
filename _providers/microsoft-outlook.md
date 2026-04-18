---
api_count: 10
apis:
- description: API for accessing Outlook email messages, folders, and mail settings through Microsoft Graph.
  name: Microsoft Graph Mail API
  slug: ''
- description: API for accessing Outlook calendar events, calendars, and meeting scheduling through Microsoft Graph.
  name: Microsoft Graph Calendar API
  slug: ''
- description: API for accessing Outlook contacts and contact folders through Microsoft Graph.
  name: Microsoft Graph Contacts API
  slug: ''
- description: API for accessing Outlook tasks and to-do items through Microsoft Graph.
  name: Microsoft Graph Tasks API
  slug: ''
- description: JavaScript API for building Outlook add-ins that extend Outlook functionality with custom features, using the Office.js library and the Mailbox requirement set.
  name: Outlook Add-ins API
  slug: ''
- description: API for accessing people data relevant to the user, aggregating information from contacts, social networks, organization directory, and recent communications.
  name: Microsoft Graph People API
  slug: ''
- description: API for subscribing to changes in Outlook resources including mail, calendar events, and contacts via webhooks, enabling real-time notifications.
  name: Microsoft Graph Change Notifications API
  slug: ''
- description: API for managing Focused Inbox overrides and message classification, allowing applications to control how incoming messages are categorized between Focused and Other tabs.
  name: Microsoft Graph Focused Inbox API
  slug: ''
- description: API for managing Outlook inbox rules that automatically process incoming messages based on conditions, enabling actions like moving messages to folders, assigning categories, and forwarding.
  name: Microsoft Graph Mail Rules API
  slug: ''
- description: API for managing Outlook categories, allowing applications to create, read, update, and delete categories in a user's master category list for organizing messages, events, and contacts.
  name: Microsoft Graph Categories API
  slug: ''
asyncapis:
- description: 'AsyncAPI specification for Microsoft Graph change notifications (webhooks) for Outlook mail resources. Enables real-time event-driven architecture by subscribing to changes in messages, mail folders, '
  name: Microsoft Outlook Change Notifications
  slug: microsoft-outlook-change-notifications-asyncapi
capabilities:
- description: Unified capability for Microsoft Outlook email productivity combining mail operations, folder management, and attachment handling via Microsoft Graph. Used by productivity teams, IT administrators, an
  name: Microsoft Outlook Email Productivity
  slug: email-productivity
common:
- title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/overview
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/outlook/
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- title: ''
  type: SDK
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
- title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/tag/outlook/
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- title: ''
  type: SignUp
  url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
- title: ''
  type: Login
  url: https://portal.azure.com
- title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/microsoft-graph
- title: ''
  type: Quickstart
  url: https://developer.microsoft.com/en-us/graph/quick-start
- title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-fundamentals/
created: '2024'
description: Microsoft Outlook is a personal information manager and email client that is part of the Microsoft Office suite. It provides email, calendar, contact management, task management, and other productivity features.
features:
- Email management with full CRUD operations on messages
- Calendar scheduling with meeting invitations and RSVPs
- Contact management across personal and organizational directories
- Task and to-do list management
- Focused Inbox classification and mail rules
- Real-time change notifications via webhooks
- Rich attachment handling with large file support
- Categories for organizing messages, events, and contacts
- People insights aggregated across multiple sources
- Outlook add-in extensibility via Office.js
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2019/11/Outlook-logo.png
integrations:
- Microsoft Teams
- Microsoft Power Automate
- Microsoft Power Apps
- SharePoint
- OneDrive
- Azure Active Directory
- Microsoft To Do
jsonld:
- class_count: 0
  name: Microsoft Graph Mail Context
  property_count: 0
  slug: microsoft-graph-mail-context
- class_count: 0
  name: Microsoft Outlook Context
  property_count: 13
  slug: microsoft-outlook-context
layout: provider
modified: '2026-04-18'
name: Microsoft Outlook
rules:
- name: Microsoft Outlook API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: microsoft-outlook-spectral-rules
skills: []
slug: microsoft-outlook
solutions: []
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
url: https://outlook.office.com
use_cases:
- Building email client integrations and automation workflows
- Scheduling meetings and managing calendars programmatically
- Syncing contacts between systems
- Creating automated email processing pipelines
- Building productivity dashboards with mail and calendar data
- Extending Outlook with custom add-ins
---
