---
description: Nodegroup schema from Amazon EKS API
layout: schema
name: Nodegroup
properties_list:
- description: The name of the managed node group.
  name: nodegroupName
  type: string
- description: The Amazon Resource Name (ARN) of the managed node group.
  name: nodegroupArn
  type: string
- description: The name of the cluster the node group is associated with.
  name: clusterName
  type: string
- description: The Kubernetes version of the managed node group.
  name: version
  type: string
- description: The AMI version of the managed node group.
  name: releaseVersion
  type: string
- description: The current status of the managed node group.
  name: status
  type: string
- description: The capacity type of the managed node group.
  name: capacityType
  type: string
- description: ''
  name: scalingConfig
  type: object
- description: The instance types associated with the managed node group.
  name: instanceTypes
  type: array
- description: The subnets that were specified for the Auto Scaling group.
  name: subnets
  type: array
- description: The AMI type associated with the managed node group.
  name: amiType
  type: string
- description: The IAM role associated with the managed node group.
  name: nodeRole
  type: string
- description: The Kubernetes labels applied to the nodes in the node group.
  name: labels
  type: object
- description: Metadata that assists with categorization and organization.
  name: tags
  type: object
- description: The Unix epoch timestamp at object creation.
  name: createdAt
  type: string
- description: The Unix epoch timestamp for the last modification.
  name: modifiedAt
  type: string
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-nodegroup-schema.json
slug: eks-openapi-nodegroup
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: Nodegroup
---
