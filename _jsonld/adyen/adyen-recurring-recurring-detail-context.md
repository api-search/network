---
class_count: 3
classes:
- RecurringDetail
- RecurringDetailWrapper
- name
context_file: json-ld/adyen-recurring-recurring-detail-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-recurring-recurring-detail-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Recurring Recurring Detail from Adyen.
layout: jsonld
name: Adyen Recurring Recurring Detail Context
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
  name: alias
  type: string
- container: ''
  name: aliasType
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
- container: set
  name: contractTypes
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: firstPspReference
  type: string
- container: ''
  name: networkTxReference
  type: string
- container: ''
  name: paymentMethodVariant
  type: string
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: shopperName
  type: string
- container: ''
  name: socialSecurityNumber
  type: string
- container: ''
  name: tokenDetails
  type: string
- container: ''
  name: variant
  type: string
property_count: 16
provider_name: Adyen
provider_slug: adyen
slug: adyen-recurring-recurring-detail-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
