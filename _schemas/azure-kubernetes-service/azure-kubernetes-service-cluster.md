---
description: Schema representing an Azure Kubernetes Service (AKS) managed cluster resource, based on the Microsoft.ContainerService/managedClusters resource type from the AKS REST API (api-version 2025-10-01).
layout: schema
name: Azure Kubernetes Service Managed Cluster
properties_list:
- description: 'Fully qualified resource ID for the managed cluster. Format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}'
  name: id
  type: string
- description: The name of the managed cluster resource.
  name: name
  type: string
- description: The resource type.
  name: type
  type: string
- description: The geo-location where the resource lives (e.g., eastus, westeurope).
  name: location
  type: string
- description: Resource tags as key-value pairs.
  name: tags
  type: object
- description: ''
  name: sku
  type: object
- description: This is primarily used to expose different UI experiences in the portal for different kinds.
  name: kind
  type: string
- description: ''
  name: identity
  type: object
- description: ''
  name: extendedLocation
  type: object
- description: ''
  name: systemData
  type: object
- description: ''
  name: properties
  type: object
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-cluster-schema.json
slug: azure-kubernetes-service-cluster
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: Azure Kubernetes Service Managed Cluster
---
