---
description: It contains a complete display operation for a Display or an Input Device type. For the Input Devices, Diagnosis and EnableService, ResponseRequiredFlag and MinimumDisplayTime shall be absent. Information to display and the way to process the display.
layout: schema
name: DisplayOutput
properties_list:
- description: Request of a message response.
  name: ResponseRequiredFlag
  type: boolean
- description: Number of seconds the message has to be displayed.
  name: MinimumDisplayTime
  type: integer
- description: ''
  name: Device
  type: object
- description: ''
  name: InfoQualify
  type: object
- description: ''
  name: OutputContent
  type: object
- description: ''
  name: MenuEntry
  type: array
- description: If protection has to be provided to the vendor on the text to display or print.
  name: OutputSignature
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-display-output-schema.json
slug: terminal-display-output
tags:
- Payments
- Financial Services
- Fintech
title: DisplayOutput
---
