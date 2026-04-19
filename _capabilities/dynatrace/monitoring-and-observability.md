---
consumed_apis:
- metrics-v2
- log-monitoring-v2
- events-v2
- entities-v2
description: Unified monitoring and observability workflow combining metrics, logs, events, and entity data for ops engineers managing infrastructure health and performance.
layout: capability
name: Dynatrace Monitoring And Observability
operations:
- description: List all available metrics
  method: GET
  name: list-metrics
  path: /v1/metrics
- description: Get descriptor for a specific metric
  method: GET
  name: get-metric-descriptor
  path: /v1/metrics/{metricKey}
- description: Delete a custom metric
  method: DELETE
  name: delete-custom-metric
  path: /v1/metrics/{metricKey}
- description: Query metric data with selectors and time ranges
  method: GET
  name: query-metric-data
  path: /v1/metrics/query
- description: Ingest custom metrics via MINT protocol
  method: POST
  name: ingest-custom-metrics
  path: /v1/metrics/ingest
- description: Search logs using DQL queries
  method: GET
  name: search-logs
  path: /v1/logs/search
- description: Ingest logs into Grail
  method: POST
  name: ingest-logs
  path: /v1/logs/ingest
- description: Aggregate logs by dimensions
  method: GET
  name: aggregate-logs
  path: /v1/logs/aggregate
- description: Export logs for bulk retrieval
  method: GET
  name: export-logs
  path: /v1/logs/export
- description: List events
  method: GET
  name: list-events
  path: /v1/events
- description: List entities matching a selector
  method: GET
  name: list-entities
  path: /v1/entities
- description: Get entity details
  method: GET
  name: get-entity
  path: /v1/entities/{entityId}
personas: []
provider_name: Dynatrace
provider_slug: dynatrace
search_terms:
- search logs
- query metric data points
- query metric data points with selectors and time ranges
- ingest log records into dynatrace grail
- digital experience management
- list monitored entities matching a selector
- get entity
- aggregate log data grouped by specified fields
- get the descriptor for a specific metric
- intelligence
- aggregate logs
- list events from the dynatrace environment
- get entity details
- cloud monitoring
- aggregate logs by dimensions
- list all available metrics
- delete custom metric
- get metric descriptor
- export logs for bulk retrieval
- query metric data
- ingest logs into grail
- export log records for bulk retrieval
- list metrics
- export logs
- ai operations
- ingest custom metrics via mint protocol
- dynatrace
- search log records
- search log records using dql queries
- delete a custom metric
- monitoring
- list entities matching a selector
- search logs using dql queries
- list events
- ingest custom metric data points via mint protocol
- analytics
- query events
- get details of a specific monitored entity
- automation
- get descriptor for a specific metric
- application performance monitoring
- application security
- export log records
- observability
- delete a custom metric from the environment
- logs
- apm
- ops engineering
- list metric descriptors
- ingest custom metrics
- ingest log records
- list entities
- ingest logs
- aggregate log data
- query monitored entities
- metrics
- list all available metric descriptors
- query metric data with selectors and time ranges
slug: monitoring-and-observability
tags:
- Dynatrace
- Monitoring
- Observability
- Ops Engineering
- Metrics
- Logs
tools:
- description: List all available metric descriptors
  hints:
    openWorld: true
    readOnly: true
  name: list-metrics
- description: Get the descriptor for a specific metric
  hints:
    openWorld: true
    readOnly: true
  name: get-metric-descriptor
- description: Query metric data points with selectors and time ranges
  hints:
    openWorld: true
    readOnly: true
  name: query-metric-data
- description: Ingest custom metric data points via MINT protocol
  hints:
    openWorld: true
    readOnly: false
  name: ingest-custom-metrics
- description: Delete a custom metric from the environment
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-custom-metric
- description: Search log records using DQL queries
  hints:
    openWorld: true
    readOnly: true
  name: search-logs
- description: Ingest log records into Dynatrace Grail
  hints:
    openWorld: true
    readOnly: false
  name: ingest-logs
- description: Aggregate log data grouped by specified fields
  hints:
    openWorld: true
    readOnly: true
  name: aggregate-logs
- description: Export log records for bulk retrieval
  hints:
    openWorld: true
    readOnly: true
  name: export-logs
- description: List events from the Dynatrace environment
  hints:
    openWorld: true
    readOnly: true
  name: list-events
- description: List monitored entities matching a selector
  hints:
    openWorld: true
    readOnly: true
  name: list-entities
- description: Get details of a specific monitored entity
  hints:
    openWorld: true
    readOnly: true
  name: get-entity
---
