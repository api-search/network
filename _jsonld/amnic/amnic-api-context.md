---
class_count: 3
classes:
- FilterRequest
- Filter
- ChartData
context_file: json-ld/amnic-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amnic/refs/heads/main/json-ld/amnic-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amnic Api from Amnic.
layout: jsonld
name: Amnic Api Context
namespaces:
- prefix: amnic
  uri: https://amnic.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: filters
  type: string
- container: ''
  name: filterBy
  type: string
- container: set
  name: values
  type: string
- container: set
  name: headers
  type: string
- container: set
  name: rows
  type: string
property_count: 5
provider_name: Amnic
provider_slug: amnic
slug: amnic-api-context
tags:
- Cloud Cost Observability
- FinOps
- Cloud Cost Management
- Cost Optimization
- Kubernetes
- AWS
- Azure
- Google Cloud
- JSON-LD
- Linked Data
- Semantic Web
---
