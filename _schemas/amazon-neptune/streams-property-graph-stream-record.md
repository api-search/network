---
description: PropertyGraphStreamRecord schema from Neptune
layout: schema
name: PropertyGraphStreamRecord
properties_list:
- description: Unix epoch timestamp in milliseconds of the transaction commit.
  name: commitTimestamp
  type: integer
- description: ''
  name: eventId
  type: object
- description: ''
  name: data
  type: object
- description: The operation type (ADD or REMOVE).
  name: op
  type: string
- description: True only if this is the last operation in the transaction.
  name: isLastOp
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/streams-property-graph-stream-record-schema.json
slug: streams-property-graph-stream-record
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: PropertyGraphStreamRecord
---
