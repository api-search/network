---
description: ''
layout: schema
name: ProxyConfiguration
properties_list:
- description: The proxy type. The only supported value is APPMESH.
  name: type
  type: string
- description: The name of the container that will serve as the App Mesh proxy.
  name: containerName
  type: string
- description: ''
  name: properties
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-proxy-configuration-schema.json
slug: amazon-ecs-proxy-configuration
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: ProxyConfiguration
---
