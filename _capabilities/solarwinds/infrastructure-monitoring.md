---
consumed_apis:
- orion
- pingdom
description: Workflow for monitoring network infrastructure and website uptime combining Orion Platform SWQL queries with Pingdom synthetic monitoring for network and IT operations teams.
layout: capability
name: SolarWinds Infrastructure Monitoring
operations:
- description: Execute a SWQL query
  method: GET
  name: query-swis
  path: /v1/query
- description: List Pingdom checks
  method: GET
  name: list-checks
  path: /v1/checks
- description: Get check details
  method: GET
  name: get-check
  path: /v1/checks
- description: Get check results
  method: GET
  name: get-results
  path: /v1/results
personas: []
provider_name: SolarWinds
provider_slug: solarwinds
search_terms:
- create check
- get check
- solarwinds
- network monitoring
- list pingdom uptime monitoring checks
- get pingdom performance summary
- infrastructure monitoring
- create a new pingdom monitoring check
- list pingdom checks
- uptime monitoring
- ip address management
- execute a swql query against orion platform
- get check details
- infrastructure
- get results
- itsm
- swql query execution
- create orion entity
- database monitoring
- query orion
- check results
- it management
- list checks
- execute a swql query
- get check results
- get pingdom check results
- query swis
- create a monitored entity in orion
- observability
- application monitoring
- log management
- uptime monitoring checks
- get pingdom check details
- get summary average
slug: infrastructure-monitoring
tags:
- SolarWinds
- Infrastructure Monitoring
- Network Monitoring
- Uptime Monitoring
tools:
- description: Execute a SWQL query against Orion Platform
  hints:
    readOnly: true
  name: query-orion
- description: Create a monitored entity in Orion
  hints:
    readOnly: false
  name: create-orion-entity
- description: List Pingdom uptime monitoring checks
  hints:
    readOnly: true
  name: list-checks
- description: Get Pingdom check details
  hints:
    readOnly: true
  name: get-check
- description: Create a new Pingdom monitoring check
  hints:
    readOnly: false
  name: create-check
- description: Get Pingdom check results
  hints:
    readOnly: true
  name: get-check-results
- description: Get Pingdom performance summary
  hints:
    readOnly: true
  name: get-summary-average
---
