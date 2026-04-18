---
description: A standard error response from the Mandrill API.
layout: schema
name: Error
properties_list:
- description: Always "error" for error responses.
  name: status
  type: string
- description: The numeric error code.
  name: code
  type: integer
- description: The name/type of the error (e.g., Invalid_Key, ValidationError).
  name: name
  type: string
- description: A human-readable description of the error.
  name: message
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-error-schema.json
slug: mailchimp-transactional-error
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: Error
---
