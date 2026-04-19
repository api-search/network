---
class_count: 3
classes:
- EvidenceItem
- Dispute
- EvidenceRequest
context_file: json-ld/affirm-disputes-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/json-ld/affirm-disputes-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Affirm Disputes from affirm.
layout: jsonld
name: Affirm Disputes Context
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
  name: type
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: submittedAt
  type: dateTime
- container: ''
  name: transactionId
  type: string
- container: ''
  name: chargeId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: reasonCode
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
  name: evidenceDueBy
  type: dateTime
- container: ''
  name: closedAt
  type: dateTime
- container: ''
  name: outcome
  type: string
- container: set
  name: evidence
  type: string
- container: set
  name: files
  type: string
- container: ''
  name: explanation
  type: string
- container: ''
  name: trackingNumber
  type: string
- container: ''
  name: shippingCarrier
  type: string
- container: ''
  name: customerCommunication
  type: string
- container: ''
  name: refundPolicyDisclosure
  type: string
property_count: 21
provider_name: affirm
provider_slug: affirm
slug: affirm-disputes-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
