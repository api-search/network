---
description: Access profile for managed cluster API server.
layout: schema
name: ManagedClusterAPIServerAccessProfile
properties_list:
- description: IP ranges authorized to access the Kubernetes API server.
  name: authorizedIPRanges
  type: array
- description: Whether to create the cluster as a private cluster or not.
  name: enablePrivateCluster
  type: boolean
- description: The private DNS zone mode for the cluster.
  name: privateDNSZone
  type: string
- description: Whether to create a public FQDN for private cluster or not.
  name: enablePrivateClusterPublicFQDN
  type: boolean
- description: Whether to disable run command for the cluster.
  name: disableRunCommand
  type: boolean
- description: Whether to enable API server VNET integration for the cluster.
  name: enableVnetIntegration
  type: boolean
- description: The subnet to be used when API server VNET integration is enabled.
  name: subnetId
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-api-server-access-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-api-server-access-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterAPIServerAccessProfile
---
