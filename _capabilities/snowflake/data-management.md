---
consumed_apis:
- snowflake-database
- snowflake-schema
- snowflake-table
- snowflake-view
- snowflake-dynamic-table
- snowflake-iceberg-table
- snowflake-event-table
- snowflake-external-volume
description: Unified workflow for managing databases, schemas, tables, views, dynamic tables, iceberg tables, and event tables. Used by Data Engineers and Database Administrators to create, organize, and maintain data structures.
layout: capability
name: Snowflake Data Management
operations:
- description: List all databases
  method: GET
  name: list-databases
  path: /v1/databases
- description: Create a database
  method: POST
  name: create-database
  path: /v1/databases
- description: Fetch a database
  method: GET
  name: fetch-database
  path: /v1/databases/{name}
- description: Delete a database
  method: DELETE
  name: delete-database
  path: /v1/databases/{name}
- description: List schemas
  method: GET
  name: list-schemas
  path: /v1/schemas
- description: Create a schema
  method: POST
  name: create-schema
  path: /v1/schemas
- description: List tables
  method: GET
  name: list-tables
  path: /v1/tables
- description: Create a table
  method: POST
  name: create-table
  path: /v1/tables
- description: List views
  method: GET
  name: list-views
  path: /v1/views
- description: Create a view
  method: POST
  name: create-view
  path: /v1/views
- description: List dynamic tables
  method: GET
  name: list-dynamic-tables
  path: /v1/dynamic-tables
- description: Create a dynamic table
  method: POST
  name: create-dynamic-table
  path: /v1/dynamic-tables
- description: List Iceberg tables
  method: GET
  name: list-iceberg-tables
  path: /v1/iceberg-tables
- description: Create an Iceberg table
  method: POST
  name: create-iceberg-table
  path: /v1/iceberg-tables
personas: []
provider_name: Snowflake
provider_slug: snowflake
search_terms:
- data sharing
- data lakes
- database management
- create an iceberg table
- list views in a schema
- create iceberg table
- restore a dropped database
- delete a schema
- list dynamic tables
- resume a dynamic table
- create an event table
- create a new database
- undrop database
- table management
- create a dynamic table
- list schemas
- list schemas in a database
- list tables in a schema
- suspend a dynamic table
- delete schema
- list external volumes
- create schema
- create database
- resume dynamic table
- data warehousing
- list views
- create a database
- list tables
- single database operations
- iceberg table management
- create a new schema
- create external volume
- sql
- fetch a database
- suspend dynamic table
- create dynamic table
- snowflake
- create a view
- view management
- create a new view
- data management
- create a new table
- create a table
- create an external volume
- fetch database
- create a schema
- list iceberg tables
- fetch schema
- list databases
- fetch database details by name
- clone a database
- clone database
- fetch table
- delete a table
- list event tables
- dynamic table management
- fetch table details
- create view
- delete a database
- create event table
- schema management
- database
- delete table
- create table
- data engineering
- fetch schema details
- list all accessible databases
- list all databases
- delete database
slug: data-management
tags:
- Snowflake
- Data Management
- Data Engineering
tools:
- description: List all accessible databases
  hints:
    readOnly: true
  name: list-databases
- description: Create a new database
  hints:
    readOnly: false
  name: create-database
- description: Fetch database details by name
  hints:
    readOnly: true
  name: fetch-database
- description: Delete a database
  hints:
    destructive: true
  name: delete-database
- description: Clone a database
  hints:
    readOnly: false
  name: clone-database
- description: Restore a dropped database
  hints:
    readOnly: false
  name: undrop-database
- description: List schemas in a database
  hints:
    readOnly: true
  name: list-schemas
- description: Create a new schema
  hints:
    readOnly: false
  name: create-schema
- description: Fetch schema details
  hints:
    readOnly: true
  name: fetch-schema
- description: Delete a schema
  hints:
    destructive: true
  name: delete-schema
- description: List tables in a schema
  hints:
    readOnly: true
  name: list-tables
- description: Create a new table
  hints:
    readOnly: false
  name: create-table
- description: Fetch table details
  hints:
    readOnly: true
  name: fetch-table
- description: Delete a table
  hints:
    destructive: true
  name: delete-table
- description: List views in a schema
  hints:
    readOnly: true
  name: list-views
- description: Create a new view
  hints:
    readOnly: false
  name: create-view
- description: List dynamic tables
  hints:
    readOnly: true
  name: list-dynamic-tables
- description: Create a dynamic table
  hints:
    readOnly: false
  name: create-dynamic-table
- description: Suspend a dynamic table
  hints:
    readOnly: false
  name: suspend-dynamic-table
- description: Resume a dynamic table
  hints:
    readOnly: false
  name: resume-dynamic-table
- description: List Iceberg tables
  hints:
    readOnly: true
  name: list-iceberg-tables
- description: Create an Iceberg table
  hints:
    readOnly: false
  name: create-iceberg-table
- description: List event tables
  hints:
    readOnly: true
  name: list-event-tables
- description: Create an event table
  hints:
    readOnly: false
  name: create-event-table
- description: List external volumes
  hints:
    readOnly: true
  name: list-external-volumes
- description: Create an external volume
  hints:
    readOnly: false
  name: create-external-volume
---
