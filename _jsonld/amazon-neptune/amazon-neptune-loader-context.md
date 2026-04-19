---
class_count: 5
classes:
- LoaderErrorResponse
- LoaderListResponse
- LoaderRequest
- LoaderStartResponse
- LoaderStatusResponse
context_file: json-ld/amazon-neptune-loader-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-loader-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Loader from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Loader Context
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
  name: allowEmptyStrings
  type: boolean
- container: ''
  name: baseUri
  type: string
- container: ''
  name: code
  type: string
- container: set
  name: dependencies
  type: string
- container: ''
  name: detailedMessage
  type: string
- container: ''
  name: failOnError
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: iamRoleArn
  type: string
- container: set
  name: loadIds
  type: string
- container: ''
  name: mode
  type: string
- container: ''
  name: namedGraphUri
  type: string
- container: ''
  name: parallelism
  type: string
- container: ''
  name: parserConfiguration
  type: reference
- container: ''
  name: payload
  type: reference
- container: ''
  name: queueRequest
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: updateSingleCardinalityProperties
  type: string
- container: ''
  name: userProvidedEdgeIds
  type: string
property_count: 21
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-loader-context
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
