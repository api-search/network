---
description: VATRatesResponse schema from Abstract API vat-validation
layout: schema
name: VATRatesResponse
properties_list:
- description: ''
  name: country_code
  type: string
- description: ''
  name: country_name
  type: string
- description: Standard VAT rate percentage
  name: standard_rate
  type: number
- description: Reduced VAT rate percentages
  name: reduced_rates
  type: array
- description: Super reduced VAT rate if applicable
  name: super_reduced_rate
  type: number
- description: Parking VAT rate if applicable
  name: parking_rate
  type: number
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/vat-validation-vat-rates-response-schema.json
slug: vat-validation-vat-rates-response
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
title: VATRatesResponse
---
