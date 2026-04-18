---
description: Auto upgrade profile for a managed cluster.
layout: schema
name: ManagedClusterAutoUpgradeProfile
properties_list:
- description: The upgrade channel for auto upgrade.
  name: upgradeChannel
  type: string
- description: The node OS upgrade channel. Manner in which the OS on your nodes is updated.
  name: nodeOSUpgradeChannel
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-auto-upgrade-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-auto-upgrade-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterAutoUpgradeProfile
---
