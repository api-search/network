---
description: Describes a model deployment.
layout: schema
name: Deployment
properties_list:
- description: The deployment identifier.
  name: id
  type: string
- description: ''
  name: object
  type: string
- description: The Unix timestamp when the deployment was created.
  name: created_at
  type: integer
- description: The Unix timestamp when the deployment was last updated.
  name: updated_at
  type: integer
- description: The model identifier deployed.
  name: model
  type: string
- description: The owner of the deployment.
  name: owner
  type: string
- description: The current status of the deployment.
  name: status
  type: string
- description: The deployment scale settings.
  name: scale_settings
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-deployment-schema.json
slug: azure-openai-service-deployment
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Deployment
---
