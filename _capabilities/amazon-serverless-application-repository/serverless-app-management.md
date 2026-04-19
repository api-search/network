---
consumed_apis:
- amazon-serverless-application-repository
description: Unified capability for publishing, discovering, and deploying serverless applications via the AWS Serverless Application Repository. Used by Serverless Developers and Platform Engineers.
layout: capability
name: Amazon SAR Serverless App Management
operations:
- description: Browse the serverless application catalog
  method: GET
  name: list-applications
  path: /v1/applications
- description: Publish a new serverless application
  method: POST
  name: publish-application
  path: /v1/applications
- description: Get application details
  method: GET
  name: get-application
  path: /v1/applications/{applicationId}
- description: List application versions
  method: GET
  name: list-versions
  path: /v1/applications/{applicationId}/versions
- description: Publish a new application version
  method: POST
  name: create-version
  path: /v1/applications/{applicationId}/versions
- description: Deploy a serverless application
  method: POST
  name: deploy
  path: /v1/applications/{applicationId}/deploy
personas: []
provider_name: Amazon Serverless Application Repository
provider_slug: amazon-serverless-application-repository
search_terms:
- devops
- create application version
- get application details
- publish a new application version
- publish a new serverless application
- get application
- publish a new serverless application to the sar
- deploy application
- get details and metadata for a serverless application
- list application versions
- individual application management
- browse the serverless application catalog
- deploy
- Serverless Developer
- application repository
- list all published versions of an application
- create version
- developers who publish and share sam-based serverless applications
- get application policy
- aws lambda-based application development, packaging, and distribution
- deploy a serverless application
- serverless
- get the sharing policy for a published application
- publish a new version of an existing application
- aws
- serverless application catalog management
- engineers who discover and deploy pre-built serverless applications from the repository
- amazon serverless application repository
- list applications
- deploy a serverless application to your aws account
- Platform Engineer
- end-to-end serverless application lifecycle management including publishing, versioning, and deployment
- lambda
- list versions
- application deployment pipeline management via cloudformation
- update metadata for a published serverless application
- browse the serverless application repository catalog
- sam
- application version management
- application deployment via cloudformation
- update application
- publish application
slug: serverless-app-management
tags:
- Amazon Serverless Application Repository
- Serverless
- Lambda
- SAM
- DevOps
tools:
- description: Browse the serverless application repository catalog
  hints:
    idempotent: true
    readOnly: true
  name: list-applications
- description: Publish a new serverless application to the SAR
  hints:
    idempotent: false
    readOnly: false
  name: publish-application
- description: Get details and metadata for a serverless application
  hints:
    idempotent: true
    readOnly: true
  name: get-application
- description: Update metadata for a published serverless application
  hints:
    idempotent: false
    readOnly: false
  name: update-application
- description: List all published versions of an application
  hints:
    idempotent: true
    readOnly: true
  name: list-application-versions
- description: Publish a new version of an existing application
  hints:
    idempotent: false
    readOnly: false
  name: create-application-version
- description: Deploy a serverless application to your AWS account
  hints:
    idempotent: false
    readOnly: false
  name: deploy-application
- description: Get the sharing policy for a published application
  hints:
    idempotent: true
    readOnly: true
  name: get-application-policy
---
