---
class_count: 3
classes:
- ConvertResponse
- HistoricalRatesResponse
- LiveRatesResponse
context_file: json-ld/abstract-api-exchange-rates-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/json-ld/abstract-api-exchange-rates-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Abstract Api Exchange Rates from Abstract API.
layout: jsonld
name: Abstract Api Exchange Rates Context
namespaces:
- prefix: abstract
  uri: https://abstractapi.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: baseCurrency
  type: string
- container: ''
  name: targetCurrency
  type: string
- container: ''
  name: baseAmount
  type: decimal
- container: ''
  name: convertedAmount
  type: decimal
- container: ''
  name: base
  type: string
- container: ''
  name: date
  type: date
- container: ''
  name: exchangeRates
  type: reference
- container: ''
  name: lastUpdated
  type: integer
property_count: 8
provider_name: Abstract API
provider_slug: abstract-api
slug: abstract-api-exchange-rates-context
tags:
- Avatars
- Company Enrichment
- Contacts
- Currencies
- Email Validation
- Exchange Rates
- IBAN Validation
- Image Processing
- IP Geolocation
- IP Intelligence
- Phone Validation
- Public Holidays
- Screenshots
- Timezones
- VAT Validation
- Web Scraping
- JSON-LD
- Linked Data
- Semantic Web
---
