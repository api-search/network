---
consumed_apis:
- goldengate-cloud
- goldengate-stream-analytics
description: Unified workflow for managing Oracle GoldenGate cloud deployments in OCI. Combines the OCI Cloud Service API with Stream Analytics for cloud platform administrators managing deployment lifecycle, connections, pipelines, backups, and stream analytics in Oracle Cloud.
layout: capability
name: Oracle GoldenGate Cloud Management
operations:
- description: List OCI GoldenGate deployments
  method: GET
  name: list-deployments
  path: /v1/deployments
- description: Create a new OCI deployment
  method: POST
  name: create-deployment
  path: /v1/deployments
- description: Get deployment details
  method: GET
  name: get-deployment
  path: /v1/deployments/{deploymentId}
- description: List database and service connections
  method: GET
  name: list-connections
  path: /v1/connections
- description: List data replication pipelines
  method: GET
  name: list-pipelines
  path: /v1/pipelines
- description: List deployment backups
  method: GET
  name: list-backups
  path: /v1/backups
- description: List GGSA stream analytics pipelines
  method: GET
  name: list-stream-pipelines
  path: /v1/stream-pipelines
- description: List asynchronous work requests
  method: GET
  name: list-work-requests
  path: /v1/work-requests
personas: []
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
search_terms:
- list data replication pipelines
- connection management
- list backups
- real-time replication
- unpublish stream pipeline
- check status of an asynchronous operation
- upgrade an oci deployment to a newer version
- list ggsa stream analytics pipelines
- data replication pipelines
- start pipeline
- create deployment
- list work requests
- start a stopped oci deployment
- start a stopped pipeline
- create a new oci deployment
- stop deployment
- publish stream pipeline
- oci
- list oci goldengate deployments
- create pipeline
- oracle goldengate
- unpublish a stream analytics pipeline
- database
- individual deployment operations
- data synchronization
- create a deployment backup
- stream analytics pipeline management
- create backup
- get deployment
- restore a deployment from a backup
- list connections
- create a new data replication pipeline
- cdc
- list asynchronous work requests
- get work request
- stop a running oci deployment
- list stream pipelines
- create a new oci goldengate deployment
- list deployments
- oci goldengate deployment lifecycle management
- list database and service connections
- publish a stream analytics pipeline to the spark runtime
- enterprise
- upgrade deployment
- get deployment details
- start deployment
- cloud management
- deployment backup management
- restore deployment
- list oci goldengate deployments in a compartment
- list pipelines
- list deployment backups
- create a new connection for a source or target system
- platform administration
- create connection
- get details of a specific oci deployment
- async operation tracking
- data integration
slug: cloud-management
tags:
- Oracle GoldenGate
- OCI
- Cloud Management
- Platform Administration
tools:
- description: List OCI GoldenGate deployments in a compartment
  hints:
    openWorld: true
    readOnly: true
  name: list-deployments
- description: Get details of a specific OCI deployment
  hints:
    openWorld: true
    readOnly: true
  name: get-deployment
- description: Create a new OCI GoldenGate deployment
  hints:
    readOnly: false
  name: create-deployment
- description: Start a stopped OCI deployment
  hints:
    readOnly: false
  name: start-deployment
- description: Stop a running OCI deployment
  hints:
    readOnly: false
  name: stop-deployment
- description: Upgrade an OCI deployment to a newer version
  hints:
    readOnly: false
  name: upgrade-deployment
- description: List database and service connections
  hints:
    openWorld: true
    readOnly: true
  name: list-connections
- description: Create a new connection for a source or target system
  hints:
    readOnly: false
  name: create-connection
- description: List data replication pipelines
  hints:
    openWorld: true
    readOnly: true
  name: list-pipelines
- description: Create a new data replication pipeline
  hints:
    readOnly: false
  name: create-pipeline
- description: Start a stopped pipeline
  hints:
    readOnly: false
  name: start-pipeline
- description: List deployment backups
  hints:
    openWorld: true
    readOnly: true
  name: list-backups
- description: Create a deployment backup
  hints:
    readOnly: false
  name: create-backup
- description: Restore a deployment from a backup
  hints:
    readOnly: false
  name: restore-deployment
- description: List GGSA stream analytics pipelines
  hints:
    openWorld: true
    readOnly: true
  name: list-stream-pipelines
- description: Publish a stream analytics pipeline to the Spark runtime
  hints:
    readOnly: false
  name: publish-stream-pipeline
- description: Unpublish a stream analytics pipeline
  hints:
    readOnly: false
  name: unpublish-stream-pipeline
- description: Check status of an asynchronous operation
  hints:
    openWorld: true
    readOnly: true
  name: get-work-request
---
