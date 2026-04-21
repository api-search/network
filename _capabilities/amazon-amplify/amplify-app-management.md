---
consumed_apis:
- amazon-amplify
description: Workflow capability for managing full-stack Amplify applications including app creation, branch management, and deployment workflows.
layout: capability
name: Amazon Amplify App Management
operations:
- description: List all Amplify apps.
  method: GET
  name: list-apps
  path: /v1/apps
personas: []
provider_name: Amazon Amplify
provider_slug: amazon-amplify
search_terms:
- hosting
- list all amazon amplify applications in the aws account.
- engineer managing ci/cd pipelines and deployments for amplify applications.
- developer building and deploying web and mobile frontends on aws amplify.
- manage amplify apps, branches, and deployments.
- web applications
- create a new amplify full-stack application connected to a code repository.
- mobile development
- amazon
- frontend
- amplify application management.
- create amplify app
- full stack
- DevOps Engineer
- amplify
- deployment
- list amplify apps
- aws
- Frontend Developer
- list apps
- list all amplify apps.
slug: amplify-app-management
tags:
- Amazon
- Amplify
- AWS
- Deployment
- Frontend
tools:
- description: List all Amazon Amplify applications in the AWS account.
  hints:
    openWorld: false
    readOnly: true
  name: list-amplify-apps
- description: Create a new Amplify full-stack application connected to a code repository.
  hints:
    openWorld: false
    readOnly: false
  name: create-amplify-app
---
