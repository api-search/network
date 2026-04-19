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
- list data change tasks
- raas get report
- wql list data sources
- prism create dataset
- list available wql data sources
- cloud computing
- wql get data source fields
- prism get dataset
- prism list data change tasks
- prism analytics datasets
- wql get data source
- list datasets
- create a data change task
- reporting
- execute query
- delete a dataset
- financial management
- enterprise software
- list all prism analytics datasets
- prism create data change task
- prism list tables
- workday
- analytics
- wql query endpoint
- create a new prism analytics dataset
- execute a wql query against workday data
- get a wql data source by id
- wql execute query
- get fields for a wql data source
- hcm
- prism list datasets
- get a dataset by id
- saas
- retrieve a custom workday report
- execute a wql query
- business intelligence
- prism delete dataset
- list all prism tables
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
