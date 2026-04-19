---
consumed_apis:
- keyspaces
description: Unified workflow capability for Amazon Keyspaces combining resource management and operations.
layout: capability
name: Amazon Keyspaces Workflow
operations: []
personas: []
provider_name: Amazon Keyspaces
provider_slug: amazon-keyspaces
search_terms:
- keyspaces get keyspace
- tables get table
- keyspaces create keyspace
- unified workflow for amazon keyspaces resource management
- creates a new keyspace.
- cassandra
- integrates api into applications
- nosql
- managed database
- amazon keyspaces
- returns a list of keyspaces.
- returns information about the table.
- tables list tables
- workflow
- tables create table
- database
- aws
- returns the name and the amazon resource name (arn) of a keyspace.
- Administrator
- Developer
- manages resources and configurations
- wide column
- keyspaces list keyspaces
- the createtable operation adds a new table to the specified keyspace.
- returns a list of tables for a specified keyspace.
slug: amazon-keyspaces-workflow
tags:
- Amazon Keyspaces
- AWS
- Workflow
tools:
- description: Creates a new keyspace.
  hints:
    idempotent: false
    readOnly: false
  name: keyspaces-create-keyspace
- description: Returns a list of keyspaces.
  hints:
    idempotent: true
    readOnly: true
  name: keyspaces-list-keyspaces
- description: Returns the name and the Amazon Resource Name (ARN) of a keyspace.
  hints:
    idempotent: true
    readOnly: true
  name: keyspaces-get-keyspace
- description: The CreateTable operation adds a new table to the specified keyspace.
  hints:
    idempotent: false
    readOnly: false
  name: tables-create-table
- description: Returns a list of tables for a specified keyspace.
  hints:
    idempotent: true
    readOnly: true
  name: tables-list-tables
- description: Returns information about the table.
  hints:
    idempotent: true
    readOnly: true
  name: tables-get-table
---
