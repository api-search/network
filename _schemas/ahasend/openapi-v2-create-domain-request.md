---
description: CreateDomainRequest schema from AhaSend API
layout: schema
name: CreateDomainRequest
properties_list:
- description: Fully qualified domain name
  name: domain
  type: string
- description: DKIM Private Key for the domain. Only RSA keys with a minimum key size of 2048 bits are supported. **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accoun
  name: dkim_private_key
  type: string
- description: Optional custom tracking subdomain. Omit to use the default on create.
  name: tracking_subdomain
  type: string
- description: Optional custom return-path subdomain. Omit to use the default on create.
  name: return_path_subdomain
  type: string
- description: Optional custom subscription management subdomain. Omit to use the default on create.
  name: subscription_subdomain
  type: string
- description: Optional custom media subdomain. Omit to use the default on create.
  name: media_subdomain
  type: string
- description: Optional custom DKIM rotation interval in days. Only supported for managed DNS domains on eligible plans.
  name: dkim_rotation_interval_days
  type: integer
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-create-domain-request-schema.json
slug: openapi-v2-create-domain-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateDomainRequest
---
