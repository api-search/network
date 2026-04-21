---
consumed_apis:
- dms
description: Workflow capability for database engineers and cloud architects to manage end-to-end database migrations using AWS Database Migration Service. Covers replication instance provisioning, source and target endpoint configuration, replication task management, migration monitoring, and schema conversion support.
layout: capability
name: Amazon DMS Database Migration Management
operations:
- description: List all replication instances
  method: GET
  name: describe-replication-instances
  path: /v1/replication-instances
- description: Create a new replication instance
  method: POST
  name: create-replication-instance
  path: /v1/replication-instances
- description: List all endpoints
  method: GET
  name: describe-endpoints
  path: /v1/endpoints
- description: Create a source or target endpoint
  method: POST
  name: create-endpoint
  path: /v1/endpoints
- description: List all replication tasks
  method: GET
  name: describe-replication-tasks
  path: /v1/tasks
- description: Create a new replication task
  method: POST
  name: create-replication-task
  path: /v1/tasks
- description: List registered SSL certificates
  method: GET
  name: describe-certificates
  path: /v1/certificates
personas: []
provider_name: Amazon DMS
provider_slug: amazon-dms
search_terms:
- describe replication tasks
- migration
- create a new replication task
- list connections between replication instances and endpoints
- describe connections
- list per-table migration statistics for a replication task
- Database Engineer
- list all replication instances
- stop replication task
- describe endpoints
- list all endpoints
- data replication
- describe certificates
- list replication tasks and their current migration status
- describe event subscriptions
- Cloud Architect
- create a new replication task to migrate data between source and target
- list registered ssl certificates
- create a new dms replication instance to process migration tasks
- list sns event subscriptions for migration notifications
- replication instances for migration processing
- list all dms replication instances used for database migration processing
- list all replication tasks
- delete replication instance
- delete a dms replication instance
- start or resume a database migration replication task
- list ssl certificates for encrypted database migration connections
- amazon dms
- create replication task
- database migration
- end-to-end database migration lifecycle using aws dms
- test connection
- source and target database endpoints
- test the connection between a replication instance and an endpoint
- stop a running database migration replication task
- cloud architect designing database migration strategy and infrastructure
- create a new replication instance
- source and target database endpoint management
- describe replication instances
- create endpoint
- aws
- describe table statistics
- database
- create replication instance
- replication tasks for migration
- start replication task
- database engineer managing migration projects and monitoring replication tasks
- create a source or target database endpoint for migration
- replication instances and network configuration
- replication task lifecycle and monitoring
- ssl certificates for encrypted migration
- create a source or target endpoint
- list all source and target database endpoints configured for migration
slug: database-migration-management
tags:
- Amazon DMS
- Database Migration
- Data Replication
- AWS
tools:
- description: List all DMS replication instances used for database migration processing
  hints:
    openWorld: true
    readOnly: true
  name: describe-replication-instances
- description: Create a new DMS replication instance to process migration tasks
  hints:
    destructive: false
    readOnly: false
  name: create-replication-instance
- description: Delete a DMS replication instance
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-replication-instance
- description: List all source and target database endpoints configured for migration
  hints:
    openWorld: true
    readOnly: true
  name: describe-endpoints
- description: Create a source or target database endpoint for migration
  hints:
    destructive: false
    readOnly: false
  name: create-endpoint
- description: Test the connection between a replication instance and an endpoint
  hints:
    destructive: false
    readOnly: false
  name: test-connection
- description: List replication tasks and their current migration status
  hints:
    openWorld: true
    readOnly: true
  name: describe-replication-tasks
- description: Create a new replication task to migrate data between source and target
  hints:
    destructive: false
    readOnly: false
  name: create-replication-task
- description: Start or resume a database migration replication task
  hints:
    destructive: false
    readOnly: false
  name: start-replication-task
- description: Stop a running database migration replication task
  hints:
    destructive: false
    readOnly: false
  name: stop-replication-task
- description: List per-table migration statistics for a replication task
  hints:
    openWorld: true
    readOnly: true
  name: describe-table-statistics
- description: List connections between replication instances and endpoints
  hints:
    openWorld: true
    readOnly: true
  name: describe-connections
- description: List SSL certificates for encrypted database migration connections
  hints:
    openWorld: true
    readOnly: true
  name: describe-certificates
- description: List SNS event subscriptions for migration notifications
  hints:
    openWorld: true
    readOnly: true
  name: describe-event-subscriptions
---
