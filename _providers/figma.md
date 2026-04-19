---
api_count: 18
apis:
- description: 'Figma allows designers to create and prototype their digital experiences - together in real-time and in one place - helping them turn their ideas and visions into products, faster. Figma''s mission is '
  name: Figma API
  slug: figma-api
- description: The Figma REST API provides programmatic access to Figma files, comments, components, and related resources. It enables developers to read and interact with design data, export assets, manage comments
  name: Figma REST API
  slug: figma-rest-api
- description: Figma Files API provides access to design file data including document trees, nodes, images, version history, and file metadata. Read and export design data from Figma files programmatically.
  name: Figma Files API
  slug: figma-files-api
- description: Figma Images API provides endpoints for rendering and exporting images from Figma files in various formats including PNG, JPG, SVG, and PDF.
  name: Figma Images API
  slug: figma-images-api
- description: Figma Teams API provides endpoints for managing team-level resources including webhooks, projects, and team configuration.
  name: Figma Teams API
  slug: figma-teams-api
- description: Figma Projects API provides endpoints for listing team projects and retrieving project files.
  name: Figma Projects API
  slug: figma-projects-api
- description: Figma Me API provides the endpoint for retrieving information about the currently authenticated user.
  name: Figma Me API
  slug: figma-me-api
- description: Figma Components API provides access to published components, component sets, and styles from team libraries. Query component metadata, retrieve thumbnails, and access documentation links for reusable
  name: Figma Components API
  slug: figma-components-api
- description: Figma Component Sets API provides endpoints for retrieving published component set metadata from team libraries.
  name: Figma Component Sets API
  slug: figma-component-sets-api
- description: Figma Styles API provides endpoints for retrieving published style metadata including colors, text styles, and effects from team libraries.
  name: Figma Styles API
  slug: figma-styles-api
- description: Figma Activity Logs API provides endpoints for retrieving activity log events for an organization, enabling audit trail and compliance monitoring.
  name: Figma Activity Logs API
  slug: figma-activity-logs-api
- description: Figma Payments API provides endpoints for querying user payment information on plugins, widgets, and Community files.
  name: Figma Payments API
  slug: figma-payments-api
- description: Figma Dev Resources API provides endpoints for creating, updating, and deleting dev resources attached to design nodes, enabling design-to-code workflows.
  name: Figma Dev Resources API
  slug: figma-dev-resources-api
- description: Figma Analytics API provides endpoints for tracking component, style, and variable usage across team libraries, enabling design system adoption measurement.
  name: Figma Analytics API
  slug: figma-analytics-api
- description: Figma Commenting mode allows users to leave comments directly on layers or objects on the canvas. You can use the Figma API to post comments and reactions to a Figma file, view existing comments and r
  name: Figma Comments API
  slug: figma-comments-api
- description: Figma allows you to distinguish different stages or versions of a file as it evolves over time. The Version History API provides endpoints to view, track, and restore previous versions of a file, reco
  name: Figma Version History API
  slug: figma-version-history-api
- description: The Variables REST API includes endpoints for querying, creating, updating, and deleting variables. Variables store reusable values that can be applied to design properties and prototyping actions. To
  name: Figma Variables API
  slug: figma-variables-api
- description: The Library Analytics REST API provides six methods for tracking component, style, and variable usage. Each resource type has an actions endpoint and a usages endpoint, allowing you to get time series
  name: Figma Library Analytics API
  slug: figma-library-analytics-api
asyncapis:
- description: Figma Webhooks allow applications to receive real-time notifications when events occur in Figma files and projects. Webhooks are configured at the team level and send HTTP POST requests with JSON payl
  name: Figma Webhooks
  slug: figma-webhooks-asyncapi
capabilities:
- description: Unified workflow for managing design files, components, styles, projects, comments, and asset export. Combines the Figma REST API endpoints into a cohesive design system management experience. Used by
  name: Figma Design System Management
  slug: design-system-management
common:
- title: ''
  type: Portal
  url: https://www.figma.com/developers
- title: ''
  type: Authentication
  url: https://developers.figma.com/docs/rest-api/authentication/
- title: ''
  type: ChangeLog
  url: https://developers.figma.com/docs/rest-api/changelog/
- title: ''
  type: RateLimits
  url: https://developers.figma.com/docs/rest-api/rate-limits/
- title: Figma REST API OpenAPI Specification
  type: OpenAPI
  url: https://github.com/figma/rest-api-spec
- title: ''
  type: GettingStarted
  url: https://developers.figma.com/docs/code-connect/quickstart-guide/
- title: ''
  type: SignUp
  url: https://www.figma.com/signup?cont=/developers/embed
- title: ''
  type: Login
  url: https://www.figma.com/login?cont=/developers/embed
- title: ''
  type: Pricing
  url: https://www.figma.com/pricing/
- title: ''
  type: Blog
  url: https://www.figma.com/blog/
- title: ''
  type: Security
  url: https://www.figma.com/security/
- title: ''
  type: StatusPage
  url: https://status.figma.com/
- title: ''
  type: TermsOfService
  url: https://www.figma.com/legal/tos/
- title: ''
  type: PrivacyPolicy
  url: https://www.figma.com/legal/privacy/
- title: ''
  type: Partners
  url: https://www.figma.com/partners/
- title: ''
  type: Events
  url: https://www.figma.com/events/
- title: ''
  type: Support
  url: https://help.figma.com/hc/en-us/
- title: ''
  type: Contact
  url: https://www.figma.com/contact/
- title: Forum
  type: Support
  url: https://forum.figma.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/figma
- title: REST API OpenAPI Specification
  type: GitHubRepository
  url: https://github.com/figma/rest-api-spec
- title: Code Connect
  type: GitHubRepository
  url: https://github.com/figma/code-connect
- title: Plugin API Typings
  type: GitHubRepository
  url: https://github.com/figma/plugin-typings
- title: Community Resources
  type: GitHubRepository
  url: https://github.com/figma/community-resources
- title: MCP Server Guide
  type: GitHubRepository
  url: https://github.com/figma/mcp-server-guide
- title: ''
  type: SpectralRules
  url: rules/figma-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/figma-vocabulary.yaml
- title: REST API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/rest-api.yaml
- title: Design System Management Workflow
  type: NaftikoCapability
  url: capabilities/design-system-management.yaml
created: '2023-11-22'
description: Figma is a collaborative interface design tool with a comprehensive REST API for accessing and manipulating design files, projects, and teams.
features:
- description: Multiple designers and stakeholders can work on the same file simultaneously with live cursors and instant updates.
  name: Real-Time Collaboration
- description: Create and maintain component libraries, styles, and variables that teams can share and reuse across projects.
  name: Design Systems
- description: Build interactive prototypes with transitions, animations, and smart animate to demonstrate user flows.
  name: Prototyping
- description: Developers can inspect designs, copy CSS/code snippets, and access design tokens directly from Figma files.
  name: Dev Mode
- description: Receive real-time notifications when files are updated, comments are added, or library components are published.
  name: Webhooks
- description: Export design assets in PNG, JPG, SVG, and PDF formats at multiple scales via the API.
  name: Asset Export
- description: Define and manage design tokens as variables that can be applied across components and exported for development.
  name: Variables and Design Tokens
- description: Enterprise organizations can track and audit user activity across files, projects, and teams.
  name: Activity Logging
- description: Track component, style, and variable adoption across teams to measure design system usage.
  name: Library Analytics
image: https://www.figma.com/favicon.ico
integrations:
- description: Receive Figma file update notifications and preview designs directly in Slack channels.
  name: Slack
- description: Embed Figma designs in Jira issues and link design tasks to development tickets.
  name: Jira
- description: Link Figma designs to pull requests and track design-to-code implementation.
  name: GitHub
- description: Connect Figma components to Storybook stories using Code Connect for design-code parity.
  name: Storybook
- description: Export designs from Figma to Zeplin for detailed developer handoff and style guides.
  name: Zeplin
- description: Version control and branching for Figma design files with Abstract integration.
  name: Abstract
- description: Share and preview Figma designs within Microsoft Teams conversations and channels.
  name: Microsoft Teams
jsonld:
- class_count: 0
  name: Figma Activity Logs Context
  property_count: 0
  slug: figma-activity-logs-context
- class_count: 0
  name: Figma Analytics Context
  property_count: 0
  slug: figma-analytics-context
- class_count: 0
  name: Figma Component Sets Context
  property_count: 0
  slug: figma-component-sets-context
- class_count: 0
  name: Figma Context
  property_count: 0
  slug: figma-context
- class_count: 0
  name: Figma Dev Resources Context
  property_count: 0
  slug: figma-dev-resources-context
- class_count: 0
  name: Figma Files Context
  property_count: 0
  slug: figma-files-context
- class_count: 0
  name: Figma Images Context
  property_count: 0
  slug: figma-images-context
- class_count: 0
  name: Figma Me Context
  property_count: 0
  slug: figma-me-context
- class_count: 0
  name: Figma Payments Context
  property_count: 0
  slug: figma-payments-context
- class_count: 0
  name: Figma Projects Context
  property_count: 0
  slug: figma-projects-context
- class_count: 0
  name: Figma Rest Context
  property_count: 0
  slug: figma-rest-context
- class_count: 0
  name: Figma Styles Context
  property_count: 0
  slug: figma-styles-context
- class_count: 0
  name: Figma Teams Context
  property_count: 0
  slug: figma-teams-context
layout: provider
modified: '2026-04-18'
name: Figma
rules:
- name: Figma API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: figma-spectral-rules
skills: []
slug: figma
solutions: []
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/apis.yml
use_cases:
- description: Build, publish, and track adoption of shared component libraries across product teams.
  name: Design System Management
- description: Programmatically export design assets for build pipelines and content delivery workflows.
  name: Automated Asset Export
- description: Attach code references to design nodes using dev resources for seamless developer handoff.
  name: Design-to-Code Handoff
- description: Extend Figma with custom plugins and widgets using the Plugin API and Widget API.
  name: Plugin and Widget Development
- description: Monitor organization activity logs for security compliance and access auditing.
  name: Compliance and Audit
- description: Programmatically back up file data and version history for disaster recovery.
  name: Design File Backup
---
