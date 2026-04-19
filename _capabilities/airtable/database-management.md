---
consumed_apis:
- airtable
- airtable-meta
description: Unified workflow for managing Airtable databases — reading and writing records, browsing base schemas, managing webhooks, and administering tables. Used by developers and data teams integrating Airtable with external systems.
layout: capability
name: Airtable Database Management
operations:
- description: List all accessible bases.
  method: GET
  name: list-bases
  path: /v1/bases
- description: List records from a table.
  method: GET
  name: list-records
  path: /v1/records
- description: Create records in a table.
  method: POST
  name: create-records
  path: /v1/records
- description: Update a record.
  method: PATCH
  name: update-record
  path: /v1/records/{recordId}
- description: Delete a record.
  method: DELETE
  name: delete-record
  path: /v1/records/{recordId}
personas: []
provider_name: Airtable
provider_slug: airtable
search_terms:
- read/write airtable records, browse schemas, manage webhooks. used by developers and data teams integrating airtable with external systems.
- list bases
- creating, reading, updating, and deleting data records.
- get base schema
- user management, audit logs, and access control.
- list all airtable bases the user has access to.
- list all accessible bases.
- collaboration
- update a record.
- list records from an airtable table with optional filtering.
- update specific fields in an airtable record.
- schema
- create records
- applications
- get the schema of an airtable base with all tables and fields.
- airtable
- database
- create records in a table.
- update record
- integrates airtable with external systems via the rest api.
- airtable bases and schemas.
- airtable table records.
- list records
- list records from a table.
- low-code
- create one or more records in an airtable table.
- real-time event-driven integrations via webhooks.
- spreadsheets
- Developer
- no-code
- Data Analyst
- productivity
- data
- databases
- records
- delete a record.
- managing the structure of bases, tables, and fields.
- delete an airtable record permanently.
- reads and analyzes airtable data programmatically.
- manages users, audit logs, and shares across the organization.
- delete record
- a specific airtable record.
slug: database-management
tags:
- Airtable
- Database
- Low-Code
- No-Code
- Records
- Schema
- Collaboration
tools:
- description: List all Airtable bases the user has access to.
  hints:
    openWorld: true
    readOnly: true
  name: list-bases
- description: Get the schema of an Airtable base with all tables and fields.
  hints:
    readOnly: true
  name: get-base-schema
- description: List records from an Airtable table with optional filtering.
  hints:
    openWorld: true
    readOnly: true
  name: list-records
- description: Create one or more records in an Airtable table.
  hints:
    readOnly: false
  name: create-records
- description: Update specific fields in an Airtable record.
  hints:
    idempotent: false
    readOnly: false
  name: update-record
- description: Delete an Airtable record permanently.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-record
---
