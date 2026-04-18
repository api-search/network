---
description: A Kubernetes add-on profile for a managed cluster.
layout: schema
name: ManagedClusterAddonProfile
properties_list:
- description: Whether the add-on is enabled.
  name: enabled
  type: boolean
- description: Key-value pairs for configuring an add-on.
  name: config
  type: object
- description: ''
  name: identity
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-kubernetes-service-managed-cluster-addon-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-addon-profile
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: ManagedClusterAddonProfile
---
