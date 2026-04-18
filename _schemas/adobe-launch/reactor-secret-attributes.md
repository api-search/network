---
description: ''
layout: schema
name: SecretAttributes
properties_list:
- description: The name of the secret.
  name: name
  type: string
- description: The type of secret.
  name: type_of
  type: string
- description: The exchange status of the secret.
  name: status
  type: string
- description: The credential payload, varies by secret type.
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
schema_file: json-schema/reactor-secret-attributes-schema.json
slug: reactor-secret-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: SecretAttributes
---
