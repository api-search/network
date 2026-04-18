---
consumed_apis:
- databricks
description: Manage Azure Databricks clusters, jobs, and workspace objects for data engineering workflows. Used by data engineers and platform administrators.
layout: capability
name: Azure Databricks Data Engineering
operations:
- description: List all clusters
  method: GET
  name: list-clusters
  path: /v1/clusters
- description: Create a new cluster
  method: POST
  name: create-cluster
  path: /v1/clusters
- description: List all jobs
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: Create a new job
  method: POST
  name: create-job
  path: /v1/jobs
- description: List workspace objects
  method: GET
  name: list-workspace-objects
  path: /v1/workspace
personas: []
provider_name: Azure Databricks
provider_slug: azure-databricks
search_terms:
- get details of a specific cluster
- apache spark
- list node types
- cancel a running job
- list all databricks clusters
- permanently delete a cluster
- trigger a one-time job run
- run job now
- delete a workspace object
- delete job
- partially update job settings
- list workspace objects
- list all clusters
- list jobs
- create job
- delete cluster
- get workspace object status
- manage databricks jobs
- create workspace directory
- delete a job
- create a directory in the workspace
- terminate cluster
- data engineering
- get job run output
- export workspace object
- cancel job run
- create a new cluster
- manage workspace objects
- edit cluster configuration
- restart cluster
- terminate a running cluster
- import workspace object
- get the output of a completed job run
- create a new databricks job
- start a terminated cluster
- get details of a specific job run
- get cluster
- list workspace objects in a directory
- manage databricks clusters
- restart a running cluster
- big data
- analytics
- list all jobs
- edit cluster
- import a notebook or file into the workspace
- list clusters
- start cluster
- delete workspace object
- list spark versions
- list available spark runtime versions
- get job details
- export a notebook or file from the workspace
- create cluster
- get status of a workspace object
- databricks
- get job run
- create a new job
- list job runs
- machine learning
- list all databricks jobs
- list available node types
- get job
- azure
- update job
- create a new databricks cluster
slug: data-engineering
tags:
- Azure
- Databricks
- Data Engineering
- Apache Spark
tools:
- description: Create a new Databricks cluster
  hints:
    readOnly: false
  name: create-cluster
- description: List all Databricks clusters
  hints:
    readOnly: true
  name: list-clusters
- description: Get details of a specific cluster
  hints:
    readOnly: true
  name: get-cluster
- description: Edit cluster configuration
  hints:
    idempotent: true
    readOnly: false
  name: edit-cluster
- description: Start a terminated cluster
  hints:
    readOnly: false
  name: start-cluster
- description: Restart a running cluster
  hints:
    readOnly: false
  name: restart-cluster
- description: Terminate a running cluster
  hints:
    destructive: true
  name: terminate-cluster
- description: Permanently delete a cluster
  hints:
    destructive: true
    idempotent: true
  name: delete-cluster
- description: List available Spark runtime versions
  hints:
    readOnly: true
  name: list-spark-versions
- description: List available node types
  hints:
    readOnly: true
  name: list-node-types
- description: Create a new Databricks job
  hints:
    readOnly: false
  name: create-job
- description: List all Databricks jobs
  hints:
    readOnly: true
  name: list-jobs
- description: Get job details
  hints:
    readOnly: true
  name: get-job
- description: Partially update job settings
  hints:
    readOnly: false
  name: update-job
- description: Delete a job
  hints:
    destructive: true
    idempotent: true
  name: delete-job
- description: Trigger a one-time job run
  hints:
    readOnly: false
  name: run-job-now
- description: List job runs
  hints:
    readOnly: true
  name: list-job-runs
- description: Get details of a specific job run
  hints:
    readOnly: true
  name: get-job-run
- description: Cancel a running job
  hints:
    destructive: true
  name: cancel-job-run
- description: Get the output of a completed job run
  hints:
    readOnly: true
  name: get-job-run-output
- description: List workspace objects in a directory
  hints:
    readOnly: true
  name: list-workspace-objects
- description: Get status of a workspace object
  hints:
    readOnly: true
  name: get-workspace-object-status
- description: Create a directory in the workspace
  hints:
    readOnly: false
  name: create-workspace-directory
- description: Delete a workspace object
  hints:
    destructive: true
    idempotent: true
  name: delete-workspace-object
- description: Import a notebook or file into the workspace
  hints:
    readOnly: false
  name: import-workspace-object
- description: Export a notebook or file from the workspace
  hints:
    readOnly: true
  name: export-workspace-object
---
