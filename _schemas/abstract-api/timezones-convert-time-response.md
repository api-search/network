---
description: Time zone conversion result
layout: schema
name: ConvertTimeResponse
properties_list:
- description: Source location
  name: base_location
  type: string
- description: Input date and time
  name: base_datetime
  type: string
- description: Source IANA timezone name
  name: base_timezone_name
  type: string
- description: Source timezone abbreviation
  name: base_timezone_abbreviation
  type: string
- description: Source UTC offset in hours
  name: base_utc_offset
  type: integer
- description: Target location
  name: target_location
  type: string
- description: Converted date and time
  name: target_datetime
  type: string
- description: Target IANA timezone name
  name: target_timezone_name
  type: string
- description: Target timezone abbreviation
  name: target_timezone_abbreviation
  type: string
- description: Target UTC offset in hours
  name: target_utc_offset
  type: integer
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/timezones-convert-time-response-schema.json
slug: timezones-convert-time-response
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
title: ConvertTimeResponse
---
