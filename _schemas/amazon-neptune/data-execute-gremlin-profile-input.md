---
description: ExecuteGremlinProfileInput schema from Neptune
layout: schema
name: ExecuteGremlinProfileInput
properties_list:
- description: The Gremlin traversal query string to profile.
  name: gremlin
  type: string
- description: Whether to include results in the profile output.
  name: results
  type: boolean
- description: Maximum length of result string per entry.
  name: chop
  type: integer
- description: The serialization format for results.
  name: serializer
  type: string
- description: Whether to include index operation details.
  name: indexOps
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/data-execute-gremlin-profile-input-schema.json
slug: data-execute-gremlin-profile-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: ExecuteGremlinProfileInput
---
