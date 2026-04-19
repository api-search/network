---
description: APIKeyScope schema from AhaSend API
layout: schema
name: APIKeyScope
properties_list:
- description: Unique identifier for the scope
  name: id
  type: string
- description: When the scope was created
  name: created_at
  type: string
- description: When the scope was last updated
  name: updated_at
  type: string
- description: ID of the API key this scope belongs to
  name: api_key_id
  type: string
- description: The scope string
  name: scope
  type: string
- description: Domain ID for domain-specific scopes
  name: domain_id
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-api-key-scope-schema.json
slug: openapi-v2-api-key-scope
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: APIKeyScope
---
