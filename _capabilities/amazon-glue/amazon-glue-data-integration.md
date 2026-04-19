---
consumed_apis:
- amazon-glue
description: Workflow capability for data engineers building ETL pipelines with Amazon Glue. Covers job management, crawler configuration, data catalog operations, workflow orchestration, and data quality for serverless data integration.
layout: capability
name: Amazon Glue Data Integration
operations:
- description: List all ETL jobs
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: Create a new ETL job
  method: POST
  name: create-job
  path: /v1/jobs
- description: Start a job run
  method: POST
  name: start-job-run
  path: /v1/jobs/{jobName}/runs
- description: List all crawlers
  method: GET
  name: list-crawlers
  path: /v1/crawlers
- description: Create a new crawler
  method: POST
  name: create-crawler
  path: /v1/crawlers
- description: List all catalog databases
  method: GET
  name: list-databases
  path: /v1/databases
- description: List all workflows
  method: GET
  name: list-workflows
  path: /v1/workflows
- description: Create a new ETL workflow
  method: POST
  name: create-workflow
  path: /v1/workflows
personas: []
provider_name: Amazon Glue
provider_slug: amazon-glue
search_terms:
- list all workflows
- list tables
- list jobs
- start a job run
- data pipeline
- execute an etl job run
- etl
- create workflow
- list all etl jobs
- create job
- list workflows
- list all amazon glue etl jobs with status and configuration
- create etl job
- list all data catalog crawlers
- start job run
- list data quality evaluation results
- list crawlers
- create connection
- data catalog
- create a crawler to discover and catalog data sources
- create crawler
- list all glue ml transforms
- run a crawler to populate the data catalog
- create a new etl workflow
- data catalog crawlers
- list all crawlers
- check the status of an etl job run
- list all etl workflow orchestrations
- amazon glue
- list all data source connections
- data engineering
- aws
- list connections
- etl job lifecycle management
- list data quality results
- data catalog databases
- list databases
- create a new crawler
- analytics
- serverless
- list tables in a data catalog database
- list all catalog databases
- etl workflow orchestration
- create a connection to a data source
- list etl jobs
- list ml transforms
- Data Engineer
- Data Analyst
- uses glue to access and prepare data for analytics
- builds and manages etl pipelines and data catalog resources
- get job run status
- job execution runs
- list all databases in the glue data catalog
- create a new etl workflow with triggers and jobs
- start crawler
- create a new etl job
- create a new amazon glue etl job
- data integration
slug: amazon-glue-data-integration
tags:
- Amazon Glue
- ETL
- Data Integration
- Data Catalog
- Data Engineering
- AWS
tools:
- description: List all Amazon Glue ETL jobs with status and configuration
  hints:
    openWorld: true
    readOnly: true
  name: list-etl-jobs
- description: Create a new Amazon Glue ETL job
  hints:
    readOnly: false
  name: create-etl-job
- description: Execute an ETL job run
  hints:
    readOnly: false
  name: start-job-run
- description: Check the status of an ETL job run
  hints:
    readOnly: true
  name: get-job-run-status
- description: List all Data Catalog crawlers
  hints:
    readOnly: true
  name: list-crawlers
- description: Create a crawler to discover and catalog data sources
  hints:
    readOnly: false
  name: create-crawler
- description: Run a crawler to populate the Data Catalog
  hints:
    readOnly: false
  name: start-crawler
- description: List all databases in the Glue Data Catalog
  hints:
    readOnly: true
  name: list-databases
- description: List tables in a Data Catalog database
  hints:
    readOnly: true
  name: list-tables
- description: List all ETL workflow orchestrations
  hints:
    readOnly: true
  name: list-workflows
- description: Create a new ETL workflow with triggers and jobs
  hints:
    readOnly: false
  name: create-workflow
- description: List all data source connections
  hints:
    readOnly: true
  name: list-connections
- description: Create a connection to a data source
  hints:
    readOnly: false
  name: create-connection
- description: List all Glue ML transforms
  hints:
    readOnly: true
  name: list-ml-transforms
- description: List data quality evaluation results
  hints:
    readOnly: true
  name: list-data-quality-results
---
