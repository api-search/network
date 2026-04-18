---
consumed_apis:
- productiv-developer
description: Unified workflow for managing SaaS applications, tracking usage and spend, provisioning users, and auditing platform activity using the Productiv Developer API.
layout: capability
name: Productiv SaaS Management
operations:
- description: Obtain an OAuth2 access token.
  method: POST
  name: get-access-token
  path: /v1/token
- description: Register a new application.
  method: POST
  name: setup-application
  path: /v1/applications
- description: Push usage events for an application.
  method: POST
  name: publish-usage-events
  path: /v1/applications/{appId}/usage-events
- description: Push spend data for an application.
  method: POST
  name: publish-spend-data
  path: /v1/applications/{appId}/spend
- description: Add provisioned users.
  method: POST
  name: publish-provisioned-users
  path: /v1/applications/{appId}/users
- description: Retrieve provisioned users.
  method: GET
  name: get-provisioned-users
  path: /v1/applications/{appId}/users
- description: Remove provisioned users.
  method: DELETE
  name: delete-provisioned-users
  path: /v1/applications/{appId}/users
- description: Publish organizational chart data.
  method: PUT
  name: publish-org-chart
  path: /v1/org-chart
- description: Get signed upload URLs.
  method: GET
  name: get-batch-upload-urls
  path: /v1/applications/{appId}/upload
- description: Query all apps in portfolio.
  method: GET
  name: get-app-summaries
  path: /v1/app-summaries
- description: Fetch detailed app information.
  method: GET
  name: get-app-details
  path: /v1/app-details/{applicationId}
- description: List all provisioning workflows.
  method: GET
  name: list-provisioning-workflows
  path: /v1/provisioning-workflows
- description: List execution summaries.
  method: GET
  name: list-provisioning-execution-summaries
  path: /v1/provisioning-workflows/{workflowId}/executions
- description: Get specific execution details.
  method: GET
  name: get-provisioning-workflow-execution
  path: /v1/provisioning-workflows/{workflowId}/executions/{executionId}
- description: Fetch audit events.
  method: GET
  name: get-audit-events
  path: /v1/audit-events
personas: []
provider_name: Productiv
provider_slug: productiv
search_terms:
- retrieve provisioned users.
- get access token
- get signed upload urls.
- manage provisioning workflows.
- get signed upload urls for batch file uploads.
- get batch upload urls
- remove provisioned users.
- query app portfolio.
- publish org chart
- saas management
- manage org chart data.
- get app summaries
- list execution summaries.
- list provisioning workflows
- productiv
- publish organizational chart data.
- manage provisioned users.
- get provisioned users
- get specific execution details.
- application portfolio
- get execution details.
- get provisioning workflow execution
- add provisioned users for an application.
- publish usage events
- register a new connected application.
- data export
- oauth2 token endpoint.
- register a new application.
- spend management
- remove provisioned users from an application.
- batch file upload.
- fetch detailed app information.
- push spend data.
- list all provisioning workflows.
- list provisioning workflow execution summaries.
- fetch audit events for platform activities.
- query all apps in portfolio.
- push spend data for an application.
- get audit events
- setup application
- get details of a specific provisioning workflow execution.
- fetch detailed information about a particular app.
- publish provisioned users
- obtain an oauth2 access token.
- provisioning
- query provisioning executions.
- get app details
- push usage events for an application.
- query audit events.
- add provisioned users.
- push usage events.
- fetch audit events.
- query all apps in your company portfolio.
- manage custom applications.
- list provisioning execution summaries
- delete provisioned users
- usage analytics
- obtain an oauth2 access token using client credentials.
- retrieve the list of users provisioned to an application.
- publish spend data
- fetch detailed app info.
slug: saas-management
tags:
- Productiv
- SaaS Management
- Usage Analytics
- Provisioning
- Data Export
tools:
- description: Obtain an OAuth2 access token using client credentials.
  hints:
    idempotent: false
    readOnly: false
  name: get-access-token
- description: Register a new connected application.
  hints:
    idempotent: false
    readOnly: false
  name: setup-application
- description: Push usage events for an application.
  hints:
    idempotent: false
    readOnly: false
  name: publish-usage-events
- description: Push spend data for an application.
  hints:
    idempotent: false
    readOnly: false
  name: publish-spend-data
- description: Add provisioned users for an application.
  hints:
    idempotent: false
    readOnly: false
  name: publish-provisioned-users
- description: Retrieve the list of users provisioned to an application.
  hints:
    openWorld: true
    readOnly: true
  name: get-provisioned-users
- description: Remove provisioned users from an application.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-provisioned-users
- description: Publish organizational chart data.
  hints:
    idempotent: true
    readOnly: false
  name: publish-org-chart
- description: Get signed upload URLs for batch file uploads.
  hints:
    openWorld: true
    readOnly: true
  name: get-batch-upload-urls
- description: Query all apps in your company portfolio.
  hints:
    openWorld: true
    readOnly: true
  name: get-app-summaries
- description: Fetch detailed information about a particular app.
  hints:
    openWorld: true
    readOnly: true
  name: get-app-details
- description: List all provisioning workflows.
  hints:
    openWorld: true
    readOnly: true
  name: list-provisioning-workflows
- description: List provisioning workflow execution summaries.
  hints:
    openWorld: true
    readOnly: true
  name: list-provisioning-execution-summaries
- description: Get details of a specific provisioning workflow execution.
  hints:
    openWorld: true
    readOnly: true
  name: get-provisioning-workflow-execution
- description: Fetch audit events for platform activities.
  hints:
    openWorld: true
    readOnly: true
  name: get-audit-events
---
