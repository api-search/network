---
description: Represents a Neptune Analytics graph resource, which is a memory-optimized graph database instance for analytical workloads with support for openCypher queries, vector search, and optimized graph algorithms.
layout: schema
name: Amazon Neptune Analytics Graph
properties_list:
- description: The unique identifier of the graph, assigned by Neptune Analytics.
  name: id
  type: string
- description: The name of the graph.
  name: name
  type: string
- description: The name of the graph (used in creation requests).
  name: graphName
  type: string
- description: The Amazon Resource Name (ARN) of the graph.
  name: arn
  type: string
- description: The current status of the graph resource.
  name: status
  type: string
- description: The reason for the current status, if applicable.
  name: statusReason
  type: string
- description: The time the graph was created.
  name: createTime
  type: string
- description: The provisioned memory size in Neptune Capacity Units (NCUs). Each NCU provides approximately 2 GiB of memory.
  name: provisionedMemory
  type: integer
- description: The DNS endpoint for connecting to the graph.
  name: endpoint
  type: string
- description: Whether the graph can be accessed over the public internet.
  name: publicConnectivity
  type: boolean
- description: Configuration for vector search capabilities.
  name: vectorSearchConfiguration
  type: object
- description: The number of read replicas for the graph.
  name: replicaCount
  type: integer
- description: The KMS key identifier used for encryption at rest.
  name: kmsKeyIdentifier
  type: string
- description: The ID of the source snapshot if the graph was restored from a snapshot.
  name: sourceSnapshotId
  type: string
- description: Whether deletion protection is enabled for the graph.
  name: deletionProtection
  type: boolean
- description: The build number of the Neptune Analytics engine.
  name: buildNumber
  type: string
- description: Tags assigned to the graph as key-value pairs.
  name: tags
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/amazon-neptune-analytics-graph-schema.json
slug: amazon-neptune-analytics-graph
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: Amazon Neptune Analytics Graph
---
