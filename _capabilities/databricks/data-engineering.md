---
consumed_apis:
- databricks-api
description: Unified workflow for Databricks data engineering including cluster management, job orchestration, and workspace operations. Used by data engineers and platform administrators.
layout: capability
name: Databricks Data Engineering
operations:
- description: List all clusters.
  method: GET
  name: list-clusters
  path: /v1/clusters
- description: Create a new cluster.
  method: POST
  name: create-cluster
  path: /v1/clusters
- description: List all jobs.
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: Create a new job.
  method: POST
  name: create-job
  path: /v1/jobs
- description: List workspace objects.
  method: GET
  name: list-workspace-objects
  path: /v1/workspace
personas: []
provider_name: Databricks
provider_slug: databricks
search_terms:
- list workspace objects.
- workspace object management.
- list all databricks clusters.
- create a new job.
- list all databricks jobs.
- identity management
- cancel job run
- get details of a specific run.
- list jobs
- analytics
- lakehouse
- import a notebook or workspace object.
- databricks
- etl
- job orchestration.
- data engineering
- terminate a running cluster.
- data analytics
- edit cluster
- start a terminated cluster.
- edit cluster configuration.
- sql
- data governance
- import workspace object
- create a new cluster.
- big data
- run job now
- get job run
- machine learning
- list clusters
- ai
- mlflow
- delta lake
- vector search
- list all jobs.
- create cluster
- create a new spark cluster.
- model serving
- get cluster details.
- start cluster
- terminate cluster
- delete a job.
- security
- delete workspace object
- list runs for a job.
- delete job
- export a notebook or workspace object.
- unity catalog
- list objects in a workspace directory.
- visualize
- clean rooms
- export workspace object
- create job
- cloud computing
- delete a workspace object.
- delta sharing
- get job
- apache spark
- cluster lifecycle management.
- list workspace objects
- data
- get job details.
- list job runs
- trigger a job run immediately.
- list all clusters.
- cancel a running job.
- get cluster
slug: data-engineering
tags:
- Databricks
- Data Engineering
- ETL
- Apache Spark
tools:
- description: List all Databricks clusters.
  hints:
    openWorld: true
    readOnly: true
  name: list-clusters
- description: Create a new Spark cluster.
  hints:
    readOnly: false
  name: create-cluster
- description: Get cluster details.
  hints:
    readOnly: true
  name: get-cluster
- description: Start a terminated cluster.
  hints:
    readOnly: false
  name: start-cluster
- description: Terminate a running cluster.
  hints:
    destructive: true
  name: terminate-cluster
- description: Edit cluster configuration.
  hints:
    idempotent: true
    readOnly: false
  name: edit-cluster
- description: List all Databricks jobs.
  hints:
    readOnly: true
  name: list-jobs
- description: Create a new job.
  hints:
    readOnly: false
  name: create-job
- description: Get job details.
  hints:
    readOnly: true
  name: get-job
- description: Trigger a job run immediately.
  hints:
    readOnly: false
  name: run-job-now
- description: List runs for a job.
  hints:
    readOnly: true
  name: list-job-runs
- description: Get details of a specific run.
  hints:
    readOnly: true
  name: get-job-run
- description: Cancel a running job.
  hints:
    destructive: true
  name: cancel-job-run
- description: Delete a job.
  hints:
    destructive: true
  name: delete-job
- description: List objects in a workspace directory.
  hints:
    readOnly: true
  name: list-workspace-objects
- description: Export a notebook or workspace object.
  hints:
    readOnly: true
  name: export-workspace-object
- description: Import a notebook or workspace object.
  hints:
    readOnly: false
  name: import-workspace-object
- description: Delete a workspace object.
  hints:
    destructive: true
  name: delete-workspace-object
---
