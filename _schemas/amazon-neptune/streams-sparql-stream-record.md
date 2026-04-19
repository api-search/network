---
description: SparqlStreamRecord schema from Neptune
layout: schema
name: SparqlStreamRecord
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
schema_file: json-schema/streams-sparql-stream-record-schema.json
slug: streams-sparql-stream-record
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: SparqlStreamRecord
---
