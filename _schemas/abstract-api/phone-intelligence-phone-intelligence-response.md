---
description: Phone number intelligence response
layout: schema
name: PhoneIntelligenceResponse
properties_list:
- description: The phone number in E.164 format
  name: phone
  type: string
- description: Whether the phone number is valid
  name: valid
  type: boolean
- description: ''
  name: country
  type: object
- description: Geographic location of the phone number
  name: location
  type: string
- description: Line type
  name: type
  type: string
- description: Carrier or service provider
  name: carrier
  type: string
- description: Whether the number is a VoIP number
  name: is_voip
  type: boolean
- description: Risk score from 0 (low risk) to 100 (high risk)
  name: risk_score
  type: integer
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/phone-intelligence-phone-intelligence-response-schema.json
slug: phone-intelligence-phone-intelligence-response
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
title: PhoneIntelligenceResponse
---
