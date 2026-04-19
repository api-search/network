---
class_count: 10
classes:
- identifier
- name
- description
- status
- dateCreated
- dateModified
- url
- region
- version
- format
context_file: json-ld/amazon-neptune-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Context
namespaces:
- prefix: neptune
  uri: https://docs.aws.amazon.com/neptune/latest/userguide/
- prefix: aws
  uri: https://aws.amazon.com/
- prefix: rdf
  uri: http://www.w3.org/1999/02/22-rdf-syntax-ns#
- prefix: rdfs
  uri: http://www.w3.org/2000/01/rdf-schema#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: owl
  uri: http://www.w3.org/2002/07/owl#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: void
  uri: http://rdfs.org/ns/void#
- prefix: sd
  uri: http://www.w3.org/ns/sparql-service-description#
- prefix: dcat
  uri: http://www.w3.org/ns/dcat#
- prefix: schema
  uri: https://schema.org/
properties:
- container: ''
  name: NeptuneService
  type: ''
- container: ''
  name: DBCluster
  type: ''
- container: ''
  name: DBInstance
  type: ''
- container: ''
  name: Graph
  type: ''
- container: ''
  name: Vertex
  type: ''
- container: ''
  name: Edge
  type: ''
- container: ''
  name: GremlinQuery
  type: ''
- container: ''
  name: SparqlQuery
  type: ''
- container: ''
  name: OpenCypherQuery
  type: ''
- container: ''
  name: StreamRecord
  type: ''
- container: ''
  name: LoaderJob
  type: ''
- container: ''
  name: MLJob
  type: ''
- container: ''
  name: Snapshot
  type: ''
- container: ''
  name: AnalyticsGraph
  type: ''
- container: ''
  name: provider
  type: reference
property_count: 15
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-context
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
