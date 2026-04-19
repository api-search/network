---
consumed_apis:
- cr-reporting
description: Unified workflow for managing Crystal Reports including authentication, repository browsing, report viewing, data access, and export. Used by report developers, BI analysts, and application developers.
layout: capability
name: Crystal Reports Report Management
operations:
- description: ''
  method: POST
  name: logon
  path: /v1/auth
- description: ''
  method: GET
  name: browse-repository
  path: /v1/reports
- description: ''
  method: GET
  name: get-report-summary
  path: /v1/reports/{id}
- description: ''
  method: GET
  name: export-report
  path: /v1/reports/{id}/export
- description: ''
  method: GET
  name: get-rows
  path: /v1/reports/{id}/rows
personas: []
provider_name: Crystal Reports
provider_slug: crystal-reports
search_terms:
- report management
- export report to pdf, excel, csv, word, xml, or other format
- browse the bi platform report repository
- authenticate to crystal reports server
- get report structure
- create a transient report instance
- get rows
- get report metadata with datasources, fields, parameters, and formulas
- get report data rows via odata with pagination and filtering
- get report grand totals and summaries
- get odata metadata
- browse repository
- data analytics
- reporting
- get report summary including name, author, and uris
- enterprise software
- list folder children
- sap
- post row
- get edmx metadata describing the report data model
- export
- list contents of a repository folder
- export report
- crystal reports
- logon
- get report summary
- create instance
- push data to a transient report instance
- business intelligence
- get grand totals
slug: report-management
tags:
- Crystal Reports
- Report Management
- Business Intelligence
- Export
tools:
- description: Authenticate to Crystal Reports server
  hints:
    readOnly: false
  name: logon
- description: Browse the BI platform report repository
  hints:
    idempotent: true
    readOnly: true
  name: browse-repository
- description: List contents of a repository folder
  hints:
    idempotent: true
    readOnly: true
  name: list-folder-children
- description: Get report summary including name, author, and URIs
  hints:
    idempotent: true
    readOnly: true
  name: get-report-summary
- description: Get report metadata with datasources, fields, parameters, and formulas
  hints:
    idempotent: true
    readOnly: true
  name: get-report-structure
- description: Create a transient report instance
  hints:
    readOnly: false
  name: create-instance
- description: Export report to PDF, Excel, CSV, Word, XML, or other format
  hints:
    idempotent: true
    readOnly: true
  name: export-report
- description: Get report data rows via OData with pagination and filtering
  hints:
    idempotent: true
    readOnly: true
  name: get-rows
- description: Push data to a transient report instance
  hints:
    readOnly: false
  name: post-row
- description: Get report grand totals and summaries
  hints:
    idempotent: true
    readOnly: true
  name: get-grand-totals
- description: Get EDMX metadata describing the report data model
  hints:
    idempotent: true
    readOnly: true
  name: get-odata-metadata
---
