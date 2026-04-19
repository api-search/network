---
description: Data breach history for the email
layout: schema
name: BreachInfo
properties_list:
- description: Total number of breaches the email appeared in
  name: total_breaches
  type: integer
- description: Date of the earliest known breach
  name: date_first_breached
  type: string
- description: Date of the most recent breach
  name: date_last_breached
  type: string
- description: Domains where the email was breached
  name: breached_domains
  type: array
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/email-reputation-breach-info-schema.json
slug: email-reputation-breach-info
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
title: BreachInfo
---
