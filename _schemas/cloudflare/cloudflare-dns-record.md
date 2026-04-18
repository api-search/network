---
description: A DNS record object from the Cloudflare API, representing a single DNS record entry within a zone. Supports all standard record types including A, AAAA, CNAME, MX, TXT, SRV, and more.
layout: schema
name: Cloudflare DNS Record
properties_list:
- description: The unique identifier of the DNS record.
  name: id
  type: string
- description: The zone identifier this record belongs to.
  name: zone_id
  type: string
- description: The domain name of the zone.
  name: zone_name
  type: string
- description: The type of DNS record.
  name: type
  type: string
- description: The DNS record name (fully qualified domain name).
  name: name
  type: string
- description: The value of the DNS record. Content format depends on the record type.
  name: content
  type: string
- description: Time to live in seconds. A value of 1 indicates automatic TTL managed by Cloudflare.
  name: ttl
  type: integer
- description: Record priority, required for MX, SRV, and URI record types.
  name: priority
  type: integer
- description: Whether the record is receiving the performance and security benefits of Cloudflare's proxy.
  name: proxied
  type: boolean
- description: Whether the record can be proxied through Cloudflare.
  name: proxiable
  type: boolean
- description: Whether the record is locked and cannot be modified.
  name: locked
  type: boolean
- description: A comment about the DNS record for documentation purposes.
  name: comment
  type: string
- description: Custom tags for categorizing and filtering DNS records.
  name: tags
  type: array
- description: Structured data for record types that require additional fields (SRV, CAA, SSHFP, etc.).
  name: data
  type: object
- description: Extra Cloudflare-specific metadata about the record.
  name: meta
  type: object
- description: When the record was created.
  name: created_on
  type: string
- description: When the record was last modified.
  name: modified_on
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-dns-record-schema.json
slug: cloudflare-dns-record
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
title: Cloudflare DNS Record
---
