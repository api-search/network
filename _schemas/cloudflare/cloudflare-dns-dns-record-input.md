---
description: ''
layout: schema
name: DnsRecordInput
properties_list:
- description: The DNS record name, e.g. example.com.
  name: name
  type: string
- description: The DNS record content value.
  name: content
  type: string
- description: Time to live in seconds. A value of 1 indicates automatic TTL.
  name: ttl
  type: integer
- description: Required for MX, SRV, and URI records. Record priority.
  name: priority
  type: integer
- description: Whether the record is receiving Cloudflare proxy services.
  name: proxied
  type: boolean
- description: A comment about the DNS record.
  name: comment
  type: string
- description: Custom tags for the DNS record.
  name: tags
  type: array
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-dns-dns-record-input-schema.json
slug: cloudflare-dns-dns-record-input
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: DnsRecordInput
---
