---
description: APIKey schema from AhaSend API
layout: schema
name: APIKey
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the API key
  name: id
  type: string
- description: When the API key was created
  name: created_at
  type: string
- description: When the API key was last updated
  name: updated_at
  type: string
- description: When the API key was last used (updates every 5-10 minutes)
  name: last_used_at
  type: string
- description: Account ID this API key belongs to
  name: account_id
  type: string
- description: Human-readable label for the API key
  name: label
  type: string
- description: Public portion of the API key
  name: public_key
  type: string
- description: Secret key (only returned on creation)
  name: secret_key
  type: string
- description: Scopes granted to this API key
  name: scopes
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-api-key-schema.json
slug: openapi-v2-api-key
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: APIKey
---
