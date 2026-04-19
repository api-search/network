---
description: Schema for an Amazon SES email message object defining the content structure including simple, raw, and template-based email formats.
layout: schema
name: EmailMessage
properties_list:
- description: The simple email message with subject and body content.
  name: Simple
  type: object
- description: The raw email message in MIME format.
  name: Raw
  type: object
- description: The template-based email message.
  name: Template
  type: object
- description: The email address to use as the From address for the message.
  name: FromEmailAddress
  type: string
- description: The recipients of the email message.
  name: Destination
  type: object
- description: The reply-to email addresses for the message.
  name: ReplyToAddresses
  type: array
- description: The name of the configuration set to use when sending the email.
  name: ConfigurationSetName
  type: string
provider_name: Amazon SES
provider_slug: amazon-ses
schema_file: json-schema/amazon-ses-emailmessage-schema.json
slug: amazon-ses-emailmessage
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
