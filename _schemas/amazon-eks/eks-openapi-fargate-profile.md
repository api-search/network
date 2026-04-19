---
description: FargateProfile schema from Amazon EKS API
layout: schema
name: FargateProfile
properties_list:
- description: The name of the Fargate profile.
  name: fargateProfileName
  type: string
- description: The full Amazon Resource Name (ARN) of the Fargate profile.
  name: fargateProfileArn
  type: string
- description: The name of the cluster the Fargate profile is associated with.
  name: clusterName
  type: string
- description: The current status of the Fargate profile.
  name: status
  type: string
- description: The Amazon Resource Name (ARN) of the pod execution role.
  name: podExecutionRoleArn
  type: string
- description: The IDs of subnets to launch pods into.
  name: subnets
  type: array
- description: The selectors to match for pods to use this Fargate profile.
  name: selectors
  type: array
- description: Metadata that assists with categorization and organization.
  name: tags
  type: object
- description: The Unix epoch timestamp at object creation.
  name: createdAt
  type: string
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-fargate-profile-schema.json
slug: eks-openapi-fargate-profile
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: FargateProfile
---
