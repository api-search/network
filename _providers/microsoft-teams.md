---
api_count: 4
apis:
- description: Core REST API for accessing Teams data including teams, channels, messages, tabs, apps, members, online meetings, and calls through Microsoft Graph.
  name: Microsoft Graph Teams API
  slug: ''
- description: API for building conversational bots that interact with users in Microsoft Teams through the Bot Framework.
  name: Microsoft Teams Bot Framework API
  slug: ''
- description: APIs for creating incoming webhooks and Office 365 connectors to post messages and notifications to Teams channels.
  name: Microsoft Teams Webhook and Connector API
  slug: ''
- description: APIs for building calling and meeting experiences in Teams including VoIP calls, group calls, IVR flows, and online meetings.
  name: Microsoft Teams Real-Time Communication APIs
  slug: ''
capabilities:
- description: Workflow capability for team collaboration including managing teams, channels, messaging, members, meetings, and calls. Used by IT administrators, team leads, and developers building Teams integration
  name: Microsoft Teams Collaboration
  slug: team-collaboration
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-teams
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/microsoftteams/platform/get-started/get-started-overview
- title: Teams Toolkit
  type: SDK
  url: https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-teams-blog/bg-p/MicrosoftTeamsBlog
- title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/products/office-teams
- title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev/Microsoft-Teams-Samples
- title: ''
  type: StatusPage
  url: https://status.teams.microsoft.com/
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: SpectralRules
  url: rules/microsoft-teams-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/team-collaboration.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-teams-vocabulary.yaml
created: '2024'
description: Microsoft Teams is a collaboration platform that combines workplace chat, meetings, file storage, and application integration. It provides APIs for building custom integrations, managing teams and channels, sending messages, scheduling meetings, and initiating calls through Microsoft Graph.
features:
- description: Create, archive, and delete teams programmatically.
  name: Team Lifecycle Management
- description: Create and manage standard, private, and shared channels.
  name: Channel Management
- description: Send and receive chat messages in channels and chats.
  name: Messaging
- description: Add, remove, and update team members and roles.
  name: Member Management
- description: Create and manage online meetings with join URLs.
  name: Online Meetings
- description: Initiate calls, answer, reject, transfer, and manage IVR flows.
  name: Calling
- description: Install and manage apps in teams and channels.
  name: App Installation
- description: Send activity feed notifications to engage users.
  name: Activity Feed Notifications
image: https://learn.microsoft.com/en-us/graph/images/teams-logo.png
integrations:
- description: Automate Teams workflows with Power Automate connectors.
  name: Microsoft Power Automate
- description: Teams channels with SharePoint document libraries.
  name: SharePoint
- description: Share and collaborate on files in Teams via OneDrive.
  name: OneDrive
- description: Build and deploy bots using Azure Bot Service.
  name: Azure Bot Service
- description: Rich interactive cards for messaging and notifications.
  name: Adaptive Cards
jsonld:
- class_count: 9
  name: Microsoft Teams Graph Api Context
  property_count: 22
  slug: microsoft-teams-graph-api-context
layout: provider
modified: '2026-04-18'
name: Microsoft Teams
rules:
- name: Microsoft Teams API Rules
  rule_count: 23
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 6
  slug: microsoft-teams-spectral-rules
skills: []
slug: microsoft-teams
solutions: []
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
url: https://raw.githubusercontent.com/api-evangelist/microsoft-teams/refs/heads/main/apis.yml
use_cases:
- description: Automate creation and configuration of teams for projects.
  name: Team Provisioning
- description: Send automated notifications and updates to channels.
  name: Messaging Automation
- description: Programmatically create and manage online meetings.
  name: Meeting Scheduling
- description: Build conversational bots for customer support in Teams.
  name: Customer Service Bots
- description: Manage shifts and schedules for frontline workers.
  name: Workforce Management
---
