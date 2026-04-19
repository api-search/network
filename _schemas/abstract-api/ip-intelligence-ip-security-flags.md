---
description: Security classification flags for the IP
layout: schema
name: IPSecurityFlags
properties_list:
- description: IP is a known VPN endpoint
  name: is_vpn
  type: boolean
- description: IP is a known proxy server
  name: is_proxy
  type: boolean
- description: IP is a Tor exit node
  name: is_tor
  type: boolean
- description: IP belongs to a hosting or cloud provider
  name: is_hosting
  type: boolean
- description: IP is used as a relay (e.g., Apple Private Relay)
  name: is_relay
  type: boolean
- description: IP is associated with a mobile network
  name: is_mobile
  type: boolean
- description: IP has been flagged for abuse
  name: is_abuse
  type: boolean
provider_name: Abstract API
provider_slug: abstract-api
schema_file: json-schema/ip-intelligence-ip-security-flags-schema.json
slug: ip-intelligence-ip-security-flags
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
title: IPSecurityFlags
---
