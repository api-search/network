---
description: Represents a file attachment on a message.
layout: schema
name: Attachment
properties_list:
- description: Unique identifier for the attachment
  name: id
  type: string
- description: MIME type of the attachment
  name: type
  type: string
- description: URL to access the attachment
  name: url
  type: string
- description: Original filename
  name: filename
  type: string
- description: File size in bytes
  name: size
  type: integer
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-conversations-attachment-schema.json
slug: hubspot-conversations-attachment
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
title: Attachment
---
