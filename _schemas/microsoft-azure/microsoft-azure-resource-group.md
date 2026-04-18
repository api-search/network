---
description: A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. Resource groups are used to organize resources by lifecycle and security boundary.
layout: schema
name: Azure Resource Group
properties_list:
- description: 'The ID of the resource group. Format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}.'
  name: id
  type: string
- description: The name of the resource group.
  name: name
  type: string
- description: The type of the resource group.
  name: type
  type: string
- description: The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations.
  name: location
  type: string
- description: The ID of the resource that manages this resource group.
  name: managedBy
  type: string
- description: The tags attached to the resource group.
  name: tags
  type: object
- description: The resource group properties.
  name: properties
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/microsoft-azure-resource-group-schema.json
slug: microsoft-azure-resource-group
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Azure Resource Group
---
