---
description: PropertyGraphStreamResponse schema from Neptune
layout: schema
name: PropertyGraphStreamResponse
properties_list:
- description: ''
  name: lastEventId
  type: object
- description: Unix epoch timestamp in milliseconds of the last commit.
  name: lastTrxTimestamp
  type: integer
- description: The serialization format (always PG_JSON for property graph).
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
schema_file: json-schema/streams-property-graph-stream-response-schema.json
slug: streams-property-graph-stream-response
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: PropertyGraphStreamResponse
---
