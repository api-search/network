---
description: SparqlRequestBody schema from Neptune
layout: schema
name: SparqlRequestBody
properties_list:
- description: A SPARQL 1.1 query (SELECT, ASK, CONSTRUCT, or DESCRIBE). Mutually exclusive with update.
  name: query
  type: string
- description: A SPARQL 1.1 Update operation (INSERT DATA, DELETE DATA, etc.). Mutually exclusive with query.
  name: update
  type: string
- description: Default graph URI for the query.
  name: using-graph-uri
  type: string
- description: Named graph URI for the query.
  name: using-named-graph-uri
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/sparql-sparql-request-body-schema.json
slug: sparql-sparql-request-body
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: SparqlRequestBody
---
