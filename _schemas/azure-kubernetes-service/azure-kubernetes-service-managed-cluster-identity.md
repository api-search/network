---
description: Identity for the managed cluster.
layout: schema
name: ManagedClusterIdentity
properties_list:
- description: The principal id of the system assigned identity associated with this resource.
  name: principalId
  type: string
- description: The tenant id of the system assigned identity associated with this resource.
  name: tenantId
  type: string
- description: The type of identity used for the managed cluster.
  name: type
  type: string
- description: The keys must be ARM resource IDs in the form of /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.
  name: userAssignedIdentities
  type: object
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-identity-schema.json
slug: azure-kubernetes-service-managed-cluster-identity
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterIdentity
---
