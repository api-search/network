---
class_count: 6
classes:
- PaymentIntent
- Transfer
- Account
- FxQuote
- name
- description
context_file: json-ld/airwallex-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/json-ld/airwallex-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Airwallex from Airwallex.
layout: jsonld
name: Airwallex Context
namespaces:
- prefix: airwallex
  uri: https://airwallex.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: amount
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: merchantOrderId
  type: string
- container: ''
  name: clientSecret
  type: string
- container: ''
  name: sourceAmount
  type: decimal
- container: ''
  name: sourceCurrency
  type: string
- container: ''
  name: targetAmount
  type: decimal
- container: ''
  name: targetCurrency
  type: string
- container: ''
  name: fxRate
  type: decimal
- container: ''
  name: reference
  type: string
- container: ''
  name: fromCurrency
  type: string
- container: ''
  name: toCurrency
  type: string
- container: ''
  name: rate
  type: decimal
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: countryCode
  type: string
- container: ''
  name: primaryCurrency
  type: string
property_count: 19
provider_name: Airwallex
provider_slug: airwallex
slug: airwallex-context
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
- JSON-LD
- Linked Data
- Semantic Web
---
