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
- clean rooms
- terminate a running cluster.
- data
- mlflow
- list workspace objects.
- databricks
- start a terminated cluster.
- list runs for a job.
- big data
- apache spark
- create job
- delete a workspace object.
- visualize
- list clusters
- delta lake
- run job now
- create a new spark cluster.
- security
- list all databricks clusters.
- vector search
- list all databricks jobs.
- start cluster
- import workspace object
- data governance
- list jobs
- workspace object management.
- cluster lifecycle management.
- list all clusters.
- list all jobs.
- terminate cluster
- cancel a running job.
- unity catalog
- machine learning
- get cluster
- sql
- get job details.
- export a notebook or workspace object.
- etl
- export workspace object
- analytics
- import a notebook or workspace object.
- cancel job run
- get details of a specific run.
- delete job
- delta sharing
- delete workspace object
- list objects in a workspace directory.
- ai
- create cluster
- identity management
- job orchestration.
- get cluster details.
- edit cluster
- create a new cluster.
- trigger a job run immediately.
- list job runs
- cloud computing
- edit cluster configuration.
- data engineering
- get job run
- list workspace objects
- delete a job.
- data analytics
- lakehouse
- model serving
- get job
- create a new job.
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
