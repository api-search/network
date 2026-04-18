---
consumed_apis:
- loggly
- papertrail
description: Workflow for centralized log management combining Loggly cloud log aggregation with Papertrail log search and system management for DevOps and operations teams.
layout: capability
name: SolarWinds Log Management
operations:
- description: Search Loggly log events
  method: GET
  name: loggly-search-events
  path: /v1/loggly-search
- description: Search Papertrail log events
  method: GET
  name: papertrail-search-events
  path: /v1/papertrail-search
- description: List log-sending systems
  method: GET
  name: list-systems
  path: /v1/systems
personas: []
provider_name: SolarWinds
provider_slug: solarwinds
search_terms:
- papertrail list saved searches
- get loggly account information
- loggly search events
- papertrail log search
- loggly get events
- list papertrail system groups
- papertrail list groups
- loggly
- list systems
- loggly log search
- search papertrail log events
- solarwinds
- list log-sending systems
- observability
- retrieve loggly search results by rsid
- papertrail system management
- infrastructure
- papertrail search events
- loggly search
- list papertrail saved searches
- log management
- ip address management
- list papertrail log-sending systems
- application monitoring
- network monitoring
- it management
- database monitoring
- loggly get account info
- papertrail list systems
- itsm
- papertrail search
- papertrail
- search loggly log events
slug: log-management
tags:
- SolarWinds
- Log Management
- Loggly
- Papertrail
tools:
- description: Search Loggly log events
  hints:
    readOnly: true
  name: loggly-search
- description: Retrieve Loggly search results by RSID
  hints:
    readOnly: true
  name: loggly-get-events
- description: Get Loggly account information
  hints:
    readOnly: true
  name: loggly-get-account-info
- description: Search Papertrail log events
  hints:
    readOnly: true
  name: papertrail-search
- description: List Papertrail log-sending systems
  hints:
    readOnly: true
  name: papertrail-list-systems
- description: List Papertrail system groups
  hints:
    readOnly: true
  name: papertrail-list-groups
- description: List Papertrail saved searches
  hints:
    readOnly: true
  name: papertrail-list-saved-searches
---
