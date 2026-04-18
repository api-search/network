---
api_count: 6
apis:
- description: RESTful API for accessing and managing tasks, plans, and buckets in Microsoft Planner through Microsoft Graph.
  name: Microsoft Planner API
  slug: ''
- description: API for creating, reading, updating, and deleting plans in Microsoft Planner through Microsoft Graph. Plans are the containers for tasks and are owned by groups or other containers.
  name: Microsoft Graph Plans API
  slug: ''
- description: API for creating, reading, updating, and deleting tasks in Microsoft Planner through Microsoft Graph. Tasks are contained in plans and can be assigned to buckets and users.
  name: Microsoft Graph Tasks API
  slug: ''
- description: API for creating, reading, updating, and deleting buckets in Microsoft Planner through Microsoft Graph. Buckets represent custom columns for organizing tasks within a plan.
  name: Microsoft Graph Buckets API
  slug: ''
- description: Beta version of the Planner API in Microsoft Graph providing access to preview features including plannerRoster resources, business scenarios integration, and expanded container type support.
  name: Microsoft Graph Planner API (Beta)
  slug: ''
- description: Beta API for integrating external business processes with Microsoft Planner through business scenarios, allowing creation of scenario-controlled Planner tasks and plans.
  name: Microsoft Graph Business Scenarios Planner API (Beta)
  slug: ''
capabilities:
- description: Manage plans, tasks, and buckets in Microsoft Planner for team collaboration and project management. Used by project managers and team leads.
  name: Microsoft Planner Task Management
  slug: task-management
common:
- title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- title: ''
  type: TermsOfService
  url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
- title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/graph/blogs/
- title: ''
  type: StatusPage
  url: https://developer.microsoft.com/en-us/graph/status
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
- title: ''
  type: Login
  url: https://planner.cloud.microsoft
- title: ''
  type: Support
  url: https://support.microsoft.com/en-us/planner
- title: ''
  type: FAQ
  url: https://support.microsoft.com/en-us/office/frequently-asked-questions-about-microsoft-planner-d1a2d4e6-a4d7-408c-a48a-31caaa267de5
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- title: ''
  type: SDK
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- title: ''
  type: SignUp
  url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
- title: ''
  type: Sandbox
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- title: ''
  type: OpenAPI
  url: openapi/microsoft-planner-openapi.yml
- title: ''
  type: JSONSchema
  url: json-schema/microsoft-planner-task-schema.json
- title: ''
  type: JSONLD
  url: json-ld/microsoft-planner-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/microsoft-planner-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-planner-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/task-management.yaml
created: '2024-01-01'
description: Microsoft Planner is a task management tool that helps teams organize work, assign tasks, share files, and collaborate on projects within Microsoft 365.
features:
- Visual task boards with drag-and-drop organization
- Plan creation tied to Microsoft 365 Groups
- Task assignment with due dates and priorities
- Bucket-based task categorization and organization
- Checklist subtasks within individual tasks
- File attachment and external reference linking
- Progress tracking with charts and status views
- Microsoft Teams integration for collaborative planning
- Category labels for cross-cutting task classification
- Microsoft Graph API for programmatic access
image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
integrations:
- Microsoft Teams for in-chat task management
- Microsoft To Do for personal task sync
- Power Automate for workflow automation
- SharePoint for document-linked tasks
- Outlook for email-to-task conversion
- Excel for data export and reporting
- Power BI for advanced analytics dashboards
- Azure DevOps for development task bridging
jsonld:
- class_count: 0
  name: Microsoft Planner Context
  property_count: 0
  slug: microsoft-planner-context
layout: provider
modified: '2026-04-18'
name: Microsoft Planner
rules:
- name: Microsoft Planner API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: microsoft-planner-spectral-rules
skills: []
slug: microsoft-planner
solutions: []
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
url: https://raw.githubusercontent.com/api-evangelist/microsoft-planner/refs/heads/main/apis.yml
use_cases:
- Project management for team-based work coordination
- Sprint planning and agile task tracking
- Onboarding workflows for new employees
- Event planning with task delegation and deadlines
- Content publishing calendars and editorial workflows
- IT helpdesk ticket organization and tracking
- Marketing campaign task management
- Cross-functional team collaboration on initiatives
---
