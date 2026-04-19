---
class_count: 2
classes:
- GetTotalsRequest
- GetTotalsResponse
context_file: json-ld/adyen-terminal-get-totals-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-get-totals-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Get Totals from Adyen.
layout: jsonld
name: Adyen Terminal Get Totals Context
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
  name: TotalDetails
  type: string
- container: ''
  name: TotalFilter
  type: string
- container: ''
  name: Response
  type: string
- container: ''
  name: POIReconciliationID
  type: integer
- container: set
  name: TransactionTotals
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-get-totals-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
