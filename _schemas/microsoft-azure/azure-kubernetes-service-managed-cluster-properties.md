---
description: Properties of a managed cluster.
layout: schema
name: ManagedClusterProperties
properties_list:
- description: The current provisioning state.
  name: provisioningState
  type: string
- description: ''
  name: powerState
  type: object
- description: The version of Kubernetes specified by the user.
  name: kubernetesVersion
  type: string
- description: The current version of Kubernetes running on the cluster.
  name: currentKubernetesVersion
  type: string
- description: This cannot be updated once the managed cluster has been created.
  name: dnsPrefix
  type: string
- description: The FQDN of the master pool.
  name: fqdn
  type: string
- description: The FQDN subdomain.
  name: fqdnSubdomain
  type: string
- description: The agent pool properties.
  name: agentPoolProfiles
  type: array
- description: The profile for Linux VMs.
  name: linuxProfile
  type: object
- description: The profile for Windows VMs.
  name: windowsProfile
  type: object
- description: Information about the service principal identity for the cluster.
  name: servicePrincipalProfile
  type: object
- description: The profile of managed cluster add-on.
  name: addonProfiles
  type: object
- description: The name of the resource group containing agent pool nodes.
  name: nodeResourceGroup
  type: string
- description: Whether to enable Kubernetes RBAC.
  name: enableRBAC
  type: boolean
- description: Whether to enable Kubernetes pod security policy (deprecated).
  name: enablePodSecurityPolicy
  type: boolean
- description: Parameters to be applied to the cluster autoscaler.
  name: autoScalerProfile
  type: object
- description: Access profile for managed cluster API server.
  name: apiServerAccessProfile
  type: object
- description: The resource ID of the disk encryption set.
  name: diskEncryptionSetID
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-kubernetes-service-managed-cluster-properties-schema.json
slug: azure-kubernetes-service-managed-cluster-properties
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: ManagedClusterProperties
---
