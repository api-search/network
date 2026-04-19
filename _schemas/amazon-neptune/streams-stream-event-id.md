---
description: A sequence identifier for a stream event.
layout: schema
name: StreamEventId
properties_list:
- description: The commit (transaction) number.
  name: commitNum
  type: integer
- description: The operation number within the commit.
  name: opNum
  type: integer
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/streams-stream-event-id-schema.json
slug: streams-stream-event-id
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: StreamEventId
---
