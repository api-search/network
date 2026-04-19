---
class_count: 5
classes:
- Jobs
- JobSpec
- JobStatus
- Error
- name
context_file: json-ld/42crunch-scand-manager-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/json-ld/42crunch-scand-manager-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 42Crunch Scand Manager from 42Crunch.
layout: jsonld
name: 42Crunch Scand Manager Context
namespaces:
- prefix: 42c
  uri: https://42crunch.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: jobs
  type: string
- container: ''
  name: token
  type: string
- container: ''
  name: expirationTime
  type: integer
- container: ''
  name: platformService
  type: string
- container: ''
  name: scandImage
  type: string
- container: ''
  name: env
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: error
  type: string
property_count: 8
provider_name: 42Crunch
provider_slug: 42crunch
slug: 42crunch-scand-manager-context
tags:
- API Security
- Platform
- Scanning
- Security
- OpenAPI
- DevSecOps
- JSON-LD
- Linked Data
- Semantic Web
---
