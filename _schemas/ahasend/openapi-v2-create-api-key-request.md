---
description: CreateAPIKeyRequest schema from AhaSend API
layout: schema
name: CreateAPIKeyRequest
properties_list:
- description: Human-readable label for the API key
  name: label
  type: string
- description: Array of scope strings to grant to this API key
  name: scopes
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-create-api-key-request-schema.json
slug: openapi-v2-create-api-key-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateAPIKeyRequest
---
