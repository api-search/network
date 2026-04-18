---
description: Security profile for the container service cluster.
layout: schema
name: ManagedClusterSecurityProfile
properties_list:
- description: Microsoft Defender settings for the security profile.
  name: defender
  type: object
- description: Workload identity settings for the security profile.
  name: workloadIdentity
  type: object
- description: Image Cleaner settings for the security profile.
  name: imageCleaner
  type: object
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-security-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-security-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterSecurityProfile
---
