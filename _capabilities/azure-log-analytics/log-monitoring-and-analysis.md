---
consumed_apis:
- log-analytics-query
- log-analytics-management
- log-analytics-ingestion
description: Unified workflow for log monitoring and analysis combining the Query API for KQL-based data exploration, the Management API for workspace and saved search administration, and the Ingestion API for custom log data collection. Used by DevOps engineers, SOC analysts, and platform administrators.
layout: capability
name: Azure Log Analytics Log Monitoring and Analysis
operations:
- description: Execute a KQL query.
  method: POST
  name: execute-query
  path: /v1/queries
- description: List all workspaces.
  method: GET
  name: list-workspaces
  path: /v1/workspaces
- description: Get a workspace.
  method: GET
  name: get-workspace
  path: /v1/workspaces/{workspaceName}
- description: List saved searches.
  method: GET
  name: list-saved-searches
  path: /v1/saved-searches
- description: List all tables.
  method: GET
  name: list-tables
  path: /v1/tables
- description: Upload custom log entries.
  method: POST
  name: upload-logs
  path: /v1/ingest
personas: []
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
search_terms:
- list workspace tables.
- create saved search
- logging
- kql-based data exploration and saved query management.
- infrastructure and application monitoring through log analysis.
- analytics
- list all log analytics workspaces in a subscription.
- create or update a saved search in a workspace.
- SOC Analyst
- list all tables in a log analytics workspace.
- manage log analytics workspaces.
- log analytics
- create workspace
- list workspaces
- get workspace
- delete workspace
- execute kql queries against workspaces.
- get details of a specific log analytics workspace.
- DevOps Engineer
- manage saved kql queries.
- administrators managing workspaces, tables, and data collection configurations.
- cloud
- list all workspaces.
- delete a log analytics workspace.
- azure
- kql
- execute a kql query.
- execute query
- list tables
- send custom log data to a workspace via data collection rule.
- list saved searches.
- upload logs
- execute a kql query against a log analytics workspace.
- list saved searches in a workspace.
- create or update a log analytics workspace.
- engineers monitoring infrastructure and application health through log queries.
- list all tables.
- security analysts investigating incidents and threats through log data.
- send custom log data.
- upload custom log entries.
- monitoring
- security event analysis and custom security log ingestion.
- get a workspace.
- Platform Administrator
- get workspace details.
- unified workflow combining query, management, and ingestion apis for complete log monitoring and analysis.
- list saved searches
slug: log-monitoring-and-analysis
tags:
- Azure
- Log Analytics
- Monitoring
- Analytics
- KQL
tools:
- description: Execute a KQL query against a Log Analytics workspace.
  hints:
    openWorld: true
    readOnly: true
  name: execute-query
- description: List all Log Analytics workspaces in a subscription.
  hints:
    openWorld: true
    readOnly: true
  name: list-workspaces
- description: Get details of a specific Log Analytics workspace.
  hints:
    openWorld: true
    readOnly: true
  name: get-workspace
- description: Create or update a Log Analytics workspace.
  hints:
    idempotent: true
    readOnly: false
  name: create-workspace
- description: Delete a Log Analytics workspace.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-workspace
- description: List saved searches in a workspace.
  hints:
    openWorld: true
    readOnly: true
  name: list-saved-searches
- description: Create or update a saved search in a workspace.
  hints:
    idempotent: true
    readOnly: false
  name: create-saved-search
- description: List all tables in a Log Analytics workspace.
  hints:
    openWorld: true
    readOnly: true
  name: list-tables
- description: Send custom log data to a workspace via data collection rule.
  hints:
    idempotent: false
    readOnly: false
  name: upload-logs
---
