---
class_count: 5
classes:
- SparqlErrorResponse
- SparqlQueryStatusDetail
- SparqlQueryStatusList
- SparqlRequestBody
- SparqlSelectResponse
context_file: json-ld/amazon-neptune-sparql-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-sparql-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Sparql from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Sparql Context
namespaces:
- prefix: neptune
  uri: https://neptune.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: acceptedQueryCount
  type: integer
- container: set
  name: bindings
  type: reference
- container: ''
  name: boolean
  type: boolean
- container: ''
  name: cancelled
  type: boolean
- container: ''
  name: code
  type: string
- container: ''
  name: detailedMessage
  type: string
- container: ''
  name: elapsed
  type: integer
- container: ''
  name: head
  type: reference
- container: set
  name: link
  type: string
- container: set
  name: queries
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: queryEvalStats
  type: reference
- container: ''
  name: queryId
  type: string
- container: ''
  name: queryString
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: results
  type: reference
- container: ''
  name: runningQueryCount
  type: integer
- container: ''
  name: update
  type: string
- container: ''
  name: using-graph-uri
  type: string
- container: ''
  name: using-named-graph-uri
  type: string
- container: set
  name: vars
  type: string
- container: ''
  name: waited
  type: integer
property_count: 22
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-sparql-context
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
- JSON-LD
- Linked Data
- Semantic Web
---
