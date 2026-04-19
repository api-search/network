---
api_count: 2
apis:
- description: The Azure App Service / Web Apps REST API provides management operations for Azure Functions apps including creating and configuring function apps, managing deployment slots, application settings, hos
  name: Azure Functions Management API
  slug: azure-functions-management-api
- description: The Azure Functions host runtime provides HTTP endpoints for function invocation, admin operations, host status, function management, and key management. Includes endpoints for listing functions, gett
  name: Azure Functions Runtime API
  slug: azure-functions-runtime-api
common:
- title: ''
  type: Portal
  url: https://portal.azure.com/
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-functions/
- title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/functions/
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- title: ''
  type: StatusPage
  url: https://status.azure.com/
- title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions
- title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-functions-host
- title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-functions-core-tools
- title: .NET SDK
  type: SDK
  url: https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker
- title: Python SDK
  type: SDK
  url: https://pypi.org/project/azure-functions/
- title: Node.js SDK
  type: SDK
  url: https://www.npmjs.com/package/@azure/functions
- title: Java SDK
  type: SDK
  url: https://central.sonatype.com/artifact/com.microsoft.azure.functions/azure-functions-java-library
- title: Azure Functions Core Tools
  type: CLI
  url: https://github.com/Azure/azure-functions-core-tools
- title: Azure CLI (az functionapp)
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/functionapp
- title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/create-serverless-applications/
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-functions
- title: ''
  type: X
  url: https://x.com/AzureFunctions
created: '2024-01-01'
description: Azure Functions is a serverless compute platform from Microsoft Azure enabling event-driven code execution triggered by HTTP requests, timers, queues, blobs, and other Azure services. The Azure Functions management API provides programmatic access to function app lifecycle management, deployment, configuration, scaling, and monitoring through Azure Resource Manager.
features:
- description: Execute functions via HTTP requests with RESTful endpoint support and built-in authentication.
  name: HTTP Triggers
- description: Schedule function execution using CRON expressions for recurring tasks.
  name: Timer Triggers
- description: Process messages from Azure Storage Queues and Service Bus for async workloads.
  name: Queue Triggers
- description: React to blob storage changes for file processing and data pipeline automation.
  name: Blob Triggers
- description: Handle events from Azure Event Grid for event-driven architectures.
  name: Event Grid Triggers
- description: Process database changes in Azure Cosmos DB using the change feed.
  name: Cosmos DB Triggers
- description: Orchestrate complex stateful workflows with function chaining, fan-out/fan-in, and human interaction patterns.
  name: Durable Functions
- description: Manage staging and production slots for zero-downtime deployments and traffic splitting.
  name: Deployment Slots
- description: Run functions in any language by implementing a lightweight HTTP server.
  name: Custom Handlers
- description: Authenticate to Azure services without managing credentials using system or user-assigned identities.
  name: Managed Identity
- description: Automatic scaling from zero to thousands of instances based on event load.
  name: Scaling
- description: Pre-warmed instances, VNET integration, and unlimited execution duration for enterprise workloads.
  name: Premium Plan
image: /assets/icons/microsoft-azure-functions.png
integrations:
- description: Front Azure Functions with API Management for rate limiting, authentication, and developer portal.
  name: Azure API Management
- description: CI/CD pipeline integration for automated function deployment and testing.
  name: Azure DevOps
- description: Deploy Azure Functions directly from GitHub repositories with Actions workflows.
  name: GitHub Actions
- description: Full development experience with the Azure Functions VS Code extension.
  name: Visual Studio Code
- description: Application Insights integration for function monitoring, logging, and diagnostics.
  name: Azure Monitor
- description: Secure secrets management with Key Vault references in application settings.
  name: Azure Key Vault
- description: Infrastructure-as-code management of function apps with the AzureRM Terraform provider.
  name: Terraform
jsonld:
- class_count: 29
  name: Azure Functions Context
  property_count: 158
  slug: azure-functions-context
layout: provider
modified: '2026-04-17'
name: Microsoft Azure Functions
rules:
- name: Microsoft Azure Functions API Rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 2
  slug: azure-functions-spectral-rules
skills: []
slug: microsoft-azure-functions
solutions:
- description: Pay-per-execution pricing with automatic scaling and 5-minute execution timeout.
  name: Consumption Plan
- description: Pre-warmed instances, VNET integration, unlimited duration, and larger instance sizes.
  name: Premium Plan
- description: Run functions on dedicated App Service plans for predictable pricing and always-on execution.
  name: Dedicated Plan
- description: Run containerized functions on Azure Container Apps for Kubernetes-based hosting.
  name: Container Apps
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/apis.yml
use_cases:
- description: Build serverless REST APIs with HTTP-triggered functions and Azure API Management integration.
  name: API Backend
- description: Process events from queues, topics, Event Grid, and IoT Hub for real-time data pipelines.
  name: Event Processing
- description: Run scheduled jobs for data cleanup, report generation, and system maintenance.
  name: Scheduled Tasks
- description: Transform, validate, and process files uploaded to blob storage.
  name: File Processing
- description: Receive and process webhooks from third-party services and SaaS platforms.
  name: Webhook Handling
- description: Build lightweight microservices with independent scaling and deployment.
  name: Microservices
- description: ETL workloads for transforming and loading data between Azure services.
  name: Data Transformation
- description: Process IoT device telemetry and events with Event Hub and IoT Hub triggers.
  name: IoT Backend
---
