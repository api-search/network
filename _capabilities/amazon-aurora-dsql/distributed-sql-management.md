---
consumed_apis: []
description: Workflow capability for creating and managing distributed SQL clusters with Amazon Aurora DSQL including multi-region configurations.
layout: capability
name: Distributed SQL Management Workflow
operations:
- description: Create a new cluster
  method: POST
  name: create-cluster
  path: /v1/clusters
- description: List all clusters
  method: GET
  name: list-clusters
  path: /v1/clusters
personas: []
provider_name: Amazon Aurora DSQL
provider_slug: amazon-aurora-dsql
search_terms:
- update the configuration of an aurora dsql cluster.
- distributed sql
- distributed sql cluster management
- create multi region clusters
- create linked aurora dsql clusters across multiple aws regions for global distribution.
- get cluster endpoint
- serverless
- list clusters
- delete an aurora dsql cluster when it is no longer needed.
- create cluster
- get the postgresql-compatible connection endpoint for an aurora dsql cluster.
- postgresql
- create a new cluster
- get the current status and configuration of an aurora dsql cluster.
- aws
- create a new aurora dsql cluster for distributed sql workloads.
- amazon aurora dsql
- delete cluster
- update cluster
- list all aurora dsql clusters to understand available databases.
- list all clusters
- get cluster
slug: distributed-sql-management
tags:
- Amazon Aurora DSQL
- Distributed SQL
- PostgreSQL
- Serverless
- AWS
tools:
- description: List all Aurora DSQL clusters to understand available databases.
  hints:
    openWorld: true
    readOnly: true
  name: list-clusters
- description: Create a new Aurora DSQL cluster for distributed SQL workloads.
  hints:
    openWorld: false
    readOnly: false
  name: create-cluster
- description: Get the current status and configuration of an Aurora DSQL cluster.
  hints:
    openWorld: true
    readOnly: true
  name: get-cluster
- description: Get the PostgreSQL-compatible connection endpoint for an Aurora DSQL cluster.
  hints:
    openWorld: true
    readOnly: true
  name: get-cluster-endpoint
- description: Update the configuration of an Aurora DSQL cluster.
  hints:
    openWorld: false
    readOnly: false
  name: update-cluster
- description: Create linked Aurora DSQL clusters across multiple AWS regions for global distribution.
  hints:
    openWorld: false
    readOnly: false
  name: create-multi-region-clusters
- description: Delete an Aurora DSQL cluster when it is no longer needed.
  hints:
    openWorld: false
    readOnly: false
  name: delete-cluster
---
