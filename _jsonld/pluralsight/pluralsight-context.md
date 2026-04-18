---
class_count: 3
classes:
- GraphQLError
- GraphQLRequest
- GraphQLResponse
context_file: json-ld/pluralsight-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/pluralsight/refs/heads/main/json-ld/pluralsight-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Pluralsight from Pluralsight.
layout: jsonld
name: Pluralsight Context
namespaces:
- prefix: ps
  uri: https://developer.pluralsight.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: data
  type: reference
- container: set
  name: errors
  type: string
- container: set
  name: locations
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: operationName
  type: string
- container: set
  name: path
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: variables
  type: reference
property_count: 8
provider_name: Pluralsight
provider_slug: pluralsight
slug: pluralsight-context
tags:
- Courses
- Education
- Engineering Metrics
- Learning
- Skills Assessment
- Technology
- Video Training
- JSON-LD
- Linked Data
- Semantic Web
---
