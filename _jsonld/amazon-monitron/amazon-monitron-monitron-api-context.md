---
class_count: 6
classes:
- Tag
- Project
- CreateProjectRequest
- ListProjectsResponse
- createdAt
- updatedAt
context_file: json-ld/amazon-monitron-monitron-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-monitron/refs/heads/main/json-ld/amazon-monitron-monitron-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Monitron Monitron Api from Amazon Monitron.
layout: jsonld
name: Amazon Monitron Monitron Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: projectArn
  type: string
- container: ''
  name: projectName
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: tags
  type: reference
- container: set
  name: items
  type: string
- container: ''
  name: nextToken
  type: string
property_count: 10
provider_name: Amazon Monitron
provider_slug: amazon-monitron
slug: amazon-monitron-monitron-api-context
tags:
- AWS
- Broadcasting
- Media Processing
- Media
- JSON-LD
- Linked Data
- Semantic Web
---
