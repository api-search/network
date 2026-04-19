---
description: DNSRecord schema from AhaSend API
layout: schema
name: DNSRecord
properties_list:
- description: DNS record type (e.g., CNAME, TXT, MX)
  name: type
  type: string
- description: DNS record host/name
  name: host
  type: string
- description: DNS record content/value
  name: content
  type: string
- description: Whether this DNS record is required for domain verification
  name: required
  type: boolean
- description: Whether this DNS record has been propagated and verified
  name: propagated
  type: boolean
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-dns-record-schema.json
slug: openapi-v2-dns-record
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: DNSRecord
---
