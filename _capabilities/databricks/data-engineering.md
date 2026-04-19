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
- data engineering
- get job run
- trigger a job run immediately.
- delete job
- clean rooms
- list runs for a job.
- cancel job run
- delete workspace object
- unity catalog
- big data
- security
- apache spark
- analytics
- job orchestration.
- cluster lifecycle management.
- start cluster
- get cluster details.
- list job runs
- export a notebook or workspace object.
- visualize
- ai
- delete a job.
- data
- identity management
- mlflow
- databricks
- list all clusters.
- cancel a running job.
- machine learning
- create a new job.
- get cluster
- delta lake
- list workspace objects.
- etl
- create a new spark cluster.
- start a terminated cluster.
- list objects in a workspace directory.
- list jobs
- terminate cluster
- get details of a specific run.
- data analytics
- create cluster
- data governance
- create a new cluster.
- import workspace object
- delta sharing
- list all jobs.
- workspace object management.
- cloud computing
- get job details.
- lakehouse
- run job now
- get job
- list workspace objects
- import a notebook or workspace object.
- terminate a running cluster.
- delete a workspace object.
- sql
- vector search
- list all databricks clusters.
- export workspace object
- list all databricks jobs.
- model serving
- edit cluster
- create job
- list clusters
- edit cluster configuration.
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
