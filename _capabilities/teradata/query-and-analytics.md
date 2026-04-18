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
- cloud
- list query systems
- system and fabric configuration management.
- get the status and results of a submitted query.
- list available vantage systems.
- execute sql queries and analytics.
- Data Analyst
- Data Engineer
- create a query session.
- sql queries.
- create session
- database
- execute query
- health monitoring and issue detection.
- create a new query session on a vantage system.
- integrates applications with teradata via rest apis.
- query
- get query status
- manages data fabric infrastructure and cross-system connectivity.
- available systems.
- sql query execution and session management.
- list available vantage systems for query execution.
- list querygrid queries
- manage querygrid data fabric infrastructure.
- Platform Administrator
- sql
- Application Developer
- analytics
- administers querygrid systems, nodes, and software.
- teradata
- enterprise
- execute a sql query.
- executes queries and analyzes data across vantage systems.
- query sessions.
- execute a sql query against teradata vantage.
- machine learning
- list cross-system query summaries from querygrid.
- data management
- data warehousing
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
