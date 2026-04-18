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
- cloud
- list bridges
- list issues
- administration
- system and fabric configuration management.
- execute sql queries and analytics.
- Data Analyst
- Data Engineer
- list connectors
- system management.
- list fabrics
- database
- health monitoring and issue detection.
- integrates applications with teradata via rest apis.
- list all data centers.
- list systems
- list all registered systems.
- list all connectors for system integration.
- manages data fabric infrastructure and cross-system connectivity.
- bridge management.
- list all current issues in the querygrid environment.
- data warehousing
- sql query execution and session management.
- list all current issues.
- manage querygrid data fabric infrastructure.
- Platform Administrator
- Application Developer
- administers querygrid systems, nodes, and software.
- analytics
- sql
- list all data fabric configurations.
- teradata
- enterprise
- run a diagnostic check on querygrid systems.
- list all bridges connecting systems.
- run diagnostic check
- executes queries and analyzes data across vantage systems.
- configuration
- list all bridges.
- data center management.
- issue monitoring.
- list data centers
- data fabric
- list all configured data centers.
- machine learning
- data management
- list all registered systems in querygrid.
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
