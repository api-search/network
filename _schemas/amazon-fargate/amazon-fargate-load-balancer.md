---
description: Load balancer configuration for a service
layout: schema
name: LoadBalancer
properties_list:
- description: Target group ARN
  name: targetGroupArn
  type: string
- description: Load balancer name
  name: loadBalancerName
  type: string
- description: Container name
  name: containerName
  type: string
- description: Container port
  name: containerPort
  type: integer
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-load-balancer-schema.json
slug: amazon-fargate-load-balancer
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: LoadBalancer
---
