---
consumed_apis:
- dd-monitors
- dd-metrics
- dd-hosts
- dd-dashboards
description: Unified workflow for infrastructure monitoring and alerting combining monitors, metrics, hosts, and dashboards. Used by SREs and DevOps engineers for setting up alerts, querying metrics, tracking host health, and organizing dashboards.
layout: capability
name: Datadog Monitoring And Alerting
operations:
- description: List all monitors
  method: GET
  name: listMonitors
  path: /v1/monitors
- description: Create a monitor
  method: POST
  name: createMonitor
  path: /v1/monitors
- description: Get a monitor
  method: GET
  name: getMonitor
  path: /v1/monitors/{monitor_id}
- description: Update a monitor
  method: PUT
  name: updateMonitor
  path: /v1/monitors/{monitor_id}
- description: Delete a monitor
  method: DELETE
  name: deleteMonitor
  path: /v1/monitors/{monitor_id}
- description: Mute a monitor
  method: POST
  name: muteMonitor
  path: /v1/monitors/{monitor_id}/mute
- description: List active metrics
  method: GET
  name: listActiveMetrics
  path: /v1/metrics
- description: Query timeseries data
  method: POST
  name: queryMetricsTimeseries
  path: /v1/metrics/query/timeseries
- description: Submit metrics
  method: POST
  name: submitMetrics
  path: /v1/metrics/series
- description: Get hosts coverage
  method: GET
  name: GetCSMHostsAndContainersCoverageAnalysis
  path: /v1/hosts/coverage
- description: Get dashboards in a list
  method: GET
  name: GetDashboardListItems
  path: /v1/dashboard-lists/{dashboard_list_id}/dashboards
personas: []
provider_name: Datadog
provider_slug: datadog
search_terms:
- submitMetrics
- getMonitor
- list active metrics
- get monitor
- monitor management
- add dashboards to a dashboard list
- analytics
- listActiveMetrics
- get a monitor
- delete monitor
- active metrics
- t1
- listMonitors
- queryMetricsTimeseries
- create a monitor
- datadog
- unmute monitor
- list monitors
- createMonitor
- validate a monitor configuration
- individual monitor operations
- infrastructure
- host coverage
- query timeseries
- get hosts coverage
- dashboards
- create monitor
- query timeseries metric data
- mute a monitor to suppress notifications
- alerting
- mute a monitor
- get a monitor by id
- update monitor
- query scalar
- get csm hosts and containers coverage
- get dashboard list items
- get dashboards in a list
- create a new monitor
- unmute a monitor to resume notifications
- GetDashboardListItems
- GetCSMHostsAndContainersCoverageAnalysis
- edit an existing monitor
- platform
- add dashboard list items
- update a monitor
- submit metric data points
- mute monitor
- fetch dashboards in a dashboard list
- validate monitor
- list all monitors
- query timeseries data
- submit metrics
- query scalar metric data
- visualizations
- updateMonitor
- dashboard list items
- metrics
- deleteMonitor
- delete a monitor
- muteMonitor
- monitoring
slug: monitoring-and-alerting
tags:
- Datadog
- Monitoring
- Alerting
- Metrics
- Dashboards
- Infrastructure
tools:
- description: List all monitors
  hints:
    readOnly: true
  name: list-monitors
- description: Get a monitor by ID
  hints:
    readOnly: true
  name: get-monitor
- description: Create a new monitor
  hints: {}
  name: create-monitor
- description: Edit an existing monitor
  hints:
    idempotent: true
  name: update-monitor
- description: Delete a monitor
  hints:
    destructive: true
  name: delete-monitor
- description: Mute a monitor to suppress notifications
  hints: {}
  name: mute-monitor
- description: Unmute a monitor to resume notifications
  hints: {}
  name: unmute-monitor
- description: Validate a monitor configuration
  hints:
    readOnly: true
  name: validate-monitor
- description: Submit metric data points
  hints: {}
  name: submit-metrics
- description: Query timeseries metric data
  hints:
    readOnly: true
  name: query-timeseries
- description: Query scalar metric data
  hints:
    readOnly: true
  name: query-scalar
- description: List active metrics
  hints:
    readOnly: true
  name: list-active-metrics
- description: Get CSM hosts and containers coverage
  hints:
    readOnly: true
  name: get-hosts-coverage
- description: Fetch dashboards in a dashboard list
  hints:
    readOnly: true
  name: get-dashboard-list-items
- description: Add dashboards to a dashboard list
  hints: {}
  name: add-dashboard-list-items
---
