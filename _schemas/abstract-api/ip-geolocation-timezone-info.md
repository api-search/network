---
description: TimezoneInfo schema from Abstract API ip-geolocation
layout: schema
name: TimezoneInfo
properties_list:
- description: IANA timezone name
  name: name
  type: string
- description: Timezone abbreviation
  name: abbreviation
  type: string
- description: GMT/UTC offset in hours
  name: gmt_offset
  type: integer
- description: Current local time
  name: current_time
  type: string
- description: Whether daylight saving time is active
  name: is_dst
  type: boolean
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/ip-geolocation-timezone-info-schema.json
slug: ip-geolocation-timezone-info
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
title: TimezoneInfo
---
