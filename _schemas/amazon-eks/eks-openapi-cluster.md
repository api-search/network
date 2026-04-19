---
description: Cluster schema from Amazon EKS API
layout: schema
name: Cluster
properties_list:
- description: The name of the cluster.
  name: name
  type: string
- description: The Amazon Resource Name (ARN) of the cluster.
  name: arn
  type: string
- description: The Unix epoch timestamp at object creation.
  name: createdAt
  type: string
- description: The Kubernetes server version for the cluster.
  name: version
  type: string
- description: The endpoint for your Kubernetes API server.
  name: endpoint
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
- description: The current status of the cluster.
  name: status
  type: string
- description: ''
  name: certificateAuthority
  type: object
- description: The platform version of your Amazon EKS cluster.
  name: platformVersion
  type: string
- description: Metadata that assists with categorization and organization.
  name: tags
  type: object
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-cluster-schema.json
slug: eks-openapi-cluster
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: Cluster
---
