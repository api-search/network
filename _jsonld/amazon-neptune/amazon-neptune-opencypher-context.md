---
class_count: 7
classes:
- OpenCypherErrorResponse
- OpenCypherNode
- OpenCypherQueryRequest
- OpenCypherQueryResponse
- OpenCypherQueryStatusDetail
- OpenCypherQueryStatusList
- OpenCypherRelationship
context_file: json-ld/amazon-neptune-opencypher-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-opencypher-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Opencypher from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Opencypher Context
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
- container: set
  name: results
  type: reference
- container: ''
  name: runningQueryCount
  type: integer
- container: ''
  name: waited
  type: integer
- container: ''
  name: ~end
  type: string
- container: ''
  name: ~entityType
  type: string
- container: ''
  name: ~id
  type: string
- container: set
  name: ~labels
  type: string
- container: ''
  name: ~properties
  type: reference
- container: ''
  name: ~start
  type: string
- container: ''
  name: ~type
  type: string
property_count: 21
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-opencypher-context
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
