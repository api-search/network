---
description: Deployment resource specific properties
layout: schema
name: DeploymentProperties
properties_list:
- description: Deployment status.
  name: status
  type: integer
- description: Details about deployment status.
  name: message
  type: string
- description: Who authored the deployment.
  name: author
  type: string
- description: Who performed the deployment.
  name: deployer
  type: string
- description: Author email.
  name: author_email
  type: string
- description: Start time.
  name: start_time
  type: string
- description: End time.
  name: end_time
  type: string
- description: True if deployment is currently active, false if completed and null if not started.
  name: active
  type: boolean
- description: Details on deployment.
  name: details
  type: string
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
schema_file: json-schema/azure-functions-deployment-properties-schema.json
slug: azure-functions-deployment-properties
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
title: DeploymentProperties
---
