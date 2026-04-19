---
description: It conveys Information related to the Stored Value transaction to process. Content of the Stored Value Request message.
layout: schema
name: StoredValueRequest
properties_list:
- description: ''
  name: SaleData
  type: object
- description: If the language is selected by the Sale System before the request to the POI.
  name: CustomerLanguage
  type: string
- description: ''
  name: StoredValueData
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-stored-value-request-schema.json
slug: terminal-stored-value-request
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueRequest
---
