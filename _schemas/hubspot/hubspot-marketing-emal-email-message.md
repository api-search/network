---
description: The email message configuration
layout: schema
name: EmailMessage
properties_list:
- description: The recipient's email address
  name: to
  type: string
- description: Override the from address (must be verified)
  name: from
  type: string
- description: A unique ID to prevent duplicate sends
  name: sendId
  type: string
- description: Reply-to email addresses
  name: replyTo
  type: array
- description: CC email addresses
  name: cc
  type: array
- description: BCC email addresses
  name: bcc
  type: array
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-marketing-emal-email-message-schema.json
slug: hubspot-marketing-emal-email-message
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: EmailMessage
---
