---
description: AAD profile for the managed cluster.
layout: schema
name: ManagedClusterAADProfile
properties_list:
- description: Whether to enable managed AAD.
  name: managed
  type: boolean
- description: Whether to enable Azure RBAC for Kubernetes authorization.
  name: enableAzureRBAC
  type: boolean
- description: The list of AAD group object IDs for cluster admin role.
  name: adminGroupObjectIDs
  type: array
- description: The AAD tenant ID for authentication.
  name: tenantID
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-kubernetes-service-managed-cluster-aad-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-aad-profile
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: ManagedClusterAADProfile
---
