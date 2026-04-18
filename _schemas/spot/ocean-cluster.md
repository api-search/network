---
description: An Ocean cluster is a serverless Kubernetes infrastructure engine that automatically manages and optimizes cloud infrastructure for containers, handling node provisioning, scaling, and cost optimization.
layout: schema
name: Spot Ocean Cluster
properties_list:
- description: The unique identifier of the Ocean cluster.
  name: id
  type: string
- description: The name of the Ocean cluster.
  name: name
  type: string
- description: The Ocean controller cluster identifier used by the controller pod.
  name: controllerClusterId
  type: string
- description: The cloud provider region where the cluster is deployed.
  name: region
  type: string
- description: The autoscaler configuration for the Ocean cluster.
  name: autoScaler
  type: object
- description: The capacity configuration for the Ocean cluster.
  name: capacity
  type: object
- description: The optimization strategy for the Ocean cluster.
  name: strategy
  type: object
- description: The timestamp when the cluster was created.
  name: createdAt
  type: string
- description: The timestamp when the cluster was last updated.
  name: updatedAt
  type: string
provider_name: Spot
provider_slug: spot
schema_file: json-schema/ocean-cluster.json
slug: ocean-cluster
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot Ocean Cluster
---
