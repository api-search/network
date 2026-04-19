---
description: Port mapping for a container
layout: schema
name: PortMapping
properties_list:
- description: Container port
  name: containerPort
  type: integer
- description: Host port
  name: hostPort
  type: integer
- description: Protocol
  name: protocol
  type: string
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-port-mapping-schema.json
slug: amazon-fargate-port-mapping
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: PortMapping
---
