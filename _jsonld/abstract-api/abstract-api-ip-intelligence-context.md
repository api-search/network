---
class_count: 8
classes:
- ASNInfo
- CompanyBasic
- CurrencyInfo
- FlagInfo
- IPIntelligenceResponse
- IPSecurityFlags
- LocationInfo
- TimezoneInfo
context_file: json-ld/abstract-api-ip-intelligence-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/json-ld/abstract-api-ip-intelligence-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Abstract Api Ip Intelligence from Abstract API.
layout: jsonld
name: Abstract Api Ip Intelligence Context
namespaces:
- prefix: abstract
  uri: https://abstractapi.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: asn
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: domain
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: isoCode
  type: string
- container: ''
  name: symbol
  type: string
- container: ''
  name: emoji
  type: string
- container: ''
  name: unicode
  type: string
- container: ''
  name: png
  type: reference
- container: ''
  name: svg
  type: reference
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: security
  type: string
- container: ''
  name: company
  type: string
- container: set
  name: domains
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: timezone
  type: string
- container: ''
  name: flag
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: isVpn
  type: boolean
- container: ''
  name: isProxy
  type: boolean
- container: ''
  name: isTor
  type: boolean
- container: ''
  name: isHosting
  type: boolean
- container: ''
  name: isRelay
  type: boolean
- container: ''
  name: isMobile
  type: boolean
- container: ''
  name: isAbuse
  type: boolean
- container: ''
  name: city
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: abbreviation
  type: string
- container: ''
  name: utcOffset
  type: integer
- container: ''
  name: localTime
  type: string
- container: ''
  name: isDst
  type: boolean
property_count: 35
provider_name: Abstract API
provider_slug: abstract-api
slug: abstract-api-ip-intelligence-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
