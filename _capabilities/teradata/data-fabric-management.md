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
- list connectors
- data warehousing
- bridge management.
- data center management.
- list all current issues.
- manages data fabric infrastructure and cross-system connectivity.
- analytics
- list all data fabric configurations.
- system and fabric configuration management.
- teradata
- list systems
- Application Developer
- execute sql queries and analytics.
- database
- list all registered systems in querygrid.
- list fabrics
- health monitoring and issue detection.
- list issues
- cloud
- list all registered systems.
- issue monitoring.
- list all current issues in the querygrid environment.
- run a diagnostic check on querygrid systems.
- run diagnostic check
- list all configured data centers.
- manage querygrid data fabric infrastructure.
- list all bridges connecting systems.
- list all data centers.
- executes queries and analyzes data across vantage systems.
- Data Engineer
- list bridges
- integrates applications with teradata via rest apis.
- configuration
- list all bridges.
- enterprise
- data fabric
- administration
- administers querygrid systems, nodes, and software.
- system management.
- sql query execution and session management.
- list data centers
- sql
- Platform Administrator
- Data Analyst
- data management
- machine learning
- list all connectors for system integration.
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
