---
description: CreateGraphInput schema from Neptune
layout: schema
name: CreateGraphInput
properties_list:
- description: The name of the graph (1-63 alphanumeric characters or hyphens).
  name: graphName
  type: string
- description: The provisioned memory size in Neptune Capacity Units (NCUs).
  name: provisionedMemory
  type: integer
- description: Tags to assign to the graph.
  name: tags
  type: object
- description: Whether the graph can be reached over the internet.
  name: publicConnectivity
  type: boolean
- description: KMS key identifier for encryption at rest.
  name: kmsKeyIdentifier
  type: string
- description: Vector search configuration for the graph.
  name: vectorSearchConfiguration
  type: object
- description: The number of read replicas.
  name: replicaCount
  type: integer
- description: Whether deletion protection is enabled.
  name: deletionProtection
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/analytics-create-graph-input-schema.json
slug: analytics-create-graph-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateGraphInput
---
