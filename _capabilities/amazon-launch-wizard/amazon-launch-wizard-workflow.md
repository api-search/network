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
- aws
- deployment
- enterprise applications
- lists the deployments that have been created.
- sql server
- deployments list deployments
- Developer
- deployments create deployment
- returns information about the deployment.
- deployments get deployment
- workflow
- Administrator
- manages resources and configurations
- unified workflow for amazon launch wizard resource management
- sap
- integrates api into applications
- amazon launch wizard
- creates a deployment for the given workload.
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
