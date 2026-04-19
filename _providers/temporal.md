---
api_count: 2
apis:
- description: The Temporal Server Frontend API provides gRPC services for interacting with the Temporal Server, including WorkflowService for managing workflow executions, OperatorService for cluster operations, an
  name: Temporal Server Frontend API
  slug: server-frontend-api
- description: The Temporal Cloud Operations API is an open source, public HTTP API and gRPC API for programmatically managing Temporal Cloud control plane resources, including Namespaces, Users, Service Accounts, A
  name: Temporal Cloud Ops API
  slug: cloud-ops-api
capabilities:
- description: Unified workflow for platform administrators to manage Temporal Cloud infrastructure including namespaces, users, service accounts, API keys, and regions.
  name: Temporal Cloud Operations
  slug: cloud-operations
common:
- title: ''
  type: Portal
  url: https://temporal.io/
- title: ''
  type: Documentation
  url: https://docs.temporal.io/
- title: ''
  type: GettingStarted
  url: https://docs.temporal.io/cloud/get-started
- title: ''
  type: Quickstart
  url: https://docs.temporal.io/quickstarts
- title: ''
  type: SDK
  url: https://docs.temporal.io/develop
- title: ''
  type: CLI
  url: https://docs.temporal.io/cli
- title: ''
  type: Pricing
  url: https://temporal.io/pricing
- title: ''
  type: Blog
  url: https://temporal.io/blog
- title: ''
  type: ChangeLog
  url: https://temporal.io/change-log
- title: ''
  type: StatusPage
  url: https://status.temporal.io
- title: ''
  type: Security
  url: https://temporal.io/security
- title: ''
  type: TermsOfService
  url: https://temporal.io/terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://temporal.io/global-privacy-policy
- title: ''
  type: Login
  url: https://cloud.temporal.io/login
- title: ''
  type: SignUp
  url: https://docs.temporal.io/cloud/get-started
- title: ''
  type: GitHubOrganization
  url: https://github.com/temporalio
- title: ''
  type: Training
  url: https://learn.temporal.io/
- title: ''
  type: NaftikoCapability
  url: capabilities/cloud-operations.yaml
created: '2026-03-03'
description: Temporal is an open-source durable execution platform for building reliable long-running distributed workflows and microservices.
features:
- description: Automatically persists workflow state and resumes execution after failures, ensuring long-running processes complete reliably.
  name: Durable Execution
- description: Create and manage isolated namespaces for organizing workflows with independent retention policies and access controls.
  name: Namespace Management
- description: Manage users, service accounts, and API keys for fine-grained access control to Temporal Cloud resources.
  name: User and Access Management
- description: Deploy workflows across multiple cloud regions for low-latency execution and disaster recovery.
  name: Multi-Region Deployment
- description: Safely deploy workflow code changes with built-in versioning that prevents breaking running executions.
  name: Workflow Versioning
- description: Query and filter workflow executions using custom search attributes for operational visibility and debugging.
  name: Visibility and Search
- description: Secure namespace communication with mutual TLS certificate-based authentication and codec server encryption.
  name: mTLS Authentication
- description: Track the status of long-running control plane operations like namespace creation and configuration changes.
  name: Async Operations
image: /assets/icons/temporal.png
integrations:
- description: Native Go client library for building Temporal workflows and activities with full type safety.
  name: Go SDK
- description: TypeScript/JavaScript SDK for building Temporal workflows in Node.js with async/await patterns.
  name: TypeScript SDK
- description: Python SDK for building Temporal workflows with native async support and type hints.
  name: Python SDK
- description: Java SDK for building Temporal workflows with annotation-based workflow and activity definitions.
  name: Java SDK
- description: .NET SDK for building Temporal workflows in C# with strong typing and async patterns.
  name: .NET SDK
jsonld:
- class_count: 0
  name: Cloud Ops Context
  property_count: 0
  slug: cloud-ops-context
layout: provider
modified: '2026-04-19'
name: Temporal
rules:
- name: Temporal API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: temporal-spectral-rules
skills: []
slug: temporal
solutions: []
tags:
- ProCode_API_Composition
- Workflows
url: https://raw.githubusercontent.com/api-evangelist/temporal/refs/heads/main/apis.yml
use_cases:
- description: Coordinate complex multi-service transactions with automatic retries, compensation logic, and timeout handling.
  name: Microservice Orchestration
- description: Build reliable ETL and data processing pipelines that handle failures gracefully and resume from the last checkpoint.
  name: Data Pipeline Processing
- description: Automate end-to-end order processing including payment, inventory, shipping, and notification steps with guaranteed completion.
  name: Order Fulfillment Workflows
- description: Orchestrate cloud infrastructure deployment and configuration management with durable state tracking.
  name: Infrastructure Provisioning
- description: Manage recurring billing cycles, subscription renewals, and payment processing with long-running timer-based workflows.
  name: Subscription and Billing Management
---
