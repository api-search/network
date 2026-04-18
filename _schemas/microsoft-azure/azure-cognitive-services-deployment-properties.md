---
description: Properties of Cognitive Services account deployment.
layout: schema
name: DeploymentProperties
properties_list:
- description: The provisioning state of the deployment.
  name: provisioningState
  type: string
- description: The deployment scale settings.
  name: scaleSettings
  type: object
- description: The rate limits for the deployment.
  name: rateLimits
  type: array
- description: The capabilities of the deployment.
  name: capabilities
  type: object
- description: Deployment model version upgrade option.
  name: versionUpgradeOption
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cognitive-services-deployment-properties-schema.json
slug: azure-cognitive-services-deployment-properties
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: DeploymentProperties
---
