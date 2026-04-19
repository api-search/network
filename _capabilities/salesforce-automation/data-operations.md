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
- list ingest jobs
- sales
- Salesforce Admin
- execute a sosl search.
- query salesforce data
- flows, process automation, and approval management.
- manages sales processes, reports, and pipeline.
- search salesforce data
- crm
- create a new record in salesforce.
- create bulk query job
- create a new bulk ingest job.
- create salesforce record
- describe salesforce sobjects
- execute a soql query against salesforce data.
- create a new record.
- execute a soql query.
- execute query
- describe all
- builds integrations between salesforce and external systems.
- crud, queries, search, and bulk data operations.
- create record
- real-time event streaming and change data capture.
- integration
- soql query execution.
- submit salesforce approval
- data operations
- sobject metadata and describe.
- record crud operations.
- describe all available sobjects.
- crud operations and data queries.
- bulk data loading and external system integration.
- sosl search.
- Integration Developer
- automation
- create a bulk data ingest job for large datasets.
- execute search
- cloud
- bulk data operations.
- describe all available sobjects in the salesforce org.
- manages salesforce configuration, data, and automation.
- create a bulk query job for large result sets.
- submit a record for approval in salesforce.
- enterprise
- list bulk ingest jobs
- execute a sosl search across salesforce.
- create bulk ingest job
- list all bulk ingest jobs.
- salesforce
- create ingest job
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
