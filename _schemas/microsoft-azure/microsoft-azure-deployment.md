---
description: An Azure Resource Manager deployment represents the process of deploying one or more resources to an Azure subscription, resource group, or management group. Deployments use ARM templates (JSON or Bicep) to define the resources to deploy, their configurations, and dependencies.
layout: schema
name: Azure Resource Manager Deployment
properties_list:
- description: The ID of the deployment.
  name: id
  type: string
- description: The name of the deployment.
  name: name
  type: string
- description: The type of the deployment.
  name: type
  type: string
- description: The location to store the deployment data.
  name: location
  type: string
- description: Deployment properties.
  name: properties
  type: object
- description: Deployment tags.
  name: tags
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/microsoft-azure-deployment-schema.json
slug: microsoft-azure-deployment
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Azure Resource Manager Deployment
---
