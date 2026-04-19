---
class_count: 1
classes:
- UpdatePaymentMethodInfo
context_file: json-ld/adyen-management-update-payment-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-update-payment-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Update Payment from Adyen.
layout: jsonld
name: Adyen Management Update Payment Context
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
  name: bcmc
  type: string
- container: ''
  name: cartesBancaires
  type: string
- container: set
  name: countries
  type: string
- container: ''
  name: cup
  type: string
- container: set
  name: currencies
  type: string
- container: set
  name: customRoutingFlags
  type: string
- container: ''
  name: diners
  type: string
- container: ''
  name: discover
  type: string
- container: ''
  name: eftposAustralia
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: girocard
  type: string
- container: ''
  name: ideal
  type: string
- container: ''
  name: interacCard
  type: string
- container: ''
  name: jcb
  type: string
- container: ''
  name: maestro
  type: string
- container: ''
  name: mc
  type: string
- container: set
  name: storeIds
  type: string
- container: ''
  name: visa
  type: string
property_count: 18
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-update-payment-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
