---
consumed_apis:
- dd-synthetics
- dd-monitors
description: Unified workflow for synthetic testing combining synthetics concurrency management and monitors. Used by QA engineers and SREs for managing synthetic test execution capacity and monitoring test results.
layout: capability
name: Datadog Synthetic Testing
operations:
- description: Get the on-demand concurrency cap
  method: GET
  name: GetOnDemandConcurrencyCap
  path: /v1/synthetics/concurrency-cap
- description: Set the on-demand concurrency cap
  method: POST
  name: SetOnDemandConcurrencyCap
  path: /v1/synthetics/concurrency-cap
- description: List monitors
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
- description: Validate a monitor
  method: POST
  name: validateMonitor
  path: /v1/monitors/validate
personas: []
provider_name: Datadog
provider_slug: datadog
search_terms:
- get monitor
- listMonitors
- synthetic testing
- mute a monitor
- get the on-demand concurrency cap
- mute monitor
- set the on-demand concurrency cap
- list monitors including synthetic alert monitors
- validate a monitor
- list monitors
- deleteMonitor
- visualizations
- monitors
- monitor management for synthetic alerts
- individual monitor operations
- create monitor
- set a new synthetics on-demand concurrency cap
- delete monitor
- get concurrency cap
- platform
- qa
- GetOnDemandConcurrencyCap
- update monitor
- get the synthetics on-demand concurrency cap
- datadog
- createMonitor
- validate monitor
- muteMonitor
- create a monitor
- unmute monitor
- getMonitor
- update a synthetics alert monitor
- monitoring
- set concurrency cap
- mute a synthetic test monitor
- update a monitor
- validate a synthetic monitor configuration
- synthetics
- updateMonitor
- unmute a synthetic test monitor
- analytics
- synthetics concurrency settings
- t1
- SetOnDemandConcurrencyCap
- delete a monitor
- dashboards
- get a monitor by id
- validate synthetic monitor configurations
- validateMonitor
- mute synthetic alert monitors
- create a synthetics alert monitor
- get a monitor
slug: synthetic-testing
tags:
- Datadog
- Synthetic Testing
- Synthetics
- Monitors
- QA
tools:
- description: Get the synthetics on-demand concurrency cap
  hints:
    readOnly: true
  name: get-concurrency-cap
- description: Set a new synthetics on-demand concurrency cap
  hints: {}
  name: set-concurrency-cap
- description: List monitors including synthetic alert monitors
  hints:
    readOnly: true
  name: list-monitors
- description: Get a monitor by ID
  hints:
    readOnly: true
  name: get-monitor
- description: Create a synthetics alert monitor
  hints: {}
  name: create-monitor
- description: Update a synthetics alert monitor
  hints:
    idempotent: true
  name: update-monitor
- description: Delete a monitor
  hints:
    destructive: true
  name: delete-monitor
- description: Mute a synthetic test monitor
  hints: {}
  name: mute-monitor
- description: Unmute a synthetic test monitor
  hints: {}
  name: unmute-monitor
- description: Validate a synthetic monitor configuration
  hints:
    readOnly: true
  name: validate-monitor
---
