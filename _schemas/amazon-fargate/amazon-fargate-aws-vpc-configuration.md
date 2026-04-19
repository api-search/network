---
description: VPC configuration for awsvpc network mode
layout: schema
name: AwsVpcConfiguration
properties_list:
- description: Subnets for the task
  name: subnets
  type: array
- description: Security groups
  name: securityGroups
  type: array
- description: Whether to assign a public IP
  name: assignPublicIp
  type: string
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-aws-vpc-configuration-schema.json
slug: amazon-fargate-aws-vpc-configuration
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: AwsVpcConfiguration
---
