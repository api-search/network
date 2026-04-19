---
description: A property graph relationship as returned by openCypher queries.
layout: schema
name: OpenCypherRelationship
properties_list:
- description: The unique identifier of the relationship.
  name: ~id
  type: string
- description: The entity type (always 'relationship').
  name: ~entityType
  type: string
- description: The ID of the source node.
  name: ~start
  type: string
- description: The ID of the target node.
  name: ~end
  type: string
- description: The relationship type.
  name: ~type
  type: string
- description: The relationship properties as key-value pairs.
  name: ~properties
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/opencypher-open-cypher-relationship-schema.json
slug: opencypher-open-cypher-relationship
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: OpenCypherRelationship
---
