---
description: Represents a change-log stream record from Neptune Streams. Each record captures a single mutation (ADD or REMOVE) made to graph data. Supports both property graph (PG_JSON format) and RDF (NQUADS format) records.
layout: schema
name: Amazon Neptune Stream Record
properties_list:
- description: The sequence identifier of the last change in the response.
  name: lastEventId
  type: object
- description: Unix epoch timestamp in milliseconds of the last transaction commit.
  name: lastTrxTimestamp
  type: integer
- description: The serialization format of the stream records.
  name: format
  type: string
- description: The array of change-log stream records.
  name: records
  type: array
- description: The total number of records in the response.
  name: totalRecords
  type: integer
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/amazon-neptune-stream-record-schema.json
slug: amazon-neptune-stream-record
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: Amazon Neptune Stream Record
---
