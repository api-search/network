---
description: Email deliverability information
layout: schema
name: Deliverability
properties_list:
- description: Overall deliverability status
  name: status
  type: string
- description: Detailed deliverability reason
  name: status_detail
  type: string
- description: Whether the email format is valid
  name: is_format_valid
  type: boolean
- description: Whether the SMTP server responded positively
  name: is_smtp_valid
  type: boolean
- description: Whether valid MX records exist for the domain
  name: is_mx_valid
  type: boolean
- description: List of MX records for the domain
  name: mx_records
  type: array
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/email-reputation-deliverability-schema.json
slug: email-reputation-deliverability
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
title: Deliverability
---
