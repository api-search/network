---
description: A virtual node group (launch specification) defines a set of node configurations within an Ocean cluster, allowing different workloads to run on nodes with specific instance types, labels, and taints.
layout: schema
name: Spot Virtual Node Group
properties_list:
- description: The unique identifier of the virtual node group.
  name: id
  type: string
- description: The name of the virtual node group.
  name: name
  type: string
- description: The identifier of the parent Ocean cluster.
  name: oceanId
  type: string
- description: The AMI or image ID for instances in this virtual node group.
  name: imageId
  type: string
- description: List of allowed instance types for this virtual node group.
  name: instanceTypes
  type: array
- description: Kubernetes labels to apply to nodes in this virtual node group.
  name: labels
  type: array
- description: Kubernetes taints to apply to nodes in this virtual node group.
  name: taints
  type: array
provider_name: Spot
provider_slug: spot
schema_file: json-schema/virtual-node-group.json
slug: virtual-node-group
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot Virtual Node Group
---
