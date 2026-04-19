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
- list workspaces
- grafana
- create grafana workspace
- get configuration and authentication details of a grafana workspace
- create workspace
- list grafana workspaces
- create an api key for programmatic grafana workspace access
- create a new grafana workspace for observability dashboards
- visualization
- grafana workspaces
- monitoring
- Operations Engineer
- aws
- get workspace details
- amazon
- create workspace api key
- update workspace
- Platform Engineer
- update grafana workspace configuration, authentication, or data sources
- observability
- list all grafana workspaces for observability dashboards
- dashboards
- create a workspace
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
