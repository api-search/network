---
description: An AKS managed cluster represents a Kubernetes cluster in Azure Kubernetes Service. It defines the cluster configuration including Kubernetes version, node pools, networking, identity, and add-on profiles. AKS manages the Kubernetes control plane while customers manage the worker nodes.
layout: schema
name: Azure Kubernetes Service Managed Cluster
properties_list:
- description: Resource ID.
  name: id
  type: string
- description: The name of the managed cluster resource.
  name: name
  type: string
- description: Resource type.
  name: type
  type: string
- description: The geo-location where the resource lives.
  name: location
  type: string
- description: Resource tags.
  name: tags
  type: object
- description: The managed cluster SKU.
  name: sku
  type: object
- description: The identity of the managed cluster.
  name: identity
  type: object
- description: Properties of a managed cluster.
  name: properties
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/microsoft-azure-managed-cluster-schema.json
slug: microsoft-azure-managed-cluster
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Azure Kubernetes Service Managed Cluster
---
