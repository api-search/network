---
description: Recipient schema from AhaSend API
layout: schema
name: Recipient
properties_list:
- description: Recipient email address
  name: email
  type: string
- description: Display name for the recipient
  name: name
  type: string
- description: Substitution data for the recipient. Used with jinja2 templating language for dynamic content
  name: substitutions
  type: object
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-recipient-schema.json
slug: openapi-v2-recipient
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Recipient
---
