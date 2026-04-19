---
class_count: 2
classes:
- TransactionStatusRequest
- TransactionStatusResponse
context_file: json-ld/adyen-terminal-transaction-status-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-transaction-status-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Transaction Status from Adyen.
layout: jsonld
name: Adyen Terminal Transaction Status Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: MessageReference
  type: string
- container: ''
  name: ReceiptReprintFlag
  type: boolean
- container: set
  name: DocumentQualifier
  type: string
- container: ''
  name: Response
  type: string
- container: ''
  name: RepeatedMessageResponse
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-transaction-status-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
