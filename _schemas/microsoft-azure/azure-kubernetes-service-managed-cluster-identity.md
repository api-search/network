---
description: Identity for the managed cluster.
layout: schema
name: ManagedClusterIdentity
properties_list:
- description: The principal ID of the system-assigned identity.
  name: principalId
  type: string
- description: The tenant ID of the system-assigned identity.
  name: tenantId
  type: string
- description: The type of identity used.
  name: type
  type: string
- description: ''
  name: userAssignedIdentities
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-kubernetes-service-managed-cluster-identity-schema.json
slug: azure-kubernetes-service-managed-cluster-identity
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: ManagedClusterIdentity
---
