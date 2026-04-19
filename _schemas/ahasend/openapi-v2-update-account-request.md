---
description: UpdateAccountRequest schema from AhaSend API
layout: schema
name: UpdateAccountRequest
properties_list:
- description: Account name
  name: name
  type: string
- description: Account website URL
  name: website
  type: string
- description: Account description (used for account verification)
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
schema_file: json-schema/openapi-v2-update-account-request-schema.json
slug: openapi-v2-update-account-request
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: UpdateAccountRequest
---
