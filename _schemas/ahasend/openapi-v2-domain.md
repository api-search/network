---
description: Domain schema from AhaSend API
layout: schema
name: Domain
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the domain
  name: id
  type: string
- description: When the domain was created
  name: created_at
  type: string
- description: When the domain was last updated
  name: updated_at
  type: string
- description: The domain name
  name: domain
  type: string
- description: Account ID this domain belongs to
  name: account_id
  type: string
- description: DNS records required for domain verification
  name: dns_records
  type: array
- description: When DNS records were last checked
  name: last_dns_check_at
  type: string
- description: Whether all required DNS records are properly configured
  name: dns_valid
  type: boolean
- description: Custom tracking subdomain. Null means the account or product default is used.
  name: tracking_subdomain
  type: string
- description: Custom return-path subdomain. Null means the account or product default is used.
  name: return_path_subdomain
  type: string
- description: Custom subscription management subdomain. Null means the account or product default is used.
  name: subscription_subdomain
  type: string
- description: Custom media subdomain. Null means the account or product default is used.
  name: media_subdomain
  type: string
- description: Custom DKIM rotation interval in days. Null means the account default is used.
  name: dkim_rotation_interval_days
  type: integer
- description: Whether the standby DKIM slot is ready for rotation.
  name: rotation_ready
  type: boolean
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-domain-schema.json
slug: openapi-v2-domain
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Domain
---
