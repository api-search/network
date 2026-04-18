---
description: ''
layout: schema
name: SecretAttributes
properties_list:
- description: The name of the secret.
  name: name
  type: string
- description: The type of secret credential.
  name: type_of
  type: string
- description: The exchange status of the secret.
  name: status
  type: string
- description: 'The credential payload. Structure varies by type_of: token (token string), simple-http (username/password), oauth2 (client_id/client_secret/token_url), oauth2-google (scopes/authorization).'
  name: credentials
  type: object
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/event-forwarding-secret-attributes-schema.json
slug: event-forwarding-secret-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: SecretAttributes
---
