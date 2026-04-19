---
description: UpdateDomainRequest schema from AhaSend API
layout: schema
name: UpdateDomainRequest
properties_list:
- description: Optional custom tracking subdomain. Omit to leave the current value unchanged.
  name: tracking_subdomain
  type: string
- description: Optional custom return-path subdomain. Omit to leave the current value unchanged.
  name: return_path_subdomain
  type: string
- description: Optional custom subscription management subdomain. Omit to leave the current value unchanged.
  name: subscription_subdomain
  type: string
- description: Optional custom media subdomain. Omit to leave the current value unchanged.
  name: media_subdomain
  type: string
- description: Optional custom DKIM rotation interval in days. Omit to leave the current value unchanged. Only supported for managed DNS domains on eligible plans.
  name: dkim_rotation_interval_days
  type: integer
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-update-domain-request-schema.json
slug: openapi-v2-update-domain-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: UpdateDomainRequest
---
