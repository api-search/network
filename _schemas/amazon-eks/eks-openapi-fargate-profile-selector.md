---
description: FargateProfileSelector schema from Amazon EKS API
layout: schema
name: FargateProfileSelector
properties_list:
- description: The Kubernetes namespace that the selector should match.
  name: namespace
  type: string
- description: The Kubernetes labels that the selector should match.
  name: labels
  type: object
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-fargate-profile-selector-schema.json
slug: eks-openapi-fargate-profile-selector
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: FargateProfileSelector
---
