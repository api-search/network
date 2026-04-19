---
description: EngineStatusOutput schema from Neptune
layout: schema
name: EngineStatusOutput
properties_list:
- description: The status of the Neptune engine (healthy, recovery, etc.).
  name: status
  type: string
- description: The start time of the engine.
  name: startTime
  type: string
- description: The Neptune engine version.
  name: dbEngineVersion
  type: string
- description: The cluster role (writer or reader).
  name: role
  type: string
- description: The DFE query engine status (enabled or viaQueryHint).
  name: dfeQueryEngine
  type: string
- description: ''
  name: gremlin
  type: object
- description: ''
  name: sparql
  type: object
- description: ''
  name: opencypher
  type: object
- description: ''
  name: labMode
  type: object
- description: ''
  name: features
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/data-engine-status-output-schema.json
slug: data-engine-status-output
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: EngineStatusOutput
---
