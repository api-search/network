---
description: Schema representing an Amazon Elastic Kubernetes Service (EKS) cluster resource.
layout: schema
name: Amazon EKS Cluster
properties_list:
- description: The unique name of the EKS cluster.
  name: name
  type: string
- description: The Amazon Resource Name (ARN) of the cluster.
  name: arn
  type: string
- description: The Kubernetes server version for the cluster.
  name: version
  type: string
- description: The endpoint URL for the Kubernetes API server.
  name: endpoint
  type: string
- description: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane.
  name: roleArn
  type: string
- description: The VPC configuration used by the cluster control plane.
  name: resourcesVpcConfig
  type: object
- description: The Kubernetes network configuration for the cluster.
  name: kubernetesNetworkConfig
  type: object
- description: The logging configuration for the cluster.
  name: logging
  type: object
- description: The current status of the cluster.
  name: status
  type: string
- description: The certificate-authority-data for the cluster.
  name: certificateAuthority
  type: object
- description: The platform version of your Amazon EKS cluster.
  name: platformVersion
  type: string
- description: Metadata tags associated with the cluster.
  name: tags
  type: object
- description: The timestamp when the cluster was created.
  name: createdAt
  type: string
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/amazon-eks-cluster-schema.json
slug: amazon-eks-cluster
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: Amazon EKS Cluster
---
