---
description: CreateSuppressionRequest schema from AhaSend API
layout: schema
name: CreateSuppressionRequest
properties_list:
- description: Email address to suppress
  name: email
  type: string
- description: Domain for which to suppress the email
  name: domain
  type: string
- description: Reason for suppression
  name: reason
  type: string
- description: When the suppression expires (RFC3339 format)
  name: expires_at
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-create-suppression-request-schema.json
slug: openapi-v2-create-suppression-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateSuppressionRequest
---
