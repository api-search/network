---
description: Domain-level information
layout: schema
name: DomainInfo
properties_list:
- description: Domain extracted from email
  name: domain
  type: string
- description: Age of the domain in days
  name: domain_age
  type: integer
- description: Whether the domain hosts a live website
  name: is_live_site
  type: boolean
- description: Domain registrar name
  name: registrar
  type: string
- description: URL of the registrar
  name: registrar_url
  type: string
- description: Date the domain was registered
  name: date_registered
  type: string
- description: Date the domain was last renewed
  name: date_last_renewed
  type: string
- description: Date the domain expires
  name: date_expires
  type: string
- description: Whether the TLD is associated with risky domains
  name: is_risky_tld
  type: boolean
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/email-reputation-domain-info-schema.json
slug: email-reputation-domain-info
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
title: DomainInfo
---
