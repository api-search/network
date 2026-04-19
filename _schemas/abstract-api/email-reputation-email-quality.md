---
description: Email quality signals
layout: schema
name: EmailQuality
properties_list:
- description: Quality score from 0.0 to 1.0
  name: score
  type: number
- description: Whether the email is from a free provider
  name: is_free_email
  type: boolean
- description: Whether the username appears suspicious
  name: is_username_suspicious
  type: boolean
- description: Whether the email is from a disposable provider
  name: is_disposable
  type: boolean
- description: Whether the domain accepts all emails
  name: is_catchall
  type: boolean
- description: Whether the email uses a subaddress (+ tag)
  name: is_subaddress
  type: boolean
- description: Whether the email is a role-based address
  name: is_role
  type: boolean
- description: Whether DMARC policy is enforced
  name: is_dmarc_enforced
  type: boolean
- description: Whether SPF is strictly enforced
  name: is_spf_strict
  type: boolean
- description: Minimum estimated age of the email in days
  name: minimum_age
  type: integer
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/email-reputation-email-quality-schema.json
slug: email-reputation-email-quality
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
title: EmailQuality
---
