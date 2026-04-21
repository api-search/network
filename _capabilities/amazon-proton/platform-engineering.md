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
- platform engineering template and deployment workflow
- deployed environment management
- deploy a new environment from a standardized template
- Platform Engineer
- service template catalog for developers
- Application Developer
- list services
- templates
- list environments
- create a service template
- create service template
- list deployed environments
- create an environment template
- deploys services using self-service templates provided by platform engineers
- list deployed services
- create service
- serverless
- devops
- amazon
- list all deployed services
- create a new service template for standardized application deployments
- list service templates available for developer self-service
- create environment
- list environment templates for standardized infrastructure
- create a service from a template
- platform engineering
- list all deployed environments
- deploy a new application service from a service template
- creates and manages environment and service templates for standardized deployments
- create a new standardized environment template for developers
- list service templates
- infrastructure as code
- self-service
- aws
- list environment templates
- ci/cd
- environment template management for platform engineers
- create environment template
- create an environment from a template
- deployed service management
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
