---
description: Deployment properties with additional details.
layout: schema
name: DeploymentPropertiesExtended
properties_list:
- description: Denotes the state of provisioning.
  name: provisioningState
  type: string
- description: The correlation ID of the deployment.
  name: correlationId
  type: string
- description: The timestamp of the template deployment.
  name: timestamp
  type: string
- description: The duration of the template deployment.
  name: duration
  type: string
- description: Key/value pairs that represent deployment output.
  name: outputs
  type: object
- description: The deployment mode.
  name: mode
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-resource-manager-deployment-properties-extended-schema.json
slug: azure-resource-manager-deployment-properties-extended
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: DeploymentPropertiesExtended
---
