---
consumed_apis:
- mainframe-modernization
description: Workflow capability for platform and migration teams to manage mainframe application modernization, including application lifecycle management, environment configuration, and batch job execution on AWS.
layout: capability
name: Amazon Mainframe Modernization - Migration Workflow
operations:
- description: Create a modernization application
  method: POST
  name: create-application
  path: /v1/applications
- description: List modernization applications
  method: GET
  name: list-applications
  path: /v1/applications
- description: Create a runtime environment
  method: POST
  name: create-environment
  path: /v1/environments
- description: List runtime environments
  method: GET
  name: list-environments
  path: /v1/environments
- description: Start a batch job
  method: POST
  name: start-batch-job
  path: /v1/applications/{id}/batch-jobs
- description: List batch jobs
  method: GET
  name: list-batch-jobs
  path: /v1/applications/{id}/batch-jobs
personas: []
provider_name: Amazon Mainframe Modernization
provider_slug: amazon-mainframe-modernization
search_terms:
- list all runtime environments available for deployment
- mainframe
- Platform Engineer
- migration
- execution of batch jobs migrated from mainframe
- Mainframe Developer
- start a batch job
- list environments
- create runtime environment
- modernization applications
- batch processing
- list all mainframe applications being modernized
- amazon
- list batch job execution history for an application
- workflow for managing mainframe application modernization, environments, and batch jobs
- create a runtime environment for modernized mainframe applications
- batch jobs
- create modernization application
- get application details
- list batch jobs
- create environment
- batch job executions
- cobol
- list runtime environments
- get details and status of a modernization application
- list batch job executions
- list modernization applications
- create application
- runtime environments
- create a modernization application
- develops and deploys modernized cobol/mainframe applications and manages batch job execution
- creation and management of modernized mainframe applications
- start batch job
- create a runtime environment
- aws
- create a new mainframe modernization application on aws
- manages runtime environments and deployment infrastructure for modernized mainframe applications
- modernization
- list applications
- start a batch job execution for a modernized mainframe application
- environment provisioning for running modernized applications
slug: modernization-workflow
tags:
- Amazon
- Mainframe
- Migration
- Modernization
- COBOL
- Batch Jobs
tools:
- description: Create a new mainframe modernization application on AWS
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-modernization-application
- description: List all mainframe applications being modernized
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: list-modernization-applications
- description: Get details and status of a modernization application
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-application-details
- description: Create a runtime environment for modernized mainframe applications
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-runtime-environment
- description: List all runtime environments available for deployment
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: list-runtime-environments
- description: Start a batch job execution for a modernized mainframe application
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: start-batch-job
- description: List batch job execution history for an application
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: list-batch-job-executions
---
