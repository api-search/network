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
- list data centers
- list all registered systems in querygrid.
- health monitoring and issue detection.
- system and fabric configuration management.
- administration
- list issues
- system management.
- configuration
- list connectors
- manages data fabric infrastructure and cross-system connectivity.
- list systems
- Platform Administrator
- list all current issues in the querygrid environment.
- data warehousing
- sql query execution and session management.
- bridge management.
- list fabrics
- manage querygrid data fabric infrastructure.
- executes queries and analyzes data across vantage systems.
- integrates applications with teradata via rest apis.
- list all bridges connecting systems.
- list all data centers.
- list all configured data centers.
- execute sql queries and analytics.
- sql
- analytics
- administers querygrid systems, nodes, and software.
- list all data fabric configurations.
- Data Analyst
- list all connectors for system integration.
- data management
- Data Engineer
- cloud
- data fabric
- list bridges
- run diagnostic check
- Application Developer
- data center management.
- list all current issues.
- database
- issue monitoring.
- teradata
- enterprise
- list all bridges.
- machine learning
- list all registered systems.
- run a diagnostic check on querygrid systems.
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
