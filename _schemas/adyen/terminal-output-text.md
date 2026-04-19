---
description: It conveys Information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole Text content. Content of text message to display or print.
layout: schema
name: OutputText
properties_list:
- description: ''
  name: Text
  type: string
- description: ''
  name: CharacterSet
  type: integer
- description: ''
  name: Font
  type: string
- description: ''
  name: StartRow
  type: integer
- description: ''
  name: StartColumn
  type: integer
- description: ''
  name: Color
  type: object
- description: ''
  name: CharacterWidth
  type: object
- description: ''
  name: CharacterHeight
  type: object
- description: ''
  name: CharacterStyle
  type: object
- description: ''
  name: Alignment
  type: object
- description: ''
  name: EndOfLineFlag
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-output-text-schema.json
slug: terminal-output-text
tags:
- Payments
- Financial Services
- Fintech
title: OutputText
---
