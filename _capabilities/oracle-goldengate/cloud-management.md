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
- deployment backup management
- start deployment
- start a stopped pipeline
- enterprise
- list stream pipelines
- list asynchronous work requests
- oci goldengate deployment lifecycle management
- individual deployment operations
- list data replication pipelines
- get details of a specific oci deployment
- real-time replication
- create a new oci deployment
- publish a stream analytics pipeline to the spark runtime
- stop a running oci deployment
- create a new data replication pipeline
- publish stream pipeline
- list backups
- list pipelines
- create deployment
- unpublish stream pipeline
- list oci goldengate deployments in a compartment
- create backup
- get work request
- connection management
- get deployment
- unpublish a stream analytics pipeline
- upgrade an oci deployment to a newer version
- restore deployment
- get deployment details
- oci
- list connections
- stream analytics pipeline management
- list deployments
- async operation tracking
- create a new oci goldengate deployment
- create a deployment backup
- platform administration
- oracle goldengate
- check status of an asynchronous operation
- create a new connection for a source or target system
- data integration
- create connection
- data synchronization
- list deployment backups
- list oci goldengate deployments
- data replication pipelines
- start pipeline
- database
- create pipeline
- restore a deployment from a backup
- list database and service connections
- upgrade deployment
- start a stopped oci deployment
- stop deployment
- cloud management
- cdc
- list work requests
- list ggsa stream analytics pipelines
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
