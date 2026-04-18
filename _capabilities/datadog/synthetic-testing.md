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
- get a monitor by id
- unmute a synthetic test monitor
- get concurrency cap
- unmute monitor
- t1
- monitor management for synthetic alerts
- qa
- SetOnDemandConcurrencyCap
- create monitor
- mute monitor
- datadog
- create a synthetics alert monitor
- set the on-demand concurrency cap
- list monitors
- delete a monitor
- validate synthetic monitor configurations
- validateMonitor
- updateMonitor
- validate a monitor
- validate a synthetic monitor configuration
- set concurrency cap
- monitoring
- get the synthetics on-demand concurrency cap
- set a new synthetics on-demand concurrency cap
- create a monitor
- deleteMonitor
- mute a synthetic test monitor
- get monitor
- dashboards
- visualizations
- monitors
- analytics
- GetOnDemandConcurrencyCap
- platform
- createMonitor
- synthetic testing
- getMonitor
- synthetics concurrency settings
- mute a monitor
- get the on-demand concurrency cap
- delete monitor
- individual monitor operations
- validate monitor
- mute synthetic alert monitors
- update a monitor
- muteMonitor
- synthetics
- list monitors including synthetic alert monitors
- update a synthetics alert monitor
- listMonitors
- update monitor
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
