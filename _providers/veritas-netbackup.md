---
api_count: 16
apis:
- description: Primary REST API for NetBackup operations including backup policies, jobs, catalogs, and asset management.
  name: Veritas NetBackup REST API
  slug: ''
- description: API for managing NetBackup jobs including getting job details, listing jobs by filter, restarting, resuming, suspending, canceling, and deleting jobs, and retrieving job file lists and logs.
  name: NetBackup Administration API
  slug: ''
- description: API for managing NetBackup assets including servers, clients, and storage devices.
  name: NetBackup Asset Management API
  slug: ''
- description: API endpoints for managing authentication, authorization, certificates, credentials, tokens, and security audit logging configurations.
  name: NetBackup Security API
  slug: ''
- description: API for managing backup images, catalogs, and media retention.
  name: NetBackup Image Management API
  slug: ''
- description: API for configuring NetBackup hosts, policies, servers, VM server credentials, and storage settings.
  name: NetBackup Configuration API
  slug: ''
- description: API for managing storage consumption, capacity reporting, and backup storage on NetBackup primary servers.
  name: NetBackup Storage API
  slug: ''
- description: API for VMware and cloud workload recovery operations including restore and instant access.
  name: NetBackup Recovery API
  slug: ''
- description: API for managing role-based access control, permissions, access rules, and access control lists.
  name: NetBackup RBAC Administration API
  slug: ''
- description: API for managing entitlements and tracking Front-end Terabytes (FETBs) consumption for NetBackup licensing.
  name: NetBackup Licensing API
  slug: ''
- description: API for managing service-level objectives (SLOs), protection plans, and subscription handling for backup operations.
  name: NetBackup Service Catalog API
  slug: ''
- description: API for managing alerts and notification operations in NetBackup environments.
  name: NetBackup Manage API
  slug: ''
- description: API for status code resolution and error reference to assist with troubleshooting NetBackup issues.
  name: NetBackup Troubleshooting API
  slug: ''
- description: REST API for accessing NetBackup IT Analytics report data, exporting reports in JSON, XML, HTML, PDF, and CSV formats, and exporting custom dashboards.
  name: NetBackup IT Analytics REST API
  slug: ''
- description: REST API for the NetBackup Self Service portal providing backup utilization data, protection status, tenant management, and self-service backup and restore operations.
  name: NetBackup Self Service REST API
  slug: ''
- description: REST API for controlling all aspects of NetBackup Flex Scale configuration including infrastructure monitoring, user management, node management, patch upgrades, and storage licensing.
  name: NetBackup Flex Scale REST API
  slug: ''
capabilities:
- description: Backup operations workflow for backup administrators to manage jobs, policies, clients, and catalog images across NetBackup environments.
  name: Veritas NetBackup Backup Operations
  slug: backup-operations
common:
- title: ''
  type: Support
  url: https://www.veritas.com/support
- title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100040135
- title: ''
  type: APIReference
  url: https://www.veritas.com/support/en_US/doc/139300789-139300792-0/index
- title: ''
  type: GettingStarted
  url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
- title: ''
  type: Pricing
  url: https://www.veritas.com/products/backup-and-recovery/netbackup/pricing
- title: ''
  type: Support
  url: https://www.veritas.com/support/en_US/netbackup
- title: ''
  type: Contact
  url: https://www.veritas.com/company/contact
- title: ''
  type: KnowledgeCenter
  url: https://www.veritas.com/support/en_US/netbackup.PRODUCT_HOME
- title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/netbackup.download
- title: ''
  type: Documentation
  url: https://vox.veritas.com/category/cohesity-discussions/discussions/netbackup
- title: ''
  type: Authentication
  url: https://sort.veritas.com/public/documents/nbu/10.0/windowsandunix/productguides/html/getting-started/
- title: ''
  type: RateLimits
  url: https://sort.veritas.com/documents/netbackup/10.1/productguides
- title: ''
  type: Blog
  url: https://www.veritas.com/blogs
- title: ''
  type: GitHubOrganization
  url: https://github.com/VeritasOS
- title: ''
  type: SDK
  url: https://github.com/VeritasOS/netbackup-api-code-samples
- title: ''
  type: CodeExamples
  url: https://veritasos.github.io/netbackup-api-code-samples/
- title: ''
  type: ChangeLog
  url: https://www.veritas.com/protection/netbackup/whats-new
- title: ''
  type: ReleaseNotes
  url: https://www.veritas.com/support/en_US/doc/103228346-168289021-0/v168307842-168289021
- title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100032801
- title: ''
  type: X
  url: https://twitter.com/veritastechllc
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veritas-technologies-llc
- title: ''
  type: TermsOfService
  url: https://www.veritas.com/company/legal/legal-terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://www.veritas.com/company/privacy
- title: ''
  type: Documentation
  url: https://www.veritas.com/company
- title: ''
  type: Documentation
  url: https://www.veritas.com/protection/netbackup/self-service
- title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100043102
- title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100052421
created: '2024'
description: Enterprise-grade data protection and backup solution with comprehensive REST APIs for backup, recovery, and data management operations.
features:
- description: Comprehensive backup and recovery for physical, virtual, and cloud workloads across heterogeneous environments.
  name: Enterprise Backup and Recovery
- description: Create and manage backup policies with configurable schedules, retention rules, and client selections.
  name: Policy-Based Protection
- description: Monitor, control, and troubleshoot backup and restore jobs with full lifecycle management via REST API.
  name: Job Management
- description: Query and manage backup image catalogs for tracking, searching, and lifecycle management of backup data.
  name: Catalog Management
- description: Fine-grained RBAC for managing user permissions across NetBackup operations and resources.
  name: Role-Based Access Control
- description: Enable tenant-level self-service backup and restore operations through the Self Service portal API.
  name: Self-Service Portal
- description: Access and export analytics reports and dashboards for backup environment monitoring and capacity planning.
  name: IT Analytics and Reporting
- description: Manage NetBackup Flex Scale appliance infrastructure including nodes, storage, users, and patch upgrades.
  name: Flex Scale Infrastructure
image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
integrations:
- description: Native integration for backup and instant recovery of VMware virtual machines and vSphere environments.
  name: VMware vSphere
- description: Support for backup and recovery of workloads running on AWS, Azure, and Google Cloud Platform.
  name: Cloud Platforms
- description: Container workload protection with backup and recovery support for Kubernetes clusters.
  name: Kubernetes
- description: Application-consistent backup and granular recovery for Oracle and Microsoft SQL Server databases.
  name: Oracle and SQL Server
- description: Comprehensive REST API coverage for programmatic integration with ITSM, orchestration, and monitoring tools.
  name: RESTful API Ecosystem
jsonld:
- class_count: 0
  name: Veritas Netbackup Context
  property_count: 8
  slug: veritas-netbackup-context
- class_count: 0
  name: Veritas Netbackup Rest Context
  property_count: 0
  slug: veritas-netbackup-rest-context
layout: provider
modified: '2026-04-18'
name: Veritas NetBackup
rules:
- name: Veritas NetBackup API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: veritas-netbackup-spectral-rules
skills: []
slug: veritas-netbackup
solutions: []
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
url: https://www.veritas.com/products/backup-and-recovery/netbackup
use_cases:
- description: Automate backup policy creation, job scheduling, and monitoring through REST API integration with CI/CD pipelines.
  name: Automated Backup Operations
- description: Programmatically manage recovery operations for VMware and cloud workloads with instant access capabilities.
  name: Disaster Recovery Orchestration
- description: Track and report on backup coverage, retention compliance, and security audit events across the enterprise.
  name: Compliance and Audit
- description: Provide self-service backup and restore capabilities to multiple tenants through the Self Service portal API.
  name: Multi-Tenant Backup Management
- description: Use IT Analytics APIs to export reports on storage consumption, backup trends, and capacity forecasting.
  name: Capacity Planning
---
