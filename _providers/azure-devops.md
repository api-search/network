---
api_count: 6
apis:
- description: 'The Azure DevOps Work Item Tracking API provides REST endpoints for creating, updating, querying, and managing work items including bugs, tasks, user stories, epics, and features across Azure Boards. '
  name: Azure DevOps Work Item Tracking API
  slug: azure-devops-work-item-tracking-api
- description: The Azure DevOps Git Repositories API provides REST endpoints for managing Git repositories, branches, commits, pull requests, and code reviews. APIs enable automation of repository management, pull r
  name: Azure DevOps Git Repositories API
  slug: azure-devops-git-api
- description: The Azure DevOps Pipelines API provides REST endpoints for managing CI/CD build and release pipelines. APIs support pipeline creation, triggering builds, retrieving build results, managing release def
  name: Azure DevOps Pipelines API
  slug: azure-devops-pipelines-api
- description: The Azure DevOps Artifacts API provides REST endpoints for managing package feeds including NuGet, npm, Maven, Python, and Universal Packages. APIs support feed creation, package publishing, version m
  name: Azure DevOps Artifacts API
  slug: azure-devops-artifacts-api
- description: 'The Azure DevOps Test Plans API provides REST endpoints for managing test plans, test suites, test cases, and test runs. APIs support automated test management, test result reporting, and integration '
  name: Azure DevOps Test Plans API
  slug: azure-devops-test-plans-api
- description: The Azure DevOps Release API provides REST endpoints for managing release pipelines, deployments, and environments. APIs support release definition management, deployment approvals, environment config
  name: Azure DevOps Release API
  slug: azure-devops-release-api
asyncapis:
- description: Azure DevOps Service Hooks deliver event notifications for work item changes, build completions, pull request events, code pushes, and release deployments. Service hooks are configured in Azure DevOps
  name: Azure DevOps Service Hooks (Webhooks)
  slug: azure-devops-hooks-asyncapi
capabilities:
- description: Unified workflow for managing Azure DevOps projects combining work item tracking and CI/CD pipeline operations. Used by development teams, project managers, and DevOps engineers to plan work, track pr
  name: Azure DevOps Project Management
  slug: devops-project-management
common:
- title: ''
  type: Documentation
  url: https://azure.microsoft.com/en-us/products/devops
- title: ''
  type: Portal
  url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
- title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
- title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits?view=azure-devops
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/dev-resources/?view=azure-devops
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- title: Node.js SDK
  type: SDK
  url: https://github.com/microsoft/azure-devops-node-api
- title: Python SDK
  type: SDK
  url: https://github.com/microsoft/azure-devops-python-api
- title: Go SDK
  type: SDK
  url: https://github.com/microsoft/azure-devops-go-api
- title: Java SDK
  type: SDK
  url: https://github.com/microsoft/azure-devops-java-api
- title: Azure DevOps CLI Extension
  type: CLI
  url: https://github.com/Azure/azure-devops-cli-extension
- title: ''
  type: OpenAPI
  url: openapi/azure-devops-work-items-openapi.yml
- title: ''
  type: OpenAPI
  url: openapi/azure-devops-pipelines-openapi.yml
- title: Create Pipeline Request Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-create-pipeline-request-schema.json
- title: Pipelines Error Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-error-schema.json
- title: Pipeline Run Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-pipeline-run-schema.json
- title: Pipeline Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-pipeline-schema.json
- title: Run Pipeline Request Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-run-pipeline-request-schema.json
- title: Work Items Error Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-error-schema.json
- title: JSON Patch Operation Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-json-patch-operation-schema.json
- title: WIQL Result Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-wiql-result-schema.json
- title: Work Item Field Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-work-item-field-schema.json
- title: Work Item Relation Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-work-item-relation-schema.json
- title: Work Item Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-work-item-schema.json
- title: Work Item Schema (Legacy)
  type: JSONSchema
  url: json-schema/azure-devops-workitem-schema.json
- title: Azure DevOps JSON-LD Context
  type: JSONLD
  url: json-ld/azure-devops-context.jsonld
- title: Pipelines JSON-LD Context
  type: JSONLD
  url: json-ld/azure-devops-pipelines-context.jsonld
- title: Work Items JSON-LD Context
  type: JSONLD
  url: json-ld/azure-devops-work-items-context.jsonld
- title: Azure DevOps Vocabulary
  type: Vocabulary
  url: vocabulary/azure-devops-vocabulary.yaml
- title: Spectral Rules
  type: Rules
  url: rules/azure-devops-spectral-rules.yml
- title: DevOps Project Management Workflow
  type: Capabilities
  url: capabilities/devops-project-management.yaml
- title: Work Items Shared Capability
  type: Capabilities
  url: capabilities/shared/work-items.yaml
- title: Pipelines Shared Capability
  type: Capabilities
  url: capabilities/shared/pipelines.yaml
created: '2024-01-01'
description: Learn the basic patterns for using the REST APIs for Azure DevOps Services and Azure DevOps Server.
features:
- description: Create, update, query, and manage work items across Azure Boards
  name: Work Item Tracking
- description: Build, test, and deploy with YAML-based and classic pipelines
  name: CI/CD Pipelines
- description: Host and manage Git repositories with branch policies and pull requests
  name: Git Repositories
- description: Package management for NuGet, npm, Maven, Python, and Universal Packages
  name: Artifacts
- description: Comprehensive test management with automated and manual testing
  name: Test Plans
- description: Multi-stage deployment pipelines with approval workflows
  name: Release Management
image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
integrations:
- description: Import repositories and trigger pipelines from GitHub events
  name: GitHub
- description: Notifications for pipeline runs and work item updates
  name: Slack
- description: Bidirectional sync of work items with Jira issues
  name: Jira
jsonld:
- class_count: 0
  name: Azure Devops Context
  property_count: 4
  slug: azure-devops-context
- class_count: 0
  name: Azure Devops Pipelines Context
  property_count: 0
  slug: azure-devops-pipelines-context
- class_count: 0
  name: Azure Devops Work Items Context
  property_count: 0
  slug: azure-devops-work-items-context
layout: provider
modified: '2026-04-18'
name: Azure DevOps
rules:
- name: Azure DevOps API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-devops-spectral-rules
skills: []
slug: azure-devops
solutions: []
tags:
- Azure
- CI/CD
- DevOps
- Pipelines
- Work Items
url: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/apis.yml
use_cases:
- description: Track work items, sprints, and backlogs for Agile development teams
  name: Agile Project Management
- description: Automate build, test, and deployment workflows across environments
  name: CI/CD Automation
- description: Enforce branch policies and manage pull request workflows
  name: Code Review
---
