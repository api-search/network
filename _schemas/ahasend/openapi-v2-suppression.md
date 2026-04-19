---
description: Suppression schema from AhaSend API
layout: schema
name: Suppression
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the suppression
  name: id
  type: string
- description: When the suppression was created
  name: created_at
  type: string
- description: When the suppression was last updated
  name: updated_at
  type: string
- description: Suppressed email address
  name: email
  type: string
- description: Domain for which the email is suppressed
  name: domain
  type: string
- description: Reason for suppression
  name: reason
  type: string
- description: When the suppression expires
  name: expires_at
  type: string
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-suppression-schema.json
slug: openapi-v2-suppression
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Suppression
---
