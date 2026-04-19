---
consumed_apis:
- entities-v2
- metrics-v2
- events-v2
description: Entity discovery and topology mapping workflow combining entities, metrics, and events for developers understanding service dependencies and infrastructure layout.
layout: capability
name: Dynatrace Entity And Topology
operations:
- description: List entities matching a selector
  method: GET
  name: list-entities
  path: /v1/entities
- description: Get entity details including topology relationships
  method: GET
  name: get-entity
  path: /v1/entities/{entityId}
- description: List all entity types
  method: GET
  name: list-entity-types
  path: /v1/entity-types
- description: Get a specific entity type definition
  method: GET
  name: get-entity-type
  path: /v1/entity-types/{type}
- description: Look up an entity by display name and type
  method: POST
  name: lookup-entity
  path: /v1/entities/lookup
- description: Query metric data for entities
  method: GET
  name: query-metric-data
  path: /v1/metrics/query
- description: List events for entities
  method: GET
  name: list-events
  path: /v1/events
- description: Ingest a deployment or custom event
  method: POST
  name: ingest-event
  path: /v1/events/ingest
personas: []
provider_name: Dynatrace
provider_slug: dynatrace
search_terms:
- look up entity by name
- developer
- get entity
- get entity type definition
- look up an entity by its display name and type
- application performance monitoring
- entity management
- query metrics for entity performance
- ingest deployment events
- ingest a deployment or custom event for an entity
- look up an entity by display name and type
- list all available entity types in the environment
- get entity type
- observability
- list entities
- query metric data
- application security
- ai operations
- query entity types
- topology
- analytics
- dynatrace
- get the definition of a specific entity type
- list entity types
- ingest event
- list events
- digital experience management
- list entities matching a selector
- query monitored entities
- get a specific entity type definition
- query metric data points for entities
- list events affecting entities
- automation
- lookup entity
- ingest a deployment or custom event
- list all entity types
- query entity events
- list monitored entities matching a selector expression
- cloud monitoring
- intelligence
- query metric data for entities
- get entity details including topology relationships
- apm
- list events for entities
- infrastructure
- get entity details with relationships
slug: entity-and-topology
tags:
- Dynatrace
- Entity Management
- Topology
- Developer
- Infrastructure
tools:
- description: List monitored entities matching a selector expression
  hints:
    openWorld: true
    readOnly: true
  name: list-entities
- description: Get entity details including topology relationships
  hints:
    openWorld: true
    readOnly: true
  name: get-entity
- description: List all available entity types in the environment
  hints:
    openWorld: true
    readOnly: true
  name: list-entity-types
- description: Get the definition of a specific entity type
  hints:
    openWorld: true
    readOnly: true
  name: get-entity-type
- description: Look up an entity by its display name and type
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: lookup-entity
- description: Query metric data points for entities
  hints:
    openWorld: true
    readOnly: true
  name: query-metric-data
- description: List events affecting entities
  hints:
    openWorld: true
    readOnly: true
  name: list-events
- description: Ingest a deployment or custom event for an entity
  hints:
    openWorld: true
    readOnly: false
  name: ingest-event
---
