---
consumed_apis:
- amazon-proton
description: Workflow capability for platform engineering teams using Amazon Proton to publish standardized templates and automate infrastructure provisioning for development teams. Covers template management, environment deployment, and service lifecycle management.
layout: capability
name: Amazon Proton Platform Engineering
operations:
- description: List environment templates
  method: GET
  name: list-environment-templates
  path: /v1/environment-templates
- description: Create an environment template
  method: POST
  name: create-environment-template
  path: /v1/environment-templates
- description: List deployed environments
  method: GET
  name: list-environments
  path: /v1/environments
- description: Create an environment from a template
  method: POST
  name: create-environment
  path: /v1/environments
- description: List service templates
  method: GET
  name: list-service-templates
  path: /v1/service-templates
- description: Create a service template
  method: POST
  name: create-service-template
  path: /v1/service-templates
- description: List deployed services
  method: GET
  name: list-services
  path: /v1/services
- description: Create a service from a template
  method: POST
  name: create-service
  path: /v1/services
personas: []
provider_name: Amazon Proton
provider_slug: amazon-proton
search_terms:
- devops
- list environments
- create environment
- list all deployed environments
- list services
- deploy a new application service from a service template
- Application Developer
- list environment templates
- deploys services using self-service templates provided by platform engineers
- list environment templates for standardized infrastructure
- platform engineering
- create a service template
- environment template management for platform engineers
- list service templates available for developer self-service
- infrastructure as code
- platform engineering template and deployment workflow
- deployed service management
- list deployed services
- create service
- create a service from a template
- list deployed environments
- deployed environment management
- create an environment template
- aws
- creates and manages environment and service templates for standardized deployments
- serverless
- amazon
- create an environment from a template
- self-service
- list all deployed services
- Platform Engineer
- create environment template
- service template catalog for developers
- create service template
- ci/cd
- deploy a new environment from a standardized template
- create a new standardized environment template for developers
- create a new service template for standardized application deployments
- templates
- list service templates
slug: platform-engineering
tags:
- Amazon
- AWS
- DevOps
- Platform Engineering
- Infrastructure as Code
- Self-Service
- Templates
tools:
- description: List environment templates for standardized infrastructure
  hints:
    openWorld: true
    readOnly: true
  name: list-environment-templates
- description: Create a new standardized environment template for developers
  hints:
    destructive: false
    readOnly: false
  name: create-environment-template
- description: List all deployed environments
  hints:
    openWorld: true
    readOnly: true
  name: list-environments
- description: Deploy a new environment from a standardized template
  hints:
    destructive: false
    readOnly: false
  name: create-environment
- description: List service templates available for developer self-service
  hints:
    openWorld: true
    readOnly: true
  name: list-service-templates
- description: Create a new service template for standardized application deployments
  hints:
    destructive: false
    readOnly: false
  name: create-service-template
- description: List all deployed services
  hints:
    openWorld: true
    readOnly: true
  name: list-services
- description: Deploy a new application service from a service template
  hints:
    destructive: false
    readOnly: false
  name: create-service
---
