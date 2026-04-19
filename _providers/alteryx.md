---
api_count: 7
apis:
- description: 'REST API for managing workflows, schedules, and jobs on Alteryx Server. Provides Subscription, User V2, Admin V1, Admin V2, and V3 API endpoints for creating, updating, searching, and deleting users, '
  name: Alteryx Server API
  slug: ''
- description: The V3 Admin API for Alteryx Server uses OAuth 2 authentication and implements POST, PUT, GET, and DELETE functionality for modifying assets, users, credentials, and connections so admins can automate
  name: Alteryx Server API V3
  slug: ''
- description: The V1 API for Alteryx Server provides endpoints for admins including the Migratable Endpoint for migrating workflows across Server environments and the Auditlog Endpoint for tracking changes to syste
  name: Alteryx Server API V1
  slug: ''
- description: API for interacting with Alteryx Analytics Gallery for workflow sharing and execution.
  name: Alteryx Gallery API
  slug: ''
- description: API for Alteryx Connect data catalog and collaboration platform.
  name: Alteryx Connect API
  slug: ''
- description: The AlteryxEngine API allows you to call into the Alteryx Engine to build applications that can programmatically execute Alteryx Designer workflows. Workflows and applications can be executed as a sep
  name: Alteryx AlteryxEngine API
  slug: ''
- description: REST API for Alteryx Designer Cloud (powered by Trifacta) providing data preparation, transformation, and pipeline management capabilities. Enables programmatic access to data preparation workflows an
  name: Alteryx Designer Cloud API
  slug: ''
capabilities:
- description: 'Analytics automation workflow combining Alteryx Server V3 API for workflow management, job execution, scheduling, user administration, credential management, and collection organization. Used by data '
  name: Alteryx Analytics Automation
  slug: analytics-automation
common:
- title: ''
  type: DeveloperPortal
  url: https://help.alteryx.com/current/en/developer-help.html
- title: ''
  type: GettingStarted
  url: https://help.alteryx.com/current/en/developer-help/apis/get-started-with-apis.html
- title: ''
  type: SDK
  url: https://help.alteryx.com/current/en/developer-help/platform-sdk.html
- title: ''
  type: StatusPage
  url: https://status.alteryx.com
- title: ''
  type: Support
  url: https://community.alteryx.com
- title: ''
  type: Blog
  url: https://community.alteryx.com/t5/Engine-Works/bg-p/engine-works
- title: ''
  type: X
  url: https://twitter.com/alteryx
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alteryx
- title: ''
  type: GitHubOrganization
  url: https://github.com/alteryx
- title: ''
  type: Pricing
  url: https://www.alteryx.com/products/pricing
- title: ''
  type: TrustCenter
  url: https://www.alteryx.com/trust
- title: ''
  type: TermsOfService
  url: https://www.alteryx.com/terms-and-conditions
- title: ''
  type: PrivacyPolicy
  url: https://www.alteryx.com/privacy-policy
- title: ''
  type: Legal
  url: https://www.alteryx.com/legal
created: '2024-01-15'
description: Alteryx is an analytics automation platform that enables data analysts and scientists to break data barriers, deliver insights, and experience the thrill of getting to the answer faster.
features:
- description: Visual drag-and-drop workflow builder for automating data preparation, blending, and analytics pipelines.
  name: Workflow Automation
- description: Schedule workflows to run at specific times or intervals for automated recurring analytics processes.
  name: Scheduled Execution
- description: Fine-grained user management with role-based access control for shared workflow environments.
  name: User and Access Management
- description: Secure storage and sharing of data source credentials across workflows and users.
  name: Credential Management
- description: Organize workflows, schedules, and users into collections for logical grouping and permission management.
  name: Collection Organization
- description: Browser-based data preparation and transformation through Designer Cloud with AI-assisted suggestions.
  name: Cloud Data Preparation
image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
integrations:
- description: Native connector for reading from and writing to Snowflake data warehouse for cloud analytics.
  name: Snowflake
- description: Publish prepared data directly to Tableau Server for visualization and business intelligence.
  name: Tableau
- description: Connect to Salesforce CRM data for analytics, reporting, and automated data synchronization.
  name: Salesforce
- description: Read and write data to Amazon S3 for cloud-based data lake analytics workflows.
  name: AWS S3
- description: Integration with Azure data services including SQL Database, Blob Storage, and Synapse Analytics.
  name: Microsoft Azure
jsonld:
- class_count: 0
  name: Alteryx Context
  property_count: 8
  slug: alteryx-context
- class_count: 0
  name: Alteryx Server V3 Context
  property_count: 0
  slug: alteryx-server-v3-context
layout: provider
modified: '2026-04-18'
name: Alteryx
rules:
- name: Alteryx API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: alteryx-spectral-rules
skills: []
slug: alteryx
solutions: []
tags:
- Analytics
- Automation
- Data Engineering
- Data Preparation
- Data Science
- ETL
- Machine Learning
- Predictive Analytics
url: https://raw.githubusercontent.com/api-evangelist/alteryx/refs/heads/main/apis.yml
use_cases:
- description: Schedule and automate data preparation workflows to generate recurring business reports.
  name: Automated Reporting Pipelines
- description: Migrate workflows and configurations across Server environments using the V1 migration API.
  name: Data Migration
- description: Automate user provisioning, credential management, and workflow deployment through the V3 admin API.
  name: Server Administration Automation
- description: Enable business users to discover and run published workflows through the Gallery API.
  name: Self-Service Analytics
- description: Catalog and discover data assets across the organization using Alteryx Connect APIs.
  name: Enterprise Data Catalog
---
