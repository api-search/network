---
description: CreateClusterRequest schema from Amazon EKS API
layout: schema
name: CreateClusterRequest
properties_list:
- description: The unique name to give to your cluster.
  name: name
  type: string
- description: The desired Kubernetes version for your cluster.
  name: version
  type: string
- description: The Amazon Resource Name (ARN) of the IAM role.
  name: roleArn
  type: string
- description: ''
  name: resourcesVpcConfig
  type: object
- description: ''
  name: kubernetesNetworkConfig
  type: object
- description: ''
  name: logging
  type: object
- description: ''
  name: tags
  type: object
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-create-cluster-request-schema.json
slug: eks-openapi-create-cluster-request
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: CreateClusterRequest
---
