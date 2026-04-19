---
api_count: 1
apis:
- description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps tra
  name: Conductor
  slug: conductor
asyncapis:
- description: 'Asynchronous event API for Conductor workflow orchestration platform. Conductor emits events when workflows and tasks change state, enabling reactive event-driven architectures. Event handlers can be '
  name: Conductor Events API
  slug: conductor-conductor-asyncapi
capabilities:
- description: Unified workflow for managing workflow definitions, task definitions, workflow executions, and event handlers. Used by backend developers and DevOps engineers.
  name: Conductor Workflow Orchestration
  slug: workflow-orchestration
common:
- title: ''
  type: GitHubRepository
  url: https://github.com/conductor-oss/conductor
- title: ''
  type: SpectralRules
  url: rules/conductor-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/conductor-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/workflow-orchestration.yaml
created: '2025-01-08'
description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps track of the state, calls tasks in the right order (sequentially or in parallel, as defined by you), retry calls if needed, handle failure scenarios gracefully, and outputs the final result.
features:
- description: Define and execute complex workflows with sequential and parallel task execution.
  name: Workflow Orchestration
- description: Register, poll, and update granular task definitions with timeout and retry policies.
  name: Task Management
- description: Create event handlers to trigger workflows or tasks based on external events.
  name: Event Handling
- description: Search and filter workflow executions by status, type, and custom parameters.
  name: Workflow Search
- description: Automatic retries, pause/resume, and graceful failure handling for long-running workflows.
  name: Fault Tolerance
- description: Pause, resume, restart, retry, and terminate workflows programmatically.
  name: Workflow Lifecycle Control
image: /assets/icons/conductor.png
integrations:
- description: Trigger workflows and tasks from Kafka events using event handler subscriptions.
  name: Apache Kafka
- description: Integrate with SQS for message-driven workflow initiation and task completion.
  name: Amazon SQS
- description: Run Conductor server and workers in containerized environments for scalable deployment.
  name: Docker
- description: Use managed Conductor service from Orkes for enterprise-grade orchestration without infrastructure management.
  name: Orkes Cloud
jsonld:
- class_count: 0
  name: Conductor Conductor Context
  property_count: 0
  slug: conductor-conductor-context
- class_count: 7
  name: Conductor Context
  property_count: 40
  slug: conductor-context
layout: provider
modified: '2026-04-18'
name: Conductor
rules:
- name: Conductor API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: conductor-spectral-rules
skills: []
slug: conductor
solutions: []
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
url: https://raw.githubusercontent.com/api-evangelist/conductor/refs/heads/main/apis.yml
use_cases:
- description: Coordinate complex business processes across distributed microservices without tight coupling.
  name: Microservices Orchestration
- description: Build and manage ETL and data processing pipelines with dependency tracking and error recovery.
  name: Data Pipeline Automation
- description: Manage multi-step order fulfillment workflows including payment, inventory, and shipping.
  name: Order Processing
- description: Orchestrate build, test, and deployment workflows with conditional logic and parallel execution.
  name: CI/CD Pipelines
---
