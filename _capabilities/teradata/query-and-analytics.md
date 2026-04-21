---
consumed_apis:
- query-service
- querygrid-manager
description: Workflow capability for executing SQL queries and analytics against Teradata Vantage systems. Combines Query Service for SQL execution with QueryGrid for cross-system query monitoring. Used by data analysts and application developers.
layout: capability
name: Teradata Query and Analytics
operations:
- description: List available Vantage systems.
  method: GET
  name: list-query-systems
  path: /v1/systems
- description: Create a query session.
  method: POST
  name: create-session
  path: /v1/sessions
- description: Execute a SQL query.
  method: POST
  name: execute-query
  path: /v1/queries
personas: []
provider_name: Teradata
provider_slug: teradata
search_terms:
- execute sql queries and analytics.
- enterprise
- list querygrid queries
- data management
- administers querygrid systems, nodes, and software.
- query
- analytics
- Application Developer
- system and fabric configuration management.
- execute query
- create session
- create a query session.
- query sessions.
- teradata
- cloud
- execute a sql query.
- sql
- manage querygrid data fabric infrastructure.
- health monitoring and issue detection.
- machine learning
- data warehousing
- Data Engineer
- integrates applications with teradata via rest apis.
- execute a sql query against teradata vantage.
- Data Analyst
- sql query execution and session management.
- available systems.
- get the status and results of a submitted query.
- Platform Administrator
- list available vantage systems.
- create a new query session on a vantage system.
- manages data fabric infrastructure and cross-system connectivity.
- list cross-system query summaries from querygrid.
- get query status
- executes queries and analyzes data across vantage systems.
- database
- list available vantage systems for query execution.
- sql queries.
- list query systems
slug: query-and-analytics
tags:
- Teradata
- Query
- Analytics
- SQL
tools:
- description: List available Vantage systems for query execution.
  hints:
    readOnly: true
  name: list-query-systems
- description: Create a new query session on a Vantage system.
  hints:
    readOnly: false
  name: create-session
- description: Execute a SQL query against Teradata Vantage.
  hints:
    readOnly: false
  name: execute-query
- description: Get the status and results of a submitted query.
  hints:
    readOnly: true
  name: get-query-status
- description: List cross-system query summaries from QueryGrid.
  hints:
    readOnly: true
  name: list-querygrid-queries
---
