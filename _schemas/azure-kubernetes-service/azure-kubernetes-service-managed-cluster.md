---
description: Managed cluster resource representing an Azure Kubernetes Service cluster.
layout: schema
name: ManagedCluster
properties_list:
- description: 'Fully qualified resource ID for the resource. Example: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}'
  name: id
  type: string
- description: The name of the resource.
  name: name
  type: string
- description: 'The type of the resource. Example: Microsoft.ContainerService/managedClusters'
  name: type
  type: string
- description: The geo-location where the resource lives.
  name: location
  type: string
- description: Resource tags.
  name: tags
  type: object
- description: This is primarily used to expose different UI experiences in the portal for different kinds.
  name: kind
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-schema.json
slug: azure-kubernetes-service-managed-cluster
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedCluster
---
