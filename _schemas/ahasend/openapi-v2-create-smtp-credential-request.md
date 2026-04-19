---
description: CreateSMTPCredentialRequest schema from AhaSend API
layout: schema
name: CreateSMTPCredentialRequest
properties_list:
- description: Credential name
  name: name
  type: string
- description: Whether this is a sandbox credential
  name: sandbox
  type: boolean
- description: Credential scope - "global" or "scoped"
  name: scope
  type: string
- description: Required if scope is "scoped"
  name: domains
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-create-smtp-credential-request-schema.json
slug: openapi-v2-create-smtp-credential-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: CreateSMTPCredentialRequest
---
