---
class_count: 3
classes:
- VATCalculateResponse
- VATRatesResponse
- VATValidationResponse
context_file: json-ld/abstract-api-vat-validation-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/json-ld/abstract-api-vat-validation-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Abstract Api Vat Validation from Abstract API.
layout: jsonld
name: Abstract Api Vat Validation Context
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
  name: amountExclVat
  type: decimal
- container: ''
  name: vatAmount
  type: decimal
- container: ''
  name: amountInclVat
  type: decimal
- container: ''
  name: vatCategory
  type: string
- container: ''
  name: vatRate
  type: decimal
- container: ''
  name: countryCode
  type: string
- container: ''
  name: countryName
  type: string
- container: ''
  name: standardRate
  type: decimal
- container: set
  name: reducedRates
  type: decimal
- container: ''
  name: superReducedRate
  type: decimal
- container: ''
  name: parkingRate
  type: decimal
- container: ''
  name: vatNumber
  type: string
- container: ''
  name: valid
  type: boolean
- container: ''
  name: company
  type: reference
- container: ''
  name: name
  type: ''
- container: ''
  name: address
  type: string
- container: ''
  name: country
  type: reference
- container: ''
  name: code
  type: string
property_count: 18
provider_name: Abstract API
provider_slug: abstract-api
slug: abstract-api-vat-validation-context
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
