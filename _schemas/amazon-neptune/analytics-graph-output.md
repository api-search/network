---
description: GraphOutput schema from Neptune
layout: schema
name: GraphOutput
properties_list:
- description: The unique identifier of the graph.
  name: id
  type: string
- description: The name of the graph.
  name: name
  type: string
- description: The ARN of the graph.
  name: arn
  type: string
- description: The current status of the graph.
  name: status
  type: string
- description: ''
  name: statusReason
  type: string
- description: ''
  name: createTime
  type: string
- description: ''
  name: provisionedMemory
  type: integer
- description: The DNS endpoint for the graph.
  name: endpoint
  type: string
- description: ''
  name: publicConnectivity
  type: boolean
- description: ''
  name: vectorSearchConfiguration
  type: object
- description: ''
  name: replicaCount
  type: integer
- description: ''
  name: kmsKeyIdentifier
  type: string
- description: ''
  name: sourceSnapshotId
  type: string
- description: ''
  name: deletionProtection
  type: boolean
- description: ''
  name: buildNumber
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/analytics-graph-output-schema.json
slug: analytics-graph-output
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: GraphOutput
---
