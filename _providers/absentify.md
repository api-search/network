---
api_count: 1
apis:
- description: 'REST API for managing employee absences, leave requests, members, departments, leave types, public holidays, and workspace settings. Requires an API key (x-api-key header) available on the Plus plan. '
  name: Absentify API
  slug: absentify
capabilities:
- description: ''
  name: Absence Management Absentify
  slug: absence-management-absentify
common:
- title: ''
  type: Portal
  url: https://absentify.com/
- title: ''
  type: Documentation
  url: https://absentify.com/docs/en/
- title: ''
  type: Pricing
  url: https://absentify.com/pricing
- title: ''
  type: PrivacyPolicy
  url: https://absentify.com/privacy-policy
- title: ''
  type: TermsOfService
  url: https://absentify.com/terms-and-conditions
- title: ''
  type: Blog
  url: https://absentify.com/blog
- title: ''
  type: StatusPage
  url: https://status.absentify.com
- title: ''
  type: Security
  url: https://absentify.com/security
- title: MCP Server
  type: Tools
  url: https://absentify.com/docs/en/mcp-server
- title: ''
  type: SpectralRules
  url: rules/absentify-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/absence-management-absentify.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/absentify-vocabulary.yaml
created: '2025-02-17'
description: Absentify is an absence management platform integrated with Microsoft 365 and Microsoft Teams that helps businesses track and manage employee absences, leave requests, approvals, and team schedules. Built by BrainCore Solutions GmbH, it provides a REST API for integrating absence management into custom workflows, HR systems, and business automation tools.
features:
- description: Track and manage employee absences, time off, and leave requests across the organization.
  name: Absence Tracking
- description: Submit, approve, decline, and cancel leave requests with multi-level approval workflows.
  name: Leave Request Management
- description: Native integration with Microsoft 365 and Microsoft Teams for seamless absence management in existing workflows.
  name: Microsoft 365 Integration
- description: Organize employees into departments with custom leave type entitlements and approval chains.
  name: Department Management
- description: Define custom leave types with color coding, limits, approval requirements, and accrual policies.
  name: Leave Type Configuration
- description: Manage public holiday calendars per region and apply them to members and departments.
  name: Public Holiday Calendars
- description: Receive real-time webhook notifications for request creation and status changes.
  name: Webhook Support
- description: Configure workspace-wide settings, fiscal year, and default approval workflows.
  name: Workspace Management
- description: Query absences broken down by individual day for reporting and payroll integration.
  name: Absence Per Day Reporting
image: /assets/icons/absentify.png
integrations:
- description: Native Microsoft Teams app for submitting and approving absence requests without leaving Teams.
  name: Microsoft Teams
- description: Deep integration with Microsoft 365 calendar, Active Directory, and identity management.
  name: Microsoft 365
- description: Connect absentify to thousands of apps via Zapier automation workflows.
  name: Zapier
- description: Automate absence management workflows using Make's visual automation platform.
  name: Make (Integromat)
- description: Send real-time absence event notifications to any system via configurable webhooks.
  name: Custom Webhooks
jsonld:
- class_count: 9
  name: Absentify Context
  property_count: 36
  slug: absentify-context
layout: provider
modified: '2026-04-19'
name: Absentify
rules:
- name: Absentify API Rules
  rule_count: 15
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 9
  slug: absentify-spectral-rules
skills: []
slug: absentify
solutions: []
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/apis.yml
use_cases:
- description: Integrate absence data into HRIS platforms like SAP, Workday, or BambooHR for unified people management.
  name: HR System Integration
- description: Export absence data to payroll systems to automatically calculate pay adjustments for time off.
  name: Payroll Processing
- description: Sync absence data into scheduling tools to prevent understaffing and manage coverage.
  name: Team Scheduling
- description: Generate absence reports for regulatory compliance, labor law adherence, and audit purposes.
  name: Compliance Reporting
- description: Build custom absence request approval workflows integrated with business process automation tools.
  name: Custom Approval Workflows
- description: Analyze absence trends, patterns, and costs to improve workforce planning and reduce absenteeism.
  name: Absence Analytics
- description: Automate absence-related notifications and approvals directly within Microsoft Teams channels.
  name: Microsoft Teams Automation
---
