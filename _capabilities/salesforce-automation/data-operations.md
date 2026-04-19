---
consumed_apis:
- salesforce-rest
- salesforce-bulk
description: Unified workflow combining the Salesforce REST API and Bulk API for comprehensive data operations including CRUD, queries, search, and bulk data loading. Used by Salesforce admins and integration developers.
layout: capability
name: Salesforce Data Operations
operations:
- description: Describe all available SObjects.
  method: GET
  name: describe-all
  path: /v1/sobjects
- description: Create a new record.
  method: POST
  name: create-record
  path: /v1/records
- description: Execute a SOQL query.
  method: GET
  name: execute-query
  path: /v1/query
- description: Execute a SOSL search.
  method: GET
  name: execute-search
  path: /v1/search
- description: List all bulk ingest jobs.
  method: GET
  name: list-ingest-jobs
  path: /v1/bulk-jobs
- description: Create a new bulk ingest job.
  method: POST
  name: create-ingest-job
  path: /v1/bulk-jobs
personas: []
provider_name: Salesforce Automation
provider_slug: salesforce-automation
search_terms:
- execute query
- Integration Developer
- submit a record for approval in salesforce.
- bulk data loading and external system integration.
- bulk data operations.
- create ingest job
- crud, queries, search, and bulk data operations.
- create a new bulk ingest job.
- manages sales processes, reports, and pipeline.
- builds integrations between salesforce and external systems.
- sobject metadata and describe.
- create a new record.
- soql query execution.
- execute a sosl search.
- enterprise
- create record
- salesforce
- list bulk ingest jobs
- execute a soql query.
- cloud
- execute search
- real-time event streaming and change data capture.
- create bulk ingest job
- integration
- crm
- execute a sosl search across salesforce.
- Salesforce Admin
- describe all available sobjects.
- query salesforce data
- sales
- describe all
- describe all available sobjects in the salesforce org.
- record crud operations.
- list ingest jobs
- search salesforce data
- create a bulk data ingest job for large datasets.
- create a bulk query job for large result sets.
- list all bulk ingest jobs.
- sosl search.
- submit salesforce approval
- crud operations and data queries.
- create salesforce record
- flows, process automation, and approval management.
- describe salesforce sobjects
- create bulk query job
- manages salesforce configuration, data, and automation.
- data operations
- execute a soql query against salesforce data.
- automation
- create a new record in salesforce.
slug: data-operations
tags:
- Salesforce
- Data Operations
- CRM
- Integration
tools:
- description: Describe all available SObjects in the Salesforce org.
  hints:
    idempotent: true
    readOnly: true
  name: describe-salesforce-sobjects
- description: Create a new record in Salesforce.
  hints:
    readOnly: false
  name: create-salesforce-record
- description: Execute a SOQL query against Salesforce data.
  hints:
    idempotent: true
    readOnly: true
  name: query-salesforce-data
- description: Execute a SOSL search across Salesforce.
  hints:
    idempotent: true
    readOnly: true
  name: search-salesforce-data
- description: Submit a record for approval in Salesforce.
  hints:
    readOnly: false
  name: submit-salesforce-approval
- description: Create a bulk data ingest job for large datasets.
  hints:
    readOnly: false
  name: create-bulk-ingest-job
- description: Create a bulk query job for large result sets.
  hints:
    readOnly: false
  name: create-bulk-query-job
- description: List all bulk ingest jobs.
  hints:
    readOnly: true
  name: list-bulk-ingest-jobs
---
