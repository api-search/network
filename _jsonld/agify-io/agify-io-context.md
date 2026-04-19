---
class_count: 2
classes:
- AgePrediction
- name
context_file: json-ld/agify-io-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agify-io/refs/heads/main/json-ld/agify-io-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agify Io from Agify.io.
layout: jsonld
name: Agify Io Context
namespaces:
- prefix: agify
  uri: https://agify.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: count
  type: integer
- container: ''
  name: age
  type: integer
- container: ''
  name: country_id
  type: string
property_count: 3
provider_name: Agify.io
provider_slug: agify-io
slug: agify-io-context
tags:
- Age Prediction
- Name Analysis
- Demographics
- REST API
- JSON-LD
- Linked Data
- Semantic Web
---
