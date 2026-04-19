---
description: An object that defines the email message content including simple, raw, and template options.
layout: schema
name: EmailMessage
properties_list:
- description: The simple email message with subject and body.
  name: Simple
  type: object
- description: The raw email message.
  name: Raw
  type: object
- description: The template email message.
  name: Template
  type: object
provider_name: Amazon SES
provider_slug: amazon-ses
schema_file: json-schema/amazon-ses-openapi-email-message-schema.json
slug: amazon-ses-openapi-email-message
tags:
- AWS
- Email
- Email Deliverability
- Email Service
- Marketing Email
- Notifications
- SMTP
- Transactional Email
title: EmailMessage
---
