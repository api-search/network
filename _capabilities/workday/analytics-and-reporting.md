---
consumed_apis:
- workday-prism
- workday-wql
- workday-raas
description: Unified analytics and reporting combining Prism Analytics, WQL, and Report-as-a-Service APIs for business analysts to query data, manage datasets, and access custom reports.
layout: capability
name: Workday Analytics and Reporting
operations:
- description: List datasets
  method: GET
  name: list-datasets
  path: /v1/datasets
- description: Execute a WQL query
  method: POST
  name: execute-query
  path: /v1/wql-query
personas: []
provider_name: Workday
provider_slug: workday
search_terms:
- delete a dataset
- prism list data change tasks
- reporting
- create a data change task
- list all prism analytics datasets
- execute a wql query
- get fields for a wql data source
- workday
- list datasets
- prism list datasets
- get a wql data source by id
- prism delete dataset
- prism list tables
- raas get report
- wql get data source
- financial management
- create a new prism analytics dataset
- get a dataset by id
- list data change tasks
- list available wql data sources
- analytics
- prism get dataset
- execute a wql query against workday data
- saas
- business intelligence
- prism analytics datasets
- list all prism tables
- wql list data sources
- execute query
- cloud computing
- enterprise software
- prism create data change task
- hcm
- wql execute query
- wql query endpoint
- prism create dataset
- wql get data source fields
- retrieve a custom workday report
slug: analytics-and-reporting
tags:
- Workday
- Analytics
- Reporting
- Business Intelligence
tools:
- description: List all Prism Analytics datasets
  hints:
    readOnly: true
  name: prism-list-datasets
- description: Create a new Prism Analytics dataset
  hints:
    readOnly: false
  name: prism-create-dataset
- description: Get a dataset by ID
  hints:
    readOnly: true
  name: prism-get-dataset
- description: Delete a dataset
  hints:
    destructive: true
    readOnly: false
  name: prism-delete-dataset
- description: List data change tasks
  hints:
    readOnly: true
  name: prism-list-data-change-tasks
- description: Create a data change task
  hints:
    readOnly: false
  name: prism-create-data-change-task
- description: List all Prism tables
  hints:
    readOnly: true
  name: prism-list-tables
- description: Execute a WQL query against Workday data
  hints:
    readOnly: true
  name: wql-execute-query
- description: List available WQL data sources
  hints:
    readOnly: true
  name: wql-list-data-sources
- description: Get a WQL data source by ID
  hints:
    readOnly: true
  name: wql-get-data-source
- description: Get fields for a WQL data source
  hints:
    readOnly: true
  name: wql-get-data-source-fields
- description: Retrieve a custom Workday report
  hints:
    readOnly: true
  name: raas-get-report
---
