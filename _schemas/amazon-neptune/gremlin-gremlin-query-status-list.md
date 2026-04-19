---
description: GremlinQueryStatusList schema from Neptune
layout: schema
name: GremlinQueryStatusList
properties_list:
- description: The total number of accepted queries.
  name: acceptedQueryCount
  type: integer
- description: The number of currently running queries.
  name: runningQueryCount
  type: integer
- description: The list of running and waiting queries.
  name: queries
  type: array
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/gremlin-gremlin-query-status-list-schema.json
slug: gremlin-gremlin-query-status-list
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: GremlinQueryStatusList
---
