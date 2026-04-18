---
class_count: 4
classes:
- QuerySystem
- Session
- QueryRequest
- QueryResult
context_file: json-ld/teradata-query-service-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/json-ld/teradata-query-service-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Teradata Query Service Api from Teradata.
layout: jsonld
name: Teradata Query Service Api Context
namespaces:
- prefix: td
  uri: https://developer.teradata.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: name
  type: string
- container: ''
  name: host
  type: string
- container: ''
  name: port
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: system
  type: string
- container: ''
  name: database
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: queryId
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: rowCount
  type: integer
- container: set
  name: columns
  type: ''
- container: set
  name: rows
  type: ''
property_count: 13
provider_name: Teradata
provider_slug: teradata
slug: teradata-query-service-api-context
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
- JSON-LD
- Linked Data
- Semantic Web
---
