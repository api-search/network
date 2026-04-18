---
description: Information about a service principal identity for the cluster to use for manipulating Azure APIs.
layout: schema
name: ManagedClusterServicePrincipalProfile
properties_list:
- description: The ID for the service principal.
  name: clientId
  type: string
- description: The secret password associated with the service principal.
  name: secret
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-service-principal-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-service-principal-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterServicePrincipalProfile
---
