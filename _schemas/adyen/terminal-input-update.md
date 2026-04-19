---
description: 'Definition: Content of the Input Update message. : It conveys update of the display of an Input request in progress.'
layout: schema
name: InputUpdate
properties_list:
- description: ''
  name: MessageReference
  type: object
- description: ''
  name: OutputContent
  type: object
- description: ''
  name: MenuEntry
  type: array
- description: ''
  name: OutputSignature
  type: string
- description: ''
  name: MinLength
  type: integer
- description: ''
  name: MaxLength
  type: integer
- description: ''
  name: MaxDecimalLength
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-input-update-schema.json
slug: terminal-input-update
tags:
- Payments
- Financial Services
- Fintech
title: InputUpdate
---
