---
api_count: 7
apis:
- description: The Jira Cloud platform REST API for building apps and integrations.
  name: Jira Cloud Platform REST API
  slug: ''
- description: Version 2 of the Jira Cloud platform REST API, offering the same operations as v3 but without Atlassian Document Format support.
  name: Jira Cloud Platform REST API v2
  slug: ''
- description: REST API for Jira Software features including boards, sprints, and backlogs.
  name: Jira Software Cloud REST API
  slug: ''
- description: REST API for Jira Service Management features including queues, customers, requests, and SLAs.
  name: Jira Service Management REST API
  slug: ''
- description: Operations APIs for Jira Service Management covering schedules, on-call rotations, alerts, escalations, and incident management.
  name: Jira Service Management Operations REST API
  slug: ''
- description: REST API for Jira Align enterprise agile planning platform, providing access to portfolios, epics, features, and program management data.
  name: Jira Align REST API
  slug: ''
- description: REST API for Atlassian Customer Service Management providing access to customers, organizations, products, and entitlements data.
  name: Jira Customer Service Management REST API
  slug: ''
asyncapis:
- description: Jira Cloud webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in your Jira instance. Webhooks can be registered via the Jira REST API or through the Jira administr
  name: Jira Cloud Webhooks
  slug: jira-webhooks-asyncapi
capabilities:
- description: Unified project management workflow combining issue tracking, workflow transitions, JQL search, and project management. Used by project managers, developers, and team leads to manage agile software de
  name: Jira Project Management
  slug: project-management
common:
- title: ''
  type: Portal
  url: https://developer.atlassian.com/cloud/jira/platform/
- title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
- title: ''
  type: SDK
  url: https://developer.atlassian.com/cloud/jira/platform/libraries/
- title: OAuth 2.0
  type: Authentication
  url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
- title: ''
  type: Support
  url: https://support.atlassian.com/
- title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/changelog/
- title: ''
  type: Blog
  url: https://www.atlassian.com/blog/developer
- title: ''
  type: Marketplace
  url: https://developer.atlassian.com/platform/marketplace/getting-started/
- title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- title: ''
  type: Security
  url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
- title: ''
  type: JSONSchema
  url: json-schema/jira-issue-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/jira-project-schema.json
- title: ''
  type: JSONLD
  url: json-ld/jira-context.jsonld
created: '2024'
description: APIs for Atlassian Jira project management and issue tracking platform.
features:
- description: Powerful Jira Query Language enabling complex issue searches with field-based filtering, functions, and operators.
  name: JQL Search
- description: Configurable workflow transitions with validators, conditions, and post-functions for automated issue lifecycle management.
  name: Workflow Automation
- description: Scrum and Kanban boards with sprint planning, backlog management, and velocity tracking for agile teams.
  name: Agile Boards
- description: SLA management with configurable goals, time tracking, and breach notifications for service management.
  name: Service Level Agreements
- description: Real-time event notifications for issue changes, sprint events, and board updates via configurable webhook endpoints.
  name: Webhooks
- description: Rich text document format supporting structured content in issue descriptions and comments via the v3 API.
  name: Atlassian Document Format
image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
integrations:
- description: Link Jira issues to Confluence pages for seamless knowledge management and documentation alongside project tracking.
  name: Confluence
- description: Connect code repositories to Jira issues for automated status updates, smart commits, and development tracking.
  name: Bitbucket
- description: Link GitHub pull requests, branches, and commits to Jira issues for end-to-end development visibility.
  name: GitHub
- description: Create and manage Jira issues from Slack channels with bi-directional notifications and status updates.
  name: Slack
- description: Receive Jira notifications and manage issues directly from Microsoft Teams conversations.
  name: Microsoft Teams
jsonld:
- class_count: 0
  name: Jira Cloud Platform Rest Context
  property_count: 0
  slug: jira-cloud-platform-rest-context
- class_count: 0
  name: Jira Context
  property_count: 15
  slug: jira-context
layout: provider
modified: '2026-04-18'
name: Jira
rules:
- name: Jira API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: jira-spectral-rules
skills: []
slug: jira
solutions: []
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
url: https://www.atlassian.com/software/jira
use_cases:
- description: Automate issue creation, assignment, and transitions based on external events from CI/CD pipelines, monitoring tools, or customer feedback systems.
  name: Issue Tracking Automation
- description: Programmatically manage sprints, backlogs, and board configurations for automated agile workflow orchestration.
  name: Sprint Management
- description: Integrate customer support channels with Jira Service Management for automated ticket creation and SLA tracking.
  name: Service Desk Integration
- description: Automate incident response workflows with on-call scheduling, alert routing, and escalation management.
  name: Incident Management
- description: Connect portfolio planning tools with Jira Align for cross-team dependency tracking and program-level reporting.
  name: Enterprise Agile Planning
---
