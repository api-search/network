---
description: VATCalculateResponse schema from Abstract API vat-validation
layout: schema
name: VATCalculateResponse
properties_list:
- description: Amount excluding VAT
  name: amount_excl_vat
  type: number
- description: VAT amount
  name: vat_amount
  type: number
- description: Amount including VAT
  name: amount_incl_vat
  type: number
- description: VAT category used
  name: vat_category
  type: string
- description: VAT rate applied
  name: vat_rate
  type: number
- description: ''
  name: country_code
  type: string
- description: ''
  name: country_name
  type: string
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/vat-validation-vat-calculate-response-schema.json
slug: vat-validation-vat-calculate-response
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
title: VATCalculateResponse
---
