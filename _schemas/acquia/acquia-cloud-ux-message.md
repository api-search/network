---
description: ux-message schema from Acquia Cloud API
layout: schema
name: Ux Message
properties_list:
- description: The message identifier.
  name: id
  type: integer
- description: The message unique identifier.
  name: uuid
  type: string
- description: The message title.
  name: title
  type: string
- description: The message body.
  name: body
  type: string
- description: The message url.
  name: url
  type: string
- description: ''
  name: filters
  type: object
- description: ''
  name: flags
  type: object
- description: The message priority weight.
  name: weight
  type: integer
- description: The UTC timestamp of when the message started.
  name: start_at
  type: string
- description: The UTC timestamp of when the message expires.
  name: expire_at
  type: string
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-ux-message-schema.json
slug: acquia-cloud-ux-message
tags:
- Content
- Experience
title: Ux Message
---
