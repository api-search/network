---
api_count: 4
apis:
- description: The SharePoint REST API enables developers to interact remotely with SharePoint data using any technology that supports REST web requests.
  name: SharePoint REST API
  slug: rest-api
- description: Access SharePoint sites, lists, and documents through the Microsoft Graph unified API endpoint.
  name: Microsoft Graph API (SharePoint)
  slug: graph-api-sharepoint
- description: Client-side object model for SharePoint that provides access to SharePoint objects through .NET managed or JavaScript libraries.
  name: SharePoint CSOM (Client-Side Object Model)
  slug: csom-client-side-object-model
- description: SharePoint webhooks provide a way to get notified about changes to SharePoint lists and document libraries.
  name: SharePoint Webhooks API
  slug: webhooks-api
capabilities:
- description: Unified workflow for managing SharePoint content including sites, lists, items, files, and search. Used by content managers, site admins, and collaboration teams.
  name: SharePoint Content Management
  slug: content-management
common:
- title: ''
  type: Developer Portal
  url: https://developer.microsoft.com/en-us/sharepoint
- title: ''
  type: Code Samples
  url: https://pnp.github.io/
- title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/sharepoint/ct-p/SharePoint
- title: ''
  type: Support
  url: https://support.microsoft.com/en-us/sharepoint
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/sharepoint/compare-sharepoint-plans
- title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
created: '2024'
description: Microsoft SharePoint is a web-based collaborative platform that integrates with Microsoft Office. It provides enterprise content management, document management, and collaboration capabilities.
features:
- description: Create, read, update, and delete SharePoint sites and subsites.
  name: Sites and Webs
- description: Full CRUD operations on lists, document libraries, and list items.
  name: Lists and Libraries
- description: Upload, download, check in/out, and manage documents and file versions.
  name: Document Management
- description: Create folder hierarchies and manage files within document libraries.
  name: Folders and Files
- description: Manage site, list, and item-level permissions with role assignments.
  name: Permissions and Security
- description: Full-text search across sites, documents, and content using the Search REST API.
  name: Search
- description: Access user profile properties, people search, and organizational data.
  name: User Profiles
- description: Manage content types, site columns, and metadata schemas.
  name: Content Types
- description: Subscribe to change notifications for lists and libraries via webhooks.
  name: Webhooks
- description: Access SharePoint data through Microsoft Graph API for unified Microsoft 365 integration.
  name: Microsoft Graph Integration
- description: Combine multiple REST operations into a single batch request.
  name: Batch Requests
- description: Filter, select, expand, and order data using OData query operators.
  name: OData Query Support
image: /assets/icons/sharepoint.png
integrations:
- description: Native integration with Teams, OneDrive, Outlook, and other Microsoft 365 apps.
  name: Microsoft 365
- description: Unified API access to SharePoint alongside all Microsoft 365 services.
  name: Microsoft Graph
- description: Power Apps, Power Automate, and Power BI integration for low-code solutions.
  name: Power Platform
- description: Azure AD for authentication, Azure Functions for serverless processing.
  name: Azure
- description: SharePoint powers file storage and document collaboration in Microsoft Teams.
  name: Teams
jsonld:
- class_count: 11
  name: Sharepoint Context
  property_count: 35
  slug: sharepoint-context
layout: provider
modified: '2026-04-17'
name: Microsoft SharePoint
rules:
- name: Microsoft SharePoint API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: sharepoint-spectral-rules
skills: []
slug: sharepoint
solutions:
- description: Cloud-hosted SharePoint as part of Microsoft 365 with REST and Graph APIs.
  name: SharePoint Online
- description: On-premises SharePoint with REST, CSOM, and server-side object model.
  name: SharePoint Server
- description: Modern client-side development framework for building web parts and extensions.
  name: SharePoint Framework (SPFx)
tags:
- Collaboration
- Document Management
- Enterprise Content Management
- Intranet
- Microsoft
url: https://raw.githubusercontent.com/api-evangelist/sharepoint/refs/heads/main/apis.yml
use_cases:
- description: Automate document upload, metadata tagging, and approval workflows.
  name: Document Automation
- description: Programmatically manage site pages, news posts, and navigation.
  name: Intranet Content Management
- description: Sync SharePoint list data with external databases and applications.
  name: Data Integration
- description: Migrate content between SharePoint sites or from file shares to SharePoint.
  name: Migration
- description: Build SPFx web parts and extensions with SharePoint Framework.
  name: Custom Applications
- description: Manage retention policies, sensitivity labels, and audit logs.
  name: Compliance and Governance
- description: Build custom search experiences with facets, refiners, and result types.
  name: Search Integration
- description: Trigger and manage automated workflows based on SharePoint events.
  name: Power Automate Flows
---
