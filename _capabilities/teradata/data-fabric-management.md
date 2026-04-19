---
consumed_apis:
- querygrid-manager
- query-service
description: Workflow capability for managing Teradata's data fabric infrastructure. Combines QueryGrid Manager for fabric configuration with Query Service for validating cross-system connectivity. Used by data engineers and platform administrators.
layout: capability
name: Teradata Data Fabric Management
operations:
- description: List all data centers.
  method: GET
  name: list-data-centers
  path: /v1/data-centers
- description: List all registered systems.
  method: GET
  name: list-systems
  path: /v1/systems
- description: List all bridges.
  method: GET
  name: list-bridges
  path: /v1/bridges
- description: List all current issues.
  method: GET
  name: list-issues
  path: /v1/issues
personas: []
provider_name: Teradata
provider_slug: teradata
search_terms:
- list all data fabric configurations.
- execute sql queries and analytics.
- teradata
- sql
- Application Developer
- machine learning
- list all connectors for system integration.
- manages data fabric infrastructure and cross-system connectivity.
- list connectors
- list data centers
- data fabric
- health monitoring and issue detection.
- data management
- list fabrics
- list all bridges connecting systems.
- run a diagnostic check on querygrid systems.
- issue monitoring.
- list all current issues in the querygrid environment.
- Platform Administrator
- database
- administration
- data warehousing
- list all current issues.
- system and fabric configuration management.
- analytics
- run diagnostic check
- administers querygrid systems, nodes, and software.
- list all configured data centers.
- bridge management.
- list all registered systems in querygrid.
- cloud
- Data Engineer
- Data Analyst
- enterprise
- executes queries and analyzes data across vantage systems.
- manage querygrid data fabric infrastructure.
- data center management.
- list all data centers.
- list systems
- list all registered systems.
- integrates applications with teradata via rest apis.
- list issues
- sql query execution and session management.
- configuration
- list bridges
- system management.
- list all bridges.
slug: data-fabric-management
tags:
- Teradata
- Data Fabric
- Configuration
- Administration
tools:
- description: List all configured data centers.
  hints:
    readOnly: true
  name: list-data-centers
- description: List all registered systems in QueryGrid.
  hints:
    readOnly: true
  name: list-systems
- description: List all bridges connecting systems.
  hints:
    readOnly: true
  name: list-bridges
- description: List all connectors for system integration.
  hints:
    readOnly: true
  name: list-connectors
- description: List all data fabric configurations.
  hints:
    readOnly: true
  name: list-fabrics
- description: List all current issues in the QueryGrid environment.
  hints:
    readOnly: true
  name: list-issues
- description: Run a diagnostic check on QueryGrid systems.
  hints:
    readOnly: false
  name: run-diagnostic-check
---
