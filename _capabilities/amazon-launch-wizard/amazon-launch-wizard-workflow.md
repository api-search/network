---
consumed_apis:
- launch-wizard
description: Unified workflow capability for Amazon Launch Wizard combining resource management and operations.
layout: capability
name: Amazon Launch Wizard Workflow
operations: []
personas: []
provider_name: Amazon Launch Wizard
provider_slug: amazon-launch-wizard
search_terms:
- deployments get deployment
- deployments create deployment
- amazon launch wizard
- creates a deployment for the given workload.
- integrates api into applications
- manages resources and configurations
- unified workflow for amazon launch wizard resource management
- aws
- deployments list deployments
- returns information about the deployment.
- deployment
- enterprise applications
- sap
- Administrator
- sql server
- workflow
- lists the deployments that have been created.
- Developer
slug: amazon-launch-wizard-workflow
tags:
- Amazon Launch Wizard
- AWS
- Workflow
tools:
- description: Creates a deployment for the given workload.
  hints:
    idempotent: false
    readOnly: false
  name: deployments-create-deployment
- description: Lists the deployments that have been created.
  hints:
    idempotent: true
    readOnly: true
  name: deployments-list-deployments
- description: Returns information about the deployment.
  hints:
    idempotent: true
    readOnly: true
  name: deployments-get-deployment
---
