---
description: LiveRatesResponse schema from Abstract API exchange-rates
layout: schema
name: LiveRatesResponse
properties_list:
- description: Base currency code
  name: base
  type: string
- description: Unix timestamp of last update
  name: last_updated
  type: integer
- description: Map of currency codes to exchange rates
  name: exchange_rates
  type: object
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/exchange-rates-live-rates-response-schema.json
slug: exchange-rates-live-rates-response
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
title: LiveRatesResponse
---
