---
description: ''
layout: schema
name: DnsRecord
properties_list:
- description: The unique identifier of the DNS record.
  name: id
  type: string
- description: The zone identifier.
  name: zone_id
  type: string
- description: The zone name.
  name: zone_name
  type: string
- description: The DNS record name.
  name: name
  type: string
- description: The DNS record content.
  name: content
  type: string
- description: Time to live in seconds.
  name: ttl
  type: integer
- description: Whether the record is proxied through Cloudflare.
  name: proxied
  type: boolean
- description: Whether the record can be proxied.
  name: proxiable
  type: boolean
- description: Whether the record is locked.
  name: locked
  type: boolean
- description: A comment about the DNS record.
  name: comment
  type: string
- description: Custom tags for the DNS record.
  name: tags
  type: array
- description: When the record was created.
  name: created_on
  type: string
- description: When the record was last modified.
  name: modified_on
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-dns-dns-record-schema.json
slug: cloudflare-dns-dns-record
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
title: DnsRecord
---
