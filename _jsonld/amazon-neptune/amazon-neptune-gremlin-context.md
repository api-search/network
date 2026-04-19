---
class_count: 5
classes:
- GremlinErrorResponse
- GremlinQueryRequest
- GremlinQueryResponse
- GremlinQueryStatusDetail
- GremlinQueryStatusList
context_file: json-ld/amazon-neptune-gremlin-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-gremlin-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Gremlin from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Gremlin Context
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
- container: ''
  name: attributes
  type: reference
- container: ''
  name: cancelled
  type: boolean
- container: ''
  name: code
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: detailedMessage
  type: string
- container: ''
  name: elapsed
  type: integer
- container: ''
  name: gremlin
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: meta
  type: reference
- container: set
  name: queries
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
  name: result
  type: reference
- container: ''
  name: runningQueryCount
  type: integer
- container: ''
  name: status
  type: reference
- container: ''
  name: subqueries
  type: reference
- container: ''
  name: waited
  type: integer
property_count: 20
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-gremlin-context
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
