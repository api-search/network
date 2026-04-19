---
class_count: 1
classes:
- LoginRequest
context_file: json-ld/adyen-terminal-login-request-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-login-request-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Login Request from Adyen.
layout: jsonld
name: Adyen Terminal Login Request Context
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
  name: DateTime
  type: dateTime
- container: ''
  name: SaleSoftware
  type: string
- container: ''
  name: SaleTerminalData
  type: string
- container: ''
  name: TrainingModeFlag
  type: boolean
- container: ''
  name: OperatorLanguage
  type: string
- container: ''
  name: OperatorID
  type: string
- container: ''
  name: ShiftNumber
  type: string
- container: ''
  name: TokenRequestedType
  type: string
- container: ''
  name: CustomerOrderReq
  type: string
- container: ''
  name: POISerialNumber
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-login-request-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
