---
description: Properties of the managed cluster.
layout: schema
name: ManagedClusterProperties
properties_list:
- description: The current provisioning state of the managed cluster resource.
  name: provisioningState
  type: string
- description: The max number of agent pools for the managed cluster.
  name: maxAgentPools
  type: integer
- description: The version of Kubernetes specified by the user. Both patch version (e.g. 1.20.13) and minor version (e.g. 1.20) are supported. When a minor version is specified, the latest supported patch version is
  name: kubernetesVersion
  type: string
- description: The version of Kubernetes the Managed Cluster is running.
  name: currentKubernetesVersion
  type: string
- description: This cannot be updated once the Managed Cluster has been created.
  name: dnsPrefix
  type: string
- description: This cannot be updated once the Managed Cluster has been created. Used only with private clusters with custom private DNS zone.
  name: fqdnSubdomain
  type: string
- description: The FQDN of the master pool.
  name: fqdn
  type: string
- description: The FQDN of private cluster.
  name: privateFQDN
  type: string
- description: The special FQDN used by the Azure Portal to access the Managed Cluster. It is only set for private cluster enabled clusters.
  name: azurePortalFQDN
  type: string
- description: Whether to enable Kubernetes Role-Based Access Control.
  name: enableRBAC
  type: boolean
- description: The support plan for the Managed Cluster.
  name: supportPlan
  type: string
- description: If set to true, getting static credentials will be disabled for this cluster.
  name: disableLocalAccounts
  type: boolean
- description: The name of the resource group containing agent pool nodes.
  name: nodeResourceGroup
  type: string
- description: The agent pool properties.
  name: agentPoolProfiles
  type: array
- description: Identities associated with the cluster.
  name: identityProfile
  type: object
- description: The profile of managed cluster add-ons.
  name: addonProfiles
  type: object
- description: The Resource ID of the disk encryption set to use for enabling encryption at rest.
  name: diskEncryptionSetID
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-properties-schema.json
slug: azure-kubernetes-service-managed-cluster-properties
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterProperties
---
