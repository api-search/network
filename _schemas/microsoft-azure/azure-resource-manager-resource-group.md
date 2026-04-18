---
description: Resource group information.
layout: schema
name: ResourceGroup
properties_list:
- description: The ID of the resource group.
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
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-resource-manager-resource-group-schema.json
slug: azure-resource-manager-resource-group
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: ResourceGroup
---
