---
class_count: 5
classes:
- UnifiedAPI
- APICatalogEntry
- name
- description
- provider
context_file: json-ld/aggregation-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aggregation/refs/heads/main/json-ld/aggregation-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aggregation from Aggregation.
layout: jsonld
name: Aggregation Context
namespaces:
- prefix: agg
  uri: https://api-evangelist.github.io/aggregation/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcat
  uri: https://www.w3.org/ns/dcat#
properties:
- container: ''
  name: category
  type: string
- container: ''
  name: baseUrl
  type: reference
- container: ''
  name: base_url
  type: reference
- container: ''
  name: documentationUrl
  type: reference
- container: ''
  name: documentation_url
  type: reference
- container: ''
  name: openapi_url
  type: reference
- container: ''
  name: pricing_model
  type: string
- container: ''
  name: normalized_schema
  type: boolean
- container: set
  name: providers
  type: reference
- container: set
  name: authentication_types
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: status
  type: string
property_count: 12
provider_name: Aggregation
provider_slug: aggregation
slug: aggregation-context
tags:
- API Aggregation
- API Directory
- API Marketplace
- JSON-LD
- Linked Data
- Semantic Web
---
