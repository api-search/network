---
api_count: 6
apis:
- description: The Airtable API can be used to integrate your data in Airtable with any external system. The API closely follows REST semantics, uses JSON to encode objects, and relies on standard HTTP codes to sign
  name: Airtable API
  slug: airtable-api
- description: The Airtable Metadata API provides access to base and schema management operations. You can list bases, retrieve base schemas with table and field definitions, create new bases, tables, and fields, an
  name: Airtable Metadata API
  slug: airtable-metadata-api
- description: The Airtable Enterprise API allows enterprise teams to manage their account programmatically outside of the Admin panel. It supports managing users, updating access permissions, and managing bases, ta
  name: Airtable Enterprise API
  slug: airtable-enterprise-api
- description: The Airtable SCIM API supports the System for Cross-domain Identity Management specification for automated user and group provisioning. It enables identity providers like Okta and Microsoft Entra ID t
  name: Airtable SCIM API
  slug: airtable-scim-api
- description: The Airtable Audit Logs API provides programmatic access to enterprise audit logs for compliance monitoring and security tracking. It supports creating and retrieving audit log requests with event fil
  name: Airtable Audit Logs API
  slug: airtable-audit-logs-api
- description: The Airtable Shares API allows enterprise administrators to list, manage, and delete share links across an organization. It provides programmatic control over base sharing and access management.
  name: Airtable Shares API
  slug: airtable-shares-api
capabilities:
- description: Unified workflow for managing Airtable databases — reading and writing records, browsing base schemas, managing webhooks, and administering tables. Used by developers and data teams integrating Airtab
  name: Airtable Database Management
  slug: database-management
common:
- title: ''
  type: Portal
  url: https://airtable.com/developers
- title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/introduction
- title: ''
  type: GettingStarted
  url: https://www.airtable.com/guides/scale/using-airtable-api
- title: ''
  type: Authentication
  url: https://airtable.com/developers/web/api/oauth-reference
- title: ''
  type: Authentication
  url: https://airtable.com/developers/web/api/scopes
- title: ''
  type: Authentication
  url: https://support.airtable.com/docs/creating-personal-access-tokens
- title: ''
  type: Errors
  url: https://airtable.com/developers/web/api/errors
- title: ''
  type: RateLimits
  url: https://airtable.com/developers/web/api/rate-limits
- title: ''
  type: RateLimits
  url: https://support.airtable.com/docs/managing-api-call-limits-in-airtable
- title: ''
  type: ChangeLog
  url: https://airtable.com/developers/web/api/changelog
- title: ''
  type: Policies
  url: https://support.airtable.com/docs/airtable-api-deprecation-guidelines
- title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/cursor-pagination
- title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/field-model
- title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/change-events
- title: ''
  type: Blog
  url: https://blog.airtable.com
- title: ''
  type: StatusPage
  url: https://status.airtable.com
- title: ''
  type: Support
  url: https://support.airtable.com
- title: ''
  type: TermsOfService
  url: https://airtable.com/tos
- title: ''
  type: PrivacyPolicy
  url: https://airtable.com/privacy
- title: ''
  type: Pricing
  url: https://airtable.com/pricing
- title: ''
  type: GitHubOrganization
  url: https://github.com/airtable
- title: ''
  type: Community
  url: https://community.airtable.com
- title: ''
  type: Forum
  url: https://community.airtable.com/c/developers/55
- title: ''
  type: Portal
  url: https://www.airtable.com
- title: ''
  type: Portal
  url: https://airtable.com/login
- title: ''
  type: SignUp
  url: https://airtable.com/signup
- title: ''
  type: Newsletter
  url: http://eepurl.com/gVD-df
- title: ''
  type: Documentation
  url: https://airtable.com/developers/extensions
- title: ''
  type: Documentation
  url: https://airtable.com/developers/scripting/api
- title: ''
  type: Documentation
  url: https://support.airtable.com/docs/airtable-enterprise-api
- title: ''
  type: AsyncAPI
  url: https://support.airtable.com/docs/airtable-webhooks-api-overview
- title: ''
  type: Documentation
  url: https://airtable.com/developers/web/guides/webhooks-api
- title: ''
  type: Documentation
  url: https://support.airtable.com/docs/airtable-resources-for-developers
- title: ''
  type: ChangeLog
  url: https://www.airtable.com/whatsnew
- title: ''
  type: Twitter
  url: https://x.com/airtable
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airtable
- title: ''
  type: YouTube
  url: https://www.youtube.com/@AirtableApp
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/airtable
- title: ''
  type: SDK
  url: https://github.com/Airtable/airtable.js
- title: ''
  type: SDK
  url: https://www.npmjs.com/package/airtable
- title: Airtable Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/rules/airtable-spectral-rules.yml
- title: Database Management
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/capabilities/database-management.yaml
- title: Airtable Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/vocabulary/airtable-vocabulary.yaml
created: '2023-11-21T00:00:00.000Z'
description: Airtable is a cloud-based collaboration service that combines the simplicity of a spreadsheet with the complexity of a database. It provides APIs for managing bases, tables, records, and more.
features:
- description: Spreadsheet-database hybrid for non-technical users to build databases without code.
  name: No-Code Database
- description: Full REST API for creating, reading, updating, and deleting records programmatically.
  name: REST API
- description: Real-time event notifications when records change.
  name: Webhooks
- description: Secure OAuth 2.0 integration for third-party apps.
  name: OAuth 2.0
- description: Enterprise user provisioning via SCIM for Okta, Entra ID, and other IdPs.
  name: SCIM Provisioning
- description: Enterprise audit logs for compliance and security monitoring.
  name: Audit Logs
- description: Custom UI extensions and scripting for advanced functionality.
  name: Extensions
- description: Built-in workflow automation with triggers and actions.
  name: Automations
image: https://www.airtable.com/images/logo.png
integrations:
- description: Connect Airtable to 5000+ apps via Zapier automations.
  name: Zapier
- description: Visual automation builder for complex Airtable workflows.
  name: Make (Integromat)
- description: Send Airtable notifications and updates to Slack channels.
  name: Slack
- description: Sync Airtable data with Salesforce CRM.
  name: Salesforce
- description: Link Airtable records to GitHub issues and pull requests.
  name: GitHub
- description: Enterprise SSO and SCIM provisioning via Okta.
  name: Okta
- description: Import from Google Sheets and sync with Google Drive.
  name: Google Workspace
jsonld:
- class_count: 1
  name: Airtable Context
  property_count: 14
  slug: airtable-context
layout: provider
modified: '2026-04-19'
name: Airtable
rules:
- name: Airtable API Rules
  rule_count: 29
  severity_counts:
    error: 9
    hint: 0
    info: 11
    warn: 9
  slug: airtable-spectral-rules
skills: []
slug: airtable
solutions: []
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/apis.yml
use_cases:
- description: Track tasks, milestones, and team assignments in structured databases.
  name: Project Management
- description: Build custom CRM systems for tracking contacts, deals, and pipelines.
  name: CRM
- description: Manage editorial calendars, content assets, and publishing workflows.
  name: Content Management
- description: Track inventory, orders, and supply chain data.
  name: Inventory Management
- description: Coordinate event logistics, attendees, and schedules.
  name: Event Planning
- description: Manage job applicants, employee records, and onboarding processes.
  name: HR & Recruiting
---
