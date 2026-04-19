---
class_count: 2
classes:
- AcidSagaStep
- AcidTransaction
context_file: json-ld/acid-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/json-ld/acid-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acid from ACID.
layout: jsonld
name: Acid Context
namespaces:
- prefix: acid
  uri: https://acid.example.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: compensationEndpoint
  type: reference
- container: ''
  name: durationMs
  type: integer
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: executionTimeMs
  type: decimal
- container: ''
  name: isolationLevel
  type: string
- container: ''
  name: operationId
  type: integer
- container: set
  name: operations
  type: string
- container: ''
  name: retryCount
  type: integer
- container: ''
  name: rollbackReason
  type: string
- container: ''
  name: rowsAffected
  type: integer
- container: ''
  name: sagaId
  type: string
- container: set
  name: savepoints
  type: string
- container: ''
  name: sequence
  type: integer
- container: ''
  name: serviceEndpoint
  type: reference
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: stepId
  type: string
- container: ''
  name: stepName
  type: string
- container: ''
  name: table
  type: string
- container: ''
  name: transactionId
  type: string
- container: ''
  name: type
  type: string
property_count: 22
provider_name: ACID
provider_slug: acid
slug: acid-context
tags:
- ACID
- Database
- Transactions
- Atomicity
- Consistency
- Isolation
- Durability
- Distributed Systems
- JSON-LD
- Linked Data
- Semantic Web
---
