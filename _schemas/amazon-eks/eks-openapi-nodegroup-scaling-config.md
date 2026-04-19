---
description: NodegroupScalingConfig schema from Amazon EKS API
layout: schema
name: NodegroupScalingConfig
properties_list:
- description: The minimum number of nodes.
  name: minSize
  type: integer
- description: The maximum number of nodes.
  name: maxSize
  type: integer
- description: The current number of nodes.
  name: desiredSize
  type: integer
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-nodegroup-scaling-config-schema.json
slug: eks-openapi-nodegroup-scaling-config
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: NodegroupScalingConfig
---
