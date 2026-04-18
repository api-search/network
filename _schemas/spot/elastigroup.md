---
description: An Elastigroup is a compute group that manages and optimizes cloud instances across spot, reserved, and on-demand capacity to ensure availability at the lowest cost.
layout: schema
name: Spot Elastigroup
properties_list:
- description: The unique identifier of the Elastigroup.
  name: id
  type: string
- description: The name of the Elastigroup.
  name: name
  type: string
- description: A description of the Elastigroup.
  name: description
  type: string
- description: The cloud provider region where the Elastigroup is deployed.
  name: region
  type: string
- description: The capacity configuration for the Elastigroup.
  name: capacity
  type: object
- description: The optimization strategy for the Elastigroup.
  name: strategy
  type: object
- description: The compute configuration for the Elastigroup.
  name: compute
  type: object
- description: The timestamp when the Elastigroup was created.
  name: createdAt
  type: string
- description: The timestamp when the Elastigroup was last updated.
  name: updatedAt
  type: string
provider_name: Spot
provider_slug: spot
schema_file: json-schema/elastigroup.json
slug: elastigroup
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot Elastigroup
---
