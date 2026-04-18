---
description: ''
layout: schema
name: LoadBalancer
properties_list:
- description: The full ARN of the Elastic Load Balancing target group.
  name: targetGroupArn
  type: string
- description: The name of the load balancer (Classic Load Balancer only).
  name: loadBalancerName
  type: string
- description: The name of the container to associate with the load balancer.
  name: containerName
  type: string
- description: The port on the container to associate with the load balancer.
  name: containerPort
  type: integer
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-load-balancer-schema.json
slug: amazon-ecs-load-balancer
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: LoadBalancer
---
