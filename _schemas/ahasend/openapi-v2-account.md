---
description: Account schema from AhaSend API
layout: schema
name: Account
properties_list:
- description: Object type identifier
  name: object
  type: string
- description: Unique identifier for the account
  name: id
  type: string
- description: When the account was created
  name: created_at
  type: string
- description: When the account was last updated
  name: updated_at
  type: string
- description: Account name
  name: name
  type: string
- description: Account website URL
  name: website
  type: string
- description: Account description
  name: about
  type: string
- description: Default open tracking setting
  name: track_opens
  type: boolean
- description: Default click tracking setting
  name: track_clicks
  type: boolean
- description: Whether to reject bad recipients
  name: reject_bad_recipients
  type: boolean
- description: Whether to reject mistyped recipients
  name: reject_mistyped_recipients
  type: boolean
- description: Default message metadata retention in days
  name: message_metadata_retention
  type: integer
- description: Default message data retention in days
  name: message_data_retention
  type: integer
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/openapi-v2-account-schema.json
slug: openapi-v2-account
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: Account
---
