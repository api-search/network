---
consumed_apis:
- managed-grafana
description: Workflow capability for platform and operations teams to create and manage Grafana workspaces, dashboards, and access controls for observability on Amazon Managed Grafana.
layout: capability
name: Amazon Managed Grafana - Observability Dashboard Workflow
operations:
- description: List workspaces
  method: GET
  name: list-workspaces
  path: /v1/workspaces
- description: Create a workspace
  method: POST
  name: create-workspace
  path: /v1/workspaces
personas: []
provider_name: Amazon Managed Grafana
provider_slug: amazon-managed-grafana
search_terms:
- Platform Engineer
- get configuration and authentication details of a grafana workspace
- grafana
- create a new grafana workspace for observability dashboards
- list workspaces
- update grafana workspace configuration, authentication, or data sources
- amazon
- observability
- Operations Engineer
- create grafana workspace
- monitoring
- update workspace
- get workspace details
- create a workspace
- list all grafana workspaces for observability dashboards
- grafana workspaces
- create workspace api key
- list grafana workspaces
- dashboards
- create workspace
- aws
- create an api key for programmatic grafana workspace access
- visualization
slug: observability-dashboard-workflow
tags:
- Amazon
- Grafana
- Dashboards
- Monitoring
- Observability
tools:
- description: List all Grafana workspaces for observability dashboards
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: list-grafana-workspaces
- description: Create a new Grafana workspace for observability dashboards
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-grafana-workspace
- description: Get configuration and authentication details of a Grafana workspace
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-workspace-details
- description: Create an API key for programmatic Grafana workspace access
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-workspace-api-key
- description: Update Grafana workspace configuration, authentication, or data sources
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-workspace
---
