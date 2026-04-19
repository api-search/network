---
class_count: 3
classes:
- TransferRouteRequest
- TransferRouteResponse
- TransferRoute
context_file: json-ld/adyen-configuration-transfer-route-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-transfer-route-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Transfer Route from Adyen.
layout: jsonld
name: Adyen Configuration Transfer Route Context
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
  name: balanceAccountId
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: counterparty
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: currency
  type: string
- container: set
  name: priorities
  type: string
- container: set
  name: transferRoutes
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: requirements
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-transfer-route-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
