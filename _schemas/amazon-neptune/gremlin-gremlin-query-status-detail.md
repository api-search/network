---
description: GremlinQueryStatusDetail schema from Neptune
layout: schema
name: GremlinQueryStatusDetail
properties_list:
- description: The unique query identifier.
  name: queryId
  type: string
- description: The Gremlin traversal query string.
  name: queryString
  type: string
- description: Query execution statistics.
  name: queryEvalStats
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/gremlin-gremlin-query-status-detail-schema.json
slug: gremlin-gremlin-query-status-detail
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: GremlinQueryStatusDetail
---
