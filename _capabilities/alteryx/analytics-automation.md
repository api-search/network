---
consumed_apis:
- alteryx-server
description: Analytics automation workflow combining Alteryx Server V3 API for workflow management, job execution, scheduling, user administration, credential management, and collection organization. Used by data analysts and server administrators to automate analytics pipelines.
layout: capability
name: Alteryx Analytics Automation
operations:
- description: List all workflows
  method: GET
  name: list-workflows
  path: /v1/workflows
- description: Upload a new workflow
  method: POST
  name: upload-workflow
  path: /v1/workflows
- description: Get workflow details
  method: GET
  name: get-workflow
  path: /v1/workflows/{workflowId}
- description: List all schedules
  method: GET
  name: list-schedules
  path: /v1/schedules
- description: Create a new schedule
  method: POST
  name: create-schedule
  path: /v1/schedules
- description: List all users
  method: GET
  name: list-users
  path: /v1/users
- description: List all collections
  method: GET
  name: list-collections
  path: /v1/collections
personas: []
provider_name: Alteryx
provider_slug: alteryx
search_terms:
- list all workflows
- download a workflow package
- get user details
- individual workflow operations
- delete collection
- upload a new workflow
- create a new collection
- machine learning
- etl
- delete a user
- list workflows
- create job
- create collection
- predictive analytics
- update workflow metadata
- get workflow details
- deactivate user
- get workflow jobs
- list credentials
- upload workflow
- list all users
- list all workflow schedules
- get details of a specific workflow
- user management
- create a new workflow schedule
- create a new user
- create user
- collection management
- update workflow
- get workflow
- schedule management
- create schedule
- delete user
- list all collections
- delete a workflow
- workflow management
- create a new schedule
- list users
- delete schedule
- data engineering
- list all stored credentials
- upload a new workflow package
- deactivate a user account
- get workflow questions
- analytics
- get user
- data science
- alteryx
- list schedules
- create and execute a workflow job
- automation
- create credential
- delete workflow
- delete a workflow schedule
- get execution jobs for a workflow
- list all users on the server
- create a new credential
- data preparation
- list all schedules
- list collections
- get analytic app questions for a workflow
- list all workflows on the alteryx server
- download workflow
- delete a collection
slug: analytics-automation
tags:
- Alteryx
- Analytics
- Automation
- Data Engineering
tools:
- description: List all workflows on the Alteryx Server
  hints:
    openWorld: true
    readOnly: true
  name: list-workflows
- description: Get details of a specific workflow
  hints:
    readOnly: true
  name: get-workflow
- description: Upload a new workflow package
  hints:
    readOnly: false
  name: upload-workflow
- description: Update workflow metadata
  hints:
    idempotent: true
    readOnly: false
  name: update-workflow
- description: Delete a workflow
  hints:
    destructive: true
  name: delete-workflow
- description: Download a workflow package
  hints:
    readOnly: true
  name: download-workflow
- description: Get analytic app questions for a workflow
  hints:
    readOnly: true
  name: get-workflow-questions
- description: Get execution jobs for a workflow
  hints:
    readOnly: true
  name: get-workflow-jobs
- description: Create and execute a workflow job
  hints:
    readOnly: false
  name: create-job
- description: List all workflow schedules
  hints:
    readOnly: true
  name: list-schedules
- description: Create a new workflow schedule
  hints:
    readOnly: false
  name: create-schedule
- description: Delete a workflow schedule
  hints:
    destructive: true
  name: delete-schedule
- description: List all users on the server
  hints:
    readOnly: true
  name: list-users
- description: Create a new user
  hints:
    readOnly: false
  name: create-user
- description: Get user details
  hints:
    readOnly: true
  name: get-user
- description: Delete a user
  hints:
    destructive: true
  name: delete-user
- description: Deactivate a user account
  hints:
    readOnly: false
  name: deactivate-user
- description: List all stored credentials
  hints:
    readOnly: true
  name: list-credentials
- description: Create a new credential
  hints:
    readOnly: false
  name: create-credential
- description: List all collections
  hints:
    readOnly: true
  name: list-collections
- description: Create a new collection
  hints:
    readOnly: false
  name: create-collection
- description: Delete a collection
  hints:
    destructive: true
  name: delete-collection
---
