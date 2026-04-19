---
description: IP geolocation response data
layout: schema
name: IPGeolocationResponse
properties_list:
- description: The queried IP address
  name: ip_address
  type: string
- description: City name
  name: city
  type: string
- description: Geonames ID for the city
  name: city_geoname_id
  type: integer
- description: Region or state name
  name: region
  type: string
- description: ISO region code
  name: region_iso_code
  type: string
- description: Geonames ID for the region
  name: region_geoname_id
  type: integer
- description: Postal or ZIP code
  name: postal_code
  type: string
- description: Country name
  name: country
  type: string
- description: ISO 3166-1 alpha-2 country code
  name: country_code
  type: string
- description: Geonames ID for the country
  name: country_geoname_id
  type: integer
- description: Whether the country is in the EU
  name: country_is_eu
  type: boolean
- description: Continent name
  name: continent
  type: string
- description: Continent code
  name: continent_code
  type: string
- description: Geonames ID for the continent
  name: continent_geoname_id
  type: integer
- description: Longitude coordinate
  name: longitude
  type: number
- description: Latitude coordinate
  name: latitude
  type: number
- description: ''
  name: security
  type: object
- description: ''
  name: timezone
  type: object
- description: ''
  name: flag
  type: object
- description: ''
  name: currency
  type: object
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/ip-geolocation-ip-geolocation-response-schema.json
slug: ip-geolocation-ip-geolocation-response
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
title: IPGeolocationResponse
---
