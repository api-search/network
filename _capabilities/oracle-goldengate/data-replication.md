---
consumed_apis:
- goldengate-rest
- goldengate-big-data
- goldengate-data-streams
description: Unified workflow for managing real-time data replication across on-premises and cloud environments. Combines the core GoldenGate REST API, Big Data API, and Data Streams API for data integration engineers managing CDC pipelines, extract/replicat processes, and data distribution.
layout: capability
name: Oracle GoldenGate Data Replication
operations:
- description: List all Extract processes
  method: GET
  name: list-extracts
  path: /v1/extracts
- description: Create a new Extract process
  method: POST
  name: create-extract
  path: /v1/extracts
- description: Get a specific Extract process
  method: GET
  name: get-extract
  path: /v1/extracts/{extract}
- description: Delete an Extract process
  method: DELETE
  name: delete-extract
  path: /v1/extracts/{extract}
- description: List all Replicat processes
  method: GET
  name: list-replicats
  path: /v1/replicats
- description: List all big data Replicat processes
  method: GET
  name: list-big-data-replicats
  path: /v1/big-data-replicats
- description: List all data streams
  method: GET
  name: list-data-streams
  path: /v1/data-streams
- description: List available big data target types
  method: GET
  name: list-data-target-types
  path: /v1/data-target-types
- description: List credential domains
  method: GET
  name: list-credential-domains
  path: /v1/credentials
- description: List distribution paths
  method: GET
  name: list-distribution-paths
  path: /v1/distribution-paths
- description: Get service health details
  method: GET
  name: get-service-health
  path: /v1/health
personas: []
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
search_terms:
- list extracts
- distribution path management
- service health
- create a new extract process
- get performance metrics for all running processes
- get configuration of a specific data stream
- data synchronization
- core issue extract command
- core issue replicat command
- get details of a specific replicat process
- core create extract
- create a new data stream for downstream distribution
- list data distribution paths
- oracle goldengate
- list data streams
- core list extracts
- core list replicats
- replicat process management
- execute a ggsci-style goldengate command
- issue a command (start, stop, kill) to an extract
- execute command
- list all data streams
- core get extract
- data replication
- enterprise
- core get replicat
- list all extract processes from the core goldengate deployment
- cdc
- list available big data target types
- extract process management across core and big data deployments
- create a new replicat process
- list replicats
- data integration
- get details of a specific extract process
- get a big data replicat process
- list all replicat processes
- available big data target types
- real-time replication
- list all configured data streams
- delete an extract process
- create data stream
- list credential domains
- issue a command to a replicat process
- get a specific extract process
- individual extract operations
- get service health
- bigdata list replicats
- list available big data target types (kafka, hdfs, mongodb, etc.)
- get service health details
- list process metrics
- list distribution paths
- get data stream
- list big data replicats
- list data target types
- bigdata get replicat
- data stream management
- big data replicat processes
- get extract
- core create replicat
- database
- credential store management
- list all extract processes
- list credential store domains
- list all big data replicat processes
- create extract
- delete extract
slug: data-replication
tags:
- Oracle GoldenGate
- Data Replication
- CDC
- Data Integration
tools:
- description: List all Extract processes from the core GoldenGate deployment
  hints:
    openWorld: true
    readOnly: true
  name: core-list-extracts
- description: Get details of a specific Extract process
  hints:
    openWorld: true
    readOnly: true
  name: core-get-extract
- description: Create a new Extract process
  hints:
    readOnly: false
  name: core-create-extract
- description: Issue a command (START, STOP, KILL) to an Extract
  hints:
    readOnly: false
  name: core-issue-extract-command
- description: List all Replicat processes
  hints:
    openWorld: true
    readOnly: true
  name: core-list-replicats
- description: Get details of a specific Replicat process
  hints:
    openWorld: true
    readOnly: true
  name: core-get-replicat
- description: Create a new Replicat process
  hints:
    readOnly: false
  name: core-create-replicat
- description: Issue a command to a Replicat process
  hints:
    readOnly: false
  name: core-issue-replicat-command
- description: List all big data Replicat processes
  hints:
    openWorld: true
    readOnly: true
  name: bigdata-list-replicats
- description: Get a big data Replicat process
  hints:
    openWorld: true
    readOnly: true
  name: bigdata-get-replicat
- description: List available big data target types (Kafka, HDFS, MongoDB, etc.)
  hints:
    openWorld: true
    readOnly: true
  name: list-data-target-types
- description: List all configured data streams
  hints:
    openWorld: true
    readOnly: true
  name: list-data-streams
- description: Get configuration of a specific data stream
  hints:
    openWorld: true
    readOnly: true
  name: get-data-stream
- description: Create a new data stream for downstream distribution
  hints:
    readOnly: false
  name: create-data-stream
- description: List data distribution paths
  hints:
    openWorld: true
    readOnly: true
  name: list-distribution-paths
- description: List credential store domains
  hints:
    openWorld: true
    readOnly: true
  name: list-credential-domains
- description: Execute a GGSCI-style GoldenGate command
  hints:
    openWorld: true
    readOnly: false
  name: execute-command
- description: Get performance metrics for all running processes
  hints:
    openWorld: true
    readOnly: true
  name: list-process-metrics
---
