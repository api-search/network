---
api_count: 27
apis:
- description: Send and read email, manage drafts and labels, and handle mailbox settings.
  name: Gmail API
  slug: gmail
- description: Store and synchronize files across devices, manage file metadata and permissions.
  name: Google Drive API
  slug: drive
- description: Create and manage calendars, events, and attendees.
  name: Google Calendar API
  slug: calendar
- description: Create and manage video conferencing meetings, spaces, recordings, and transcripts.
  name: Google Meet REST API
  slug: meet
- description: Create and edit documents programmatically.
  name: Google Docs API
  slug: docs
- description: Read and write data in Google Sheets.
  name: Google Sheets API
  slug: sheets
- description: Create and modify presentations.
  name: Google Slides API
  slug: slides
- description: Manage users, groups, organizational units, and devices in a Google Workspace domain.
  name: Admin SDK Directory API
  slug: admin-directory
- description: Build bots and integrations for Google Chat.
  name: Google Chat API
  slug: chat
- description: View audit and usage reports for a Google Workspace domain including user activity and admin actions.
  name: Admin SDK Reports API
  slug: admin-reports
- description: Create and modify forms and quizzes, retrieve form responses and quiz grades.
  name: Google Forms API
  slug: forms
- description: Search, read, and update Google Tasks content and metadata.
  name: Google Tasks API
  slug: tasks
- description: Manage Google Keep notes including creating, listing, and deleting notes and managing permissions.
  name: Google Keep API
  slug: keep
- description: Manage eDiscovery for your organization including matters, holds, and exports across Google Workspace services.
  name: Google Vault API
  slug: vault
- description: Manage classes, rosters, invitations, and coursework in Google Classroom.
  name: Google Classroom API
  slug: classroom
- description: Read and manage the authenticated user contacts and profiles, and search the directory.
  name: People API
  slug: people
- description: Index non-Google Workspace data and search across all organizational data sources.
  name: Google Cloud Search API
  slug: cloud-search
- description: Retrieve information about changes made to objects within a user Google Drive.
  name: Drive Activity API
  slug: drive-activity
- description: Create and manage labels to organize and classify files in Google Drive.
  name: Drive Labels API
  slug: drive-labels
- description: Manage alerts on issues affecting your Google Workspace domain including security and compliance warnings.
  name: Alert Center API
  slug: alert-center
- description: Update and retrieve settings for existing Google Groups including permissions and access controls.
  name: Groups Settings API
  slug: groups-settings
- description: Migrate shared emails from public folders and distribution lists to Google Groups discussion archives.
  name: Groups Migration API
  slug: groups-migration
- description: Transfer ownership of user data from one user to another within a domain.
  name: Admin SDK Data Transfer API
  slug: data-transfer
- description: Manage Google Workspace and related product licenses for all users of a customer.
  name: Enterprise License Manager API
  slug: license-manager
- description: Perform common reseller functions at scale including placing orders and managing customer subscriptions.
  name: Google Workspace Reseller API
  slug: reseller
- description: Gather statistics on bulk emails sent to Gmail users including spam reports and delivery errors.
  name: Gmail Postmaster Tools API
  slug: postmaster
- description: Manage customer and user license status for Google Workspace Marketplace applications.
  name: Google Workspace Marketplace API
  slug: marketplace
capabilities:
- description: Unified workflow for managing Google Workspace domain resources including users, groups, and organizational units. Used by IT administrators and workspace domain managers.
  name: Google Workspace Domain Administration
  slug: domain-administration
common:
- title: ''
  type: Console
  url: https://console.cloud.google.com
- title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- title: ''
  type: TermsOfService
  url: https://workspace.google.com/terms/service-terms/
- title: ''
  type: Support
  url: https://support.google.com/workspace
- title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- title: ''
  type: DeveloperPortal
  url: https://developers.google.com/workspace
- title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com
- title: ''
  type: ReleaseNotes
  url: https://developers.google.com/workspace/release-notes
- title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/guides/get-started
- title: ''
  type: SDK
  url: https://developers.google.com/workspace/guides/libraries
- title: Admin SDK Directory API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/admin-directory.yaml
- title: Domain Administration Workflow
  type: NaftikoCapability
  url: capabilities/domain-administration.yaml
created: '2024-01-01'
description: A collection of productivity and collaboration tools from Google including Gmail, Drive, Calendar, Meet, and more.
features:
- description: Send, receive, and manage email with Gmail API, build chat bots with Chat API, and host video meetings with Meet API.
  name: Email and Communication
- description: Create and edit documents, spreadsheets, presentations, and forms programmatically across Google Workspace apps.
  name: Document Collaboration
- description: Store, sync, and manage files with Drive API including permissions, metadata, labels, and activity tracking.
  name: File Storage and Management
- description: Manage users, groups, organizational units, and devices across a Google Workspace domain with Admin SDK.
  name: Directory and User Management
- description: Create and manage calendars, events, and attendees with automatic conflict detection and resource booking.
  name: Calendar and Scheduling
- description: Monitor security alerts, manage eDiscovery holds, and generate audit reports for compliance requirements.
  name: Security and Compliance
- description: Index and search across Google Workspace and external data sources with Cloud Search API.
  name: Enterprise Search
- description: Manage tasks and notes programmatically with Tasks API and Keep API for productivity workflows.
  name: Task and Note Management
image: https://workspace.google.com/static/img/logo.svg
integrations:
- description: Sync contacts, calendar events, and emails between Google Workspace and Salesforce CRM.
  name: Salesforce
- description: Bridge Google Workspace content and notifications with Slack channels for unified collaboration.
  name: Slack
- description: Interoperability support for document sharing and calendar synchronization with Microsoft Office apps.
  name: Microsoft 365
- description: Link Google Drive files, create documents from Jira issues, and sync calendar events with project timelines.
  name: Jira
- description: Connect Google Workspace apps with thousands of services through Zapier automation workflows.
  name: Zapier
- description: Integrate Google Drive attachments, Calendar events, and Gmail notifications with Asana project management.
  name: Asana
jsonld:
- class_count: 0
  name: Admin Sdk Directory Context
  property_count: 0
  slug: admin-sdk-directory-context
- class_count: 0
  name: Google Workspace Context
  property_count: 3
  slug: google-workspace-context
layout: provider
modified: '2026-04-18'
name: Google Workspace
rules:
- name: Google Workspace API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-workspace-spectral-rules
skills: []
slug: google-workspace
solutions: []
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
url: https://raw.githubusercontent.com/api-evangelist/google-workspace/refs/heads/main/apis.yml
use_cases:
- description: Provision user accounts, assign groups and licenses, and configure organizational units for new employee onboarding.
  name: Automated Onboarding
- description: Automate document creation, approval workflows, and distribution using Docs, Sheets, and Drive APIs.
  name: Document Workflow Automation
- description: Schedule meetings, manage recordings and transcripts, and integrate video conferencing into custom applications.
  name: Meeting Management
- description: Monitor security alerts, audit user activity, and enforce compliance policies across the Google Workspace domain.
  name: Security Monitoring
- description: Automate email campaigns, manage support inboxes, and integrate Gmail with CRM and helpdesk systems.
  name: Customer Communication
---
