---
consumed_apis:
- airbyte
description: Unified workflow capability for managing Airbyte data integration pipelines — sources, destinations, connections, and sync jobs. Used by data engineers and platform teams.
layout: capability
name: Airbyte Data Pipeline Management
operations:
- description: List all data sources.
  method: GET
  name: list-sources
  path: /v1/sources
- description: Create a new data source.
  method: POST
  name: create-source
  path: /v1/sources
- description: List all destinations.
  method: GET
  name: list-destinations
  path: /v1/destinations
- description: Create a new destination.
  method: POST
  name: create-destination
  path: /v1/destinations
- description: List all connections.
  method: GET
  name: list-connections
  path: /v1/connections
- description: Create a new connection.
  method: POST
  name: create-connection
  path: /v1/connections
- description: List sync jobs.
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: Trigger a sync job.
  method: POST
  name: trigger-job
  path: /v1/jobs
- description: List workspaces.
  method: GET
  name: list-workspaces
  path: /v1/workspaces
personas: []
provider_name: Airbyte
provider_slug: airbyte
search_terms:
- list sources
- list sync jobs.
- trigger job
- Platform Admin
- trigger sync
- create a new airbyte data destination connector.
- list jobs
- manage source-to-destination connections.
- trigger a sync job.
- list sync jobs
- etl
- list all connections.
- create a new connection.
- list workspaces
- list airbyte workspaces.
- list all data sources.
- data engineering
- connectors
- create a new destination.
- list airbyte connections between sources and destinations.
- delete source
- elt
- manage data source connectors.
- open source
- Data Engineer
- manage data destination connectors.
- create an airbyte connection between a source and destination.
- manage airbyte sources, destinations, connections, and sync jobs.
- create destination
- create a new airbyte data source connector.
- list connections
- manage workspaces.
- monitoring and operating sync pipelines.
- airbyte
- check the status of an airbyte sync job.
- list all destinations.
- list all airbyte data source connectors.
- data pipeline
- create a new data source.
- list all airbyte data destination connectors.
- trigger an airbyte sync job for a connection.
- data integration
- list airbyte sync jobs with optional status filtering.
- create connection
- list workspaces.
- list destinations
- builds and maintains data pipelines using airbyte connectors and connections.
- create source
- get job status
- data
- manages airbyte workspaces, users, permissions, and organizational settings.
- monitor and trigger sync jobs.
- moving data between sources and destinations.
- delete an airbyte source connector.
- user, workspace, and organizational management.
slug: data-pipeline-management
tags:
- Airbyte
- Data Integration
- ETL
- ELT
- Data Pipeline
- Data Engineering
tools:
- description: List all Airbyte data source connectors.
  hints:
    openWorld: true
    readOnly: true
  name: list-sources
- description: Create a new Airbyte data source connector.
  hints:
    readOnly: false
  name: create-source
- description: List all Airbyte data destination connectors.
  hints:
    openWorld: true
    readOnly: true
  name: list-destinations
- description: Create a new Airbyte data destination connector.
  hints:
    readOnly: false
  name: create-destination
- description: List Airbyte connections between sources and destinations.
  hints:
    openWorld: true
    readOnly: true
  name: list-connections
- description: Create an Airbyte connection between a source and destination.
  hints:
    readOnly: false
  name: create-connection
- description: List Airbyte sync jobs with optional status filtering.
  hints:
    openWorld: true
    readOnly: true
  name: list-sync-jobs
- description: Trigger an Airbyte sync job for a connection.
  hints:
    readOnly: false
  name: trigger-sync
- description: Check the status of an Airbyte sync job.
  hints:
    readOnly: true
  name: get-job-status
- description: List Airbyte workspaces.
  hints:
    readOnly: true
  name: list-workspaces
- description: Delete an Airbyte source connector.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-source
---
