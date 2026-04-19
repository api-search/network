---
api_count: 9
apis:
- description: The Acronis Account Management API allows organizations to manage and automate user accounts within the Acronis platform, including creating, updating, and deleting users, and assigning roles and perm
  name: Acronis Account Management API
  slug: account-management-api
- description: The Acronis Agent Management REST API allows users to remotely manage and monitor Acronis agents from a centralized location, including creating, updating, and deleting agent profiles.
  name: Acronis Agent Management REST API
  slug: agent-management-rest-api
- description: Acronis Resource and Policy Management API enables organizations to efficiently manage resources and policies within their IT infrastructure.
  name: Acronis Resource and Policy Management API
  slug: resource-and-policy-management-api
- description: Acronis Task Manager API allows users to manage tasks and processes within the Acronis backup platform, including creating, editing, and monitoring tasks.
  name: Acronis Task Manager API
  slug: task-manager-api
- description: The Acronis Advanced Automation API allows users to automate and streamline their backup and recovery processes with custom scripts and workflows.
  name: Acronis Advanced Automation API
  slug: advanced-automation-api
- description: The Acronis Event Manager API allows users to monitor and manage events across their entire Acronis ecosystem with real-time access to event data.
  name: Acronis Event Manager API
  slug: event-manager-api
- description: The Acronis Disaster Recovery Service API allows organizations to automate and streamline their disaster recovery processes.
  name: Acronis Disaster Recovery Service API
  slug: disaster-recovery-service-api
- description: The Acronis Endpoint Detection and Response API is a comprehensive security solution that helps organizations detect and respond to cybersecurity threats in real-time.
  name: Acronis Endpoint Detection and Response API
  slug: endpoint-detection-and-response-api
- description: The Acronis Vault Manager REST API allows users to manage and interact with their Acronis Vault storage solutions programmatically.
  name: Acronis Vault Manager REST API
  slug: vault-manager-rest-api
capabilities:
- description: 'Unified workflow for managing Acronis Cyber Protect Cloud operations including tenant administration, agent monitoring, backup task tracking, and usage reporting. Used by MSPs, IT administrators, and '
  name: Acronis Cyber Protection Operations
  slug: cyber-protection-operations
common:
- title: ''
  type: Portal
  url: https://developer.acronis.com/
- title: ''
  type: GettingStarted
  url: https://developer.acronis.com/doc/outbound/apis/getting-started/index.html
- title: ''
  type: Authentication
  url: https://developer.acronis.com/doc/outbound/apis/authentication/index.html
- title: ''
  type: Blog
  url: https://www.acronis.com/en-us/blog/
- title: ''
  type: Support
  url: https://www.acronis.com/en-us/support/
- title: ''
  type: Pricing
  url: https://www.acronis.com/en-us/products/cloud/cyber-protect/pricing/
- title: ''
  type: Partners
  url: https://www.acronis.com/en-us/partners/
- title: ''
  type: CaseStudies
  url: https://www.acronis.com/en-us/resource-center/category/case-studies/
- title: ''
  type: GitHubOrganization
  url: https://github.com/acronis
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/capabilities/cyber-protection-operations.yaml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/vocabulary/acronis-vocabulary.yaml
- title: ''
  type: TermsOfService
  url: https://www.acronis.com/en-us/legal/
- title: ''
  type: ChangeLog
  url: https://developer.acronis.com/doc/outbound/apis/index.html
created: '2025-02-17'
description: Acronis is a leading provider of cyber protection solutions that deliver innovative technology to protect data, applications, and systems from the ever-evolving threats of today's digital world. They offer a comprehensive suite of products, including backup and disaster recovery solutions, file sync and share services, and anti-malware protection.
features:
- description: Multi-tier tenant management for MSPs, partners, and customers with offering item quotas.
  name: Tenant Hierarchy Management
- description: Remote management of Acronis backup agents across Windows, Linux, macOS, and cloud workloads.
  name: Agent Management
- description: Real-time monitoring of backup and protection tasks with state, result, and activity tracking.
  name: Backup Task Monitoring
- description: Automated usage metrics collection and report generation for billing and capacity planning.
  name: Usage Reporting
- description: Programmatic creation and application of protection policies to resources.
  name: Policy Management
- description: Automated failover and recovery orchestration for business continuity.
  name: Disaster Recovery API
- description: EDR capabilities for threat detection, investigation, and response via API.
  name: Endpoint Detection and Response
image: /assets/icons/acronis.png
integrations:
- description: Integration with ConnectWise, Autotask, and other PSA platforms for MSP billing and ticketing.
  name: PSA Platforms
- description: Event streaming to SIEM platforms via Event Manager API for security monitoring.
  name: SIEM Systems
- description: Integration with RMM platforms for agent deployment and backup policy management.
  name: RMM Tools
- description: Usage data export for automated billing via usage and offering item APIs.
  name: Billing Systems
jsonld:
- class_count: 18
  name: Acronis Context
  property_count: 61
  slug: acronis-context
layout: provider
modified: '2026-04-19'
name: Acronis
rules:
- name: Acronis API Rules
  rule_count: 33
  severity_counts:
    error: 15
    hint: 0
    info: 7
    warn: 11
  slug: acronis-spectral-rules
skills: []
slug: acronis
solutions: []
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/apis.yml
use_cases:
- description: Automate tenant provisioning, licensing management, and usage reporting for managed service providers.
  name: MSP Platform Automation
- description: Build custom dashboards tracking backup task status, failures, and completion rates.
  name: Backup Monitoring Dashboard
- description: Monitor agent online status, version compliance, and update management across endpoints.
  name: Agent Health Monitoring
- description: Generate automated reports on data protection status for compliance and audit requirements.
  name: Compliance Reporting
- description: Trigger and monitor DR failover workflows programmatically for RTO/RPO compliance.
  name: Disaster Recovery Automation
---
