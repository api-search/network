---
description: ''
layout: schema
name: CapacityProviderStrategyItem
properties_list:
- description: The short name of the capacity provider.
  name: capacityProvider
  type: string
- description: The weight value designating the relative percentage of the total number of tasks launched that should use the capacity provider (0-1000).
  name: weight
  type: integer
- description: The number of tasks, at a minimum, to run on the specified capacity provider (0-100000).
  name: base
  type: integer
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-capacity-provider-strategy-item-schema.json
slug: amazon-ecs-capacity-provider-strategy-item
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: CapacityProviderStrategyItem
---
