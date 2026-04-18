---
description: Schema for creating WhatsApp message templates via the Business Management API POST /{waba-id}/message_templates endpoint. Templates must be approved by Meta before use.
layout: schema
name: WhatsApp Message Template
properties_list:
- description: Template name. Must be lowercase with underscores only.
  name: name
  type: string
- description: Language/locale code (e.g., en_US, pt_BR, es)
  name: language
  type: string
- description: Template category determining approval criteria and pricing
  name: category
  type: string
- description: POSITIONAL uses {{1}}, {{2}} placeholders. NAMED uses {{variable_name}}.
  name: parameter_format
  type: string
- description: Template component definitions
  name: components
  type: array
provider_name: WhatsApp
provider_slug: whatsapp
schema_file: json-schema/whatsapp-message-template-schema.json
slug: whatsapp-message-template
tags: []
title: WhatsApp Message Template
---
