---
description: A property graph node as returned by openCypher queries.
layout: schema
name: OpenCypherNode
properties_list:
- description: The unique identifier of the node.
  name: ~id
  type: string
- description: The entity type (always 'node').
  name: ~entityType
  type: string
- description: The labels assigned to the node.
  name: ~labels
  type: array
- description: The node properties as key-value pairs.
  name: ~properties
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/opencypher-open-cypher-node-schema.json
slug: opencypher-open-cypher-node
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: OpenCypherNode
---
