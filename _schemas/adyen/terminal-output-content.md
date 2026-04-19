---
description: This is a sequence of elements if they have different formats. Content to display or print.
layout: schema
name: OutputContent
properties_list:
- description: ''
  name: OutputFormat
  type: object
- description: ''
  name: PredefinedContent
  type: object
- description: ''
  name: OutputText
  type: array
- description: Mandatory, if OutputFormat is XHTML, not allowed otherwise.
  name: OutputXHTML
  type: string
- description: ''
  name: OutputBarcode
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-output-content-schema.json
slug: terminal-output-content
tags:
- Payments
- Financial Services
- Fintech
title: OutputContent
---
