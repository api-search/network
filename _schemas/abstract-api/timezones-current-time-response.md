---
description: Current time and timezone data for a location
layout: schema
name: CurrentTimeResponse
properties_list:
- description: Current date and time in the target timezone
  name: datetime
  type: string
- description: IANA timezone name
  name: timezone_name
  type: string
- description: Human-readable location description
  name: timezone_location
  type: string
- description: Timezone abbreviation
  name: timezone_abbreviation
  type: string
- description: GMT/UTC offset in hours
  name: gmt_offset
  type: integer
- description: Whether daylight saving time is active
  name: is_dst
  type: boolean
- description: The input location string
  name: requested_location
  type: string
- description: Latitude of the location
  name: latitude
  type: number
- description: Longitude of the location
  name: longitude
  type: number
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/timezones-current-time-response-schema.json
slug: timezones-current-time-response
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
title: CurrentTimeResponse
---
