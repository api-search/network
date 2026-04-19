---
description: VpcConfigResponse schema from Amazon EKS API
layout: schema
name: VpcConfigResponse
properties_list:
- description: ''
  name: subnetIds
  type: array
- description: ''
  name: securityGroupIds
  type: array
- description: ''
  name: clusterSecurityGroupId
  type: string
- description: ''
  name: vpcId
  type: string
- description: ''
  name: endpointPublicAccess
  type: boolean
- description: ''
  name: endpointPrivateAccess
  type: boolean
- description: ''
  name: publicAccessCidrs
  type: array
provider_name: Amazon EKS
provider_slug: amazon-eks
schema_file: json-schema/eks-openapi-vpc-config-response-schema.json
slug: eks-openapi-vpc-config-response
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
title: VpcConfigResponse
---
