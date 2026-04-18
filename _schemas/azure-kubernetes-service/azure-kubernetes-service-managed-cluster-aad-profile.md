---
description: Azure Active Directory configuration for integration with AKS.
layout: schema
name: ManagedClusterAADProfile
properties_list:
- description: Whether to enable managed AAD.
  name: managed
  type: boolean
- description: Whether to enable Azure RBAC for Kubernetes authorization.
  name: enableAzureRBAC
  type: boolean
- description: The list of AAD group object IDs that will have admin role of the cluster.
  name: adminGroupObjectIDs
  type: array
- description: (DEPRECATED) The client AAD application ID. Used for legacy/non-managed AAD.
  name: clientAppID
  type: string
- description: (DEPRECATED) The server AAD application ID. Used for legacy/non-managed AAD.
  name: serverAppID
  type: string
- description: (DEPRECATED) The server AAD application secret. Used for legacy/non-managed AAD.
  name: serverAppSecret
  type: string
- description: The AAD tenant ID to use for authentication. If not specified, will use the tenant of the deployment subscription.
  name: tenantID
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-aad-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-aad-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterAADProfile
---
