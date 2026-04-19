---
class_count: 6
classes:
- PropertyGraphData
- PropertyGraphStreamRecord
- PropertyGraphStreamResponse
- SparqlStreamRecord
- SparqlStreamResponse
- StreamEventId
context_file: json-ld/amazon-neptune-streams-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-streams-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Streams from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Streams Context
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
  name: commitNum
  type: integer
- container: ''
  name: commitTimestamp
  type: integer
- container: ''
  name: data
  type: reference
- container: ''
  name: dataType
  type: string
- container: ''
  name: eventId
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: isLastOp
  type: boolean
- container: ''
  name: key
  type: string
- container: ''
  name: lastEventId
  type: string
- container: ''
  name: lastTrxTimestamp
  type: integer
- container: ''
  name: op
  type: string
- container: ''
  name: opNum
  type: integer
- container: set
  name: records
  type: string
- container: ''
  name: stmt
  type: string
- container: ''
  name: to
  type: string
- container: ''
  name: totalRecords
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: reference
property_count: 20
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-streams-context
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
