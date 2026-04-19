---
class_count: 4
classes:
- SettlementEvent
- TransactionEvent
- SettlementEventSummary
- Transaction
context_file: json-ld/affirm-transactions-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/json-ld/affirm-transactions-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Affirm Transactions from affirm.
layout: jsonld
name: Affirm Transactions Context
namespaces:
- prefix: affirm
  uri: https://affirm.com/schema/
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
  name: transactionId
  type: string
- container: ''
  name: transactionEventId
  type: string
- container: ''
  name: amount
  type: integer
- container: ''
  name: currency
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: type
  type: string
- container: ''
  name: fee
  type: integer
- container: ''
  name: referenceId
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: totalAmount
  type: integer
- container: ''
  name: eventCount
  type: integer
- container: ''
  name: disbursedAt
  type: dateTime
- container: ''
  name: checkoutId
  type: string
- container: ''
  name: orderId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: amountRefunded
  type: integer
- container: ''
  name: authorizationExpiration
  type: dateTime
- container: ''
  name: providerId
  type: integer
- container: ''
  name: removeTax
  type: boolean
- container: set
  name: events
  type: string
- container: ''
  name: token
  type: string
property_count: 22
provider_name: affirm
provider_slug: affirm
slug: affirm-transactions-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
