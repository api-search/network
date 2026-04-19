---
class_count: 1
classes:
- OriginalPOITransaction
context_file: json-ld/adyen-terminal-original-poi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-original-poi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Original Poi from Adyen.
layout: jsonld
name: Adyen Terminal Original Poi Context
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
  name: SaleID
  type: string
- container: ''
  name: POIID
  type: string
- container: ''
  name: POITransactionID
  type: string
- container: ''
  name: ReuseCardDataFlag
  type: boolean
- container: ''
  name: ApprovalCode
  type: string
- container: ''
  name: CustomerLanguage
  type: string
- container: ''
  name: AcquirerID
  type: integer
- container: ''
  name: AmountValue
  type: decimal
- container: ''
  name: HostTransactionID
  type: string
property_count: 9
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-original-poi-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
