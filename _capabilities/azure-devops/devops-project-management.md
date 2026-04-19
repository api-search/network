---
consumed_apis:
- azure-devops-work-items
- azure-devops-pipelines
description: Unified workflow for managing Azure DevOps projects combining work item tracking and CI/CD pipeline operations. Used by development teams, project managers, and DevOps engineers to plan work, track progress, and automate build/release processes.
layout: capability
name: Azure DevOps Project Management
operations:
- description: Get a work item by ID
  method: GET
  name: get-work-item
  path: /v1/work-items/{id}
- description: Update a work item
  method: PATCH
  name: update-work-item
  path: /v1/work-items/{id}
- description: Get multiple work items by IDs
  method: GET
  name: get-work-items-batch
  path: /v1/work-items
- description: Create a new work item
  method: POST
  name: create-work-item
  path: /v1/work-items
- description: Query work items using WIQL
  method: POST
  name: query-work-items
  path: /v1/queries
- description: List work item fields
  method: GET
  name: list-fields
  path: /v1/fields
- description: List all pipelines
  method: GET
  name: list-pipelines
  path: /v1/pipelines
- description: Create a new pipeline
  method: POST
  name: create-pipeline
  path: /v1/pipelines
- description: Get a pipeline by ID
  method: GET
  name: get-pipeline
  path: /v1/pipelines/{pipelineId}
- description: List pipeline runs
  method: GET
  name: list-pipeline-runs
  path: /v1/pipelines/{pipelineId}/runs
- description: Trigger a pipeline run
  method: POST
  name: run-pipeline
  path: /v1/pipelines/{pipelineId}/runs
- description: Get a pipeline run
  method: GET
  name: get-pipeline-run
  path: /v1/pipelines/{pipelineId}/runs/{runId}
personas: []
provider_name: Azure DevOps
provider_slug: azure-devops
search_terms:
- query work items
- list fields
- get a work item by id
- get details of a pipeline run
- list runs for a pipeline
- ci/cd
- update work item
- get work item
- list all work item field definitions
- create a new work item
- update a work item
- list all pipelines
- wiql query execution
- query work items using wiql
- list pipeline runs
- azure devops
- pipeline definitions
- work item field definitions
- get pipeline run
- get a pipeline run
- list work item fields
- list pipelines
- run pipeline
- devops
- pipelines
- create pipeline
- single pipeline run
- trigger a pipeline run
- work item batch and creation
- create a new pipeline
- project management
- work items
- get work items batch
- azure
- get a pipeline by id
- get multiple work items by ids
- pipeline runs
- get pipeline
- create work item
- single pipeline
- list all pipelines in a project
- individual work item operations
slug: devops-project-management
tags:
- Azure DevOps
- Project Management
- CI/CD
- Work Items
- Pipelines
tools:
- description: Get a work item by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-work-item
- description: Create a new work item
  hints:
    readOnly: false
  name: create-work-item
- description: Update a work item
  hints:
    idempotent: true
    readOnly: false
  name: update-work-item
- description: Get multiple work items by IDs
  hints:
    idempotent: true
    readOnly: true
  name: get-work-items-batch
- description: Query work items using WIQL
  hints:
    idempotent: true
    readOnly: true
  name: query-work-items
- description: List all work item field definitions
  hints:
    idempotent: true
    readOnly: true
  name: list-work-item-fields
- description: List all pipelines in a project
  hints:
    idempotent: true
    readOnly: true
  name: list-pipelines
- description: Get a pipeline by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-pipeline
- description: Create a new pipeline
  hints:
    readOnly: false
  name: create-pipeline
- description: Trigger a pipeline run
  hints:
    readOnly: false
  name: run-pipeline
- description: List runs for a pipeline
  hints:
    idempotent: true
    readOnly: true
  name: list-pipeline-runs
- description: Get details of a pipeline run
  hints:
    idempotent: true
    readOnly: true
  name: get-pipeline-run
---
