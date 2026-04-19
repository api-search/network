---
class_count: 4
classes:
- StoreDetailAndSubmitRequest
- StoreDetailAndSubmitResponse
- StoreDetailRequest
- StoreDetailResponse
context_file: json-ld/adyen-payouts-store-detail-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payouts-store-detail-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payouts Store Detail from Adyen.
layout: jsonld
name: Adyen Payouts Store Detail Context
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
  name: additionalData
  type: reference
- container: ''
  name: amount
  type: string
- container: ''
  name: bank
  type: string
- container: ''
  name: billingAddress
  type: string
- container: ''
  name: card
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: entityType
  type: string
- container: ''
  name: fraudOffset
  type: integer
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: nationality
  type: string
- container: ''
  name: recurring
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: selectedBrand
  type: string
- container: ''
  name: shopperEmail
  type: string
- container: ''
  name: shopperName
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: shopperStatement
  type: string
- container: ''
  name: socialSecurityNumber
  type: string
- container: ''
  name: telephoneNumber
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: refusalReason
  type: string
- container: ''
  name: resultCode
  type: string
- container: ''
  name: recurringDetailReference
  type: string
property_count: 23
provider_name: Adyen
provider_slug: adyen
slug: adyen-payouts-store-detail-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
