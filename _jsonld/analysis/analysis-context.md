---
class_count: 3
classes:
- APIAnalysisTool
- name
- description
context_file: json-ld/analysis-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/analysis/refs/heads/main/json-ld/analysis-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Analysis from Analysis.
layout: jsonld
name: Analysis Context
namespaces:
- prefix: analysis
  uri: https://apievangelist.com/schema/analysis/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: url
  type: reference
- container: ''
  name: github
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: license
  type: string
- container: ''
  name: api
  type: boolean
- container: set
  name: tags
  type: ''
property_count: 6
provider_name: Analysis
provider_slug: analysis
slug: analysis-context
tags:
- API Analysis
- API Governance
- API Linting
- API Monitoring
- API Security
- Analytics
- Observability
- Traffic Analysis
- JSON-LD
- Linked Data
- Semantic Web
---
