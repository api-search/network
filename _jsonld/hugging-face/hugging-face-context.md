---
class_count: 4
classes:
- id
- type
- name
- description
context_file: json-ld/hugging-face-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/json-ld/hugging-face-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hugging Face from Hugging Face.
layout: jsonld
name: Hugging Face Context
namespaces:
- prefix: hf
  uri: https://huggingface.co/ns/
- prefix: schema
  uri: https://schema.org/
- prefix: ml
  uri: http://ml-schema.org/
- prefix: dcat
  uri: http://www.w3.org/ns/dcat#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: foaf
  uri: http://xmlns.com/foaf/0.1/
- prefix: rdfs
  uri: http://www.w3.org/2000/01/rdf-schema#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: sc
  uri: https://schema.org/
- prefix: cr
  uri: http://mlcommons.org/croissant/
properties:
- container: ''
  name: Model
  type: ''
- container: ''
  name: Dataset
  type: ''
- container: ''
  name: Space
  type: ''
- container: ''
  name: InferenceEndpoint
  type: ''
- container: ''
  name: User
  type: ''
- container: ''
  name: Organization
  type: ''
- container: ''
  name: url
  type: reference
- container: ''
  name: dateCreated
  type: dateTime
- container: ''
  name: dateModified
  type: dateTime
- container: ''
  name: author
  type: reference
- container: ''
  name: license
  type: ''
- container: set
  name: keywords
  type: ''
- container: ''
  name: identifier
  type: ''
- container: ''
  name: image
  type: reference
- container: ''
  name: sameAs
  type: reference
property_count: 15
provider_name: Hugging Face
provider_slug: hugging-face
slug: hugging-face-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
