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
- mute a monitor
- get a monitor
- validate a monitor
- create monitor
- mute a synthetic test monitor
- unmute a synthetic test monitor
- listMonitors
- analytics
- validate a synthetic monitor configuration
- dashboards
- mute synthetic alert monitors
- datadog
- unmute monitor
- update monitor
- deleteMonitor
- SetOnDemandConcurrencyCap
- getMonitor
- t1
- synthetics
- list monitors including synthetic alert monitors
- muteMonitor
- get concurrency cap
- validate synthetic monitor configurations
- update a synthetics alert monitor
- set the on-demand concurrency cap
- monitors
- delete monitor
- list monitors
- synthetic testing
- set concurrency cap
- get a monitor by id
- createMonitor
- update a monitor
- create a synthetics alert monitor
- validate monitor
- updateMonitor
- visualizations
- GetOnDemandConcurrencyCap
- monitor management for synthetic alerts
- synthetics concurrency settings
- monitoring
- get the on-demand concurrency cap
- get the synthetics on-demand concurrency cap
- mute monitor
- platform
- delete a monitor
- validateMonitor
- set a new synthetics on-demand concurrency cap
- qa
- get monitor
- individual monitor operations
- create a monitor
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
