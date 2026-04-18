---
description: ''
layout: schema
name: CreateClusterRequest
properties_list:
- description: The name of the cluster to create (up to 255 characters). If not specified, the default cluster is created.
  name: clusterName
  type: string
- description: The short names of capacity providers to associate with the cluster.
  name: capacityProviders
  type: array
- description: The default capacity provider strategy for the cluster.
  name: defaultCapacityProviderStrategy
  type: array
- description: The cluster settings (e.g., Container Insights).
  name: settings
  type: array
- description: Metadata tags to apply to the cluster (up to 50).
  name: tags
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-create-cluster-request-schema.json
slug: amazon-ecs-create-cluster-request
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: CreateClusterRequest
---
