---
description: The serialized property graph change data. The type field indicates the element kind.
layout: schema
name: PropertyGraphData
properties_list:
- description: The unique identifier of the element.
  name: id
  type: string
- description: 'The element type: v (vertex), vl (vertex label), vp (vertex property), e (edge), ep (edge property).'
  name: type
  type: string
- description: The property key name.
  name: key
  type: string
- description: The property value with its data type.
  name: value
  type: object
- description: Source vertex ID (for edges only).
  name: from
  type: string
- description: Target vertex ID (for edges only).
  name: to
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/streams-property-graph-data-schema.json
slug: streams-property-graph-data
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: PropertyGraphData
---
