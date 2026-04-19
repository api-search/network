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
- integrates applications with teradata via rest apis.
- manage querygrid data fabric infrastructure.
- manages data fabric infrastructure and cross-system connectivity.
- list data centers
- data center management.
- analytics
- list fabrics
- list all data centers.
- run a diagnostic check on querygrid systems.
- administration
- list all registered systems.
- list all registered systems in querygrid.
- enterprise
- health monitoring and issue detection.
- machine learning
- list systems
- list bridges
- data management
- data warehousing
- list all configured data centers.
- cloud
- list all data fabric configurations.
- execute sql queries and analytics.
- list all bridges.
- Data Engineer
- Data Analyst
- issue monitoring.
- run diagnostic check
- configuration
- list all current issues in the querygrid environment.
- executes queries and analyzes data across vantage systems.
- list all connectors for system integration.
- system and fabric configuration management.
- data fabric
- bridge management.
- sql query execution and session management.
- system management.
- list issues
- administers querygrid systems, nodes, and software.
- sql
- list connectors
- list all bridges connecting systems.
- teradata
- database
- list all current issues.
- Application Developer
- Platform Administrator
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
