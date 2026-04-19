---
class_count: 4
classes:
- Index
- DataSource
- QueryResult
- Faq
context_file: json-ld/amazon-kendra-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-kendra/refs/heads/main/json-ld/amazon-kendra-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Kendra from Amazon Kendra.
layout: jsonld
name: Amazon Kendra Context
namespaces:
- prefix: kendra
  uri: https://kendra.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
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
  name: edition
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: schedule
  type: string
- container: ''
  name: indexId
  type: string
- container: ''
  name: queryId
  type: string
- container: set
  name: resultItems
  type: ''
- container: ''
  name: totalNumberOfResults
  type: integer
- container: set
  name: facetResults
  type: ''
- container: ''
  name: fileFormat
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
property_count: 16
provider_name: Amazon Kendra
provider_slug: amazon-kendra
slug: amazon-kendra-context
tags:
- AI
- AWS
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
- JSON-LD
- Linked Data
- Semantic Web
---
