---
consumed_apis: []
description: Workflow capability for running and managing SQL analytics queries with Amazon Athena including query execution, named queries, work groups, and data catalog management.
layout: capability
name: SQL Analytics Workflow
operations:
- description: Start a SQL query execution
  method: POST
  name: start-query-execution
  path: /v1/queries
- description: List query executions
  method: GET
  name: list-query-executions
  path: /v1/queries
- description: Create a named query
  method: POST
  name: create-named-query
  path: /v1/named-queries
- description: List named queries
  method: GET
  name: list-named-queries
  path: /v1/named-queries
personas: []
provider_name: Amazon Athena
provider_slug: amazon-athena
search_terms:
- sql
- list named queries
- create a named query
- sql query management
- list query executions
- download the results of a completed athena sql query.
- list recent query executions in an athena workgroup.
- list databases in an athena data catalog to explore available schemas.
- list data catalogs
- start query execution
- get query results
- get query execution
- named query management
- list tables in an athena database to understand available data.
- list table metadata
- start a sql query execution
- list data catalogs registered with athena to discover available data sources.
- amazon athena
- serverless
- analytics
- aws
- check the status of a running or completed athena query execution.
- list databases
- list athena workgroups to understand available query isolation environments.
- create named query
- save a sql query as a named query for reuse in athena.
- list work groups
- list saved named queries available in an athena workgroup.
- run a sql query against s3 data using amazon athena for serverless analytics.
slug: sql-analytics
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
- AWS
tools:
- description: Run a SQL query against S3 data using Amazon Athena for serverless analytics.
  hints:
    openWorld: false
    readOnly: false
  name: start-query-execution
- description: Check the status of a running or completed Athena query execution.
  hints:
    openWorld: true
    readOnly: true
  name: get-query-execution
- description: Download the results of a completed Athena SQL query.
  hints:
    openWorld: true
    readOnly: true
  name: get-query-results
- description: List recent query executions in an Athena workgroup.
  hints:
    openWorld: true
    readOnly: true
  name: list-query-executions
- description: Save a SQL query as a named query for reuse in Athena.
  hints:
    openWorld: false
    readOnly: false
  name: create-named-query
- description: List saved named queries available in an Athena workgroup.
  hints:
    openWorld: true
    readOnly: true
  name: list-named-queries
- description: List Athena workgroups to understand available query isolation environments.
  hints:
    openWorld: true
    readOnly: true
  name: list-work-groups
- description: List data catalogs registered with Athena to discover available data sources.
  hints:
    openWorld: true
    readOnly: true
  name: list-data-catalogs
- description: List databases in an Athena data catalog to explore available schemas.
  hints:
    openWorld: true
    readOnly: true
  name: list-databases
- description: List tables in an Athena database to understand available data.
  hints:
    openWorld: true
    readOnly: true
  name: list-table-metadata
---
