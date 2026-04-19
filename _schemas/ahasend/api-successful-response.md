---
description: SuccessfulResponse schema from AhaSend API
layout: schema
name: SuccessfulResponse
properties_list:
- description: Number of messages that were queued for sending.
  name: success_count
  type: integer
- description: Number of messages that failed to be queued for sending.
  name: fail_count
  type: integer
- description: List of email addresses that the email was not sent to.
  name: failed_recipients
  type: array
- description: ''
  name: errors
  type: array
provider_name: AhaSend
provider_slug: ahasend
schema_file: json-schema/api-successful-response-schema.json
slug: api-successful-response
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
title: SuccessfulResponse
---
