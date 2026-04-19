---
class_count: 0
classes: []
context_file: json-ld/allianz-trade-claims-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/json-ld/allianz-trade-claims-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Allianz Trade Claims from Allianz Trade.
layout: jsonld
name: Allianz Trade Claims Context
namespaces:
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
- prefix: trade
  uri: https://api.allianz-trade.com/vocab/
properties:
- container: ''
  name: claimId
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: debtorName
  type: string
- container: ''
  name: debtorId
  type: string
- container: ''
  name: claimAmount
  type: decimal
- container: ''
  name: approvedAmount
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: claimStatus
  type: string
- container: ''
  name: lossDate
  type: date
- container: ''
  name: invoiceReference
  type: string
- container: ''
  name: overdueId
  type: string
- container: ''
  name: submittedAt
  type: dateTime
- container: ''
  name: resolvedAt
  type: dateTime
- container: ''
  name: jobId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: result
  type: ''
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: code
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: requestId
  type: string
- container: list
  name: data
  type: ''
property_count: 22
provider_name: Allianz Trade
provider_slug: allianz-trade-online
slug: allianz-trade-claims-context
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
- JSON-LD
- Linked Data
- Semantic Web
---
