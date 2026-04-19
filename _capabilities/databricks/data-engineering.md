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
- list all databricks clusters.
- model serving
- list jobs
- list all databricks jobs.
- trigger a job run immediately.
- sql
- data governance
- visualize
- get job
- cloud computing
- etl
- databricks
- create a new job.
- create job
- ai
- lakehouse
- list clusters
- machine learning
- identity management
- get job run
- get cluster
- cancel job run
- get cluster details.
- cancel a running job.
- cluster lifecycle management.
- create a new spark cluster.
- delta lake
- data analytics
- import workspace object
- export workspace object
- clean rooms
- start a terminated cluster.
- terminate cluster
- security
- export a notebook or workspace object.
- terminate a running cluster.
- delete job
- create a new cluster.
- job orchestration.
- data engineering
- edit cluster configuration.
- analytics
- unity catalog
- start cluster
- mlflow
- delta sharing
- list objects in a workspace directory.
- list job runs
- list all clusters.
- create cluster
- delete a job.
- import a notebook or workspace object.
- get details of a specific run.
- apache spark
- delete workspace object
- workspace object management.
- data
- vector search
- get job details.
- delete a workspace object.
- list all jobs.
- run job now
- list workspace objects
- list runs for a job.
- big data
- list workspace objects.
- edit cluster
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
