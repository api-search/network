---
class_count: 4
classes:
- Organization
- Project
- Pipeline
- PipelineExecution
context_file: json-ld/harness-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/json-ld/harness-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Harness from Harness.
layout: jsonld
name: Harness Context
namespaces:
- prefix: harness
  uri: https://harness.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: identifier
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: orgIdentifier
  type: string
- container: ''
  name: color
  type: string
- container: set
  name: tags
  type: ''
property_count: 7
provider_name: Harness
provider_slug: harness
slug: harness-context
tags:
- DevOps
- GitOps
- Internal Developer Portal
- Lifecycle
- Software Delivery
- JSON-LD
- Linked Data
- Semantic Web
---
