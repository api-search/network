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
- list all current issues in the querygrid environment.
- list all configured data centers.
- execute sql queries and analytics.
- run diagnostic check
- enterprise
- list fabrics
- data management
- administers querygrid systems, nodes, and software.
- analytics
- list all registered systems.
- Application Developer
- administration
- system and fabric configuration management.
- bridge management.
- list all registered systems in querygrid.
- teradata
- cloud
- manage querygrid data fabric infrastructure.
- configuration
- sql
- data center management.
- system management.
- run a diagnostic check on querygrid systems.
- health monitoring and issue detection.
- machine learning
- data warehousing
- Data Engineer
- list all connectors for system integration.
- list data centers
- integrates applications with teradata via rest apis.
- list systems
- list issues
- list all bridges.
- Data Analyst
- list all bridges connecting systems.
- sql query execution and session management.
- list all current issues.
- Platform Administrator
- issue monitoring.
- data fabric
- list bridges
- manages data fabric infrastructure and cross-system connectivity.
- executes queries and analyzes data across vantage systems.
- database
- list all data fabric configurations.
- list all data centers.
- list connectors
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
