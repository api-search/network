---
description: Input schema from Adyen API
layout: schema
name: Input
properties_list:
- description: ''
  name: InputCommand
  type: object
- description: ''
  name: ConfirmedFlag
  type: boolean
- description: ''
  name: FunctionKey
  type: integer
- description: ''
  name: TextInput
  type: string
- description: ''
  name: DigitInput
  type: integer
- description: ''
  name: Password
  type: string
- description: ''
  name: MenuEntryNumber
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-input-schema.json
slug: terminal-input
tags:
- Payments
- Financial Services
- Fintech
title: Input
---
