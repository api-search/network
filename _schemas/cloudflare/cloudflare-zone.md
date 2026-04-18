---
description: A zone object from the Cloudflare API, representing a domain and its associated configuration managed through Cloudflare's DNS and proxy services.
layout: schema
name: Cloudflare Zone
properties_list:
- description: The unique identifier of the zone.
  name: id
  type: string
- description: The domain name of the zone.
  name: name
  type: string
- description: The status of the zone.
  name: status
  type: string
- description: Whether the zone is paused, meaning Cloudflare will not proxy traffic.
  name: paused
  type: boolean
- description: The type of zone configuration.
  name: type
  type: string
- description: Seconds remaining in development mode. Zero means development mode is off.
  name: development_mode
  type: integer
- description: Cloudflare-assigned nameservers for the zone.
  name: name_servers
  type: array
- description: The original nameservers before moving to Cloudflare.
  name: original_name_servers
  type: array
- description: The original domain registrar.
  name: original_registrar
  type: string
- description: The original DNS host.
  name: original_dnshost
  type: string
- description: The account that owns the zone.
  name: account
  type: object
- description: The owner of the zone.
  name: owner
  type: object
- description: The plan associated with the zone.
  name: plan
  type: object
- description: Available permissions on the zone.
  name: permissions
  type: array
- description: When the zone was activated on Cloudflare.
  name: activated_on
  type:
  - string
  - 'null'
- description: When the zone was created.
  name: created_on
  type: string
- description: When the zone was last modified.
  name: modified_on
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-zone-schema.json
slug: cloudflare-zone
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
title: Cloudflare Zone
---
