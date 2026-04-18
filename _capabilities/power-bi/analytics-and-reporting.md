---
consumed_apis:
- power-bi
description: Unified workflow for Power BI analytics operations including dataset management, report creation and distribution, dashboard monitoring, workspace administration, and gateway configuration. Used by BI analysts, report developers, and Power BI administrators.
layout: capability
name: Power BI Analytics and Reporting
operations:
- description: List all datasets
  method: GET
  name: list-datasets
  path: /v1/datasets
- description: Create a dataset
  method: POST
  name: create-dataset
  path: /v1/datasets
- description: Get dataset details
  method: GET
  name: get-dataset
  path: /v1/datasets/{datasetId}
- description: Delete a dataset
  method: DELETE
  name: delete-dataset
  path: /v1/datasets/{datasetId}
- description: List all reports
  method: GET
  name: list-reports
  path: /v1/reports
- description: List all dashboards
  method: GET
  name: list-dashboards
  path: /v1/dashboards
- description: Create a dashboard
  method: POST
  name: create-dashboard
  path: /v1/dashboards
- description: List workspaces
  method: GET
  name: list-workspaces
  path: /v1/workspaces
- description: List gateways
  method: GET
  name: list-gateways
  path: /v1/gateways
personas: []
provider_name: Power BI
provider_slug: power-bi
search_terms:
- list reports
- list all power bi datasets
- get gateway
- create a dashboard
- get dataset details by id
- get dashboard
- analytics
- create a new workspace
- dashboards
- business intelligence
- create a dataset
- create a new dataset
- get dataset refresh history
- workspace management
- delete a dataset
- create dataset
- individual dataset operations
- get datasources
- list workspaces
- export report
- list gateways
- get report
- get pages for a report
- create a new dashboard
- power bi
- list all datasets
- export a report
- dashboard management
- get tiles for a dashboard
- data analysis
- trigger a dataset refresh
- dataset management
- clone report
- get dashboard details
- get dataset
- get dataset details
- get report details by id
- report management
- get report pages
- create dashboard
- get refresh history
- clone a report
- get dashboard tiles
- list dashboards
- get workspace users
- list data gateways
- visualization
- list all dashboards
- gateway management
- get gateway details
- list workspace users
- list all workspaces
- get gateway datasources
- list all reports
- create workspace
- list datasets
- refresh dataset
- list all power bi reports
- delete dataset
- reporting
- get datasources for a dataset
slug: analytics-and-reporting
tags:
- Power BI
- Analytics
- Business Intelligence
- Reporting
tools:
- description: List all Power BI datasets
  hints:
    openWorld: true
    readOnly: true
  name: list-datasets
- description: Get dataset details by ID
  hints:
    readOnly: true
  name: get-dataset
- description: Create a new dataset
  hints:
    readOnly: false
  name: create-dataset
- description: Delete a dataset
  hints:
    destructive: true
    idempotent: true
  name: delete-dataset
- description: Trigger a dataset refresh
  hints:
    readOnly: false
  name: refresh-dataset
- description: Get dataset refresh history
  hints:
    readOnly: true
  name: get-refresh-history
- description: Get datasources for a dataset
  hints:
    readOnly: true
  name: get-datasources
- description: List all Power BI reports
  hints:
    openWorld: true
    readOnly: true
  name: list-reports
- description: Get report details by ID
  hints:
    readOnly: true
  name: get-report
- description: Clone a report
  hints:
    readOnly: false
  name: clone-report
- description: Export a report
  hints:
    readOnly: true
  name: export-report
- description: Get pages for a report
  hints:
    readOnly: true
  name: get-report-pages
- description: List all dashboards
  hints:
    openWorld: true
    readOnly: true
  name: list-dashboards
- description: Get dashboard details
  hints:
    readOnly: true
  name: get-dashboard
- description: Create a new dashboard
  hints:
    readOnly: false
  name: create-dashboard
- description: Get tiles for a dashboard
  hints:
    readOnly: true
  name: get-dashboard-tiles
- description: List all workspaces
  hints:
    openWorld: true
    readOnly: true
  name: list-workspaces
- description: Create a new workspace
  hints:
    readOnly: false
  name: create-workspace
- description: List workspace users
  hints:
    readOnly: true
  name: get-workspace-users
- description: List data gateways
  hints:
    readOnly: true
  name: list-gateways
- description: Get gateway details
  hints:
    readOnly: true
  name: get-gateway
- description: Get gateway datasources
  hints:
    readOnly: true
  name: get-gateway-datasources
---
