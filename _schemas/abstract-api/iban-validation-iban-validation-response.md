---
description: IBAN validation and enrichment response
layout: schema
name: IBANValidationResponse
properties_list:
- description: The IBAN submitted for validation
  name: iban
  type: string
- description: Whether the IBAN is valid
  name: is_valid
  type: boolean
- description: ''
  name: country
  type: object
- description: ''
  name: bank
  type: object
- description: Account number extracted from the IBAN
  name: account_number
  type: string
- description: Check digits from the IBAN
  name: check_digits
  type: string
- description: Whether the country is a SEPA member
  name: sepa_member
  type: boolean
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/iban-validation-iban-validation-response-schema.json
slug: iban-validation-iban-validation-response
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
title: IBANValidationResponse
---
