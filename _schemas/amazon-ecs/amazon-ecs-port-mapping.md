---
description: ''
layout: schema
name: PortMapping
properties_list:
- description: The port number on the container bound to the host port.
  name: containerPort
  type: integer
- description: The port number on the container instance to reserve for the container.
  name: hostPort
  type: integer
- description: The protocol used for the port mapping.
  name: protocol
  type: string
- description: The name to use for the port mapping (used with Service Connect).
  name: name
  type: string
- description: The application protocol used for the port mapping.
  name: appProtocol
  type: string
- description: The port number range on the container.
  name: containerPortRange
  type: string
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-port-mapping-schema.json
slug: amazon-ecs-port-mapping
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: PortMapping
---
