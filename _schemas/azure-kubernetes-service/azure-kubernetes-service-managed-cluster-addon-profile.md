---
description: A Kubernetes add-on profile for a managed cluster.
layout: schema
name: ManagedClusterAddonProfile
properties_list:
- description: Whether the add-on is enabled or not.
  name: enabled
  type: boolean
- description: Key-value pairs for configuring an add-on.
  name: config
  type: object
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-addon-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-addon-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterAddonProfile
---
