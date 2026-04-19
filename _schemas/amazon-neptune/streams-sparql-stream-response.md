---
description: SparqlStreamResponse schema from Neptune
layout: schema
name: SparqlStreamResponse
properties_list:
- description: ''
  name: lastEventId
  type: object
- description: Unix epoch timestamp in milliseconds of the last commit.
  name: lastTrxTimestamp
  type: integer
- description: The serialization format (always NQUADS for RDF).
  name: format
  type: string
- description: The array of change-log stream records.
  name: records
  type: array
- description: Total number of records in the response.
  name: totalRecords
  type: integer
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/streams-sparql-stream-response-schema.json
slug: streams-sparql-stream-response
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: SparqlStreamResponse
---
