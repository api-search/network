---
description: SMTPCredential schema from AhaSend API
layout: schema
name: SMTPCredential
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the SMTP credential
  name: id
  type: string
- description: When the credential was created
  name: created_at
  type: string
- description: When the credential was last updated
  name: updated_at
  type: string
- description: Credential name
  name: name
  type: string
- description: SMTP username
  name: username
  type: string
- description: Whether this is a sandbox credential
  name: sandbox
  type: boolean
- description: Credential scope
  name: scope
  type: string
- description: Domains this credential can send from
  name: domains
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-smtp-credential-schema.json
slug: openapi-v2-smtp-credential
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: SMTPCredential
---
