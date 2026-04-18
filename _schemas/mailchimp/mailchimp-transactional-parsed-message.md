---
description: A parsed MIME message.
layout: schema
name: ParsedMessage
properties_list:
- description: The parsed subject line.
  name: subject
  type: string
- description: The parsed sender email address.
  name: from_email
  type: string
- description: The parsed sender name.
  name: from_name
  type: string
- description: Parsed recipient list.
  name: to
  type: array
- description: All parsed headers.
  name: headers
  type: object
- description: The plain-text body.
  name: text
  type: string
- description: The HTML body.
  name: html
  type: string
- description: Parsed file attachments.
  name: attachments
  type: array
- description: Parsed inline images.
  name: images
  type: array
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/mailchimp-transactional-parsed-message-schema.json
slug: mailchimp-transactional-parsed-message
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: ParsedMessage
---
