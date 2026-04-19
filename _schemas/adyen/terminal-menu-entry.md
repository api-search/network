---
description: It conveys message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entryof the menu. An entryof the menu to present to the Cashier.
layout: schema
name: MenuEntry
properties_list:
- description: ''
  name: MenuEntryTag
  type: object
- description: ''
  name: DefaultSelectedFlag
  type: boolean
- description: ''
  name: OutputFormat
  type: object
- description: ''
  name: PredefinedContent
  type: object
- description: ''
  name: OutputText
  type: array
- description: ''
  name: OutputXHTML
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-menu-entry-schema.json
slug: terminal-menu-entry
tags:
- Payments
- Financial Services
- Fintech
title: MenuEntry
---
