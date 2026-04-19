---
api_count: 5
apis:
- description: API for integrating Microsoft Copilot capabilities into applications.
  name: Microsoft Copilot API
  slug: ''
- description: Microsoft Graph API endpoints for accessing Copilot features within Microsoft 365, including the Copilot namespace with retrieval, chat, search, and meeting insights capabilities.
  name: Microsoft Graph API (Copilot Integration)
  slug: ''
- description: REST APIs under the Microsoft Graph /copilot/ namespace that enable secure access to Microsoft 365 Copilot capabilities including retrieval, chat, and search, for use in custom applications and agents
  name: Microsoft 365 Copilot APIs
  slug: ''
- description: API for building custom connectors that bring external data into Microsoft Graph to enhance Microsoft 365 Copilot experiences including search and retrieval augmented generation.
  name: Microsoft 365 Copilot Connectors API
  slug: ''
- description: APIs for building, publishing, and integrating custom agents and copilots using Microsoft Copilot Studio, including Direct Line API for connecting web and custom applications.
  name: Microsoft Copilot Studio API
  slug: ''
common:
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/copilot/get-started
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-copilot/pricing
- title: ''
  type: Support
  url: https://support.microsoft.com/copilot
- title: ''
  type: Blog
  url: https://blogs.microsoft.com/blog/tag/copilot/
- title: ''
  type: StatusPage
  url: https://status.microsoft.com
- title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365/copilot
- title: ''
  type: SDK
  url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/sdks/api-libraries
- title: ''
  type: CodeExamples
  url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/samples
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/whats-new
- title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/CopilotStudioSamples
created: '2024-01-15'
description: Microsoft Copilot is an AI-powered assistant that helps users with productivity tasks, content generation, and information retrieval across Microsoft 365 applications and services.
features:
- description: Retrieve relevant enterprise content from Microsoft 365 using AI-powered retrieval augmented generation with permissions and sensitivity label awareness.
  name: Retrieval API
- description: Perform semantic search across Microsoft 365 content including SharePoint, OneDrive, and Exchange with AI-enhanced ranking.
  name: Search API
- description: Programmatically start and continue conversations with Microsoft 365 Copilot grounded in enterprise and web search data.
  name: Chat API
- description: Export and audit Copilot interaction history across the organization for compliance and governance purposes.
  name: Interaction Export
- description: Subscribe to real-time notifications for Copilot interactions and events across Microsoft 365.
  name: Change Notifications
- description: Low-code platform for building custom agents, copilots, and conversational AI experiences.
  name: Copilot Studio
- description: Bring external data into Microsoft Graph to enhance Copilot search and retrieval capabilities.
  name: Connectors
- description: Extend Copilot with custom plugins, agents, and API integrations using declarative or code-first approaches.
  name: Extensibility
image: https://www.microsoft.com/en-us/microsoft-copilot/assets/images/copilot-icon.png
integrations:
- description: Deep integration with Word, Excel, PowerPoint, Outlook, Teams, and other Microsoft 365 applications.
  name: Microsoft 365
- description: Access organizational data through the Microsoft Graph API for retrieval, search, and chat capabilities.
  name: Microsoft Graph
- description: Enterprise authentication and authorization using Azure AD with OAuth 2.0 and OIDC.
  name: Azure Active Directory
- description: Connect Copilot with Power Automate, Power Apps, and Power BI for end-to-end workflow automation.
  name: Power Platform
jsonld:
- class_count: 0
  name: Microsoft Copilot Context
  property_count: 0
  slug: microsoft-copilot-context
layout: provider
modified: '2026-04-18'
name: Microsoft Copilot
rules:
- name: Microsoft Copilot API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: microsoft-copilot-spectral-rules
skills: []
slug: microsoft-copilot
solutions: []
tags:
- Agents
- AI Assistant
- Artificial Intelligence
- Chatbot
- Copilot
- Extensibility
- Generative AI
- Microsoft 365
- Productivity
url: https://copilot.microsoft.com
use_cases:
- description: Build applications that retrieve relevant enterprise content from Microsoft 365 while respecting permissions and compliance controls.
  name: Enterprise Knowledge Retrieval
- description: Integrate Copilot capabilities into line-of-business applications for document summarization, drafting, and data analysis.
  name: AI-Assisted Productivity
- description: Create domain-specific AI agents using Copilot Studio that automate workflows and answer questions from custom data sources.
  name: Custom Agent Development
- description: Monitor and audit Copilot usage across the organization with interaction history export and change notifications.
  name: Compliance and Governance
---
