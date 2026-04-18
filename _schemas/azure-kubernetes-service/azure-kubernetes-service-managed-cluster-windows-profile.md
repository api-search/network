---
description: Profile for Windows VMs in the managed cluster.
layout: schema
name: ManagedClusterWindowsProfile
properties_list:
- description: The administrator username to use for Windows VMs.
  name: adminUsername
  type: string
- description: The administrator password to use for Windows VMs.
  name: adminPassword
  type: string
- description: The license type to use for Windows VMs.
  name: licenseType
  type: string
- description: Whether to enable CSI proxy.
  name: enableCSIProxy
  type: boolean
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-windows-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-windows-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterWindowsProfile
---
